# Podcast CD 7 de 8 — Medios de transmisión y cómo elegir el medio de acceso

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

Par telefónico, coaxil, fibra, radioenlace y satélite: ventajas y desventajas. Después el razonamiento para elegir el medio según la zona, la velocidad, la permanencia y la segurización, con los casos que toma la cátedra. Cerrá con lo que casi no se toma (OSI, CDM, WDM) en dos minutos.

## Contenido principal

### 8. Medios de transmisión y elección del medio de acceso

*Fuentes: Elección medio de acceso V03, Medios de transmisión (práctica) y El Santo Resumen. Salió en los 6 finales de teoría.*

#### 8.1 Los medios

| Medio | Cómo funciona | Lo que hay que saber |
|---|---|---|
| **Par trenzado** | dos conductores de cobre trenzados para cancelar interferencias | barato y ya tendido; la atenuación depende mucho de la frecuencia |
| **Coaxil** | núcleo, aislante, malla y cubierta | mejor blindaje que el par; hoy queda para **cablemodem residencial** |
| **Fibra óptica** | **pulsos de luz** por reflexión interna total | enorme ancho de banda; repetidores cada unos 50 km (cobre: unos 5 km); **inmune a la interferencia electromagnética**; frágil |
| **Microondas** (radioenlace) | haz concentrado con antena parabólica | **visión directa** y torres altas; la lluvia las absorbe desde unos 4 GHz; multitrayecto |
| **Satélite** | repetidor de microondas en el cielo | llega a cualquier lado; el GEO, a unos 36 000 km, tiene latencia alta (unos 270 ms según el apunte) |

> **Ojo:** "el ruido eléctrico y las interferencias afectan a la fibra" es **falso**: lleva luz. "La atenuación de las ondas de radio depende de la frecuencia y la distancia" es **verdadero**. La ventaja del satélite es "llegar a lugares lejanos e inaccesibles". Una empresa urbana con gran ancho de banda **no** contrata cablemodem: el coaxil es residencial.

#### 8.2 Elegir el medio de acceso

El **medio de acceso** ("última milla") conecta la organización con la red del **operador de comunicaciones**, que cubre las grandes distancias con sus troncales. Hoy hay cuatro:

| Medio | Ventajas | Desventajas | Uso típico |
|---|---|---|---|
| **Par telefónico** (+ HDSL o xDSL) | barato; ya tendido en zona urbana; se habilita rápido | poco ancho de banda; se degrada con la distancia, el ruido y la diafonía | organización chica, urbana, con poco ancho de banda |
| **Fibra óptica** | enorme ancho de banda; baja atenuación; inmune a interferencias; difícil de intervenir; escalable | costo de tendido y obra civil; frágil; personal especializado; sólo llega donde hay red | alto ancho de banda en zona urbana o suburbana; anillo para segurizar |
| **Radioenlace** | sin obra de tendido; más barato que la fibra en zonas difíciles; rápido | **visión directa**; mástil y espacio físico; lluvia; multitrayecto; licencias | suburbana con ancho de banda bajo o medio y espacio para el mástil; respaldo de la fibra |
| **Satélite** (VSAT) | llega a cualquier lado; se instala y se muda fácil; no necesita mástil | latencia alta; caro por Mbps; ancho de banda limitado | zona inaccesible, ubicación transitoria; respaldo |

La cátedra decide con siete variables: **ubicación**, **permanencia** (definitiva o transitoria), **espacio físico**, **ancho de banda** (bajo de 4 a 8 M, medio de 10 a 50 M, alto de más de 100 M), **madurez** de la organización, **segurización** y **recursos económicos**.

| Caso | Medio | Por qué |
|---|---|---|
| **Montaña o selva, baja velocidad** | **Satélite** | no hay red tendida, y el relieve o la vegetación impiden la visión directa |
| **Urbana, alta velocidad** | **Fibra** (en anillo si pide segurización) | sólo la fibra da más de 100 M; en la ciudad el operador la tiene cerca |
| **Urbana, baja velocidad** | **Par + HDSL** | la infraestructura ya está y es lo más barato |
| **Suburbana, alta velocidad** | **Fibra en anillo** | el ancho de banda manda |
| **Suburbana, baja velocidad** | **Radioenlace**, si hay espacio para el mástil | sin obra de tendido; con segurización, radioenlace + satélite |
| Suburbana, baja, **sin espacio** o **transitoria** | **Satélite** | no se justifica un mástil ni una obra si se va a mudar |
| Suburbana, media, **con espacio físico** | **Radioenlace** | el dato del espacio apunta al mástil |
| Industria sobre la ruta 9, alta velocidad | **Fibra** | el satélite no da gran velocidad |

**Segurización.** Si el servicio no admite cortes, se agrega un segundo acceso con recursos **disjuntos**. Dos fibras no pueden compartir ningún tramo hasta la sala de equipos: una retroexcavadora corta las dos. Y conviene que el respaldo lo dé **otro operador con infraestructura propia**: si alquila la del primero, cuando cae uno caen los dos.

**El espacio para el radioenlace.** El pie de cada rienda del mástil está al **60 % de su altura**. Un mástil de 30 m necesita un terreno libre de unos 36 × 36 m.

**Para la pregunta del final 2025:** definí medio de acceso; tabla de al menos tres medios; para cada caso, el medio y la variable que decide (montañosa baja → satélite; urbana alta → fibra; suburbana alta → fibra en anillo; suburbana baja → radioenlace); y **escribí los supuestos** que el enunciado no da.

### 10. Por las dudas: lo que casi no se toma

*Nunca salieron en los finales de teoría 2020–2025; sí en el 2° parcial.*

#### 10.1 Modelo OSI y TCP/IP

*Fuente: apunte OSI, TCP/IP y Hardware de Redes (Tanenbaum).*

**OSI** es un **modelo de referencia** de 7 capas: dice qué hace cada una, no qué protocolos usar. De arriba abajo: **aplicación** (HTTP, correo), **presentación** (sintaxis de los datos), **sesión** (diálogo y sincronización), **transporte** (extremo a extremo, entrega en orden), **red** (enrutamiento, congestión), **enlace** (tramas, errores, flujo) y **física** (bits por el medio: tensiones, duración del bit, conectores).

**Capa 1 y capa 2** (2° parcial 2025). La física manda bits crudos y no garantiza que lleguen bien. La de enlace los **organiza en tramas**, **detecta y corrige errores** (ahí viven los códigos de §5) y **regula el flujo**, para que la capa de red vea una línea libre de errores. Todo lo de §6 a §8 es capa 1.

**TCP/IP** tiene 4 capas: host a red, interred (IP, sin conexión), transporte (TCP confiable y con conexión; UDP sin conexión) y aplicación. Sus protocolos son anteriores al modelo.

#### 10.2 CDM y WDM

| Técnica | Qué se reparte | Medio |
|---|---|---|
| **CDM** | **códigos** pseudoaleatorios: todos a la vez en toda la banda, con **espectro ensanchado** casi a nivel de ruido | **no guiado** (CDMA); origen militar |
| **WDM** | **longitudes de onda** (colores de luz) | **sólo fibra**; DWDM: más de 4 λ, hasta 80 o más |

WDM resuelve una fibra saturada sin tender otra: se ponen multiplexores ópticos en las puntas y la misma fibra lleva muchas λ *(conocimiento general: es un FDM óptico)*. FSK y PSK son **modulación**, no multiplexado.

#### 10.3 Errores de canal

El **ruido blanco** (agitación térmica) es imposible de eliminar y limita la capacidad. El **ruido impulsivo** es la **principal** causa de error: picos que alteran **varios binits seguidos (ráfaga)**. Las otras causas son modulaciones espurias, desvanecimiento y distorsión.

## Preguntas reales de teoría de los finales, con su respuesta

### 8. Medios de transmisión y elección del medio de acceso

#### 8.1 Propiedades de los medios (MC verdadero/falso y opciones)
**Salió:** fibra y ruido eléctrico en 28/08/2020, 18/12/2020, 10/09/2021; "la fibra transmite por…" en 18/12/2020; atenuación de ondas de radio en 28/08/2020, 18/12/2020, 10/09/2021; ventaja del satélite en 28/08/2020 y 10/09/2021; cablemodem en 10/09/2021.

**Respuestas.**
- **"El ruido eléctrico, interferencias y acoplamientos eléctricos afectan a la fibra óptica" → FALSO.** La fibra transporta **luz**, así que las sobrecargas de energía, la interferencia electromagnética y los cortes de suministro no la afectan.
- **"La transmisión por fibra óptica se realiza por…" → pulsos de luz.** Un pulso de luz es un 1 y su ausencia es un 0. El sistema tiene fuente de luz, medio (fibra) y detector.
- **"La atenuación de las ondas de radio depende de la frecuencia y de la distancia recorrida" → VERDADERO.** Las propiedades de las ondas de radio dependen de la frecuencia: a baja frecuencia atraviesan obstáculos pero la potencia cae drásticamente con la distancia; a alta frecuencia viajan en línea recta, rebotan y la lluvia las absorbe (microondas desde unos 4 GHz).
- **"Una de las ventajas de las microondas satelitales es…" → poder llegar con la señal a lugares muy lejanos e inaccesibles.** El satélite es un repetidor en el cielo con gran cobertura. Las demás opciones son falsas: el ancho de banda satelital es caro y menor que el de la fibra, el aire no da "más velocidad" y la instalación del enlace no es barata.
- **"Una empresa de zona urbana que requiere gran ancho de banda contrata cablemodem por coaxil a la empresa de TV cable" → FALSO.** Según la cátedra, el coaxil queda **solo para cablemodem de usuarios residenciales** por la red de TV cable. Para una empresa urbana con gran BW se usa fibra óptica.

(practica/3 - Medios de transmisión.md; teoria/Elección medio de acceso V03.md)

#### 8.2 Características (ventajas y desventajas) de los medios de acceso: par telefónico, fibra óptica, radioenlace, satélite
**Salió:** **04/04/2025** (3-a, desarrollo); FAQ ("Indicar al menos tres medios de comunicación de acceso…").

**Respuesta.** El **medio de acceso** ("última milla") conecta la organización con la red del **operador de comunicaciones**, que cubre las grandes distancias con troncales propios. Hoy son par telefónico, fibra óptica, radioenlace y satélite. El coaxil queda para cablemodem residencial y el láser no tuvo expansión.

| Medio | Ventajas | Desventajas | Uso típico |
|---|---|---|---|
| **Par telefónico** (+ módem HDSL/xDSL) | Bajo costo de contratación; infraestructura ya tendida en zonas urbanas; fácil instalación | Ancho de banda limitado; atenuación muy dependiente de la frecuencia y la distancia (amplificadores cada 2–6 km); baja inmunidad al ruido y a la diafonía; altas tasas de error a alta velocidad | Organización pequeña en zona urbana con bajo ancho de banda |
| **Fibra óptica** | Ancho de banda muy superior al cobre; baja atenuación (repetidores cada unos 50 km contra unos 5 km en cobre); inmune a sobrecargas, interferencia electromagnética y corrosivos; difícil de intervenir (segura) | Costo del tendido (obra civil) y de las interfaces; requiere mano de obra calificada; se daña si se dobla; unidireccional (dos fibras o dos bandas para full-dúplex); solo llega donde hay red | Alto ancho de banda en zona urbana o suburbana; segurización en anillo |
| **Radioenlace** (microondas) | No requiere tendido; instalación rápida; relativamente barato frente a tender fibra; salva obstáculos naturales (ríos, rutas); buena relación S/N con antenas alineadas | **Requiere visión directa** e instalación en altura: mástil arriostrado, con pie de rienda de alrededor del 60 % de la altura (para 30 m hace falta un espacio de unos 36 × 36 m); la lluvia lo atenúa desde unos 4 GHz; desvanecimiento por múltiples trayectorias; espectro saturado y licencias | Zona suburbana o rural con espacio físico y BW bajo o medio; segurización de la fibra |
| **Satélite** (VSAT) | **Llega a lugares lejanos, aislados o inaccesibles**; el costo no depende de la distancia; antena chica (VSAT ≤ 1 m), instalación rápida y trasladable; no necesita mástil ni gran espacio | Ancho de banda bajo y caro; **retardo alto** (GEO, unos 270 ms); bandas Ku/Ka sensibles a la lluvia; dependencia de un único proveedor y vida útil del satélite (unos 10 años) | Zona montañosa o selvática; ubicación transitoria; segurización |

(teoria/Elección medio de acceso V03.md; practica/3 - Medios de transmisión.md)

#### 8.3 Elegir un medio de acceso según la zona y la velocidad
**Salió:** **04/04/2025** (3-b, cuatro casos) y MC de 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021; FAQ (dos variantes con tres casos cada una).

**Criterio de la cátedra.** Se evalúan estas variables:
- ubicación (urbana, suburbana, rural, montañosa, bosque/selva);
- permanencia (definitiva o temporal);
- espacio físico para infraestructura (sí/no);
- ancho de banda: bajo de 4 a 8 M, medio de 10 a 50 M, alto de más de 100 M;
- madurez (pequeña, en crecimiento, madura);
- segurización (sí/no);
- recursos económicos.

Como las consignas no dan todas las variables, **conviene escribir el supuesto** (espacio, segurización, permanencia).

| Caso (fechas) | Medio | Justificación (ejemplo del apunte) |
|---|---|---|
| **Zona montañosa, baja velocidad** (28/08/20, 10/09/21, 04/04/25-b1) | **Satélite** | Ej. 8: pequeña en zona montañosa o selva, BW bajo → satelital. El relieve impide la visión directa del radioenlace y no hay red de cobre ni de fibra. |
| **Zona selvática, baja velocidad** (19/11/21, 17/12/21) | **Satélite** | Ej. 8 (montaña/selva). La vegetación obstruye el radioenlace. |
| **Zona urbana, alta velocidad** (28/08/20, 10/09/21, 19/11/21, 17/12/21, 04/04/25-b2) | **Fibra óptica** (en anillo si requiere segurización) | Ej. 2: madura, urbana definitiva, gran BW, segurización → FO en anillo. En la ciudad hay red de fibra del operador. |
| **Zona urbana, baja velocidad** (18/12/20; FAQ) | **Par telefónico + módem HDSL** | Ej. 1: pequeña, urbana, BW bajo, sin segurización y pocos recursos → par + HDSL (infraestructura existente y barata). |
| **Zona suburbana, alta velocidad** (04/04/25-b3; FAQ) | **Fibra óptica** (anillo) | Ej. 6: suburbana definitiva, gran BW, segurización → FO en anillo. Solo la fibra da más de 100 M. |
| **Zona suburbana, baja velocidad** (28/08/20, 10/09/21, 04/04/25-b4) | **Radioenlace** (supuesto: hay espacio físico para el mástil) | Ej. 4: suburbana definitiva, BW bajo, con espacio, sin segurización → RE. Si además pide segurización: RE + satélite (ej. 5). Sin espacio físico: satélite (o par + HDSL si llega la red). |
| **Zona suburbana, baja velocidad, edificio transitorio** (18/12/20; FAQ) | **Satélite** | Ej. 3: transitoria, sin espacio, BW bajo → satelital. No tiene sentido levantar un mástil ni tender fibra si se va a mudar; la VSAT se traslada. |
| **Zona suburbana, velocidad media, con espacio físico** (19/11/21, 17/12/21) | **Radioenlace** | El dato "disponiendo de espacio físico" apunta al mástil del RE, y el RE cubre BW medio. FO si hay presupuesto o segurización (ej. 7 usa FO + RE para BW medio). El cablemodem es residencial. |
| **Industria en la ruta 9 entre Cañada de Gómez y Rosario, gran velocidad** (18/12/20, 19/11/21, 17/12/21) | **Fibra óptica** | Gran BW (>100 M) solo lo da la fibra. Sobre el corredor Rosario–Córdoba el operador tiene troncales de fibra; zona suburbana o rural (ej. 6/7: FO, con segurización por RE). El satélite no da gran velocidad. |

**Segurización.** Si el servicio no admite cortes, se agrega un segundo acceso con **recursos disjuntos**:
- recorridos de fibra que no compartan tramo hasta la sala de equipos;
- y, mejor, **otro operador con infraestructura propia** (si el operador 2 alquila infraestructura al 1, una caída del 1 tira ambos).

(teoria/Elección medio de acceso V03.md; resumenes/El Santo Resumen/el-santo-resumen.md, "Elección del medio de acceso")
