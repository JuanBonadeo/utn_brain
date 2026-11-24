Comunicaciones 1er parcial práctica
Información, codificación y canales
Conceptos fundamentales (mensajes equiprobables)
Siendo:
𝑛: cantidad de dígitos de información
𝑁: cantidad de dígitos del mensaje
𝑇: duración del mensaje
𝜏: duración del pulso
𝜇: cantidad de niveles
|                               |     |     |     | 𝐼(𝑀) | 𝑏𝑖𝑡  |     |     |     |     |
| ----------------------------- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- |
|   - Tasa de información (𝑅):  |     |     |     | =    | [ ]  |     |     |     |     |
|                               |     |     |     | 𝑇    | 𝑠𝑒𝑔  |     |     |     |     |
1
|   - Velocidad de señalización (𝑠):  |     |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝜏 𝑚𝑖𝑛
𝑁 𝑏𝑖𝑛𝑖𝑡
|   - Tasa de dígitos:                    |     |        | = [   | ]   |       |         |     |     |     |
| --------------------------------------- | --- | ------ | ----- | --- | ----- | ------- | --- | --- | --- |
|                                         |     | 𝑇      | 𝑠𝑒𝑔   |     |       |         |     |     |     |
|   - Cantidad de mensajes posibles: 𝑀(𝑇) |     |        |       |     |       | = 𝜇𝑛    |     |     |     |
|                                         | 1   |        |       |     |       | 𝑛lg     | 𝜇   |     |     |
|   - 𝑷(𝑴)                                | =   | ⇒ 𝑰(𝑴) | = 𝑛lg | 𝜇   | ⇒ 𝑹 = | 2       |     |     |     |
|                                         | 𝜇𝑛  |        |       | 2   |       | 𝑇       |     |     |     |

Detección de errores
Paridad por zonas – código Hamming: cada dígito de control será la paridad par del
conjunto de dígitos de información incluidos en su zona:
|     |     |     |     |     |     | 0   | = 𝐶1 | ⊕ 𝐼 ⊕ 𝐼 | ⊕ 𝐼   |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ----- |
|     |     |     |     |     |     |     |      | 0 1     | 2     |
|     |     |     |     |     |     | 0   | = 𝐶2 | ⊕ 𝐼 ⊕ 𝐼 | ⊕ 𝐼   |
|     |     |     |     |     |     |     |      | 1 2     | 3     |
|     |     |     |     |     |     | 0   | = 𝐶3 | ⊕ 𝐼 ⊕ 𝐼 | ⊕ 𝐼   |
|     |     |     |     |     |     |     |      | 0 2     | 3     |
En el receptor genero nuevamente los dígitos de control y los
comparo con los dígitos de control recibidos.
Los dígitos de control se descartan una vez realizada el
control y la corrección.
Ganancia y atenuación
Ganancia: relación entre la magnitud de salida y la de entrada.
Atenuación: relación entre la magnitud de entrada y la de salida.
|     |     | 𝐴     | =   | 10log𝐴 |                  𝐺 |     |      | = 10log𝐺  |     |
| --- | --- | ----- | --- | ------ | ------------------ | --- | ---- | --------- | --- |
|     |     | 𝐻(𝑑𝑏) |     |        | 𝐻                  |     | (𝑑𝑏) |           |     |

Sistemas de telecomunicaciones

Transductor de entrada y salida: realiza la adaptación de las señales (mensajes) de entrada
y salida, tal que el sistema pueda ser manejado por el hombre. Esto es necesario porque el
emisor y el receptor son dispositivos que trabajan con señales eléctricas, mientras que las
entradas y las salidas normales no lo son (acústicas, visuales, alfanuméricas).
Sistemas de emisión y recepción: adaptan las señales entregadas por el transductor de
entrada al canal mediante el emisor o transmisor, y luego convertirlas en señales útiles al
transductor de salida a través del receptor. Esta adaptación se realiza cambiando los niveles
de potencia de la señal, su frecuencia e incluso, en algunos casos, su forma de onda.
Canal: enlace entre un emisor y su correspondiente receptor, es decir, es el camino por el
cual se envía la información. En el es donde pueden presentarse perturbaciones como la
Distorsión, la Interferencia y el Ruido. Las dos primeras, teóricamente se pueden eliminar,
mientras que el ruido no.
La fuente genera Información (mensajes a transmitir), y no necesariamente en forma de
impulsos eléctricos. Información es todo aquello que elimina una incertidumbre y que
ayuda a tomar una decisión.
Transmisor: tres etapas: filtrado, procesamiento de la señal, amplificación.
Tipos de perturbaciones:
- Ruido: comportamiento aleatorio, independiente de la señal, inevitable.
- Interferencia: señal parecida a la transmitida que se mete en el canal.
- Distorsión: generada por el canal, debido a la atenuación no constante.
Medios de transmisión
Confinados: par trenzado, coaxial, fo, guía de andar.
No confinados: radiotransmisión, microondas, infrarrojo, láser, satélite.
Cable Coaxial:
Dos clases:
Banda base (fino): 200m- 250Mhz.
50 Ohms: tx digital.
Banda ancha (grueso): 500m- 500Mhz
75 Ohms: tx analógica y tv por cable.

Cable Par Trenzado:
UTP: par trenzado sin blindaje. Mas barato, fácil uso, producen más errores, limitaciones
por distancia, impedancia 100 ohmios.
STP: par trenzado blindado. Cables aislados dentro de una cubierta protectora. Se utiliza en
redes de ordenadores. Caro, impedancia 150 ohmios.
FTP: par trenzado con blindaje global: pantalla conductora en forma trenzada, impedancia
120 ohmios.
Fibra:
El emisor en fibra optica se denomina: diodo emisor de luz o LED laser.
El receptor en fibra óptica se denomina: fotodiodo.
La fibra monomodo: ninguna de las anteriores es válida.
Fibra multimodo: menos frágil y costosa que la monomodo.
La transm por fibra: longitud de onda 1300 nm
Ley de snell: ángulos de incidencia y reflexión de la luz dentro de la fibra óptica.
Propagación FO: mayor que cualquier medio.
Pelos de fibra para Tx y Rx: 2
Perdidas en fibra debido a un empalme: 3%
Microondas:
Microondas: 1000-38000 Mhz
Microondas: bajo costo, fácil instalación
Microondas: frecuencia elevada y longitud de onda pequeña
Microondas: medio mas eficiente terrestre.
Microondas punto a punto: 100m altura-80km
Desvanecimiento trayectoria multiple microondas: emitidas por re terrestre, rebotan en la atmosfera luego llegan al
receptor y causan interferencias.
Onda 2,4 Ghz: longitud de onda 125mm CALCULO: 3*10^8= longitud de onda*frecuencia
UTP:
Entre cat 5 y cat 6: el cat 6 tiene mas vueltas por metro que el cat 5.

Trenzado UTP: Disminuir la interferencia entre pares
Pines UTP: 8
Satélite:
Satélite orbita baja: 700km
Satélite orbita media: 10000km
Satélite Geo: 10 años vida útil
Banda L satélite: 1.5/1.6 GHz
Banda S satélite: 1.9/2.2 GHz
Banda C satélite: 4/6 GHz
Banda Ku satélite: 11/14 Ghz
Banda Ka satélite: 20/30 GHz
Satelite: transpondedor 50 a 100 mhz
Vsat: Very Small Amplitude Terminals
Vida útil satélite: 10 años
Coaxial:
Banda ancha con cable coaxial: utiliza el cableado de 50 Ohms para banda ancha. Falso
Banda base con cable coaxial: utiliza el cableado de 50 Ohms para banda base. Verdadero
Infrarrojas y laser:
Las infrarrojas: se pueden utilizar en una lan con haces desenfocados para conectar PC
Infrarrojas: no se puede en exteriores por la luz solar
Infrarrojo: requiere baja inversión en su implementación