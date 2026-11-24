MULTIPLEXADOS
Vimos hasta ahora:
FDM (Multiplexación por División de Frecuencia) para el caso de Señales
Analógicas y Portadora Analógica mediante Modulación en Amplitud (AM) , en
Frecuencia (FM) y en Fase (PM) , donde cada señal modulada ocupa una
porción específica dentro del Ancho de Banda (Bw) del Canal.
Este Multiplexado se puede dar por medios guiados o no guiados (Par
Telefónico, Cable Coaxil como ser la red de TV Cable, Fibra Óptica, Radio
Enlace, Satélite)
TDM (Multiplexación por División de Tiempo) para el caso de Señales
Analógicas y Portadora Digital mediante Modulación PCM (Modulación por
Pulso Codificado) donde cada señal ocupa una ranura de tiempo (Time Slice)
ocupando todo el Ancho de Banda (Bw) del Canal durante ese tiempo.
Este Multiplexado se puede dar por medios guiados o no guiados (Par
Telefónico, Cable Coaxil, Fibra Óptica, Radio Enlace, Satélite)
Si el Multiplexado se utiliza para acceder a una Red se usan los términos
FDMA y TDMA (A: Acceso)
OBSERVACIÓN
Para el caso de señales digitales y portadora analógica como ser FSK y
PSK son procesos de Modulación, no hay multiplexado. Es decir estas
señales moduladas FSK/PSK puede ser luego multiplexadas en frecuencia
(FDM) o en el tiempo (TDM)
Ahora Veremos otros dos tipos de Multiplexado:
Multiplexado por división de Código-CDM
La Multiplexación por División de Código, (del inglés Code Division Multiple)
se trata básicamente en la transmisión de una palabra código suficientemente
extensa como para ser considerada una secuencia aleatoria, (código pseudo

aleatorio) esto da origen a una transmisión de un gran ancho de banda pero de
muy baja amplitud de ahí que este tipo de transmisión recibe el nombre de
Espectro Ensanchado (en inglés Spread Spectrum) , es decir la energía de la
transmisión en vez de estar concentrada en una banda fija dentro del espectro
radioeléctrico (aire) y con gran amplitud, se distribuye en una gran banda de
frecuencia pero de muy baja amplitud, casi a nivel de ruido por lo tanto no
interfiere con otros servicios que tienen asignación de banda, esto lo hace muy
útil en la transmisión de datos donde se requieren servicios con urgencia sin
tener que esperar la asignación de frecuencia por el organismo regulador.
Como dato anecdótico, este tipo de multiplexado fue desarrollado para
aplicaciones militares como una forma de encriptar los mensajes, pero luego fue
aplicado a servicios civiles
Nuevamente si este tipo de multiplexado se utiliza para acceder a una red
se le da el término CDMA (del inglés Code Division Multiple Access)
ESTE TIPO DE MULTIPLEXADO SE DA FUNDAMENTALMENTE
POR MEDIO NO GUIADO (AIRE) RADIOENLACES SPREAD
SPECTRUM
Multiplexado por División en Longitudes de Onda
(WDM)
WDM es un método de combinación de múltiples señales en una sola fibra óptica
a través de portadoras ópticas de diferente longitud de onda, usando luz
procedente de un láser o un LED. Cada láser se modula mediante un conjunto
independiente de señales.

La transmisión por FO se basa en transmitir una determinada  ʎ (Longitud de

Onda) sobre un pelo de Fibra Óptica.

ʎ  ʎ

FO

Con el desarrollo de las comunicaciones y los requerimientos de transmisión de
datos se agotó la capacidad de las FO tendidas, la solución de tender nuevas
FO es muy costosa y tanto por el costo de la FO como la del tendido, entonces
se desarrollaron equipos que Multiplexan Longitudes de Ondas

| ʎ   |     |     |     |     | ʎ   |
| --- | --- | --- | --- | --- | --- |
| 1   |     |     |     |     | 1   |

| ʎ   |     |     |     |     | ʎ   |
| --- | --- | --- | --- | --- | --- |
| 2   |     |     |     |     | 2   |

|     | MUX  |     |     | MUX  |     |
| --- | ---- | --- | --- | ---- | --- |
FO
|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
|   ʎ |     |     |     |     | ʎ   |
| n   |     |     |     |     | n   |

| Multiplexado  | Denso  | por  | División  | en  Longitudes  |     |
| ------------- | ------ | ---- | --------- | --------------- | --- |
de Onda (DWDM)
Cuando el multiplexado es mayor a 4 longitudes de onda de denomina DWDM.
Usando DWDM, se puede multiplexar en una sola fibra óptica hasta 80 (o incluso
más) longitudes de onda o canales de datos separados.
| ESTE  TIPO  | DE  MULTIPLEXADO  |     | SE  DA  | ÚNICAMENTE  | POR  |
| ----------- | ----------------- | --- | ------- | ----------- | ---- |
MEDIO GUIADO. FIBRA ÓPTICA