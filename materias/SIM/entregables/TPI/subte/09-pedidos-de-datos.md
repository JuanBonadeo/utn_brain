---
title: "Pedidos de datos - TPI Subte Constitución"
subject: "Simulación"
status: "Correos del 23/09 enviados; faltan los dos trámites formales (TAD y Ley 104)"
actualizado: 2026-10-05
---

# Pedidos de datos

La cátedra aprobó usar la Pedestrian Library y pidió que **solicitemos los planos**. Por eso los dos
trámites formales ponen los planos primero. Los textos están acortados a propósito: un pedido corto y
concreto se responde antes. Lo que no figura acá ya se pidió en los correos del 23/09.

## Estado (revisado en Gmail el 2026-10-05)

| Organismo | Canal usado | Enviado | Respuesta | Qué falta |
|---|---|---|---|---|
| SBASE | correo `info@sbase.com.ar` | 23/09 | Ninguna | Pedido formal por Ley 104 (BA Colaborativa). El correo no es el canal formal |
| Emova | correo `comunicaciones@emova.com.ar` | 23/09 | Ninguna | Emova es concesionaria privada y la Ley 104 no le alcanza directamente: su parte se pide a SBASE (§2, punto 4). Opcional: un recordatorio por correo |
| Trenes Argentinos Operaciones (SOFSE) | correo `informacionpublica@trenesargentinos.gob.ar` | 23/09 | 25/09: "los pedidos deberán efectuarse a través de TAD" | Cargar el trámite en TAD (§1) |

Plazos legales: 15 días hábiles en los dos casos. La Nación admite una prórroga de 15 días (Ley 27.275) y
la Ciudad, una de 10 (Ley 104). Si no responden, hay reclamo: ante la AAIP para Trenes Argentinos y ante
el órgano garante de la Ciudad para SBASE.

Registrar acá cada trámite apenas se cargue:

| Trámite | Fecha | Número | Vence (15 hábiles) | Comprobante |
|---|---|---|---|---|
| TAD Trenes Argentinos | | | | `datos/solicitudes/` |
| Ley 104 SBASE | | | | `datos/solicitudes/` |

Los comprobantes van en `datos/solicitudes/` en PDF o como captura, **sin CUIL ni DNI visibles**: el repo
es público.

---

## 1. Trenes Argentinos: trámite TAD

- **Dónde:** <https://tramitesadistancia.gob.ar/tramitesadistancia/detalle-tipo?id=1001>, el enlace que
  mandaron en la respuesta. Hay que entrar con Mi Argentina o AFIP/ARCA.
- **Organismo destinatario:** Trenes Argentinos Operaciones (SOFSE).
- **Alternativa presencial:** mesa de entradas de Av. Ramos Mejía 1302 PB, CABA.
- **Lo carga:** Juan, que es el titular del correo original. Claude no completa formularios con tu cuenta.

**Texto para pegar en "información solicitada":**

> En el marco de la Ley 27.275 solicito la siguiente información sobre la estación terminal Plaza
> Constitución de la Línea Roca, para un trabajo académico de la materia Simulación (UTN, Facultad Regional
> Rosario), que modela el trasbordo de pasajeros del Roca a la Línea C de subterráneos en días hábiles de
> 07:00 a 09:30. Este pedido ya fue enviado por correo electrónico a informacionpublica@trenesargentinos.gob.ar el 23/09/2026, y la respuesta indicó que se presentara por esta vía.
>
> 1. Plano o croquis esquemático de las áreas públicas de la estación, con escala o dimensiones
>    principales: andenes, hall, pasillos y escaleras, y los accesos o vinculaciones con la Línea C del
>    subte. No se solicitan planos de instalaciones técnicas ni de sectores restringidos.
> 2. Cantidad de pasajeros que descienden en Plaza Constitución por formación, o por intervalo de 15 o 60
>    minutos si no existe el dato por tren, entre las 07:00 y las 09:30 de días hábiles de un período
>    reciente (preferentemente marzo a junio de 2026).
> 3. Horarios efectivos de llegada a Plaza Constitución de las formaciones de esa franja para el mismo
>    período, indicando el ramal.
> 4. Si existen: estudios, conteos o estimaciones del flujo de pasajeros entre los andenes del Roca y los
>    accesos de la Línea C, o de la proporción que combina con el subte.
>
> No se requieren datos personales ni grabaciones. Sirve información agregada en cualquier formato
> disponible (PDF, imagen, DWG, CSV o XLSX). Si parte de la información corresponde a otro organismo, por
> ejemplo ADIF o Trenes Argentinos Infraestructura, solicito que se derive o se indique a cuál dirigirla.

---

## 2. SBASE: Ley 104 (BA Colaborativa)

- **Dónde:** <https://buenosaires.gob.ar/tramites/ley-104-solicitud-de-informacion-publica>. Se entra a BA
  Colaborativa con usuario miBA. Hay que indicar el organismo **Subterráneos de Buenos Aires S.E.
  (SBASE)**.
- **Datos que piden:** nombre y apellido, teléfono, correo y la información solicitada. No hace falta
  explicar el motivo, pero conviene mencionarlo para que entiendan el alcance.
- **Lo carga:** Juan.

**Texto para pegar:**

> En el marco de la Ley 104 solicito a Subterráneos de Buenos Aires S.E. la siguiente información sobre la
> estación Constitución de la Línea C, para un trabajo académico de la materia Simulación (UTN, Facultad
> Regional Rosario), que modela el ingreso de pasajeros por los molinetes del vestíbulo Principal en días
> hábiles de 07:00 a 09:30. Un pedido similar se envió por correo electrónico a info@sbase.com.ar el
> 23/09/2026.
>
> 1. Plano o croquis esquemático de las áreas públicas de los vestíbulos Principal y Plaza de la estación,
>    con escala o dimensiones principales: accesos desde la calle y desde la estación ferroviaria,
>    pasillos, escaleras, baterías de molinetes y boletería. No se solicitan planos de instalaciones técnicas
>    ni de sectores restringidos: alcanza con una planta desensibilizada o un croquis acotado.
> 2. Correspondencia entre los identificadores del dataset abierto "Subte: Viajes Molinetes"
>    (LineaC_Constitucion_TurnNN y LineaC_Constitucion_Plaza_TurnNN) y los equipos físicos: en qué batería y
>    vestíbulo está cada uno y si funciona en ingreso, egreso o en ambos sentidos. En el dataset de 2026
>    encontramos 22 identificadores en el vestíbulo Principal (Turn07 y Turn09 a Turn29) y 8 en Plaza.
> 3. Cantidad de molinetes habilitados para ingreso en cada vestíbulo entre las 07:00 y las 09:30, y el
>    criterio habitual para habilitarlos o invertirlos.
> 4. Si SBASE dispone de esa información o puede requerirla a la concesionaria Emova Movilidad S.A.:
>    tiempos de validación por pasajero en molinete (media, percentiles o una muestra), discriminados por
>    SUBE, tarjeta EMV y QR si existe el dato, y mediciones de largo de cola o de espera en el pico de la
>    mañana.
>
> No se requieren datos personales ni grabaciones. Sirve información agregada en cualquier formato
> disponible (PDF, imagen, DWG, CSV o XLSX).

Corrección respecto del correo del 23/09: ese correo hablaba de "28 identificadores del vestíbulo
Principal". El dato correcto es 22 en el Principal y 8 en Plaza, como dice el texto de arriba.

---

## 3. Emova: recordatorio opcional

Emova no tiene un canal de información pública propio. Si se quiere insistir, conviene responder sobre el
mismo hilo del 23/09 con un recordatorio de tres líneas y pedir **sólo dos cosas**: el plano o croquis del
vestíbulo Principal y el tiempo de validación por pasajero. Así resulta más fácil que alguien lo derive.
Claude puede dejarlo como borrador en Gmail, pero no lo envía.

## Cuando llegue una respuesta

1. Guardar el original en `datos/solicitudes/` y registrarlo en la tabla de arriba.
2. Si llega un plano, reemplazar el plano hipotético. Ver `02-modelo-anylogic.md`, sección del plano
   hipotético, y el paso 3 de "Al recibir los datos" en `06-checklist-cierre.md`.
3. Anotarlo en el Log de `materias/SIM/SIM.md`.
