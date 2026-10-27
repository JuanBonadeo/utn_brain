---
title: "Pedidos de datos - TPI Subte Constitución"
subject: "Simulación"
status: "Trenes Argentinos respondió el 26/10 (plano, llegadas reales y origen-destino); SBASE pidió prórroga (respuesta ≈ 10/11)"
actualizado: 2026-10-27
---

# Pedidos de datos

La cátedra aprobó usar la Pedestrian Library y pidió que **solicitemos los planos**. Por eso los dos
trámites formales ponen los planos primero. Los textos están acortados a propósito: un pedido corto y
concreto se responde antes. Lo que no figura acá ya se pidió en los correos del 23/09.

## Estado (revisado en Gmail el 2026-10-05)

| Organismo | Canal usado | Enviado | Respuesta | Qué falta |
|---|---|---|---|---|
| SBASE | correo `info@sbase.com.ar` (23/09); Ley 104 n.º 01084412/26 (05/10) | 23/09 y 05/10 | 26/10: usa la prórroga del art. 10 (nota IF-2026-47895115-GCABA-SBASE; expediente EX-2026-44567557-GCABA-DGAIGA) | Esperar la respuesta de fondo, ≈ 10/11 (10 hábiles más) |
| Emova | correo `comunicaciones@emova.com.ar` | 23/09 | Ninguna | Emova es concesionaria privada y la Ley 104 no le alcanza directamente: su parte se pide a SBASE (§2, punto 4). Opcional: un recordatorio por correo |
| Trenes Argentinos Operaciones (SOFSE) | correo (23/09); TAD EX-2026-96962531- -APN-DNPAIP#AAIP (05/10) | 23/09 y 05/10 | 25/09: derivó a TAD. **26/10: respondido** por correo (nota NO-2026-104102701-APN-UCIYT#SOFSE) | Nada: ver "Respuesta de Trenes Argentinos" abajo |

Plazos legales: 15 días hábiles en los dos casos. La Nación admite una prórroga de 15 días (Ley 27.275) y
la Ciudad, una de 10 (Ley 104). Si no responden, hay reclamo: ante la AAIP para Trenes Argentinos y ante
el órgano garante de la Ciudad para SBASE.

Registrar acá cada trámite apenas se cargue:

| Trámite | Fecha | Número | Vence (15 hábiles) | Comprobante |
|---|---|---|---|---|
| TAD Trenes Argentinos (dependencia: SOFSE) | 05/10/2026 | EX-2026-96962531- -APN-DNPAIP#AAIP | ≈ 27/10/2026 (feriado 12/10 descontado); +15 hábiles de prórroga | Buzón de TAD; las notificaciones llegan a la cuenta TAD, no al mail |
| Ley 104 SBASE (BA Colaborativa, área Ministerio de Infraestructura) | 05/10/2026 13:50 | 01084412/26 | ≈ 27/10/2026 (feriado 12/10 descontado); +10 hábiles de prórroga | Pantalla de confirmación; la DGAIGA avisa por mail en 2 días hábiles |

Los comprobantes van en `datos/solicitudes/` en PDF o como captura, **sin CUIL ni DNI visibles**: el repo
es público.

## Respuesta de Trenes Argentinos (26/10)

Llegó por correo desde `informacionpublica@trenesargentinos.gob.ar`, no por el buzón de TAD. Los originales,
sin modificar, están en [`datos/solicitudes/sofse-2026-10-26/`](datos/solicitudes/sofse-2026-10-26/). Los dos
Excel venían embebidos en el PDF de la nota y se sacaron con `pdfdetach -saveall`.

| Punto pedido | Qué mandaron | Archivo |
|---|---|---|
| 1. Plano | Plano del sistema SIENA de la estación (cuadro de estación y superficies concesionadas), en DWG, en metros. Muestra el hall, los paragolpes y los andenes 2 a 14. **No marca los accesos de la Línea C** | `CONSTITUCION_NUEVO_FINAL.dwg` y `plano-cabecera-render.png` (render propio) |
| 2. Pasajeros que bajan | No es el dato por tren. Mandaron una matriz origen-destino (marzo a junio, por día hábil, sábado y domingo) y los pasajeros por estación de origen en días hábiles de 07:00 a 09:59 (hoja `PPT FRANJA HORARIA`) | `origen-destino-lgr-mar-jun-2026.xlsx` |
| 3. Llegadas efectivas | Llegada real de cada tren a Constitución, de 07:00 a 09:30, del 02/03 al 30/06/2026, con número de tren y ramal: 4816 filas, al minuto | `trenes-a-pc-mar-jun-2026.xlsx` |
| 4. Estudios de trasbordo | "No se realizaron estudios en relación a lo solicitado" | — |

Primera lectura (2026-10-27):

- **Llegadas reales.** Hay 76 días hábiles normales, con 43 a 52 trenes cada uno (media 48,9). Los días
  con menos trenes son feriados o tienen el servicio cortado. Comparado contra el horario vigente desde el
  03/08 (47 trenes), el atraso real tiene mediana +4 min, p10 −1 min, p90 +11 min y p99 +24 min. El horario
  de marzo a junio no es exactamente el del 03/08: el tren 302 (Mar del Plata) llega todos los días y no
  figura en `arribos_roca_constitucion_habiles.csv`. El período es el mismo que el del perfil SBASE
  (marzo-junio), así que cada réplica puede usar **un día real** (sus trenes y su perfil SBASE) en vez del
  día medio.
- **Carga del Roca hacia Constitución.** De cada estación sale entre un 44 y un 60 % de los viajes hacia
  Constitución. Si eso se aplica a los pasajeros que suben de 07:00 a 09:59, llegan unos 2,9 M en el período,
  o sea ≈ 36.000 por día hábil (≈ 700 por tren). Frente a los ≈ 14.800 ingresos a la Línea C que el modelo
  atribuye al Roca (0,80 × 18.532), haría falta que trasborde un 40 % de los que llegan. Es verosímil, pero
  **no fija la proporción**: el punto 4 dice que no hay estudios.
- **Plano.** La fila de paragolpes está alineada (todas las vías terminan en el mismo x). Las vías tienen de
  170 a 330 m y los andenes útiles, de 134 a 275 m. Sirve para comprobar la dispersión de la descarga
  (145 s ≈ caminar un andén de 170 m) y la distancia que se midió en OSM desde los paragolpes. No sirve para
  dibujar el vestíbulo de la Línea C, que es de SBASE.

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
