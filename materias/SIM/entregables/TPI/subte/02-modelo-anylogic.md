# TPI subte — primer modelo en AnyLogic

**2026-09-20 · preparación para el miércoles 23/09.**

Archivo: [`SubteConstitucion.alp`](SubteConstitucion.alp), formato **AnyLogic 8.9.9**.
Implementa el circuito y los escenarios de la [definición del caso](01-definicion-del-caso.md).
Es un **prototipo sin calibrar**: los parámetros de campo permanecen en `-1`.
El modo de demostración usa valores sintéticos explícitos; sus salidas no son resultados del TPI.

## 1. Abrir y ejecutar

1. Abrir el `.alp` en AnyLogic 8.9.9 o posterior.
2. En el árbol del proyecto, abrir `Main`: contiene los siete bloques, los parámetros y las funciones.
3. Ejecutar uno de los experimentos `E0`, `E1`, `E2` o `E3`. Cada experimento fija `escenario`;
   los demás parámetros heredan sus valores de `Main`, salvo que se sobrescriban en el experimento.
4. Mantener `modoDemo = true` para verificar inicialmente el circuito. Abrir la consola: al inicio
   imprime **DEMO SINTETICA - NO CALIBRADA** y al terminar imprime las medidas de la réplica.
5. Para cargar mediciones, completar los parámetros de la tabla siguiente y cambiar `modoDemo` a
   `false`. Si falta un dato necesario, la inicialización lanza un error explicativo.

**Verificación realizada:** XML, referencias de escenarios e identificadores; compilación de las
funciones Java contra la API local de AnyLogic 8.9.9; pruebas de lógica con trazas controladas.
**Verificado en el IDE el 2026-09-23:** el `.alp` completo compila correctamente en AnyLogic 8.9.9 y el
experimento `E0` inicia en modo demo, mostrando el aviso `DEMO SINTETICA - NO CALIBRADA E0`. La interfaz
actual es un tablero técnico provisorio; todavía no representa la geometría de la estación ni el movimiento
espacial de peatones.

Para repetir las verificaciones realizadas, desde la raíz del repositorio:

```sh
python3 materias/SIM/entregables/TPI/subte/verificar_modelo.py
```

El verificador usa el JDK y las bibliotecas de `/Applications/AnyLogic 8 PLE.app`; no modifica el modelo.

## 2. Circuito y unidades

```mermaid
flowchart LR
    T[Evento: próxima tanda] -. "inject(n)" .-> S[Source]
    S --> Q[Queue FIFO]
    Q --> Z[Seize: 1 molinete]
    Z --> D[Delay: servicio en segundos]
    D --> R[Release]
    R --> K[Sink]
    P[ResourcePool: molinetes estáticos] -.-> Z
    R -. "libera recurso" .-> P
```

Un agente representa **un pasajero**. `source` está en modo **Calls of inject() function**:
`proximaTanda` genera simultáneamente los pasajeros de una tanda mediante `source.inject(n)` y
programa la siguiente. No se usa una tasa Poisson individual ni se trata una tanda como un solo agente.

La unidad de tiempo del modelo es el **segundo**. `t = 0` representa las 07:00;
el pico 08:15–08:45 corresponde a `[4500, 6300)` y las 09:30 a `t = 9000`.
La primera tanda aparece en `primeraTandaSeg`, inicialmente cero.

`queue` es FIFO, sin abandono y de capacidad máxima. `seize` toma una unidad de `molinetes`;
su cola interna tiene capacidad **1**. Por eso la espera se registra desde `queue.onEnter` hasta
`seize.onSeizeUnit`, incluyendo ambas colas. La cola total se mantiene con `nEsperando`.
`delay` tiene capacidad máxima: la concurrencia la limita el ResourcePool, no otro servidor oculto.
`release` devuelve el recurso antes de destruir al pasajero en `sink`.

## 3. Parámetros expuestos

| Parámetro de Main | Inicial | Interpretación |
|---|---:|---|
| `escenario` | 0 | E0=0, E1=1, E2=2, E3=3; lo fija cada experimento |
| `modoDemo` | `true` | Usa valores sintéticos para revisar el funcionamiento |
| `molinetesBase` | 20 | Aproximación entera provisional; contrastar también 19 |
| `molinetesE1` | 28 | Hipótesis E1 de la definición del caso |
| `fraccionDesvioE2` | 0,15 | Fracción del flujo originalmente dirigido a Principal que se desvía; decisión de prueba |
| `servicioSUBESeg` | **-1** | **Completar en campo**: duración de servicio SUBE, segundos |
| `servicioEMVSeg` | **-1** | **Completar en campo**: duración EMV/QR, requerida en E3 |
| `tamanoTanda` | **-1** | **Completar en campo**: pasajeros por tanda a la intensidad de referencia |
| `intervaloTandaSeg` | **-1** | **Completar en campo**: intervalo entre tandas, segundos |
| `primeraTandaSeg` | 0 | Desfase de la primera tanda desde las 07:00 |
| `usarPerfilSBASE` | `true` | Modula el tamaño de las tandas con el perfil de diez ventanas |
| `perfil15min` | Diez medias del caso | `{1437,1578,1765,1824,1799,2054,2066,1742,1581,1636}` |
| `semilla` | 1 | Semilla del generador independiente usado para el desvío E2 |
| `horizonteSeg` | 9000 | Corte de arribos; para pruebas puede reducirse, hasta un máximo de 9000 |

En modo demo se usan **300 pasajeros por tanda de referencia, 150 s entre tandas, 3 s de servicio
SUBE y 2,5 s EMV/QR**. Son datos artificiales para ejercitar los bloques; no estimaciones ni mediciones.
Se ignoran los cuatro campos pendientes mientras `modoDemo` sea verdadero.

Con `usarPerfilSBASE = true`, en cada arribo:

```text
ventana = floor(t / 900)
tamaño generado = round(tamanoTanda × perfil15min[ventana] / 1748,2)
```

`1748,2 = 17482 / 10` es la intensidad de referencia del día hábil. El intervalo entre tandas sigue
siendo `intervaloTandaSeg`. **El perfil aporta la forma temporal, no impone 17.482 arribos exactos**:
el total depende del tamaño, intervalo, desfase y redondeo. Compararlo con el total observado es un
control de calibración. Si se mide una tanda solo en el pico, convertir su tamaño a la intensidad de
referencia antes de cargarlo, o desactivar el perfil para pruebas de una intensidad constante.

Los conteos SBASE son **validaciones**, no arribos observados. Usarlos para modular demanda es un
supuesto provisional, sujeto a verificar colas iniciales y censura por capacidad en campo.

Esta versión utiliza **duraciones e intervalos constantes** y tamaños modulados por ventana.
No se eligió una distribución estadística sin datos. Los puntos a extender tras medir son
`servicioSeg()`, `intervaloSeg()` y `tamanoActual()`: allí se incorporarán muestras empíricas o
distribuciones ajustadas. Repetir E0/E1/E3 con distintas semillas hoy da los mismos resultados;
todavía no corresponde realizar el test de medias del TPI.

## 4. E0–E3

| Experimento | Capacidad | Servicio | Desvío |
|---|---|---|---|
| E0 | `molinetesBase` | SUBE | 0 |
| E1 | `molinetesE1` | SUBE | 0 |
| E2 | `molinetesBase` | SUBE | `fraccionDesvioE2` |
| E3 | `molinetesBase` | EMV/QR | 0 |

**E0:** 19,5 es un promedio de molinetes con tráfico por ventana, no una capacidad fraccionaria.
La aproximación de 20 permite iniciar el modelo. Se debe verificar la disponibilidad y habilitación
real, y luego decidir entre capacidad constante o un horario de habilitaciones. La cola común y los
servidores intercambiables todavía no reproducen el reparto observado Turn14/Turn23.

**E1:** 28 conserva la hipótesis definida. Antes de interpretar la mejora hay que verificar que esos
28 sean utilizables para ingreso en Principal, respetando la exclusión del Turn07 declarada en el caso.
El modelo no convierte automáticamente identificadores registrados en capacidad operativa.

**E2:** antes de inyectar la tanda en Principal, se decide el desvío de cada pasajero con una Bernoulli.
Los desviados se cuentan en `nDesviados`; no entran en el circuito ni se computan como atendidos.
El 15 % inicial es una decisión de prueba, **no** el 15,3 % de participación histórica de Plaza.
Se consume un número aleatorio por pasajero en todos los escenarios, usando `semilla`.

Así se mide el alivio de **Principal**, bajo el supuesto de que Plaza acepta el flujo desviado. No se
modelan todavía el flujo propio, capacidad, caminata ni cola de Plaza. Por tanto, la espera de Principal
en E2 **no permite recomendar una mejora para todos los pasajeros de la estación**. Para esa comparación
se necesitará un segundo circuito para Plaza y medidas sobre la población completa.

**E3:** sustituye el servicio de todos los servidores por el parámetro EMV/QR y mantiene la capacidad
base. Es una hipótesis de conversión completa; no reproduce una mezcla de medios de pago ni implica
que contactless sea necesariamente más rápido. Una mezcla requiere medir su participación y asignar
el tipo de servicio por pasajero.

## 5. Salidas, corte y drenaje

Se generan arribos únicamente en `[0, 9000)`. A las 09:30 se fija el estado al cierre y se sigue
procesando hasta que sale el último pasajero de Principal. El modelo finaliza mediante
`getEngine().finish()`; el tiempo final muy grande del experimento es solo un límite técnico.

La consola imprime `resumen()` al finalizar. Las variables quedan disponibles en `Main`:

| Salida | Definición |
|---|---|
| `esperaMediaSeg`, `p90Seg`, `propMas30` | Cohorte de pasajeros ingresados a Principal dentro de la franja, con espera completa incluso si termina después de las 09:30 |
| `esperas` | Lista sin truncamiento de las esperas individuales; P90 usa rango más próximo: `ceil(0,9 n)` |
| `Lq` | Integral de la cola total dividida por 9000; excluye el período de drenaje |
| `qMax` | Máximo de pasajeros que deben esperar; descuenta lugares disponibles para transferencias instantáneas |
| `utilizacion` | Segundos ocupados en la franja / (9000 × capacidad) |
| `ocupacionPorUnidad` | Segundos ocupados de cada molinete dentro de la franja, incluyendo unidades nunca usadas |
| `desvioUtilizacionMolinetes` | Desvío poblacional de las utilizaciones individuales, al finalizar el drenaje |
| `procesadosFranja` | Pasajeros que salen antes de `t = 9000`; salida exactamente a las 09:30 queda fuera |
| `procesadosConDrenaje` | Pasajeros atendidos de toda la cohorte de Principal |
| `pendientes0930`, `cola0930` | Cohorte pendiente y cola al cierre, respectivamente |
| `disipaciones` | Para cada tanda con al menos un pasajero en Principal, tiempo hasta la siguiente cola total vacía |

Las tandas superpuestas comparten el siguiente instante de vaciado, cada una medida desde su arribo.
Si toda la tanda obtiene servicio inmediatamente, la disipación es cero. Se comprueba el vaciado en un
evento diferido `0,000001 s`, para evitar cierres falsos durante las transferencias de un mismo instante;
la duración se calcula con el instante del último cambio real de cola. La disipación significa **fin
de la espera**, no salida del último pasajero de la tanda.

La espera se mide en `onSeizeUnit`, y la ocupación termina en `onReleaseUnit`. Las áreas se actualizan
antes de cada cambio y se recortan al horizonte. Al terminar se exige:

```text
nGenerados = nDesviados + nProcesados
nProcesados = nPrincipal
```

No se interpretan pasajeros desviados como perdidos ni se omiten los pendientes a las 09:30.
La cola inicial es vacía, un supuesto pendiente de verificar a las 07:00; no se aplicó un calentamiento
arbitrario a este sistema de horizonte finito. Las salidas actuales agregan toda la franja: un reporte
separado de la cohorte del pico `[4500, 6300)` queda para la siguiente iteración.

## 6. Verificación y estrategia de calibración remota

El verificador reproduce una tanda de **5 pasajeros, 2 molinetes y servicio de 3 s** mediante trazas
explícitas: esperas `0, 0, 3, 3, 6`, media **2,4 s**, P90 **6 s**, cola máxima **3**, área de cola
**12 pasajero·s**, ocupación **15 molinete·s** y disipación **6 s**. Comprueba también el bloqueo por
parámetros faltantes, E0–E3, conservación y un servicio que cruza las 09:30. No es una simulación
alternativa al motor AnyLogic.

En la primera ejecución del IDE, verificar esa misma tanda (`modoDemo=false`, perfil desactivado,
`tamanoTanda=5`, `intervaloTandaSeg=150`, `servicioSUBESeg=3`, `molinetesBase=2`, `horizonteSeg=10`).
Después ejecutar los cuatro demos completos. Estos checks del motor siguen pendientes.

El grupo reside en Rosario y no puede realizar una medición presencial propia en Constitución. Para avanzar
sin presentar supuestos como observaciones:

- usar horarios oficiales del Ferrocarril Roca para aproximar los intervalos entre oleadas;
- solicitar a SBASE/Emova y Trenes Argentinos datos operativos de mayor granularidad;
- tratar los tiempos de servicio, tamaños de tanda y proporción de transferencia como factores
  experimentales dentro de rangos explícitos, sujetos a la conformidad del docente;
- validar el caudal agregado contra ventanas SBASE no usadas para parametrizar el modelo, dejando claro
  que el dataset disponible no permite validar la espera ni la cola real;
- Incorporar semillas independientes por fuente aleatoria y entradas comunes por réplica entre
  escenarios antes de calcular diferencias apareadas e intervalos de confianza.

## 7. Referencias técnicas

Propiedades contrastadas con `library.xml` de **ProcessModelingLibrary.jar 8.9.9**, instalado
localmente, y estructura del `.alp` basada en el modelo local `TP_Colas.alp`.

- [Source — documentación oficial](https://anylogic.help/9/libraries/process-modeling/source.html): generación por llamadas a `inject(n)`.
- [Seize — documentación oficial](https://anylogic.help/9/libraries/process-modeling/seize.html): captura de recursos y cola interna.
- [Recursos — documentación oficial](https://anylogic.help/library-reference-guides/process-modeling-library/using-resources.html): unidades de recursos compartidos por procesos.
