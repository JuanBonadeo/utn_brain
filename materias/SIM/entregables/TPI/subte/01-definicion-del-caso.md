# TPI Simulación — Definición del caso: molinetes de Constitución (Línea C)

> Para la reunión del **miércoles 2026-09-23** con el docente (Guillermo Leale).
> Responde los tres puntos que pidió por mail el 2026-09-20: qué línea en específico, qué franja
> horaria y días, y cuáles son en concreto las medidas de rendimiento.
> Todos los números de este documento salen del perfilado propio del dataset de SBASE (§6), no de
> estimaciones. El script que los reproduce es [`scripts/sbase-perfil.py`](../../../../../scripts/sbase-perfil.py).

---

## 1. El caso en una oración

Simulación de la línea de molinetes del vestíbulo principal de la estación **Constitución de la Línea C**
del subte de Buenos Aires durante el pico de la mañana de los días hábiles, para evaluar el efecto de la
cantidad de molinetes habilitados y de la velocidad de validación sobre el tiempo de espera de los
pasajeros que llegan en tandas desde la terminal ferroviaria Roca.

## 2. Qué línea y qué estación, y por qué esa

**Línea C, estación Constitución, vestíbulo Principal.**

La elección no es por preferencia: Constitución domina el sistema por un margen que no admite discusión.
Sobre junio de 2026 completo, las **14 ventanas de 15 minutos más cargadas de las seis líneas del subte son
todas de Constitución**. La siguiente estación del ranking (Catedral, Línea D, 17:15) mueve 1.042 pax/15 min
contra los 2.302 de Constitución: menos de la mitad.

| | pax junio 2026 | molinetes registrados |
|---|---:|---:|
| **Constitución (C)** | **1.293.543** | 28 |
| Congreso de Tucumán (D) | 563.862 | 17 |
| San Pedrito (A) | 527.214 | 11 |
| Federico Lacroze (B) | 455.588 | 20 |
| Retiro (C) | 392.331 | 6 |

Constitución mueve **2,3 veces** la segunda estación del sistema.

La estación tiene **dos vestíbulos** y el dato los distingue por el nombre del molinete
(`LineaC_Constitucion_TurnNN` vs `LineaC_Constitucion_Plaza_TurnNN`):

| Vestíbulo | pax ene-jun 2026 | share | pax en pico 07:00-09:30 |
|---|---:|---:|---:|
| **Principal** | 6.261.245 | **84,7 %** | 2.065.291 |
| Plaza | 1.131.122 | 15,3 % | 358.314 |

**El alcance es el vestíbulo Principal.** Es el que recibe la descarga de la terminal ferroviaria y
concentra el 85 % del flujo. El vestíbulo Plaza queda fuera del modelo base, pero **no se descarta**:
está subutilizado y es el sustento del escenario alternativo E2 (§5).

## 3. Qué días y qué franja horaria

**Días hábiles, franja 07:00 – 09:30.** El pico está en **08:15 – 08:45**.

Perfil del día hábil depurado (n = 117 días, vestíbulo Principal, pax promedio por ventana de 15 min):

| Ventana | media | desvío | CV | mín | máx | molinetes activos | pax/molinete/min |
|---|---:|---:|---:|---:|---:|---:|---:|
| 07:00 | 1.437 | 385 | 0,27 | 450 | 2.583 | 19,5 | 4,91 |
| 07:15 | 1.578 | 373 | 0,24 | 606 | 2.660 | 19,5 | 5,40 |
| 07:30 | 1.765 | 374 | 0,21 | 667 | 2.621 | 19,5 | 6,03 |
| 07:45 | 1.824 | 439 | 0,24 | 605 | 2.963 | 19,5 | 6,23 |
| 08:00 | 1.799 | 445 | 0,25 | 302 | 2.773 | 19,5 | 6,15 |
| **08:15** | **2.054** | 496 | 0,24 | 156 | 3.158 | 19,5 | **7,02** |
| **08:30** | **2.066** | 492 | 0,24 | 125 | 3.045 | 19,5 | **7,06** |
| 08:45 | 1.742 | 519 | 0,30 | 205 | 3.181 | 19,5 | 5,95 |
| 09:00 | 1.581 | 434 | 0,27 | 204 | 2.881 | 19,5 | 5,40 |
| 09:15 | 1.636 | 323 | 0,20 | 192 | 2.569 | 19,5 | 5,58 |

**Total de la franja: 17.482 pasajeros por día hábil.**

El pico es inequívoco y angosto: la tarde no lo replica. En Constitución la franja vespertina apenas llega
a 500 pax/15 min, porque el flujo de la tarde es de **salida** (los molinetes cuentan ingresos al subte, y a
la tarde la gente ingresa en el centro y sale en Constitución). El fenómeno de cola está solo a la mañana.

**Día de la semana.** El miércoles es el más cargado y el lunes el más liviano; la diferencia es de 27 %:

| | lun | mar | mié | jue | vie |
|---|---:|---:|---:|---:|---:|
| pax en la ventana 08:30 | 1.976 | 2.255 | **2.510** | 2.334 | 2.112 |

Propuesta: modelar el día hábil genérico y usar el día de la semana como análisis de sensibilidad, no como
escenario (no es una variable de decisión: nadie elige el día).

**Depuración.** De los 128 días hábiles de enero a junio de 2026 se **excluyen 11**, detectados por caída
del flujo diario por debajo del 50 % de la mediana. Los 11 corresponden uno a uno a feriados y fines de
semana largos (1/1, 16-17/2 Carnaval, 24/3, 2-3/4, 1/5, 25/5, 15/6), lo que valida el criterio: el filtro no
se eligió a dedo, y el dato mismo identifica los días a sacar. Quedan **117 días** para el ajuste.

## 4. El fenómeno: por qué esto requiere simulación y no una fórmula

Este es el punto central del caso, y conviene plantearlo así en la reunión.

En el pico, el vestíbulo Principal mueve **7,06 pax/min por molinete**, o sea **un pasajero cada 8,5
segundos**. Una validación de molinete demora del orden de 2 a 3 segundos. Con esos números la utilización
por molinete es ρ ≈ 0,3, y **cualquier modelo analítico de colas (M/M/c) concluye que no hay cola**.

Pero en Constitución sí hay cola, y cualquiera que haya pasado por ahí a las 8:30 la vio. La razón es que
**los arribos no están distribuidos en el tiempo: llegan en tandas**. Constitución es la terminal del
Ferrocarril Roca, y cada formación que llega descarga cientos de personas que caminan juntas hasta los
molinetes. Entre tren y tren el vestíbulo está prácticamente vacío.

Esa es exactamente la situación donde la fórmula falla y la simulación es la herramienta correcta:
**congestión transitoria por arribos en lote sobre un sistema que, en promedio, está subutilizado**. Es el
argumento de por qué el caso vale como TPI, y conviene que sea lo primero que se diga el miércoles.

Consecuencia metodológica: el dato de SBASE da la **tasa** de arribos (cuánta gente por cuarto de hora) pero
no la **estructura de tandas** (cuántas tandas, de qué tamaño, cada cuánto). Esa estructura hay que
conseguirla de otra fuente, y hoy es el principal hueco (§7).

## 5. Escenarios

| | Escenario | Qué cambia |
|---|---|---|
| **E0** | Base — configuración actual | ~19,5 molinetes activos de los 28 instalados, con la distribución de carga observada |
| **E1** | Abrir todos los molinetes instalados | 28 en lugar de ~20 durante la franja pico. Es la hipótesis de mejora más directa y la de menor costo |
| **E2** | Redistribuir hacia el vestíbulo Plaza | Desviar parte del flujo al vestíbulo que hoy absorbe solo el 15 %, vía señalización |
| **E3** | Validación contactless (EMV/QR) | Cambia el tiempo de servicio, no la cantidad de servidores. La estación **ya tiene** un molinete `Plaza_TurnEMV+QR`, así que es medible en campo y no un supuesto |

E1 es el escenario alternativo obligatorio del enunciado. E2 y E3 son los que hacen interesante el trabajo,
y E3 en particular se apoya en algo que ya existe en la estación.

Dato que sostiene a E1: de los 28 molinetes instalados, en la franja pico hay **21 con tráfico real** y
~19,5 activos en promedio por ventana. La carga además está muy desbalanceada — Turn14 procesa 1.485
pax/día hábil en la franja y Turn23 solo 129, un factor de 11 entre el más y el menos usado. Hay capacidad
instalada ociosa y mal repartida, que es justo lo que un modelo puede cuantificar.

## 6. Medidas de rendimiento (lo que el docente pidió "en concreto")

**Primarias** — sobre las que se hace el test de medias entre escenarios:

1. **Tiempo de espera en cola por pasajero**, en segundos: media y **percentil 90**. El percentil va
   además de la media porque el fenómeno es de picos: comparar solo medias esconde exactamente lo que se
   quiere medir (SIM.md, Unidad 9).
2. **Proporción de pasajeros que esperan más de 30 segundos.** Es una proporción, no una media, y da un
   criterio de nivel de servicio comunicable.
3. **Tiempo de disipación de la tanda**: cuánto tarda la cola en volver a cero después de que llega una
   formación. Es la medida que captura el fenómeno transitorio y la que mejor distingue los escenarios.

**Secundarias** — para caracterizar el sistema y para la validación:

4. Largo de cola: promedio temporal (Lq) y máximo por réplica.
5. Utilización por molinete (ρ) y su dispersión entre molinetes (mide el desbalance de E2).
6. Pasajeros procesados en la franja (throughput), como control de que el modelo no pierde gente.

**Regla de decisión**: se recomienda la configuración de menor percentil 90 de espera, **solo si** el
intervalo de confianza del 95 % de la diferencia apareada contra E0 no contiene al cero. Si lo contiene, la
conclusión es que no hay evidencia de mejora, y se informa así — que el enunciado lo admite explícitamente
como resultado válido.

## 7. Lo que falta y estrategia remota

Dos parámetros no están en ningún dataset y son los que definen el modelo. El grupo reside en Rosario,
por lo que no puede realizar un relevamiento presencial propio en Constitución. No corresponde completar
estos parámetros con estimaciones presentadas como mediciones.

| Falta | Por qué no está | Cómo se consigue |
|---|---|---|
| **Tiempo de servicio del molinete** | SBASE publica conteos, no duraciones | Solicitar información a SBASE/Emova. Si no se obtiene, tratarlo como factor experimental dentro de rangos explícitos aprobados por el docente |
| **Estructura de las tandas** (cuántas, de qué tamaño, cada cuánto) | El dato es agregado a 15 minutos y borra la tanda | Usar los horarios oficiales de llegada del Roca para aproximar intervalos y distribuir el total SBASE entre oleadas mediante supuestos explícitos; analizar sensibilidad sobre tamaños y proporción de transferencia |

La estrategia remota permite validar el **caudal agregado** contra ventanas de SBASE no utilizadas para
parametrizar el modelo, pero no valida la espera ni el largo de cola reales. Los molinetes registran a quien
pasó, no a quien esperó. Por eso las conclusiones sobre espera deberán ser condicionales a los rangos de
entrada y esta reformulación requiere conformidad del docente. Si se exige validación empírica de la cola,
será necesario conseguir un observador local o revisar el caso.

## 8. Riesgos declarados

- **Censura por capacidad.** El conteo registra validaciones, no demanda. Si en el pico los molinetes están
  saturados, el dato mide el caudal máximo del molinete y no la gente que quería pasar. Es un motivo más
  para medir la cola en campo.
- **Formato inconsistente del dataset.** El campo de hora cambia de formato según el mes: marzo y abril de
  2026 usan `HH:MM` y el resto `HH:MM:SS`. Agregar sin normalizar parte cada hora en dos y da resultados
  silenciosamente mal. Está normalizado en el script y hay que declararlo en el paso 2 del informe.
- **El molinete `Turn07` figura con 3 pasajeros en seis meses** y `Plaza_Turn07` con 2.980: molinetes fuera
  de servicio o mal identificados. Se excluyen del modelo y se declara.
- **Arribos dentro de la ventana.** Mientras no tengamos la estructura de tandas medida, cualquier supuesto
  de arribos homogéneos subestima la cola. No se puede cerrar el modelo sin ese dato.

## 9. Fuente de datos

| Dataset | Origen | Estado |
|---|---|---|
| Subte — Viajes Molinetes, 2026 (ene-jun) | [BA Data — Subte Viajes Molinetes](https://data.buenosaires.gob.ar/dataset/subte-viajes-molinetes) | ✅ Descargado (45 MB zip → 548 MB CSV) y perfilado |
| Series 2013-2025 | mismo dataset | Disponibles si se quiere ampliar el horizonte |

Granularidad: una fila por **molinete individual** y ventana de 15 minutos, con línea, estación, molinete
(con vestíbulo y número) y pasajeros discriminados por tipo de pago (`pax_pagos`, `pax_pases_pagos`,
`pax_franq`, `pax_TOTAL`). Es más fino de lo que suponíamos en julio, cuando el tema era la reserva: no es
por estación, es **por molinete**, que es justamente la unidad de servicio del modelo.

Los archivos de datos **no se commitean** (548 MB). Se regeneran con el script y el link del portal.
