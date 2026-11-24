24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
El Santo Resumen
Comunicación de Datos
Ingeniería en Sistemas, UTN
QUÉ TIENE
1. Para entender
2. 1° parcial
3. 2° parcial
4. Final
DE DÓNDE SALE
Resumen armado a partir del material del Drive de UTN (exámenes hasta 2025). Si el
programa cambió, manda la cátedra.
Los quiz, los ejercicios de examen y las figuras que se mueven están en la web.
https://lutastudios.com/utn/comunicacion-de-datos/pdf.html 1/60

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
COMUNICACIÓN DE DATOS
Para entender
Cómo llevar información de un punto a otro: cuánta hay, cómo se codifica,
cómo viaja por un canal con ruido y cómo se dimensiona la red.
Resumen no juzgado. Todavía nadie evaluó si alcanza para estudiar solo con esto.
Los exámenes de 2022 o antes son del plan anterior. En esta materia el contenido es el
mismo, así que siguen sirviendo.
La idea general
Mandar un dato parece simple hasta que aparecen tres problemas. El canal tiene un límite de
velocidad, el ruido cambia bits y muchos usuarios quieren usar lo mismo a la vez. Casi toda la materia
es una respuesta a alguno de esos tres.
Primero la materia mide. Un mensaje poco probable trae más información que uno esperado, y esa
cantidad se mide en bits. Con esa medida se puede comparar lo que emite una fuente con lo que
aguanta un canal.
Después adapta. La información se codifica para ocupar menos, se le agrega redundancia para detectar
errores y se modula para que el medio la pueda transportar.
Al final dimensiona. Con teoría de colas se calcula cuánto espera un mensaje en un nodo, y con eso se
decide cuánta capacidad darle a cada enlace.
El recorrido
Dónde
Bloque Pregunta que contesta
está
Sistema de ¿Qué partes tiene y qué lo perturba? 1° parcial
telecomunicaciones
Transmisión multinivel ¿Cuántos bits por segundo salen de estos 1° parcial
pulsos?
Teoría de la información ¿Cuánta información hay y cuánta llega? 1° parcial
Códigos ¿Cómo la represento gastando lo menos posible? 1° parcial
Errores ¿Cómo detecto y corrijo lo que cambió el ruido? 1° parcial
Medios ¿Por dónde viaja la señal? 1° parcial
2

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Dónde
Bloque Pregunta que contesta
está
Modulación y multiplexado ¿Cómo comparto un canal entre muchas 2° parcial
señales?
Medio de acceso ¿Qué le contrato a una empresa según dónde 2° parcial
está?
Colas y capacidad ¿Cuánto espera un mensaje y cuánto canal le 2° parcial
doy?
Modelo OSI ¿Dónde cae todo esto en una red? 2° parcial
Cómo se conecta
La entropía dice cuánta información emite una fuente por símbolo. Multiplicada por los dígitos por
segundo da la tasa de informaciónR. El teorema del canal compara esa R con la capacidadC. Si R no
supera a C, existe una codificación que transmite con error tan chico como se quiera.
La longitud media de un código no puede bajar de la entropía. Por eso un código compacto ahorra, y
agregarle redundancia para corregir errores le baja el rendimiento. Confiabilidad y economía tiran
para lados opuestos.
La tasa de Nyquist une señal y canal. Fija cada cuánto muestrear, y eso define cuánto dura una trama
TDM y qué ancho de banda hace falta.
La cola M/M/1 de un nodo es el mismo modelo que usa la asignación de capacidad. Si las colas te salen,
el retardo de un enlace también.
Qué se evalúa y cómo
Leí 16 hojas de examen de 2023 a 2025. De ahí sale lo que sigue.
1° parcial. Tiene práctica y teoría. Las cuatro prácticas de 2023 a 2025 piden graficar el sistema de
telecomunicaciones y resolver una transmisión multinivel a partir de un gráfico. Tres de ellas piden
además explicar la atenuación. El multiple choice de 2025 sobre medios trae 24 consignas, y el de 2023
repite varias.
2° parcial. Encontré dos modelos según la comisión. Uno gira alrededor de la trama digital y el
multiplexado, con definiciones de señales. El otro gira alrededor de colas abiertas, con un problema
M/M/1 y preguntas de capacidad.
Final. Solo hay uno de 2023 en adelante, el del 04/04/2025. Tiene una hoja de práctica con tres
problemas y otra de teoría con tres consignas.
3

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Lo de antes de 2023 acá sigue sirviendo
Lo de 2022 para atrás es del plan viejo. Igual comparé finales de 2021 con el de 2025 y volvieron
dos problemas con los mismos números. El 2° parcial de 2022 y uno de 2025 repiten la misma
trama. Por eso esta materia usa también ese material, y cada ejercicio muestra su año.
No hay resoluciones oficiales
Todo lo resuelto que hay en el Drive es de alumnos o no tiene firma. Por eso los ejercicios van
solo con el enunciado. Las respuestas teóricas de estas páginas salen de los apuntes y citan
archivo y página.
Cómo usar esto
Leé la página de tu parcial de arriba abajo. Las partes en amarillo son lo que se tomó en un examen
que leí. Después hacé los ejercicios sin mirar nada y usá la hoja de repaso para las fórmulas.
4

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
COMUNICACIÓN DE DATOS
1° parcial
Qué es un sistema de telecomunicaciones, cómo se calcula una transmisión
multinivel, cuánta información hay, cómo se codifica, cómo se protege de
errores y por qué medio viaja.
Resumen no juzgado. Todavía nadie evaluó si alcanza para estudiar solo con esto.
Cómo viene el examen
Leí cuatro prácticas, una de 2023, dos de 2024 y una de 2025, y los multiple choice de medios de 2023 y
2025.
La práctica tiene una estructura muy estable.
Consigna Hojas
Graficar el sistema de telecomunicaciones, etiquetarlo y explicar cada bloque 4 de 4
Sacar datos de un gráfico multinivel y explicar cómo duplicar la velocidad 4 de 4
Explicar la atenuación. Una hoja de 2024 pidió cómo se calcula, y la de 2025 3 de 4
pidió ejemplos
Calcular R, r y s con pulsos de arranque y parada 3 de 4
Método de Hamming 1 de 4, en
2023
Tipos de perturbaciones y un problema de fax 1 de 4, en
2024
El multiple choice de 2025 trae 24 consignas sobre medios de transmisión. El del 06/07/2023 pregunta
por los mismos medios, y consignas como la ley de Snell, las torres de microondas y UTP categoría 5
contra 6 aparecen en los dos. Una nota del Drive avisa que las preguntas viejas volvieron con palabras
cambiadas para confundir.
La teoría de información y códigos se toma también como multiple choice. No tengo esa hoja de 2025.
La misma nota dice que fue casi idéntica a la del 30/06/2021, que sí leí.
Sistema de telecomunicaciones
Sirve para llevar un mensaje de una fuente a un destino a través de un canal que lo perturba.
5

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Fuente -> Transductor de entrada -> Tx -> Canal -> Rx -> Transductor de salida
-> Destino
^
perturbaciones
Graficar, etiquetar y desarrollar cada elemento
1° parcial 06/07/2023, 1° parcial 2024, dos hojas, y 1° parcial 2025
Tenés que saber dibujar el diagrama de siete bloques y contar qué hace cada uno.
Elemento Qué hace
Fuente Genera la información, no necesariamente como impulsos eléctricos
Transductor de Convierte el mensaje en señal eléctrica, porque Tx y Rx trabajan con
entrada señales eléctricas
Transmisor (Tx) Adapta la señal al canal. Tiene tres etapas: filtrado, procesamiento y
amplificación
Canal Es el enlace entre emisor y receptor. Acá aparecen distorsión,
interferencia y ruido
Receptor (Rx) Hace el trabajo inverso y además tiene que lidiar con las
perturbaciones
Transductor de Pasa la señal eléctrica a algo que el destino entienda
salida
Destino Recibe la información
Fuente: apunte «1 - Principios Básicos», sección «Sistema de Telecomunicaciones» (página 14 de su
índice).
La información es todo lo que elimina una incertidumbre y ayuda a tomar una decisión.
Por qué se modula en el transmisor
El apunte da tres razones. Sirve para adaptar la señal al medio, para combatir interferencia y ruido, y
para multiplexar varias señales en un mismo canal.
6

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Perturbaciones
Enumerar los tipos y explicar uno
1° parcial 2024
Son tres y hay una diferencia que conviene decir, y es que distorsión e interferencia se pueden
eliminar en teoría. El ruido no.
Perturb
Qué es ¿Se elimina?
ación
Distors Altera la forma de la señal por la respuesta imperfecta del Sí, en teoría. Si es lineal
ión sistema. Desaparece cuando la señal deja de aplicarse se corrige
Interfe Contaminación por señales extrañas con forma parecida, Sí, en teoría,
rencia generalmente de origen artificial eliminando la señal o
su fuente
Ruido Señal aleatoria e impredecible, de origen natural No. Solo se mejora la
relación señal a ruido
Fuente: apunte «1 - Principios Básicos», secciones «Sistema de Telecomunicaciones» y «Ruido como
elemento limitante» (páginas 14 y 18 de su índice).
En criollo
Pensá en una llamada. Si la voz sale metálica porque el parlante es malo, es distorsión. Si se
escucha otra conversación, es interferencia. Si hay un «shhh» de fondo que nadie genera a
propósito, es ruido.
El mismo apunte lista estos tipos de ruido: atmosférico, térmico, hecho por el hombre, impulsivo y
diafonía. El ruido blanco nace de la agitación molecular por temperatura. Es imposible de eliminar
por ser aleatorio (apunte «Errores en Canales», página 1).
El apunte «Errores en Canales» agrega otras causas de error (páginas 2 a 4):
Ruido impulsivo: grandes picos que afectan varios binits. Eso se llama ráfaga. Es la principal fuente
de error de canal.
Modulaciones espurias: modulación cruzada, intermodulación y eco.
Variaciones de nivel: incluye el desvanecimiento, por ejemplo por lluvia en microondas.
Distorsiones del canal: atenuación, fase y frecuencia, variación de la portadora y variación del
umbral de muestreo.
7

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Ganancia, atenuación y decibeles
Explicar qué es la atenuación
1° parcial 2024, dos hojas, y 1° parcial 2025
Una hoja de 2024 pidió también cómo se calcula y la de 2025 pidió ejemplos.
La ganancia es la relación entre la magnitud de salida y la de entrada que la provoca. La atenuación es
la inversa.
| P       | 1     | P   |
| ------- | ----- | --- |
| G = o   | A = = | i   |
p
|   P   | G   | P   |
| ----- | --- | --- |
| i     |     | o   |
Como los niveles cubren un rango enorme, se expresan en forma logarítmica. Así la ganancia total de
varias etapas sale sumando las parciales.
P
| X   | i         |     |
| --- | --------- | --- |
| dB  | = 10log   |     |
  P
o

Si la impedancia es la misma en los dos puntos, se puede medir con tensión o corriente.
|            | E       | I   |
| ---------- | ------- | --- |
| X          | 1       | 1   |
| dB = 20log | = 20log |     |
|            | E       | I   |
|            | 2       | 2   |
Fuente: apunte «1 - Principios Básicos», secciones «Niveles», «Ganancia y Atenuación» y «El decibel
relativo» (páginas 9 a 11 de su índice).
▾ ¿Qué es la atenuación?
1° parcial 2025
Es la relación entre la magnitud de entrada de un sistema y la salida que ella provoca, es decir, la
inversa de la ganancia. En sistemas pasivos, como cables, se usa como expresión normal de la
transferencia. El apunte de medios la presenta como la pérdida de potencia a través del medio,
expresada en decibeles. Como ejemplo, el apunte define la Unidad de Transmisión con una
atenuación de 10 veces sobre 10 millas de cable telefónico. Fuente: «1 - Principios Básicos»,
páginas 10 y 11 de su índice; «3 - Medios de transmisión», página 9.
La atenuación es del medio
No la confundas con el ruido. El ruido se suma a la señal desde afuera. La atenuación aparece por
el propio medio y es «el menos perjudicial» de los efectos, según el apunte «Principios Básicos»
(sección «Ruido como elemento limitante»).
8

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Los apuntes no coinciden en una fórmula
«Errores en Canales» (página 1) escribe 10logG también para amplitudes. «Principios Básicos»
usa 20log para tensión o corriente con la misma impedancia. Acá seguimos «Principios Básicos»,
que además explica de dónde sale.
Respuesta en frecuencia y ancho de banda
Ningún sistema reproduce igual todas las frecuencias. Las frecuencias de corte son aquellas donde la
potencia cae a la mitad de su máximo, o sea donde la curva cae 3 dB.
AB = f −f
2 1
Si la frecuencia inferior de corte es chica, el ancho de banda se puede aproximar a la superior. Fuente:
«1 - Principios Básicos», página 12 de su índice; «Errores en Canales», página 1.
Relación señal a ruido y rango dinámico
La relación señal a ruido compara la potencia de la señal con la del ruido, en decibeles. Cuanto más
alta, mejor. El rango dinámico es la diferencia entre el nivel máximo que emite un dispositivo y su
ruido de fondo (apunte «Principios Básicos», página 13 de su índice).
Banda base y modulación
En banda base no hay corrimiento del espectro de frecuencias. En modulación sí lo hay. El apunte
aclara que banda base es una sola transmisión en un canal, y banda ancha lleva más de una señal en
canales distintos.
Transmisión multinivel
Una transmisión es multinivel cuando cada pulso puede tomar más de dos niveles. Con más niveles,
cada pulso lleva más bits sin cambiar su duración.
Calcular datos desde un gráfico, y cómo duplicar la velocidad
1° parcial 06/07/2023, 1° parcial 2024, dos hojas, y 1° parcial 2025
Las cuatro hojas muestran un primer bloque multinivel y un segundo bloque de n pulsos binarios
dentro de un período T. Te dan R y T. La hoja de 2025 pide cantidad de niveles, información total,
cantidad de pulsos y cómo duplicar la velocidad.
9

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Las fórmulas
| Magnitud           |     |     |     | Fórmula   |     |     | Unidad   |
| ------------------ | --- | --- | --- | --------- | --- | --- | -------- |
| Mensajes distintos |     |     |     | M(T) = μn |     |     | mensajes |
| Información        |     |     |     |           |     |     | bits     |
I = lgM(T)
| Tasa de información |     |     |     | R = I/T |     |     | bps      |
| ------------------- | --- | --- | --- | ------- | --- | --- | -------- |
| Tasa de dígitos     |     |     |     |         |     |     | binits/s |
r = dˊıgitos totales/T
| Velocidad de señalización |     |     |     | s = 1/τ |     |     | baudios |
| ------------------------- | --- | --- | --- | ------- | --- | --- | ------- |
min

Acá μ es la cantidad de niveles, n los pulsos de información y τ la duración de un pulso. Si todos los
pulsos son de información y duran lo mismo, n = T/τ y queda R = 1 lgμ.
τ
Para la calculadora: lgN 3,32logN. Fuente: «1 - Información, Codificación y Canales»,
|     |     | = logN/log2 ≈ |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- |
páginas 2, 11 y 12.
La diferencia entre R, r y s
R cuenta solo lo que informa. r cuenta todos los dígitos, informen o no. s imagina que todos los pulsos
duran lo mismo que el más corto.
Calcular R, r y s con arranque, stop y un pulso más largo
1° parcial 06/07/2023, 1° parcial 2024 y 1° parcial 2025
El apunte tiene un ejemplo del mismo tipo con otros números. Hay arranque y parada, y el total
dura 150 ms.
Este es el ejemplo del apunte, con sus números. El pulso más corto dura 20 ms. Hay 5 dígitos de
información y 7 en total.
|     | 1     |              |     | 7      |     | 5        |     |
| --- | ----- | ------------ | --- | ------ | --- | -------- | --- |
|     | s =   | = 50 baudios | r = | ≈ 46   | R = | ≈ 33 bps |     |
|     | 20ms  |              |     | 150ms  |     | 150ms    |     |
Fuente: «1 - Principios Básicos», sección «Algunos conceptos fundamentales» (página 21 de su índice).
Arranque y parada
Cuentan para el tiempo T y para r, pero no para la información, porque tienen valor fijo. El
apunte lo muestra en su ejercicio 11, con 13 pulsos de 58 niveles más arranque y stop de 10 µs
cada pulso. Ahí T 150μs y M(T) 5813. Da I 77 bits y R 513 Kbps. Fuente: «2
|     | =   | 15×10μs = |     | =   | ≈   | ≈   |     |
| --- | --- | --------- | --- | --- | --- | --- | --- |
- Transmisión Multinivel (Resuelto)», página 4.
10

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Cómo contar niveles
Contá los niveles en el eje del gráfico, y el 0 cuenta si la consigna o el gráfico lo incluyen. En el
ejercicio 14 del apunte, «se ha considerado el 0 como un nivel posible». La hoja de 2025 lo aclara
en la propia consigna.
Tasa de información según los niveles
Fuente: 1 - Información, Codificación y Canales, pág. 12
RR  ((KKbbppss))
660000
550000
440000
330000
220000
110000
55 1100 1155 2200 2255 3300 3355 4400 4455 5500 5555 NNiivvee66ll00eess  μ
μ
R
Varios bloques en una misma transmisión
Si hay subsistemas, los mensajes se multiplican y por lo tanto las informaciones se suman.
|     |     | M(T) = | M ×M | I = lgM +lgM |
| --- | --- | ------ | ---- | ------------ |
|     |     |        | 1 2  | 1 2          |
|     |     |        |      |              |
El ejercicio 14 del apunte tiene un bloque de 5 pulsos de 7 niveles que dura 100 µs y uno de 8 pulsos
binarios que dura 40 ms.
| 1. I = 5lg7+8lg2 | ≈ 14+8       | = 22 bits. |     |     |
| ---------------- | ------------ | ---------- | --- | --- |
| 2. T             | 40,1ms.      |            |     |     |
| = 100μs+40ms     | =            |            |     |     |
| 3. R = 22/40,1ms | ≈ 548,6 bps. |            |     |     |
Fuente: «2 - Transmisión Multinivel (Resuelto)», páginas 5 y 6.
11

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Cómo se duplica la velocidad
Si no se pueden tocar los tiempos, lo único que queda es aumentar los niveles. El apunte plantea dos
opciones: cambiar los niveles del bloque multinivel o los del binario.
Siguiendo el ejercicio 14, se duplica R y se vuelve a plantear la ecuación con la incógnita μ en el bloque
elegido. Ahí 5lgμ+8 = 2R⋅T, sale μ ≈ 146,8 y se redondea para arriba a 147 niveles. Fuente: «2 -
Transmisión Multinivel (Resuelto)», página 6.
Redondeá los niveles para arriba. Con menos niveles no llegás a la velocidad
pedida.
Problemas de imágenes y fax
Tiempo para transmitir una imagen de fax
1° parcial 2024
Se piensa cada punto como un pulso y el brillo como sus niveles.
El ejercicio 13 del apunte tiene 400 líneas de 400 puntos, 64 niveles y 4800 bps. Son 160.000 puntos de
lg64 = 6 bits, o sea 960.000 bits. Entonces T = 960.000/4.800 = 200 s. Fuente: «2 - Transmisión
Multinivel (Resuelto)», página 5.
Información, entropía y canal
Cuánta información trae un suceso
Cuanto menos esperado es un suceso, más información trae. Si es seguro, no trae ninguna.
1
I(A) = lg [bits]
p(A)
Se usa logaritmo porque es la única función que vale cero en 1, tiende a infinito en 0 y convierte el
producto de probabilidades en suma de informaciones. El apunte reserva bit para la información y
binit para el dígito binario. Fuente: «1 - Información, Codificación y Canales», páginas 1 y 2.
Entropía de la fuente
La fuente emite símbolos con cierta probabilidad. La entropía es la esperanza matemática de la
información por símbolo de la fuente.
1
H(S) = p lg
∑ i p
i
i
12

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Es máxima cuando los símbolos son equiprobables. El estudio se centra en fuentes ergódicas y de
memoria nula. Fuente: mismo apunte, páginas 3 y 4.
En criollo
Si un dado está cargado y casi siempre sale 6, tirarlo te dice poco, porque ya lo esperabas. Esa
fuente tiene entropía baja. Un dado parejo te sorprende más en cada tiro, y su entropía es la
máxima para seis caras.
Entropía de una fuente de dos símbolos
Fuente: 1 - Información, Codificación y Canales, pág. 4
HH ((bbiittss))
mmááxxiimmoo
11,,00
00,,99
00,,88
00,,77
00,,66
00,,55
00,,44
00,,33
00,,22
00,,11
00,,11 00,,22 00,,33 00,,44 00,,55 00,,66 00,,77 00,,88 00,,99 pp
H
El canal
Un canal se define por sus alfabetos de entrada y salida y por las probabilidades condicionales
P(b /a ). Es la probabilidad de recibir b cuando se envió a .
j i j i
Canal transparente: no introduce error. Su matriz es diagonal.
Canal binario simétrico: tiene dos entradas y dos salidas, y P(b /a ) = P(b /a ). Esa probabilidad
1 2 2 1
es la probabilidad de error p.
Probabilidades de salida y hacia atrás, según Bayes:
P(a )P(b /a )
P(b ) = P(a )P(b /a ) P(a /b ) = i j i
j ∑ i j i i j P(b )
j
i
Fuente: mismo apunte, páginas 5 y 6.
13

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Entropías del sistema
| Nombre        |     | Fórmula |       |     |       |     | Qué mide                     |     |
| ------------- | --- | ------- | ----- | --- | ----- | --- | ---------------------------- | --- |
| A priori      |     | H(A) =  | ∑ P(a | )lg | 1     |     | Incertidumbre de la entrada  |     |
|               |     |         | i     | i   | P( a  |     |                              |     |
|               |     |         |       |     | i  )  |     |                              |     |
| A posteriori, |     | H(A/B)  | =     |     |       |     | Lo que queda sin saber de la |     |
equivocación de A −∑ P(b )P(a /b )lgP(a /b ) fuente después de recibir
|     |     |     | j   | i   | j   | i j |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | ij  |     |     |     |     |     |     |
respecto de B
| Del canal, equivocación |     |        |      |     |        |      | Lo que introduce el canal |     |
| ----------------------- | --- | ------ | ---- | --- | ------ | ---- | ------------------------- | --- |
|                         |     | H(B/A) | =    |     |        |      |                           |     |
| de B respecto de A      |     | −∑ P(a | )P(b | /a  | )lgP(b | /a ) |                           |     |
|                         |     |        | i    | j   | i      | j i  |                           |     |
|                         |     | ij     |      |     |        |      |                           |     |
Información mutua
Es la información transferida desde la fuente al receptor a través del canal, esto es, la información real
que llega al receptor en promedio. Fuente: mismo apunte, página 8.
Simetría de la información mutua
Una importante propiedad de la información mutua es la simetría con respecto a las variables de
entrada y salida, entonces es valido decir que:
|     |     | I(A,B) | = I(B,A) | =   | H(B)−H(B/A) |     | (12) |     |
| --- | --- | ------ | -------- | --- | ----------- | --- | ---- | --- |
En el caso de canales transparentes:
|     | H(A) | = H(B) = | H(A,B) | = I(A,B) |     | H(A/B) | = H(B/A) | = 0 |
| --- | ---- | -------- | ------ | -------- | --- | ------ | -------- | --- |
«1 - Información, Codificación y Canales», pág. 8
Lo que recibís es lo que había menos lo que el canal «bloqueó». Por eso se resta la
equivocación.
Capacidad y eficiencia
Información mutua en función de las probabilidades conjuntas
Supuesto un canal de alfabeto de salida B y probabilidades condicionales P(b ) la información
/a
j   i
mutua resulta:
P(a /b )
|     | I(A,B) | = H(A)−H(A/B) |     | =   |     | P(a ,b ) | lg i   j   | (13) |
| --- | ------ | ------------- | --- | --- | --- | -------- | ---------- | ---- |
i j
|     |     |     |     |     | ∑ ∑  |     | P(a )   |     |
| --- | --- | --- | --- | --- | ---- | --- | ------- | --- |
|     |     |     |     |     | j i  |     | i       |     |
«1 - Información, Codificación y Canales», pág. 8
14

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Demostración
ya que:
|     |     |      |     | I(A,B)   | = H(A)−H(A/B) |      |                  |         |     |
| --- | --- | ---- | --- | -------- | ------------- | ---- | ---------------- | ------- | --- |
|     |     | = −  | P(a | )lgP(a   | )+            |      | P(a ,b )lgP(a    | /b )    |     |
|     |     | ∑    |     | i        | i             | ∑ ∑  | i   j            | i   j   |     |
|     |     | i    |     |          |               | j i  |                  |         |     |
|     |     | =    |     | P(a i ,b | j )lgP(a      | i /b | j )−P(a i )lgP(a | i )     |     |
|     |     | ∑ ∑  |     |          |               |      |                  |         |     |
|     |     |      | j i |          |               |      |                  |         |     |
(∗)
|     |     | =    | P(a | ,b  | )lgP(a | /b )−P(a | ,b )lgP(a | )   |     |
| --- | --- | ---- | --- | --- | ------ | -------- | --------- | --- | --- |
|     |     | ∑ ∑  |     | i   | j      | i   j    | i   j     | i   |     |
j i
|     |     |     |      |     |        |       | P(a ,b ) |     |     |
| --- | --- | --- | ---- | --- | ------ | ----- | -------- | --- | --- |
|     |     |     | (∗∗) |     | P(a ,b |       | i j      |     |     |
|     |     |     | =    |     | i      | j )lg |          |     |     |
|     |     |     |      | ∑   |        |   P(a | )P(b )   |     |     |
|     |     |     |      |     |        |       | i j      |     |     |
|     |     |     |      |     |        |       |          |     |     |
(*) Se a introducido dentro de la sumatoria sobre j la expresión de la H(A), esto es posible ya que ella
es independiente de ese subíndice. Ahora, si reemplazamos P(a ) por P(a ,b ) la expresión no
|     |     |     |     |     |     |     | i   | i   | j   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |
cambia ya que al sumar sobre todos los símbolos de la salida (cuando se realiza la sumatoria sobre j)
resulta P(a ) nuevamente.
i
| (**) Es válido ya que P(a |     | /b )P(b | ) = | P(a ,b | ).  |     |     |     |     |
| ------------------------- | --- | ------- | --- | ------ | --- | --- | --- | --- | --- |
|                           |     | i j     | j   | i      | j   |     |     |     |     |
|                           |     |         |     |        |     |     |     |     |     |
«1 - Información, Codificación y Canales», págs. 8 y 9
Canal transparente con fuente equiprobable
En los canales transparentes H(A/B) 0 y resulta I(A,B) H(A), entonces
|     |     |     |     | =   |     |     | = H(A)−H(A/B) |     | =   |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
C = maxH(A). Si la fuente resultara equiprobable, H(A) = lgn (bit/simb) y C = lgn (bit/simb).
«1 - Información, Codificación y Canales», pág. 9
La capacidad es el valor máximo de la información mutua, que se logra sintonizando la fuente. Será
función exclusivamente de las probabilidades condicionales y no dependerá de las probabilidades de
los símbolos de entrada. El valor mínimo de I(A,B) es cero (página 9).
I(A,B)
|     | C   | = maxI(A,B) |     | FF  | =   |     | RED | = 1−FF |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- | ------ | --- |
|     |     |             |     |     |     | C   |     |        |     |
En un canal transparente con fuente equiprobable, C = lgn bit/símbolo. En el caso binario con
símbolos de duración τ, C = 1/τ bps. Fuente: mismo apunte, páginas 9 y 10.
Las velocidades, definidas
| Concepto |     | Definición del apunte |     |     |     |     |     |     |     |
| -------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
Tasa de información Cantidad de información promedio producida por una fuente en un
| R   |     | segundo |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
15

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Concepto Definición del apunte
Tasa de dígitos r Cantidad de dígitos por segundo transmitidos
Relación R = rH(A)
Con ruido R = H′(A)−H′(A/B)
Señalización s Inversa del tiempo mínimo que dura un pulso
Fuente: mismo apunte, páginas 10 y 11.
Capacidad, velocidad y ancho de banda
Capacidad de un canal y velocidad de información
La capacidad de un canal es su capacidad de transportar información. Se mide en bits/seg. y una
fuente con tasa de información promedio R, si R ≤ C existe una codificación tal que la salida de
la fuente pude ser transmitida sobre el canal con una frecuencia arbitrariamente pequeña de
error, a pesar de la existencia de ruido. Si R > C no es posible transmitir sin error.
«1 - Información, Codificación y Canales», pág. 11
Errata del apunte
La hoja imprime «S R > C». Puse «Si R > C», porque la frase es la condición contraria a la
anterior y le falta la letra. Fuente: «1 - Información, Codificación y Canales», pág. 11.
Fuente binaria
Si son sucesos equiprobables y τ = τ , entonces R es máximo y deberá ser C = R . Si el sistema
min max
es binario, la capacidad de canal coincide con la de señalización, C = s, y el ancho de banda resulta
B = s/2.
«1 - Información, Codificación y Canales», pág. 12
En criollo
Es como una ruta con un máximo de autos por hora. Si mandás menos que ese máximo, existe
alguna forma de organizarlos para que casi ninguno choque. Si mandás más, no hay organización
que alcance.
16

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Capacidad de un canal con ruido, Hartley y Shannon
Estudios de Hartley y posteriores trabajos de Shannon prueban que si la potencia media del ruido
blanco es N, entonces, la entropía media del canal o equivocación de Y respecto de X es:
H(Y/X) = B ⋅lg(2⋅π⋅e⋅N)
En la expresión, B es el ancho de banda del canal, N es la potencia media del ruido y e es el
número neperiano.
La señal emitida es continua y con distribución normal, la entropía en la recepción para una
potencia media S es:
H(Y) = B ⋅lg(2⋅π⋅e⋅(N +S))
Entonces la capacidad del canal:
C = I(X,Y) = H(Y)−H(Y/X) = B ⋅lg(1+S/N) [bps]
«Errores en Canales», pág. 2
Errata del apunte
Tres cambios respecto de la hoja. Fuente: «Errores en Canales», pág. 2.
Imprime «2 . | | . e . N» con un símbolo que no se lee. Puse π, porque el símbolo perdido va
entre 2 y e, y lo confirma la cuenta. La resta solo da lg(1+S/N) si el factor es el mismo en las
dos entropías. Esa lectura es mía.
Imprime «distribución mal». Puse «distribución normal», porque la palabra está cortada.
Imprime «H(Y) = H(Y/X)» en la línea de la capacidad. Puse H(Y)−H(Y/X), porque una
igualdad daría capacidad cero y el resultado Blg(1+S/N) solo sale de la resta.
Canal de 1000 Hz
Con B = 1000 Hz y S/N = 3, la expresión da C = 1000⋅lg(1+3) = 1000⋅2 = 2000 bps.
Armado para este resumen
Códigos
Codificar es poner en correspondencia secuencias de un alfabeto fuente S con secuencias de un
alfabeto código Z.
17

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
La familia de códigos, de lo general a lo particular
Definir unívoco, instantáneo, compacto, Kraft y cota inferior
Final 04/04/2025 y 1° parcial 30/06/2021
Se pide definir cada concepto. En el multiple choice las opciones se parecen mucho, así que
importan las palabras exactas.
Pági
| Concepto | Definición |     |
| -------- | ---------- | --- |
na
Código Asigna a cada símbolo fuente una secuencia fija de símbolos del alfabeto 1
| bloque  | código             |     |
| ------- | ------------------ | --- |
| Palabra | Esa secuencia fija | 1   |
código
| No  | Todas sus palabras son distintas | 1   |
| --- | -------------------------------- | --- |
singular
Unívoco A cualquier secuencia de palabras código le corresponde una y solo una 1
secuencia de símbolos fuente
Instantán Ninguna palabra coincide con el prefijo de otra. Es condición necesaria y 2
| eo  | suficiente |     |
| --- | ---------- | --- |
Compacto Instantáneo con longitud media igual o menor que la de todos los 5
instantáneos para esa fuente y ese alfabeto
Fuente: apunte «2 - Codificación», en las páginas de la tabla.
El apunte muestra un código no singular que no es unívoco: S1=1, S2=11, S3=00, S4=10. Si llega 1100,
puede ser S2 S3 o S1 S1 S3 (página 1).
Da además otra definición: «Un código bloque se dice unívocamente decodificado sí y solo sí su
extensión de orden n es no singular para cualquier valor finito de n» (página 2).
Condición de código instantáneo
Sea Z z ;z ;z  una palabra de código. Se denomina prefijo de esta palabra a la secuencia
| i = | i1 i2 ;… im |     |
| --- | ----------- | --- |
|     |             |     |
 con j m. A partir de esto se puede enunciar: «La condición necesaria y suficiente
| z ;z ;… | ;z ≤ |     |
| ------- | ---- | --- |
| i1  i2  | ij   |     |
para que un código sea instantáneo es que ninguna palabra del código coincida con el prefijo de
otra».
«2 - Codificación», pág. 2
18

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Códigos A y B
Con el código A (0, 01, 011, 0111), 0 es prefijo de 01: al recibir 01 hay que esperar el símbolo
siguiente. Con el código B (1, 01, 001, 0001) se decodifica instantáneamente.
«2 - Codificación», pág. 2
Inecuación de Kraft
Inecuación de Kraft
Si los enteros l ;l ;… ;l satisfacen la inecuación:
1 2 q
q
r−l i ≤ 1 (4.6.1)
∑
i=1
Entonces esta es condición suficiente y necesaria para que exista al menos un código instantáneo
de r símbolos en su alfabeto y cuyas q palabras códigos tienen las longitudes l ;l ;… ;l
1 2 q
respectivamente.
Nota: el teorema no dice que cualquier código cuyas longitudes cumplan la condición (4.6.1) es un
código instantáneo.
«2 - Codificación», págs. 2 y 3
Cumple Kraft y no es instantáneo
El código S1=0, S2=00, S3=11 da ∑2−li = 2−1 +2−2 +2−2 = 1/2+1/4+1/4 = 1. Satisface (4.6.1), sin
embargo no es un código instantáneo. El teorema dice que existe algún código de longitud 1, 2, 2 que
es instantáneo, por ejemplo S1=0, S2=10, S3=11.
«2 - Codificación», pág. 3
Ecuación de McMillan
Dado que los códigos instantáneos son una sub-clase de los unívocos, la condición suficiente para
que exista, al menos un código unívoco, es que las longitudes l verifiquen la expresión:
i
q
r−li ≤ 1 (4.7.1)
∑
i=1
es decir, si las longitudes l ;l ;… ;l satisfacen la relación pueden construirse con ellas un código
1 2 q
unívoco. La condición necesaria fue demostrada por Mc. Millan.
«2 - Codificación», pág. 3
19

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Longitud media y su cota
Dado un código bloque que asocia los símbolos de una fuente S ;S ;S  con las palabras
|     |     |     |     |     | ;…    | N   |
| --- | --- | --- | --- | --- | ----- | --- |
|     |     |     |     |     | 1  2  |     |
Z ;Z ;… ;Z  y las probabilidades de los símbolos son P ;P ;… ;P , la longitud media del código L
| 1  2  | N   |     |     | 1  2  | N   |     |
| ----- | --- | --- | --- | ----- | --- | --- |
|       |     |     |     |       |     |     |
se define como (página 5):
N
|     |     |     | L = | P l |     |     |
| --- | --- | --- | --- | --- | --- | --- |
i i
|     |     |     | ∑   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
i=1
Para minimizar L, a mayor probabilidad le toca menor longitud.
Cota inferior de la longitud media
La longitud media de un código es mayor o igual que la entropía de la fuente dividida por el log
2
del número de símbolos del alfabeto código.
H(s)
|     |     | L   | (logaritmo base 2 de x: logx) |     |     |     |
| --- | --- | --- | ----------------------------- | --- | --- | --- |
≤
logr
«2 - Codificación», págs. 5 y 6
La desigualdad con la que arranca la demostración
Fuente: 2 - Codificación, pág. 6
yy
22,,55
| 22,,00 |     |     |     |     | yy  ==  zz  --  11 |     |
| ------ | --- | --- | --- | --- | ------------------ | --- |
11,,55
yy  ==  llnn  zz
11,,00
00,,55
11 zz
|     | 00,,55 11,,00 | 11,,55 | 22,,00 | 22,,55 | 33,,00 | 33,,55 |
| --- | ------------- | ------ | ------ | ------ | ------ | ------ |
−−00,,55
−−11,,00
−−11,,55
−−22,,00
−−22,,55
y = z - 1
y = ln z
Demostración
Es fácil demostrar que:
20

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
|     |     |     |     |     | lnz | ≤ z−1 | (4.9.1) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --- | --- | --- | --- |
multiplicando (4.9.1) por −1:
1
|     |     |     |     |     | ln  | ≥ 1−z |     | (4.9.2) |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | --- |
z
Sean Z(z ;z ;… ;z ) e Y (y ;y ;… ;y ) dos conjuntos de probabilidades; es decir: z ≥ 0, y ≥ 0∀i,j
| 1 2 | q   |     | 1 2 |     | q   |     |     |     |     |     | i j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     |
y
|     |     |     |     |     | q   | q   |       |         |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --- | --- | --- |
|     |     |     |     |     | z   |     | y     |         |     |     |     |
|     |     |     |     |     | i   | =   | i = 1 | (4.9.3) |     |     |     |
|     |     |     |     | ∑   |     | ∑   |       |         |     |     |     |
|     |     |     |     |     | i=1 | i=1 |       |         |     |     |     |
podemos escribir, haciendo uso de log a:
|     |     |     |     |     | a  z = | 1/log | b           |     |       |     |     |
| --- | --- | --- | --- | --- | ------ | ----- | ----------- | --- | ----- | --- | --- |
|     |     |     |     | q   |        |       | q           |     |       |     |     |
|     |     |     |     |     |        | y i   |             |     | y i   |     |     |
|     |     |     |     |     | z log  |   =   | z (ln2)−1ln |     |       |     |     |
|     |     |     |     | ∑   | i      |       | ∑  i        |     |       |     |     |
|     |     |     |     |     |        | z i   |             |     | z i   |     |     |
|     |     |     |     | i=1 |        |       | i=1         |     |       |     |     |
o sea:
|     |     |     |     | q   |       |     |        | q    |       |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ------ | ---- | ----- | --- | --- |
|     |     |     |     |     |       | y   | 1      |      | y     |     |     |
|     |     |     |     |     |       | i   |        |      | i     |     |     |
|     |     |     |     |     | z log |   = |        | z ln |       |     |     |
|     |     |     |     | ∑   | i     | z   | ln2 ∑  | i    | z     |     |     |
|     |     |     |     |     |       | i   |        |      | i     |     |     |
|     |     |     |     | i=1 |       |     |        | i=1  |       |     |     |
I
Y aplicando la inecuación (4.9.1) a cada término de la  ∑(I) obtenemos:
|     |     | q   |        |     |        | q     |        |        | q   |        |     |
| --- | --- | --- | ------ | --- | ------ | ----- | ------ | ------ | --- | ------ | --- |
|     |     |     |        | y   | 1      |       | y      | 1      |     | y      |     |
|     |     |     | z log  | i = |        | z     | ln i   | ≤      | z   | i   −1 |     |
|     |     |     | i      |     |        | i     |        |        | i   |        |     |
|     |     | ∑   |        | z   | ln2 ∑  |       |   z    | ln2 ∑  |  (z |   )    |     |
|     |     | i=1 |        | i   |        | i=1   | i      |        | i=1 | i      |     |
|     |     |     |        | q   |        |       |        | q      | q   |        |     |
|     |     |     | 1      |     | y −z   |       | 1      |        |     |        |     |
|     |     |     | =      | z   | i      | i   = |        | y      | − z | 0      |     |
|     |     |     |        |     | i      |       |        | i      |     | i =    |     |
|     |     |     | ln2 ∑  |     |   z    |       | ln2    | ∑      | ∑   |        |     |
|     |     |     |        | i=1 | i      |       | (      | i=1    | i=1 | )      |     |
Luego:
q
|                                                    |     |     |     |     |        | y i   |                     |      |         |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | ------ | ----- | ------------------- | ---- | ------- | --- | --- |
|                                                    |     |     |     |     | z log  |   ≤   | 0 lo que significa: |      |         |     |     |
|                                                    |     |     |     | ∑   | i      |       |                     |      |         |     |     |
|                                                    |     |     |     |     |        | z i   |                     |      |         |     |     |
|                                                    |     |     |     | i=1 |        |       |                     |      |         |     |     |
|                                                    |     |     |     | q   |        |       | q                   |      |         |     |     |
|                                                    |     |     |     |     | z logy | ≤     | z                   | logz | ⟹       |     |     |
|                                                    |     |     |     | ∑   | i      | i     | ∑  i                | i    |         |     |     |
|                                                    |     |     |     |     |        |       |                     |      |         |     |     |
|                                                    |     |     |     | i=1 |        |       | i=1                 |      |         |     |     |
|                                                    |     |     |     |     | q      |       | q                   |      |         |     |     |
|                                                    |     |     |     |     |        | 1     |                     | 1    |         |     |     |
|                                                    |     |     | ⟹   |     | z log  | ≤     | z                   | log  | (4.9.5) |     |     |
|                                                    |     |     |     | ∑   | i      | z     | ∑                   | i y  |         |     |     |
|                                                    |     |     |     |     |        | i     |                     |      | i       |     |     |
|                                                    |     |     |     | i=1 |        |       | i=1                 |      |         |     |     |
| que será una igualdad, ∀ valor de i si y sólo si z |     |     |     |     |        | =     | y .                 |      |         |     |     |
|                                                    |     |     |     |     |        | i     | i                   |      |         |     |     |
|                                                    |     |     |     |     |        |       |                     |      |         |     |     |
21

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Consideremos una fuente de memoria nula de símbolos S  con sus probabilidades
|     |     |     |     |     |     |     | ;S  | ;… ;S | q   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |     |     |     |     |     | 1   | 2     |     |     |
P ;P ;… ;P . Supongamos un código bloque que codifica a la fuente S con un alfabeto de r
1 2 q

símbolos y l  la longitud de la palabra que codifica a S . La entropía valdrá:
| i   |     |     |     |     |     | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |
q
|     |     |     |     | H(s) | = − | P   | logP |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |      |     | i   |      | i   |     |     |
|     |     |     |     |      |     | ∑   |      |     |     |     |
i=1
Supongamos además que Q ;Q ;… ;Q   son números tales que Q ≥ 0∀i y  q Q = 1.
|     |     |     | 1  2  | q   |     |     |     | i   |     | ∑ i i |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----- |
|     |     |     |       |     |     |     |     |     |     | =1    |
Luego, de acuerdo a la (4.9.5) podemos escribir:
|     |     |     | q   |     |     | q   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     | P i log | = H(s) | ≤   | −   | P i logQ | i (4.9.6) |     |     |
| --- | --- | --- | ------- | ------ | --- | --- | -------- | --------- | --- | --- |
|     |     |     | ∑       | P      |     | ∑   |          |           |     |     |
i
|     |     |     | i=1 |     |     | i=1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Igualdad para todo i si y sólo Q . La (4.9.6) es valida para conjunto de números positivos, Q ,
|     |     |     | i = | P i |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |
cuya suma sea la unidad. En particular para:
r−li
|     |     |     |     | Q   | =   |       |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     |     |     | i   | q     |     |     |     |     |
|     |     |     |     |     |   ∑ | r−lj  |     |     |     |     |
|     |     |     |     |     |     | j=1   |     |     |     |     |
Luego:
|        | q   |        |     | q      | q   |           | q   |           | q   |                |
| ------ | --- | ------ | --- | ------ | --- | --------- | --- | --------- | --- | -------------- |
|        |     | logr−l |     |        | r−l |           |     |           |     | r−l            |
| H(s) ≤ | −   | P      | i + | P log  |     | j  ≤ logr |     | P l +log  |     | j  (4.9.6 bis) |
|        | ∑   | i      |     | ∑  i   | ∑   |           | ∑   | i   i     | ∑   |                |
|        | i=1 |        |     | i=1    | j=1 |           | i=1 |           | j=1 |                |
|        |     |        |     |        |     |           |     | I         |     | II             |
Si exigimos que el código sea instantáneo por Kraft; (II) es ≤ 1 ⟹ log(II) ≤ 0
|     |     |     |     | H(s) | ≤   | logr⋅L |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ------ | --- | --- | --- | --- |
H(s)
|     |     |     |     | ≤   | L donde H(s) |     | =   | bits |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --- | ---- | --- | --- |
logr
Pudiendo expresar el cociente H(s)/logr, como la entropía en unidades r-arias quedando:
|     |     |     |     | H   | (s) ≤ | L (4.9.7) |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- |
r

O sea la (4.9.7) expresa que nunca podremos obtener un código cuya longitud media sea menor que
la H (s) (entropía en unidades r-arias).
r

«2 - Codificación», págs. 6 a 8
22

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Errata del apunte
Cambios respecto de la hoja. Fuente: «2 - Codificación», págs. 6 a 8.
(4.9.1). Imprime «ln x» y un exponente «z-1». Puse lnz z−1, porque la figura de esa misma
≤
| hoja dibuja y | = lnz debajo de y | = z−1, y así se usa después. |     |     |     |     |
| ------------- | ----------------- | ---------------------------- | --- | --- | --- | --- |
(4.9.2). Imprime «ln 1/X ≥ 1-z». Puse ln 1 1−z, por la misma mezcla de letras.
≥
z
Paso de la suma. Imprime z ). Puse z y − z , porque es lo que sale de la línea anterior
|     |     | ((y /z    | )/z   | i   i   |     |     |
| --- | --- | --------- | ----- | ------- | --- | --- |
|     |     | i   i   i |   i   | i   z   |     |     |
i
| y lo único que da  | ∑y −∑z | .   |     |     |     |     |
| ------------------ | ------ | --- | --- | --- | --- | --- |
i i

(4.9.5). Las tres líneas salen invertidas en la hoja, como en un espejo vertical. Las puse
derechas y en el orden en que se deducen. Ese orden es lectura mía.
Fuente y Q . Imprime «fuente de memoria de símbolos», «la fuente S », «palara» y «Q ≥ 0».
|     | i   |     |     |     | 1   | 1   |
| --- | --- | --- | --- | --- | --- | --- |

Puse «memoria nula», «la fuente S», «palabra» y «Q 0», como sigue después el apunte.
≥
i
Índice de Q . Imprime i arriba y abajo. Puse j en el denominador, como en la línea siguiente
i

de la hoja.
Última desigualdad. Imprime «H(s) ≤ log r L –» con un guion suelto. Lo saqué.
Queda como está impreso, aunque es dudoso: «log a» y el segundo ≤ de (4.9.6) bis.
z = 1/log
a  b
Fuentes particulares, condición de igualdad
Un código instantáneo y una fuente de memoria nula L debe ser igual o mayor que H (s). Además
r

L será mínima sí y sólo sí pueden elegirse las l  iguales a log (1/P ); esto se podrá lograr
|                       |     |                           | i   | r  i |     |     |
| --------------------- | --- | ------------------------- | --- | ---- | --- | --- |
|                       |     |                           |     |      |     |     |
| indudablemente si log |     | ) es un número entero ∀i. |     |      |     |     |
(1/P i
|     | r   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Esto significa que L = H (s) se logra si las probabilidades de los símbolos P  son de la forma
|     | r   |     |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |
(1/r)li   para cada palabra código de cada símbolo.
«2 - Codificación», págs. 8 y 9
Errata del apunte
La hoja imprime «es es» y, en la capa de texto del PDF, (1/r)i. Saqué la palabra repetida y puse
(1/r)l i  , porque es lo que da P = r−l i   en la (4.9.8) y la (4.9.9). Esa página no se renderiza bien, así
i

que la leí de la capa de texto y de sus fórmulas extraídas. Fuente: «2 - Codificación», pág. 8.
Demostración
El signo desigualdad se introdujo en dos puntos, primero en la (4.9.6) y luego en la (4.9.6) bis
cuando suprimimos el término II. Entonces, la (4.9.6) es una igualdad para la condición P  ∀i o
= Q
i   i
sea:
r−li

|     |     | P i | = Q i = | q (4.9.8) |     |     |
| --- | --- | --- | ------- | --------- | --- | --- |
|     |     |     |     ∑   | r−l       |     |     |
|     |     |     |         | i =1  i   |     |     |
23

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Si se cumple la (4.9.8) y además:
q
r−l i = 1 (4.9.9)
∑
i=1
Entonces, de la (4.9.6) bis obtenemos H(s) = logr⋅L. Resumiendo, el código mínimo en longitud
media, lo obtenemos si se cumplen la (4.9.8) y la (4.9.9) o sea:
P i = r−l i
O de otra forma:
1
log = l ∀i
r P i
i
«2 - Codificación», pág. 8
Fuente con probabilidades ½, , , y
⅛ ⅛ ⅛ ⅛
Con el código S1=0, S2=101, S3=100, S4=111, S5=110, la longitud promedio es L = 1 ⋅1+ 1(3×4) = 2
2 8
binit/símb. Comparándola con la entropía, H (s) = 1 log2+4× 1 log8 = 1 + 3 = 2 bit. Ya que el
r 2 8 2 2
código es instantáneo y de longitud media mínima, implica que es un código compacto.
«2 - Codificación», pág. 9
Inecuación de Kraft
Fuente: 2 - Codificación, págs. 2 y 3
Símbolos del alfabeto Palabras de longitud 1 Palabras de longitud 2
2 1 2
Palabras de longitud 3 Palabras de longitud 4
0 0
Suma
1,0000
¿Existe un instantáneo? (1 sí, 0 no)
1
Capacidad con ruido
Fuente: Errores en Canales, pág. 2
Ancho de banda B Relación S/N
Hz
1000 3
Capacidad C
2000 bps
24

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Primer teorema de Shannon
Primer teorema de Shannon o teorema de la codificación sin ruido
Para una extensión de orden n de una fuente de memoria nula:
|         | L     |        | 1        |
| ------- | ----- | ------ | -------- |
| H (s) ≤ | n   < | H (s)+ | (4.12.6) |
| r       |       | r      |          |
|         | n     |        | n        |
Es posible encontrar un valor de L /n tan próximo a H (s) como queramos, sin más que agrandar
| n   |     |     | r   |
| --- | --- | --- | --- |
|     |     |     |     |
el valor de la extensión, ya que haciendo límite en la (4.12.6) se obtiene:
L
| lim | n   = | H (s) (4.12.7) |     |
| --- | ----- | -------------- | --- |
r
| n→∞  | n   |     |     |
| ---- | --- | --- | --- |
«2 - Codificación», pág. 10
Errata del apunte
El apunte no lo escribe como enunciado aparte. Dice «La ecuación (4.12.6) se conoce como el
primer teorema de Shannon». La frase de apertura, «Para una extensión de orden n de una
fuente de memoria nula», es mía, armada con lo que dice antes de la (4.12.4). Fuente: «2 -
Codificación», pág. 10.
Demostración
Dado que log  no es un número entero, parece lógico tratar de elegir las l  iguales al número
1/P i i
r
entero inmediatamente superior. Por lo tanto, hacemos que l  cumpla:
i

|      | 1     | 1      |          |
| ---- | ----- | ------ | -------- |
| log  | ≤ l < | log +1 | (4.12.1) |
| r  P |   i   | r  P   |          |
|      | i     | i      |          |
|      |       |        |          |
Primeramente veremos que eligiendo las l  de forma tal que cumplan con la (4.12.1), se pueda
i

construir un código instantáneo, esto es, cumplen con la inecuación de Kraft. Aplicando
antilogaritmo a la (4.12.1):
1
| rl  |           |       | r−l         |
| --- | --------- | ----- | ----------- |
| ≤   | i  o bien | P i ≥ | i  (4.12.2) |
| P   |           |       |             |
i

Sumando esta expresión, para todos los i:
|     | q    | q     |     |
| --- | ---- | ----- | --- |
|     | P    | = 1 ≥ | r−l |
|     | i    |       | i   |
|     | ∑    | ∑     |     |
|     | i=1  | i=1   |     |
relación esta que nos dice que este código cumple con la inecuación de Kraft lo que implica que es
instantáneo. Multiplicando la (4.12.1) por P  y haciendo la sumatoria para todo i, se obtiene:
i
| H r (s) | ≤ L < | H r (s)+1 | (4.12.3) |
| ------- | ----- | --------- | -------- |
|         |       |           |          |
25

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
La (4.12.3) se cumple sí y sólo sí para codificar usamos el criterio enunciado en la (4.12.1). La (4.12.3)
es válida para cualquier fuente de memoria nula, en particular, para una extensión de orden n, de la
fuente original.
|     |     |     | H (sn) | L H   | (sn)+1 |          |
| --- | --- | --- | ------ | ----- | ------ | -------- |
|     |     |     | r      | ≤ n < | r      | (4.12.4) |
|     |     |     |        |       |        |          |
Donde L  es la longitud media de las palabras código correspondientes a los símbolos de la fuente
n

extendida, es decir, si λ  es la longitud de la palabra correspondiente al símbolo σ  y P(σ ) su
i   i   i
| probabilidad, L |  será: |     |     |     |     |     |
| --------------- | ------ | --- | --- | --- | --- | --- |
n

qn
|     |     |     | L   | P(σ  | )λ  |          |
| --- | --- | --- | --- | ---- | --- | -------- |
|     |     |     | n   | =    | i i | (4.12.5) |
|     |     |     |     |   ∑  |     |          |
i=1
La (4.12.4) puede escribirse:
|     |     |     | n⋅H | (s) ≤ L | < n⋅H | (s)+1 |
| --- | --- | --- | --- | ------- | ----- | ----- |
|     |     |     |     | r n     |       | r     |
|     |     |     |     |         |       |       |
dividiendo esta por n:
|     |     |     |         | L       |      | 1        |
| --- | --- | --- | ------- | ------- | ---- | -------- |
|     |     |     | H (s) ≤ | n   < H | (s)+ | (4.12.6) |
|     |     |     | r       |         | r    |          |
|     |     |     |         | n       |      | n        |
«2 - Codificación», págs. 9 y 10
Errata del apunte
En estas páginas el PDF pierde los signos de desigualdad en la capa de texto. En (4.12.1) y (4.12.2)
puse ≤, < y ≥, que son los que hacen falta para llegar a la (4.12.3), donde sí se lee <. Es lectura
mía. Fuente: «2 - Codificación», págs. 9 y 10.
Fuente binaria de probabilidades 0,7 y 0,3
Con r = 2, H (s) ≈ 0,881. La regla (4.12.1) da l = 1 y l = 2, porque lg(1/0,7) ≈ 0,51 y lg(1/0,3) ≈ 1,74.
|            | 2             |     |                        | 1   | 2     |        |
| ---------- | ------------- | --- | ---------------------- | --- | ----- | ------ |
|            |               |     |                        |     |       |        |
| Entonces L |               |     | 1,3, y se cumple 0,881 |     |       | 1,881. |
|            | = 0,7⋅1+0,3⋅2 | =   |                        |     | ≤ 1,3 | <      |
Armado para este resumen
Agrupar símbolos antes de codificar deja gastar casi exactamente lo que dice la
entropía. El costo es que el código crece, porque ahora hay qn símbolos que
codificar (apunte, página 11).
Huffman
Construye un código compacto.
1. Ordená los símbolos de mayor a menor probabilidad.
26

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
2. Fundí los dos menos probables en uno, sumando sus probabilidades. Reordená.
3. Repetí hasta que queden dos símbolos. Asignales 0 y 1.
4. Volvé hacia atrás. Al símbolo que se desdobla le agregás un 0 y un 1 a su palabra.
Caso r-ario. Se agrupan los símbolos de a r. Para que la última reducción tenga r símbolos, la cantidad
ω de símbolos fuente tiene que cumplir esta condición, con α entero. Si no, se agregan símbolos falsos
con probabilidad cero.
|     |     |     |     |     | ω   | = r+α(r−1) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
Fuente: «2 - Codificación», páginas 11 a 14.
El código de Huffman es compacto
| Se desea demostrar que si C |     |     |  es compacta, C |     |     |     |  también lo es. |     |     |     |
| --------------------------- | --- | --- | --------------- | --- | --- | --- | --------------- | --- | --- | --- |
|                             |     |     | j               |     |     | j−1 |                 |     |     |     |
|                             |     |     |                 |     |     |     |                 |     |     |     |
«2 - Codificación», págs. 13 y 14
Demostración
| Supongamos la reducción S |     |     | .   |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j

|     |     |     |     |     | L   | = P | l +⋯+P |     | l   |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
|     |     |     |     |     | j   | j1  | j1     | jn  | jn  |     |
|     |     |     |     |     |     |     |        |     |     |     |
Supongamos además que esta reducción está codificada de forma compacta con C . La reducción
j

| anterior S |  tendrá una L |     |          | .   |          |     |          |          |            |            |
| ---------- | ------------- | --- | -------- | --- | -------- | --- | -------- | -------- | ---------- | ---------- |
|            | j−1           |     | j−1      |     |          |     |          |          |            |            |
|            |               | L   | = P      | l   | +⋯+P     |     |          | l        | +P         | l          |
|            |               | j−1 | (j−1,1)  |     | (j−1,1)  |     | (j−1,n)  | (j−1,n)  | (j−1,n+1)  | (j−1,n+1)  |

| Donde P |     |  y l    |         |           | . Además: |            |            |        |        |     |
| ------- | --- | ------- | ------- | --------- | --------- | ---------- | ---------- | ------ | ------ | --- |
| (j−1,1) | =   | P (j,1) | (j−1,1) | = l (j,1) |           |            |            |        |        |     |
|         |     |         |         |           |           |            |            |        |        |     |
|         |     |         |         |           | l         | = l        |            | = l    | +1     |     |
|         |     |         |         |           | (j−1,n)   | (j−1,n+1)  |            | (j,n)  |        |     |
|         |     |         |         |           | P         | +P         |            | = P    |        |     |
|         |     |         |         |           | (j−1,n)   |            | (j−1,n+1)  |        | (j,n)  |     |
Luego:
|     |     |     | L    | = P | l +⋯+{(l |     | +1)(P |          | +P         | )}  |
| --- | --- | --- | ---- | --- | -------- | --- | ----- | -------- | ---------- | --- |
|     |     |     | j−1  | j1  | j1       |     | jn    | (j−1,n)  | (j−1,n+1)  |     |

|     |     |     |     | = P | l +⋯+l |     | P +P |          | +P         |     |
| --- | --- | --- | --- | --- | ------ | --- | ---- | -------- | ---------- | --- |
|     |     |     |     | j1  | j1     | jn  | jn   | (j−1,n)  | (j−1,n+1)  |     |

O sea:
|     |     |     |     |     | L = | L +P | +P  | (4.13.1.1) |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ---------- | --- | --- |
|     |     |     |     |     | j−1 | j    | 0   | 1          |     |     |
|     |     |     |     |     |     |      |     |            |     |     |
Donde P  y P  son las probabilidades de los símbolos S  y S : símbolos que provienen de haber
| 0   | 1   |     |     |     |     |     |     | 0   | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
desdoblado el S; donde S es el símbolo menos probable de la reducción compacta S .
j

27

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Se hará por reducción al absurdo, queremos demostrar que si L la menor longitud media de un
j
código instantáneo correspondiente a S ; L (dado por la ecuación 4.13.1.1) es también la longitud
j j−1
media mínima para S . Sea un código de longitud media L′ menor y sean X′,…,X′,X′ las
j−1 j−1 1 0 1
palabras de dicho código de longitudes l′,…,l′,l′. Supongamos los subíndices ordenados según el
1 0 1
orden decrecientes de las probabilidades de los símbolos respectivos, es decir
l′ ≤ ⋯ ≤ l′ ≤ l′
1 0 1
Ahora construyamos C′, código correspondiente a S , combinando X′ y X′ y suprimiendo el último
j j 0 1
binit sin alterar los demás. El resultado es un código instantáneo para S ; de longitud media L′; que
j j
debe cumplir.
L′ = L′ +P +P
j−1 j 0 1
Esta ecuación comparada con la (4.13.1.1) implica que existe un código de longitud media L′ < L lo
j j
que es absurdo ya que se supuso que el C era compacto.
j
«2 - Codificación», págs. 13 y 14
Errata del apunte
Hipótesis sumada. La frase «Sea un código de longitud media L′ menor» no está en la hoja. La
j−1
agregué porque la reducción al absurdo la necesita y sin ella no se entiende de dónde sale X′.
Fuente: «2 - Codificación», págs. 13 y 14.
Otros cambios respecto de la hoja:
Imprime «P(j-1, 1) = l(j-1, 1)». Puse l = l , porque compara longitudes.
(j−1,1) (j,1)
Imprime «P(j-1, n) = P(j-1, n+1) = P(j, n)». Puse la suma, P +P = P , porque al
(j−1,n) (j−1,n+1) (j,n)
fundir dos símbolos se suman sus probabilidades.
Imprime «(lj,1 +1)» en la llave. Puse (l +1), y la suma entre las dos probabilidades, que falta.
jn
Imprime «lʼ1 < ... < l0 < l1», con ese orden de subíndices. Puse ≤ y primas en todas, porque dos
palabras pueden tener igual longitud.
Imprime «Lʼ = Lʼj + P0 + P1» y «construyamos Cj». Puse L′ y C′, porque es el código supuesto,
j−1 j
no el compacto.
Imprime «se puso». Puse «se supuso».
Fuente de seis símbolos
Con probabilidades 0,4; 0,3; 0,1; 0,1; 0,06 y 0,04, las reducciones llegan a 0,6 y 0,4. Volviendo hacia
atrás, el apunte obtiene S1=1, S2=00, S3=0100, S4=0101, S5=0110 y S6=0111.
«2 - Codificación», pág. 12
28

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Rendimiento y redundancia
H (S)
r
η = Red = 1−η
L
Fuente: «2 - Codificación», página 14.
Detección y corrección de errores
Distancia
La distancia entre dos palabras es la cantidad de dígitos que cambian entre ellas. La distancia mínima
es la menor de todas. Si vale 1, un error simple convierte una palabra en otra del mismo código y no se
detecta. Por eso hay que aumentarla. Fuente: «3 - Detección y Corrección de errores», página 1.
Bit de paridad
Agrega un dígito para que la cantidad de unos sea par o impar. Con 3 dígitos de información y uno de
paridad hay 16 combinaciones pero se usan 8. Las otras 8 son las que absorben el error simple.
Detecta errores, no los corrige. Se debe descartar la palabra y pedir que se retransmita. También
detecta errores de orden impar (apunte «2 - Codificación», página 15).
El costo es rendimiento. Pasa de 3/3 a H/L = 3/4 = 0,75, con redundancia de 0,25 (apunte «3 -
Detección», página 3).
Paridad por filas y columnas
Se arma un bloque con paridad por fila y por columna. El dígito con error está en la intersección de la
fila y la columna que no coinciden. Si falla solo una, el error está en un bit de paridad.
Su inconveniente es que hay que armar bloques, no corrige por palabra. Fuente: «3 - Detección»,
páginas 4 a 6.
Otros detectores
El apunte nombra también por mayoría y de igual peso. Se controla si se violó el peso de unos de la
palabra. Detectan todos los errores unitarios. Fuente: «2 - Codificación», páginas 16 y 17.
Hamming
Controla la paridad por zonas que se superponen. Cada dígito de información cae en una combinación
distinta de zonas, y por eso se puede corregir.
Con m dígitos de información hacen falta n de control, tales que:
29

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
2n
≥ m+n+1
Cada configuración indica un dígito con error, y una más indica que está todo bien. Para m 4 da n
= =
3. Fuente: «2 - Codificación», páginas 18 y 19.
El ejemplo del apunte usa estas zonas:
|     |     | C = I | +I +I     | C = I +I | +I    | C = I +I | +I      |     |
| --- | --- | ----- | --------- | -------- | ----- | -------- | ------- | --- |
|     |     | 1   0 |   1   2   | 2   1    | 2   3 | 3   0    | 2   3   |     |
Se transmite  1000 110  en el orden I I I I C C C  y se recibe  1010 110 . Al recalcular cambian C  y
|     |     |     | 3 2 1 | 0 3 2 1   |     |     |     | 1   |
| --- | --- | --- | ----- | --------- | --- | --- | --- | --- |
|     |     |     |       |           |     |     |     |     |
C , y el único dígito común a esas dos zonas es I . La información correcta es  . Si cambia un solo
| 2   |     |     |     | 1   |     |     | 1000 |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- |
|     |     |     |     |     |     |     |      |     |
dígito de control, el error no está en la información. Fuente: «3 - Detección», páginas 6 a 8.
| Su rendimiento es 4/7 |     | 57,1% y su redundancia 0,43 (página 9). |     |     |     |     |     |     |
| --------------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
=
Con los controles intercalados. Los dígitos de control van en las posiciones 2n, y la información en el
resto. Cada control mira las posiciones que tienen un 1 en su mismo binit.
| Control |     |     | Posición |     |     | Zona       |     |     |
| ------- | --- | --- | -------- | --- | --- | ---------- | --- | --- |
| C       |     |     | 1        |     |     | 1, 3, 5, 7 |     |     |
1

|     |     |     | 2   |     |     | 2, 3, 6, 7 |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
C
2
| C   |     |     | 4   |     |     | 4, 5, 6, 7 |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
3

Pones 1 por cada zona alterada, y ese número binario indica en decimal el dígito con error. Fuente: «2 -
Codificación», páginas 19 a 21.
En criollo
Es como buscar a alguien en un edificio preguntando «¿está en el ala norte?» y «¿está en los pisos
altos?». Con la combinación de respuestas sabés el lugar exacto. Cada zona alterada es una
respuesta.
Códigos lineales
No tienen un campo separado de control. Se toman menos palabras que las posibles para aumentar la
distancia mínima.
| Espacio | Qué es          |     |     |     |     | Dimensión               |     |     |
| ------- | --------------- | --- | --- | --- | --- | ----------------------- | --- | --- |
|         | Código de grupo |     |     |     |     | 2m filas por n columnas |     |     |
V
| G   | Matriz generadora de V |     |     |     |     | m filas por n columnas    |     |     |
| --- | ---------------------- | --- | --- | --- | --- | ------------------------- | --- | --- |
| V′  | Espacio ortogonal a V  |     |     |     |     | 2n−m filas por n columnas |     |     |
30

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
| Espacio | Qué es |     |     |     |     | Dimensión |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --------- | --- | --- | --- |
H Matriz de control de paridad, base de V′ n−m filas por n columnas
La base debe ser linealmente independiente y no es única. La suma es sin acarreo.
|     |     |     |     | v ×HT | v′ ×GT |     |     |     |     |
| --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- |
|     |     |     |     | i =   | 0      | = 0 |     |     |     |
|     |     |     |     |       | i      |     |     |     |     |
Fuente: «3 - Detección», páginas 10 a 15.
Síndrome
Se multiplica lo recibido por HT. Si da cero, la palabra es correcta o tiene un error no detectable. Si no,
hay error.
Síndrome asociado a un error
Cómo el error e  es el mismo en ambos casos ambos resultados distintos de cero son iguales y se
a

lo denomina Síndrome asociado al error e  (S ). En principio cada vez que al recibir una palabra
a ea
|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
y al multiplicarla por HT el resultado dé el síndrome S  sabremos que el error está en el cuarto
ea

dígito pudiendo entonces corregir. La matriz H se denomina matriz de control de paridad.
«3 - Detección y Corrección de errores», pág. 14
Errata del apunte
La hoja imprime «LA MARIZ H SE DENOMINA MATRIZ DE CONTROL DE PARIDAD». Puse «La
matriz H» en minúsculas, y agregué un punto tras «pudiendo entonces corregir», donde saqué
«las palabras correctas serán», que va en el ejemplo. Fuente: «3 - Detección y Corrección de
errores», pág. 14.
Demostración
Sea v ∈ V y v ∈ V. Modelizando el error mediante la suma sin acarreo, aplicamos la detección de
| 1   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |
errores:
|     | v ×HT | (v +e     | )⋅HT | v ×HT | +e ×HT | 0, con v    | ×HT | 0 (v   | V)     |
| --- | ----- | --------- | ---- | ----- | ------ | ----------- | --- | ------ | ------ |
|     | 1ea   | = 1       | a    | = 1   | a      | =          | 1   | =      | 1 ∈    |
|     |       |           |      |       |        |             |     |        |        |
|     | ×HT   |           | )⋅HT | ×HT   | ×HT    |             | ×HT |        |        |
|     | v 2ea | = (v 2 +e | a    | = v 2 | +e a   | = 0, con v | 2   | = 0 (v | 2 ∈ V) |
|     |       |           |      |       |        |             |     |        |        |
«3 - Detección y Corrección de errores», pág. 14
31

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Error en el cuarto dígito
Con v 1 = 101110 , v 2 = 111001 y e a = 000100 , se reciben 101010 y 111101 . Los dos dan el mismo
síndrome, y las palabras correctas serán y .
101110 111001
«3 - Detección y Corrección de errores», pág. 14
En criollo
Pensá en un médico que ve síntomas, no a la persona. Dos pacientes distintos con la misma
enfermedad muestran el mismo cuadro. El síndrome es ese cuadro. Depende del error y no de la
palabra que venía.
Dos reglas del apunte
Detectar no es corregir. Si dos errores simples distintos dan el mismo síndrome, se detectan pero
no se corrigen.
Cuántos síndromes hacen falta. Para corregir error simple en cada uno de los n dígitos, hacen
falta tantos síndromes como dígitos. Hay 2n−m −1 síndromes distintos, porque el cero
corresponde a palabra correcta. Fuente: «3 - Detección», páginas 14 y 15.
Errores que no se detectan. Son los que coinciden con palabras del código, porque sumarlos a una
palabra da otra palabra del código. Todos los demás caen en alguna familia asociada a un síndrome.
Fuente: «3 - Detección», página 16.
Ejemplo del apunte «4 - Ejemplos Códigos Lineales» (página 1), con G de filas 100011 , 101101 y
111000
. Combinando con sus constantes sale V, con palabras
000000
,
100011
,
101101
,
001110
,
111000 , 011011 , 010101 y 110110 . Por 100011 , no se detecta el error triple en x 1 ,x 5 ,x 6 .
Para hallar H: planteás v′ ×GT = 0, despejás en un sistema binario y elegís una base independiente de
V′. Después se plantea cada síndrome para ver qué error simple corrige (páginas 2 a 6).
Familia de errores asociada a un síndrome
Qué se observa en la familia de errores de un síndrome
1° parcial 30/06/2021 y finales 28/08/2020, 10/09/2021, 19/11/2021 y 17/12/2021
«En la familia de errores asociadas a cada síndrome se pueden observar», con opciones. Abajo
está la teoría del apunte para contestarla.
El apunte la arma así, con el código de seis dígitos de arriba («4 - Ejemplos Códigos Lineales», páginas 2
a 6).
32

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
1. Como no conocés la palabra con error, la ponés como incógnita y planteás (x ,x ,x ,x ,x ,x )×
1 2 3 4 5 6
HT = S para cada síndrome distinto de cero. Son 2n−m −1, en el ejemplo 23 −1 = 7, y por
i
comodidad se cuentan en binario.
2. Queda un sistema de n−m ecuaciones con n incógnitas binarias, con suma sin acarreo. Le das
todos los valores a las variables independientes y despejás las demás. Conviene elegir como
independientes las que más se repiten en las ecuaciones.
3. Las soluciones son la familia. En palabras del apunte, es la «Familia de palabras de V que tienen un
determinado error que dá como resultado el Síndrome S1 = 001, resumiendo es Familia de Errores
asociadas al Síndrome 001».
4. Mirando la familia sola no se ve en qué dígito está el error. Pero el código tiene una palabra
particular, la . Su versión con error está en la familia, y muestra el error mismo. En el
000000
ejemplo, para el síndrome 001 sale 100000 , error simple en x 1 . Todas las palabras de esa familia
son palabras del código con un error en x .
1
5. El mismo síndrome también lo pueden causar errores dobles, triples, cuádruples o quíntuples. El
apunte nombra cuáles en el ejemplo. Se usa el criterio de la mayor probabilidad, y se toma el error
simple.
La conclusión del apunte para ese caso es «con el Síndrome 001 se detecta y corrige error simple en
x1». Con la palabra recibida , la correcta es .
111011 011011
En criollo
Cada síndrome junta a todas las palabras que llegaron con el mismo error, vengan de la palabra
del código que vengan. La que vino de te muestra el error desnudo, porque sumarle el
000000
error al cero da el error.
Armar las ecuaciones de control y mostrar el método de Hamming
1° parcial 06/07/2023
Te dan los dígitos de información y qué controla cada C. Después pide mostrar la detección y
corrección de un error simple. No volvió en las hojas de 2024 y 2025 que leí. El síndrome aparece
en el multiple choice teórico del 30/06/2021.
Medios de transmisión
Multiple choice de medios
1° parcial 06/07/2023 y 1° parcial 2025
El de 2025 trae 24 consignas. Los dos preguntan por fibra, UTP, microondas, infrarrojo y satélites.
En cada uno hay que saber datos y números. Esta sección junta lo que está escrito en el apunte.
Fuente de toda esta sección, salvo aviso: apunte «3 - Medios de transmisión».
33

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Par trenzado
Dos alambres de cobre aislados. Se trenzan porque dos paralelos forman una antena, y al trenzarlos las
ondas de las distintas vueltas se cancelan (página 3).
| Tipo | Qué es                                  | Impedancia |
| ---- | --------------------------------------- | ---------- |
| UTP  | Sin blindaje, de bajo costo y fácil uso | 100 ohmios |
| STP  | Blindado, más caro                      | 150 ohmios |
| FTP  | Pantalla conductora global              | 120 ohmios |
Datos para recordar (páginas 4 y 5):
La categoría 5 tiene más vueltas por centímetro que la 3. Eso da menos diafonía y mejor señal.
En la tabla, categoría 5 tiene 100 MHz y categoría 6 tiene 250 MHz.
Distancia limitada: 100 metros por segmento.
La atenuación depende fuertemente de la frecuencia.
Usando dos de los cuatro pares se transmite half-dúplex. Con los cuatro, full-dúplex.
Cable coaxial
Tiene mejor blindaje que el par trenzado. El de 50 ohms se usa para transmisión digital, y el de 75
ohms para analógica y televisión por cable. Se reemplazó por fibra en rutas largas (página 5).
Fibra óptica
Tiene tres componentes: fuente de luz, medio de transmisión y detector. Un pulso de luz indica un 1 y
la ausencia indica un 0. Un rayo que incide con ángulo mayor o igual al crítico queda atrapado (página
6).
Multimodo Monomodo
| Luz | Muchos rayos con ángulos Un solo modo, en línea recta |     |
| --- | ----------------------------------------------------- | --- |
distintos
| Núcle | 50 micras 8 a 10 micras |     |
| ----- | ----------------------- | --- |
o
Uso Corta distancia, menos de 2 Grandes distancias, hasta 400 km con láser de alta
km intensidad
| Preci | Simple y económica Más cara |     |
| ----- | --------------------------- | --- |
o
Fuente: páginas 6 a 8.
34

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Ventajas sobre el cobre (página 10):
Mucho mayor ancho de banda.
Baja atenuación. Repetidores cada 50 km aproximadamente, contra casi 5 km en cobre.
No la afectan sobrecargas, interferencia electromagnética ni corrosivos.
Difícil de intervenir.
Desventajas (página 10):
Requiere habilidades y se daña si se dobla mucho.
La transmisión es unidireccional, así que en ambos sentidos hacen falta dos fibras o dos bandas.
Las interfaces cuestan más.
Pérdidas: absorción, Rayleigh, dispersión cromática, radiación, dispersión modal y acoplamiento
(página 9). Los conectores pierden entre un 10 y 20% de la luz (página 7).
Medios no guiados
Pág
Medio Datos del apunte
ina
Radio Fácil de generar, atraviesa edificios y es omnidireccional. Sus propiedades 11
dependen de la frecuencia. HF y VHF rebotan en la ionosfera
Micro Por encima de 100 MHz, en línea recta y haz estrecho. No atraviesan bien 11
ondas edificios. Desde unos 4 GHz, las absorbe la lluvia. Relativamente baratas frente y
a tender fibra 12
Infrar Corto alcance. No atraviesa objetos sólidos, lo que evita interferir con el cuarto 12
rojo de al lado. No requiere licencia
Altura de torres. La distancia entre repetidores crece aproximadamente con la raíz cuadrada de la
altura. Con torres de 100 m, los repetidores pueden estar a 80 km (página 12).
Desvanecimiento por múltiples trayectorias. Algunas ondas se refractan en capas bajas de la
atmósfera y llegan más tarde que las directas. Llegan fuera de fase y pueden cancelar la señal (página
12).
Satélites
Un satélite es un enorme repetidor de microondas en el cielo. Cada transpondedor amplifica la señal y
la retransmite en otra frecuencia para no interferir. Fuente: página 12.
Tipo Altitud en la figura Latencia Satélites necesarios
GEO 35.000 km 270 ms 3
35

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
| Tipo | Altitud en la figura |     | Latencia   | Satélites necesarios |
| ---- | -------------------- | --- | ---------- | -------------------- |
| MEO  | Unos 10.000 km       |     | 35 a 85 ms | 10                   |
| LEO  | Baja                 |     | 1 a 7 ms   | 50                   |
Fuente: página 13. Los MEO tardan unas seis horas en dar la vuelta (página 14). Cuando se termina el
combustible, por lo general a los 10 años, el satélite queda a la deriva (página 13).
| Banda | Bajada  | Subida  | Ancho de banda | Problemas                     |
| ----- | ------- | ------- | -------------- | ----------------------------- |
| L     | 1,5 GHz | 1,6 GHz | 15 MHz         | Bajo ancho de banda, saturada |
| S     | 1,9 GHz | 2,2 GHz | 70 MHz         | Bajo ancho de banda, saturada |
| C     | 4 GHz   | 6 GHz   | 500 MHz        | Interferencia terrestre       |
| Ku    | 11 GHz  | 14 GHz  | 500 MHz        | Lluvia                        |
| Ka    | 20 GHz  | 30 GHz  | 3500 MHz       | Lluvia, costo del equipo      |
Fuente: página 13. El apunte dice que la banda C fue la primera destinada al tráfico comercial por
satélite. Las VSAT son microestaciones de bajo costo, Terminales de Apertura Muy Pequeña, con
antenas de un metro o menos (página 14).
Lo que el apunte no cubre
Los multiple choice de 2023 y 2025 también preguntan por la ley de Snell, el retardo por
kilómetro, el láser y la longitud de onda. No encontré esas respuestas en los apuntes de la
cátedra, así que acá no se contestan. Podés verlos en el multiple choice de 2014 como práctica,
consultando en clase.
Qué practicar
Andá a Ejercicios y hacé los de 1° parcial. Conviene empezar por las cuatro prácticas de 2023 a 2025.
36

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
COMUNICACIÓN DE DATOS
2° parcial
Cómo se adapta y se comparte un canal, qué medio elegir, cuánto espera un
mensaje en una cola y cuánta capacidad darle a cada enlace.
Resumen no juzgado. Todavía nadie evaluó si alcanza para estudiar solo con esto.
Cómo viene el examen
Leí nueve hojas de 2023 a 2025. Hay dos modelos de práctica, que dependen de la comisión, y un
multiple choice teórico de 2023.
Modelo trama, tres hojas (26/10/2023, 31/10/2024 y 23/10/2025). Las tres tienen definiciones de señales y
una trama digital TDM. Dos agregan un problema FDM (2023 y 2025) y una las etapas de digitalización
(2024).
Modelo colas, cinco hojas (26/10/2023, 23/10/2024 y tres temas del 23/10/2025). Las cinco piden
elementos de un sistema de colas abierto, punto de saturación y un problema M/M/1. Los tres temas de
2025 preguntan por el retardo cerca de η C , y las hojas de 2023 y 2024 traen un cálculo de asignación
i i
de capacidad.
Multiple choice teórico, una hoja de 2023 con 20 consignas. Seis son de medio de acceso, tres de colas
y tres de TDM. El resto va por síndrome, AM, WDM, CDM, FSK y PSK, ruido en fibra y atenuación en
radio.
Preguntá en tu comisión cuál toca
Con estas hojas no puedo decir qué modelo te corresponde. Estudiá los dos si no lo sabés.
Modulación
Es el proceso de adaptar una señal mensaje, la que se quiere transmitir, al medio de transmisión.
También es un traslado en frecuencia del mensaje a la frecuencia de la señal portadora, mucho mayor,
con f ≪ f . Fuente: apunte «5 - Comunicaciones Digitales», página 3.
m c
Definir ancho de banda y portadora, con gráficas
2° parcial 23/10/2025
Esta hoja pide las dos definiciones con su dibujo. El apunte da los gráficos en sus páginas 4 a 7.
37

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
▾ ¿Qué es la portadora?
2° parcial 23/10/2025
Es la señal de alta frecuencia a la que se traslada el mensaje. Siempre es de alta frecuencia
comparada con el mensaje, f f . Por ejemplo, en radio AM el mensaje va de 20 Hz a 20 KHz y
m ≪ c

la portadora ronda los 1000 KHz. Fuente: apunte «5 - Comunicaciones Digitales», página 3.
▾ ¿Qué es el ancho de banda?
2° parcial 23/10/2025
Las frecuencias de corte son aquellas donde la potencia cae a la mitad de su máximo, 3 dB menos.
El ancho de banda es la diferencia entre ellas, AB . Fuente: apunte «1 - Principios
= f −f
2   1
Básicos», sección «Respuesta en frecuencia» (página 12 de su índice).
En criollo
Tu voz sola no llega lejos por el aire. Es como una carta. La subís a un camión rápido que va por la
ruta, y al llegar la bajás. La portadora es el camión, y modular es cargarle el mensaje.
Modulación analógica
El mensaje modula algún parámetro de la portadora: amplitud (AM), frecuencia (FM) o fase (PM).
|     | X AM (t) | = (A c +A m cos2πf | m t)cos2πf | c t |     |
| --- | -------- | ------------------ | ---------- | --- | --- |
|     |          |                    |            |     |     |
Aparecen componentes en f , f  y f . Son la portadora y las dos bandas laterales. Fuente:
|     | −f          | +f      |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
|     | c   c   m   | c   m   |     |     |     |
apunte 5, páginas 5 y 6.
| Variante          | Qué transmite                     |     |     |     | Ancho |
| ----------------- | --------------------------------- | --- | --- | --- | ----- |
| BSD (doble banda) | Banda lateral inferior y superior |     |     |     |       |
2W
| SSB o BLU (una banda) | Una sola banda lateral |     |     |     | W              |
| --------------------- | ---------------------- | --- | --- | --- | -------------- |
| DSB-SC, SSB-SC        | Sin portadora          |     |     |     | Ahorra energía |
Fuente: apunte 5, páginas 7 y 8.
38

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Una portadora modulada en amplitud
Fuente: 5 - Comunicaciones Digitales, pág. 5
yy
22,,55
22,,00
11,,55
11,,00
CCoonnttoorrnnoo
00,,55
tt
SSeeññaall  mmoodduullaaddaa
00,,22 00,,44 00,,66 00,,88 11,,00 11,,22 11,,44 11,,66 11,,88
−−00,,55
−−11,,00
−−11,,55
−−22,,00
−−22,,55
Señal modulada
Contorno
FDM
Cada mensaje modula una portadora distinta y las señales se ubican una al lado de la otra en
frecuencia. Con N señales:
|     |        |          | B W = f cMax | −f         | cMin = N | ⋅2W (DSB)                           | B W = N ⋅W (SSB) |
| --- | ------ | -------- | ------------ | ---------- | -------- | ----------------------------------- | ---------------- |
|     |        |          |              |            |          |                                     |                  |
|     |        | , y si f |              |  se toma W |          | . Fuente: apunte 5, páginas 9 y 10. |                  |
| W   | = f −f |          | ≪ f          |            |          | ≈ f                                 |                  |
|     | max    | min      | min          | max        |          | max                                 |                  |
Un caso real es el acceso a internet por ADSL. El cable de cobre del abonado reparte su espectro en tres
bandas (apunte «6 - Espectro de la señal ADSL», página 1).
| Banda |     |     | Frecuencias |     |     | Para qué                   |     |
| ----- | --- | --- | ----------- | --- | --- | -------------------------- | --- |
| PSTN  |     |     | 0 a 4 kHz   |     |     | Comunicaciones telefónicas |     |
Upstream 25,875 a 138 kHz Subida de datos, del cliente a la nube
Downstream 138 a 1104 kHz Bajada de datos, de la nube al cliente
39

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Graficar y calcular un sistema FDM, multiplexado y modulación
2° parcial 26/10/2023 y 2° parcial 23/10/2025
Te dan el ancho de banda del canal, la frecuencia mínima y el ancho de cada señal. Mirá las
fórmulas de arriba y el enunciado completo.
Modulación digital
Son tres maneras de mandar bits por un canal que transporta señales analógicas. El ejemplo del
apunte es una computadora por línea telefónica, con un MODEM. Fuente: apunte 5, página 11.
Técnica Qué cambia Dato del apunte
ASK Amplitud No se usa actualmente
FSK Frecuencia Existe multinivel
PSK Fase Existe multinivel. Solo se demodula en forma coherente
El apunte ordena todo el tema en tres combinaciones de mensaje y portadora (apunte 5, página 3).
1. Mensaje analógico con portadora analógica. Es la modulación analógica de arriba.
2. Mensaje digital con portadora analógica. Es esta sección.
3. Mensaje analógico con portadora digital. Son los pulsos, PAM, PDM y PPM.
Según el apunte, los casos 1 y 2 se analizan igual, y lo que vale para el 1 vale para el 2. Solo cambia el
tipo de señal que se transmite.
Demodulación coherente o incoherente (apunte 5, páginas 16 y 17).
Sincrónica o coherente. La portadora tiene la misma frecuencia en el origen y en el receptor. Hace
falta tener la portadora en el lugar de recepción, y en sincronismo con la de emisión. Es un
inconveniente, porque aumenta el costo. En FSK hacen falta las dos portadoras en destino.
Asincrónica o incoherente, por detección de envolvente. Se recupera por pasos sucesivos la forma
de la envolvente, con un absolutor o rectificador. Existe para ASK y FSK. Para PSK, el apunte aclara
«no existe incoherente».
La combinación de amplitud y fase da QAM o APSK. Con 2 amplitudes y 4 fases hay 8 estados, o sea 3
dígitos por símbolo. Fuente: apunte 5, páginas 11 a 17.
Las técnicas de pulsos analógicos son PAM, PDM y PPM. El mensaje varía la amplitud, la duración o la
posición del pulso. Fuente: apunte 5, página 18.
40

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
▾ ¿Qué es PDM?
2° parcial 26/10/2023 y 31/10/2024
Es una modulación por pulsos en la que la muestra del mensaje determina la duración del pulso.
Fuente: apunte «5 - Comunicaciones Digitales», página 18.
ASK, FSK y PSK con los mismos bits
Fuente: 5 - Comunicaciones Digitales, pág. 11
yy
66
AASSKK
44
22
FFSSKK
tt
00,,55 11,,00 11,,55 22,,00 22,,55 33,,00 33,,55
−−22
−−44
PPSSKK
−−66
ASK
FSK
PSK
41

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Armónicos y espectro
Espectro de un tren de pulsos
Tren de pulso de amplitud A, Frecuencia f (= 1/T), Ancho de Pulso τ. Para estudiar eso
definimos la función:
sen πx
|     | sinc X | =   |      |     |     |
| --- | ------ | --- | ---- | --- | --- |
|     |        |     | πx   |     |     |
De acuerdo a Fourier el Tren de Pulsos puede ser expresado como:
∞
|      | Aτ     | 2Aτ  | nτ    |          |     |
| ---- | ------ | ---- | ----- | -------- | --- |
| x(t) |        |      |       | ⋅cos2πnf | t   |
|      | = +    | sinc |       |          | 0   |
|      | T   ∑  | T    | (T  ) |          |     |
|      | 0      | 0    | 0     |          |     |
|      |        | 1    |       |          |     |
: componente continua. n: orden de las armónicas. f . Frecuencia Fundamental =
| Aτ/T 0  |     |     |     | = nf 0  |     |
| ------- | --- | --- | --- | ------- | --- |
f = 1/T . La Amplitud de las armónicas se puede expresar como:
0 0

|     | 2Aτ  | nτ 2Aτ |        |     |     |
| --- | ---- | ------ | ------ | --- | --- |
|     | sinc | =      | sincnf | τ   |     |
0
|     | T 0    | (T 0   ) | T 0    |     |     |
| --- | ------ | -------- | ------ | --- | --- |
Observación: La separación entre armónicas = a la frecuencia del tren de pulso. Las armónicas de
mayor amplitud se encuentran entre 0 y 1/τ.
«5 - Comunicaciones Digitales», Anexo 1, pág. 26
Errata del apunte
Dos cambios respecto de la hoja. Fuente: «5 - Comunicaciones Digitales», Anexo 1, pág. 26.
En la sumatoria imprime 2Aτ sin dividir por T . Puse 2Aτ, porque así lo escribe la misma hoja
|     |     | 0   | T0  |     |     |
| --- | --- | --- | --- | --- | --- |
dos renglones más abajo, como amplitud de las armónicas.
Imprime «T  → componente continua». Puse Aτ/T , que es el término constante de la
0  0
fórmula.
Tren de 1 KHz
Con T 1 ms, la fundamental es f 1 KHz, y las armónicas caen en 1 KHz, 2 KHz, 3 KHz y
| =   | = 1/T | =   |     |     |     |
| --- | ----- | --- | --- | --- | --- |
| 0   | 0     | 0   |     |     |     |
así. Con τ = 0,25 ms, las de mayor amplitud están entre 0 y 1/τ = 4 KHz.
Armado para este resumen
42

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
▾ ¿Qué es un armónico?
2° parcial 26/10/2023 y 31/10/2024
Las armónicas son las componentes de frecuencia f = nf que forman el tren de pulsos según
0
Fourier. n es su orden y f = 1/T es la frecuencia fundamental. Fuente: apunte «5 -
0 0
Comunicaciones Digitales», Anexo 1, página 26.
En criollo
Una nota de guitarra no es una sola frecuencia. Suena la fundamental y varias múltiplos de ella,
más suaves. Por eso la misma nota suena distinto en un piano. Cada una de esas múltiplos es un
armónico.
Armónicas de un tren de pulsos
Fuente: 5 - Comunicaciones Digitales, Anexo 1, pág. 26
AAmmpplliittuudd
33
22
11
ff
11 22 33 44 55 66 77 88 99 1100 1111
−−11
−−22
−−33
Envolvente
Si querés jugar con un espectro de barras como este, el experimentador de armónicos de ChordWeaver
te deja subir y bajar cada armónico de una nota y escuchar cómo cambia el sonido. Es un programa
gratis y de código abierto, para Windows.
43

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Muestreo y PCM
Tasa de Nyquist o Teorema de Muestreo
Por Tasa de Nyquist o Teorema de Muestreo; la frecuencia mínima de muestreo f siempre tiene
s
que ser mayor o igual que las 2 frecuencias máximas del mensaje. Condición para que pueda
recuperar el mensaje:
f ≥ 2f
s max
«5 - Comunicaciones Digitales», pág. 23
Demostración
Estas muestras en realidad no son un pedacito aislado del mensaje, sino que esta repetido infinitas
veces, si para recuperar mi señal necesito el espectro, lo tengo infinitas veces.
Entre una muestra y otra muestra quiero que el tiempo de muestreo sea lo más grande posible para
que me pueda entrar mayor cantidad de mensajes (muchas muestras). Al bajar la frecuencia me
acerco al origen.
Donde N = cantidad de mensajes muestrados o transportados. T = tiempo o periodo de muestreo
s
(tiempo desde que se toma una muestra hasta que volvamos a tomar otra del mismo mensaje). f =
s
frecuencia de muestreo.
Lo que se hace es disminuir la frecuencia de muestreo f lo máximo posible para poder mandar
s
más cantidad de señales en el mismo canal. Hay un punto que es f −w que si lo sigo tirando hacia
s
el origen se me junta con el w. Superposición de información. ¿Cuál es el limite?
f −w ≥ w ⟹ f ≥ 2w w = f −f ≈ f
s s max min max
«5 - Comunicaciones Digitales», págs. 22 y 23
Errata del apunte
La hoja imprime «minimade», «disminur» y «un p unto», y los puse bien escritos. Los signos de
f −w ≥ w no salen en la capa de texto del PDF. Los puse según la conclusión impresa, f ≥ 2f
s s max
. Saqué los dibujos del espectro, que están redibujados en el gráfico de abajo, y la línea de flechas
. Fuente: «5 - Comunicaciones Digitales», págs. 22 y 23.
N ==> Ts ==> fs
Un mensaje de música
Si el mensaje llega hasta 20 KHz, como el del ejemplo de radio del apunte, f es chica y w ≈ f .
min max
Entonces f ≥ 2⋅20 KHz = 40 KHz.
s
Armado para este resumen
44

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
En criollo
Si filmás una rueda con muy pocos cuadros por segundo, parece girar para atrás. Tomaste
muestras demasiado espaciadas y la película te muestra otro movimiento. Con el mensaje pasa
igual. Si muestreás lento, los espectros se pisan y no lo recuperás.
Espectro de una señal muestreada
Fuente: 5 - Comunicaciones Digitales, págs. 22 y 23
yy
11,,11
11,,00 CCooppiiaa eenn 22ffss
00,,99
00,,88
00,,77
00,,66 CCooppiiaa eenn ffss
00,,55
00,,44
00,,33 MMeennssaajjee,, ww == 22
00,,22
00,,11
22ww
11 22 33 44 55 66 77 88 99 1100 1111 ff
Mensaje, w = 2
Copia en fs
Copia en 2fs
▾ ¿Qué es la tasa de Nyquist?
2° parcial 26/10/2023 y 31/10/2024
Es la frecuencia mínima de muestreo para poder recuperar el mensaje. Tiene que ser mayor o
igual que las 2 frecuencias máximas del mensaje, f ≥ 2f . Fuente: apunte «5 - Comunicaciones
s max
Digitales», página 23.
TDM y la trama
En TDM va una señal por vez y cada una ocupa todo el canal durante su turno. Una trama tiene una
muestra de cada mensaje y dura T = 1/f . Fuente: apunte 5, páginas 18 a 20.
s s
45

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Una trama, de duración Ts = 1/fs:
| A0 | B0 | C0 | ... | N muestras |
Una muestra, de duración TM = n * tau:
| 1 | 0 | 1 | 1 | 0 | ... | n dígitos |
Es la figura del apunte, página 24, con A, B y C como mensajes distintos.
En criollo
FDM es como las radios. Todas suenan a la vez, cada una en su frecuencia. TDM es como una
ronda donde cada uno dice una palabra por turno, tan rápido que parece que todos hablan a la
vez.
La cuantificación aproxima cada muestra al nivel cuántico más cercano. El cuanto es el salto entre
niveles (página 20).
Ancho de banda de una trama digital
n = cantidad de dígitos del código de la muestra, τ = ancho del pulso, T = n⋅τ lo que dura la
M
muestra, N = cantidad de muestras.
1 1
T = N ⋅T = N ⋅n⋅τ = N ⋅n⋅ = ⟹ B = N ⋅n⋅f
s M w s
B f
w s
Para que pase, el ancho de banda del canal tiene que ser mayor o igual que al cruce en cero.
«5 - Comunicaciones Digitales», págs. 23 y 24
Calcular velocidad, ancho de banda y graficar una trama digital
2° parcial 26/10/2023, 31/10/2024, 23/10/2025 y Final 04/04/2025
Las cuatro hojas dan muestras de información y de control, frecuencia máxima y dígitos por
muestra. La fórmula de arriba alcanza y el enunciado está en Ejercicios. No hay resolución oficial.
Dos fórmulas distintas para el ancho de banda
El apunte 1 da B = s/2 (página 12). El apunte 5 usa B = 1/τ para el cruce en cero del espectro
w
(página 24). Son contextos distintos, y conviene preguntar cuál pide tu comisión.
PCM 30+2
El ejemplo del apunte tiene 30 canales de información y 2 de sincronización y señalización (página 21).
46

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Muestrador -> Multiplex -> Cuantificador -> Multiplexor -> Codificador ->
Código de línea
^
señalización y sincronismo
▾ ¿Cuáles son las etapas de la digitalización?
2° parcial 31/10/2024
Muestreo, multiplexado por tiempo, cuantificación, multiplexado con señalización y
sincronismo, codificación y código de línea. El apunte lo muestra en ese diagrama en bloques.
Fuente: apunte «5 - Comunicaciones Digitales», página 21.
Otros multiplexados
El apunte de multiplexado dice que A significa Acceso, como en FDMA y TDMA. También aclara que
FSK y PSK son modulación, no multiplexado (página 1).
Técnic
Cómo funciona Medio
a
CDM Espectro ensanchado, de baja amplitud y cerca del ruido No guiado (CDMA)
WDM Varias portadoras ópticas. DWDM usa más de 4 longitudes de Únicamente fibra
onda, hasta 80 óptica
Fuente: apunte «Multiplexado CDM-WDM», páginas 1 a 3.
Elección del medio de acceso
Hoy los medios de acceso son par telefónico, fibra óptica, radio enlace y satélite. El coaxil queda solo
para cable módem residencial, y el láser no se expande. Fuente: apunte «Elección medio de acceso»,
página 1.
Las variables
Para elegir se miran estas variables (páginas 2 y 3):
Ubicación de la organización: urbana, suburbana, rural o montañosa.
Temporalidad: permanente o transitoria.
Espacio físico.
Ancho de banda: bajo de 4 a 8 M, medio de 10 a 50 M y alto de más de 100 M.
Madurez de la empresa.
47

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Segurización.
Recursos disponibles.
Elegir un medio de acceso según la zona y la velocidad
Final 04/04/2025 y 2° parcial teórico 2023
En 2023 es multiple choice, con seis consignas de 20. En 2025 son preguntas abiertas.
Los ejemplos del apunte
Ancho de
| Organización | Ubicación |     | Solución |
| ------------ | --------- | --- | -------- |
banda
| Pequeña | Urbana | Bajo | Par telefónico con |
| ------- | ------ | ---- | ------------------ |
HDSL
| Madura, con segurización      | Urbana    | Alto     | Fibra en anillo |
| ----------------------------- | --------- | -------- | --------------- |
| Transitoria, sin espacio      | Rural     | Sin dato | Satelital       |
| Con espacio, sin segurización | Suburbana | Bajo     | Radio enlace    |
Con espacio, con segurización Suburbana Bajo Radio enlace y satelital
| Con segurización    | Suburbana | Alto  | Fibra en anillo      |
| ------------------- | --------- | ----- | -------------------- |
| En crecimiento, con | Rural     | Medio | Fibra y radio enlace |
segurización
| Pequeña | Montañosa o | Bajo | Satelital |
| ------- | ----------- | ---- | --------- |
selva
Fuente: apunte «Elección medio de acceso», páginas 4 y 5.
Segurización. Se logra con recursos disjuntos, como recorridos distintos u operadores diferentes con
infraestructura propia (páginas 6 a 9).
Radio enlace. Necesita visión directa. El mástil con pie de rienda ocupa alrededor del 60% de su
altura. Para 30 m son 18 m a cada lado, o sea 36 × 36 m (página 10).
Teoría de colas
Elementos de un sistema de colas abierto y punto de saturación
2° parcial 26/10/2023, 23/10/2024 y los tres temas del 23/10/2025
Aparece en las cinco hojas del modelo colas. Tenés que nombrar los elementos y definir el punto
de saturación.
48

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Elementos
Los usuarios de una población llegan a una cola y pasan por los servidores (Colas, página 1).
Elemento Qué es
Fuente Conjunto de usuarios que pueden solicitar el servicio. Finita o
infinita
Proceso de arribo Cómo llegan los usuarios. Se usa Poisson
Tiempo de servicio Cuánto tarda cada atención. Se usa exponencial
Capacidad máxima Cuántos caben en el sistema
Número de Cuántos atienden en paralelo
servidores
Disciplina En qué orden se atiende: FIFO, LIFO o prioridades
Fuente: apunte «Teoría de Colas», páginas 4 y 5.
Notación
1
t = t +t μ =
w q s
E[s]
Símbolo Qué es
λ Frecuencia promedio de arribos
μ Frecuencia promedio de servicio
L y L Usuarios en el sistema y en la cola, en promedio
q
W y W Tiempo en el sistema y en la cola, en promedio
q
ρ Utilización del servidor
Fuente: apunte «Teoría de Colas», páginas 1 a 3.
Kendall. Se escribe A/B/c/k/n/Z. La notación más frecuente es A/B/c. Se la utiliza cuando la cola de
espera no tiene limites, la fuente de usuarios es infinita y la disciplina es FIFO. Para A y B, M es
exponencial, D determinística, E Erlang-k, G general, GI general e independiente, y H hiper-
k k
exponencial (páginas 5 y 6).
49

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
▾ ¿Qué significa M/M/1?
2° parcial 26/10/2023, 23/10/2024 y Tema 3 del 23/10/2025
Es la notación A/B/c. Se usa cuando la cola no tiene límites, la fuente es infinita y la disciplina es
FIFO. La primera M indica intervalo entre arribos exponencial, la segunda tiempo de servicio
exponencial, y el 1 un solo servidor. Fuente: apunte «Teoría de Colas», páginas 5 y 6.
Intensidad de tráfico y utilización
|     |     | E[s]    | u   |     |
| --- | --- | ------- | --- | --- |
|     | u = | = λE[s] | ρ = |     |
|     |     | E[τ]    | c   |     |
La intensidad de tráfico determina el número mínimo de servidores. El apunte da este ejemplo: si E[s]
es 15 segundos y E[τ] es 10 segundos, u = 1,5 y se requieren al menos dos servidores. La unidad es el
Erlang. Fuente: «Teoría de Colas», página 6.
Leyes de Little
Las siguientes formulas llamadas leyes de Little, son bastante útiles relacionándolas con cuatro
medidas de performance primarias:
|     | L   | = λW | L = λW |     |
| --- | --- | ---- | ------ | --- |
q q

«Teoría de Colas», pág. 7
Errata del apunte
La hoja imprime «leyes de Littlo». Puse «Little», como en las demás páginas del mismo apunte.
Fuente: «Teoría de Colas», pág. 7.
Ejemplo 1 del apunte
Con λ = 1/48 ing./min, W = 50 min y W = 80 min, resulta L = 50/48 = 1,0417 y L = 80/48 = 1,667.
| q   |     |     | q   |     |
| --- | --- | --- | --- | --- |
|     |     |     |     |     |
«Teoría de Colas», pág. 9
En criollo
Si cada persona pasa 30 minutos en un bar y entran 10 por hora, adentro hay en promedio 5.
Multiplicás cuánta gente llega por cuánto se queda.
Modelo M/M/c abierto
| C(c,u)E[s] |     |           | E[s]       |              |
| ---------- | --- | --------- | ---------- | ------------ |
| W q =      | W = | W q +E[s] | π q (90) = | ln(10C(c,u)) |
|   c(1−ρ)   |     |           |   c(1−ρ)   |              |
50

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Fuente: «Teoría de Colas», página 7.
El caso de un servidor
Cuando c = 1 las fórmulas se simplifican (página 8):
ρE[s] E[s]
C = ρ = λE[s] W = W = π (90) = W ln(10ρ)
q q
1−ρ 1−ρ
Ejemplo 1 del apunte
Un terminal con E[s] = 30 min y ρ = 5/8. Sale W = 50 min, W = 80 min, L = 1,0417 y L = 1,667.
q q
«Teoría de Colas», pág. 9
Calcular un problema M/M/1
2° parcial 26/10/2023, 23/10/2024 y los tres temas del 23/10/2025
Te dan llegadas y servicio, y piden tiempos y usuarios promedio. Las de 2023 y 2024 piden también
conclusiones, y la de 2024 el 90 percentil. Primero poné las dos frecuencias en la misma unidad. El
enunciado está en Ejercicios.
Tiempo en el sistema según la utilización
Fuente: Teoría de Colas, págs. 8 y 9
WW ((mmiinn))
555500
550000
445500
440000
335500
330000
225500
220000
115500
110000 EEjjeemmpplloo 11
5500
00,,11 00,,22 00,,33 00,,44 00,,55 00,,66 00,,77 00,,88 00,,99 ρ
ρ
W
51

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
En criollo
Una caja de supermercado ocupada a la mitad casi no hace esperar. Ocupada al 95% arma una fila
enorme, porque cualquier demora se acumula y no hay tiempo libre para recuperarla.
Controlá el dato antes de calcular
Si λE[s] da mayor que 1 en una cola de un servidor, hace falta más de un servidor según la página
6 del apunte. Algunas hojas son transcripciones de alumnos, así que mirá también el original.
Modelo interactivo y punto de saturación
Es un sistema cerrado con N terminales. Cada usuario piensa E[t] y después pide E[s] de CPU (páginas
12 y 13).
Punto de saturación
La intersección de las dos asíntotas se produce en N∗ tal como:
E[s]+E[t]
N∗ =
E[s]
Este valor de N se llama punto de saturación del sistema. Se concluye que si cada interacción
requiere exactamente E[s] unidades de tiempo de servicio de CPU y exactamente E[t] «tiempo de
pensamiento», N∗ es el número máximo de terminales que pueden ser incluidos de tal forma de
no causar ninguna interferencia mutua.
«Teoría de Colas», pág. 14
Demostración
Para pocos terminales N la interferencia entre usuarios es mínima, esto quiere decir que cuando
uno de los usuarios busca una interacción con la CPU los demás generalmente están en el modo de
pensamiento, por lo tanto, ocasionalmente se formara una cola de espera. Es posible entonces
considerar la curva asintótica a W = E[s] cuando se tiene pocos terminales. Cuando el número de
terminales tiende a infinito, la probabilidad de tener la CPU desocupada (p ) tiende a cero,
0
consecuentemente la curva será asintótica a la recta N ×E[s]−E[t] con N tendiendo a infinito. La
intersección de las dos asíntotas se produce en N∗.
«Teoría de Colas», pág. 14
Errata del apunte
La hoja imprime «la curva estratégica a W = E[s]». Puse «asintótica», porque el párrafo siguiente
habla de «las dos asíntotas». Fuente: «Teoría de Colas», pág. 14.
52

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Las dos asíntotas y el punto de saturación
Fuente: Teoría de Colas, pág. 14
WW  ((ss))
55,,55
55,,00
44,,55
44,,00
33,,55
33,,00
WW  ==  NN··EE[[ss]]  --  EE[[tt]]
22,,55
22,,00
11,,55
11,,00
00,,55
WW  ==  EE[[ss]]
NN**
|     | 55  | 1100 | 1155 |     | 2200 | 2255 |     | 3300 | TT33ee55rrmmiinnaalleess  NN |     |
| --- | --- | ---- | ---- | --- | ---- | ---- | --- | ---- | ---------------------------- | --- |
W = E[s]
W = N·E[s] - E[t]
Ejemplo 3 del apunte
| Con E[t] | = 3 s y E[s] | = 0,2 s, resulta N∗ |     | =   | 3,2/0,2 | = 16 terminales. |     |     |     |     |
| -------- | ------------ | ------------------- | --- | --- | ------- | ---------------- | --- | --- | --- | --- |
«Teoría de Colas», págs. 13 y 14
Asignación de capacidad
| Cerca de  | C, ¿el retardo crece sin límites? Justificar |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
η
Los tres temas del 23/10/2025
El cálculo de asignación de capacidad con tiempo mínimo aparece en las hojas del 26/10/2023 y
23/10/2024.
Cada enlace se comporta como una cola M/M/1. λ  es la frecuencia de arribo, 1/η  la longitud promedio
|                         |     |                          |     |     | i   |     |     |     |     | i   |
| ----------------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| del mensaje en bits y C |     |  la capacidad del canal. |     |     |     |     |     |     |     |     |
i

λ
|     |     |         |     | 1   |     | 1        |      |     | i   |     |
| --- | --- | ------- | --- | --- | --- | -------- | ---- | --- | --- | --- |
|     |     | μ = η C | T = |     | =   |          |      | ρ   | =   | < 1 |
|     |     | i i     | i i | η C | −λ  | η C (1−ρ |      | i   | η C |     |
|     |     |         |     | i i | i   | i i      | i )  |     | i   | i   |
|     |     |         |     |     |     |          |      |     |     |     |
Fuente: apunte «Asignación de Capacidad», páginas 2 y 3.
53

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
▾ ¿Cerca de  η C el retardo crece sin límites?
2° parcial 23/10/2025, Tema 1
El apunte dice: «Cuando de la frecuencia de flujo de tráfico es cercana al valor η C  el tiempo de
i i

retardo crece sin límites». Su justificación es la fórmula de T , porque cuando ρ  se acerca a 1 el
i i

denominador tiende a cero. Fuente: apunte «Asignación de Capacidad», página 3.
Enlace del apunte
Con λ 0,33 mens/s, mensajes de 120 bits y 100 bps, T 2 s. De eso, 1,2 s son para transmitir y 0,8 s
= ≈
de almacenamiento.
«Asignación de Capacidad», pág. 3
Regla de la raíz cuadrada
Regla de asignación de la raíz cuadrada del flujo de información
Suponemos el objetivo es minimizar el tiempo de retardo promedio sobre la red completa con
una capacidad total supuesta fija. Minimizando por diferenciación de E[T]+αC con respecto a C
i

, se encuentra la solución óptima dada por:
|      | λ i     | C(1−ρ) λ i /η | i   |
| ---- | ------- | ------------- | --- |
| Copt | =   +   |               |     |
|      | i       | n             |     |
|      |   η i   | ∑ λ /η        |     |
|      |         | j =1  j j     |     |
|      |         |               |     |
Esta asignación de capacidad se denomina la «regla de asignación de la raíz cuadrada del flujo de
información». El T  depende inversamente de C (o sea del costo). La ecuación de T  da el
min   min
mínimo tiempo de retardo posible para un determinado costo.
«Asignación de Capacidad», págs. 5 y 6
Errata del apunte
El multiplicador de Lagrange se imprime con un signo parecido a ∝. Puse α para que no se lea
como «proporcional». Fuente: «Asignación de Capacidad», pág. 5.
Las otras dos fórmulas del método (páginas 5 y 6):
1
| E[T] | = λ  | E[T ] δ = | λ   |
| ---- | ---- | --------- | --- |
|      | i    | i         | i   |
|      | δ ∑  |     ∑     |     |
|      | i    | i         |     |
2
λ /η
|       | ∑ i     | i 1     | λ   |
| ----- | ------- | ------- | --- |
| Tˉ    | ( i     |  )      | i   |
| =     |         | ρ =     |     |
| min   | δC(1−ρ) |   C ∑ η |     |
i
i
54

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Errata del apunte
En la definición de ρ, la hoja imprime δ en lugar de ρ. Puse ρ, porque la frase siguiente la llama
intensidad de tráfico de la red y el ejemplo la usa así. Fuente: «Asignación de Capacidad», págs. 5
y 6.
La ecuación de Copt tiene dos partes. La primera, λ /η , es el valor mínimo necesario para habilitar el
i i i
tráfico sobre el canal. La segunda indica la capacidad remanente según la estrategia de la raíz
cuadrada (página 6).
Red del apunte
Con δ = 1,7 mens/s, 120 bits y C = 4500 bps, ρ = 1,7⋅120/4500 = 0,0453.
«Asignación de Capacidad», págs. 5 y 6
Ejemplo de estrella y árbol
El apunte compara redes en estrella y en árbol en sus páginas 7 a 9. No aparece como consigna en
las hojas de 2023 a 2025.
Modelo OSI
Capa 1 de OSI y su relación con la capa 2
Temas 1 y 2 del 23/10/2025
Solo se pide esta relación. El resto del modelo no aparece en las hojas que leí.
Tiene siete capas. El modelo no es en sí una arquitectura de red, porque solo indica lo que debe hacer
cada capa. Fuente: apunte «OSI, TCP/IP y Hardware de Redes», página 17.
Capa Qué hace
7. Aplicación Protocolos que los usuarios necesitan, como HTTP
6. Sintaxis y semántica de la información
Presentación
5. Sesión Establece sesiones entre máquinas
4. Transporte Comunicación extremo a extremo
3. Red Enruta paquetes y controla la congestión
2. Enlace Transforma un medio puro en una línea libre de errores, con tramas y
control de flujo
55

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Capa Qué hace
1. Física Transmisión de bits puros por un canal
Fuente: mismo apunte, páginas 17 a 20.
▾ ¿Qué hace la capa 1 de OSI y cómo se relaciona con la capa 2?
2° parcial 23/10/2025, Tema 1
La capa física lleva a cabo la transmisión de bits puros a través de un canal de comunicación. Se
ocupa de voltios, nanosegundos, pines y del medio que está debajo. La capa de enlace transforma
ese medio puro en una línea libre de errores no detectados para la capa de red, separando los
datos en tramas. Fuente: apunte «OSI, TCP/IP y Hardware de Redes», páginas 17 y 18.
Qué practicar
Andá a Ejercicios. Hacé primero los del modelo que toca en tu comisión.
56

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
COMUNICACIÓN DE DATOS
Final
Qué trae el único final de 2023 en adelante que leí, y dónde está la teoría de
cada consigna.
Resumen no juzgado. Todavía nadie evaluó si alcanza para estudiar solo con esto.
Cómo viene el examen
Leí un final de 2023 en adelante, el del 04/04/2025, con una hoja de práctica y otra de teoría. También
leí finales de 2021, del plan viejo, y dos problemas de 2025 repiten los mismos números.
Un solo final no alcanza para decir qué se repite. Lo que sigue muestra esa fecha y remite a la teoría.
La práctica
Multinivel con arranque y stop, trama PCM y un problema de colas
Final práctica 04/04/2025
Tiene tres problemas. El primero pide M(T), I , R y la gráfica. El segundo pide el ancho de banda
x
y los gráficos de una trama de 25+2 muestras. El tercero es una sala de emergencias con llegadas
de Poisson.
Cada tema está desarrollado en estas secciones:
Transmisión multinivel.
TDM y la trama y Muestreo y PCM.
El caso de un servidor.
Los enunciados están en Ejercicios. No hay resolución oficial de ninguno.
Cuidado con el canal binario
Los finales de 2021 tienen un problema de canal binario simétrico. No está en la hoja de 2025. Si
querés practicarlo, la teoría está en Información, entropía y canal.
La teoría
La hoja tiene tres consignas. Las respuestas salen de los apuntes y citan archivo y página.
57

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
Modulación para mensajes digitales
▾ ¿Qué modulaciones se usan para mandar mensajes digitales por una red que
transporta señales analógicas?
Final 04/04/2025
ASK, FSK y PSK. El apunte da el ejemplo de una computadora por línea telefónica con MODEM, y
aclara que ASK no se usa actualmente. Fuente: apunte «5 - Comunicaciones Digitales», página 11.
▾ ¿Cómo se aumenta la velocidad?
Final 04/04/2025
Con modulación multinivel. Se usan más frecuencias en FSK o más fases en PSK. Combinando
amplitud y fase, con 2 amplitudes y 4 fases hay 8 estados, o sea 3 dígitos por símbolo. Fuente:
apunte «5 - Comunicaciones Digitales», página 13.
▾ ¿Qué aplicación práctica tiene?
Final 04/04/2025
El apunte nombra la computadora conectada por línea telefónica mediante un MODEM,
modulador y demodulador. Fuente: apunte «5 - Comunicaciones Digitales», páginas 3 y 11.
Las gráficas de cada técnica están en el apunte, página 11 en adelante: Diagrama en el Drive.
Códigos
▾ ¿Qué es un código unívoco?
Final 04/04/2025
Un código es unívocamente decodificable si a cualquier secuencia de palabras código le
corresponde una y sólo una secuencia de símbolos de la fuente. Fuente: apunte «2 -
Codificación», página 1.
▾ ¿Qué es un código instantáneo?
Final 04/04/2025
La condición necesaria y suficiente para que un código sea instantáneo es que ninguna palabra
del código coincida con el prefijo de otra. Fuente: apunte «2 - Codificación», página 2.
58

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
▾ ¿Qué es la inecuación de Kraft?
Final 04/04/2025
Si los enteros l 1 ;… ;l q satisfacen ∑r−l i ≤ 1, esta es condición suficiente y necesaria para que
exista al menos un código instantáneo de r símbolos en su alfabeto y con esas longitudes. Fuente:
apunte «2 - Codificación», páginas 2 y 3.
▾ ¿Qué es un código compacto?
Final 04/04/2025
Dada la fuente S, un código instantáneo aplicado a S es compacto si su longitud media es igual o
menor que la longitud media de todos los códigos instantáneos que puedan aplicarse a la misma
fuente y al mismo alfabeto. Fuente: apunte «2 - Codificación», página 5.
▾ ¿Cuál es la cota inferior de la longitud media?
Final 04/04/2025
La longitud media de un código es mayor o igual que la entropía de la fuente dividida por el log
2
del número de símbolos del alfabeto código, H(s)/logr ≤ L. Fuente: apunte «2 - Codificación»,
páginas 5 a 8.
La demostración completa está en el 1° parcial.
Medios de transmisión y de acceso
Ventajas y desventajas de par telefónico, fibra, radio enlace y satélite
Final 04/04/2025
Las ventajas están en Medios de transmisión, y lo de cada medio de acceso en Elección del medio
de acceso.
▾ ¿Qué medio elegís para una zona montañosa sin gran velocidad?
Final 04/04/2025
El ejemplo 8 del apunte es una organización pequeña en zona montañosa o selva con ancho de
banda bajo, y usa satelital. Fuente: apunte «Elección medio de acceso», páginas 4 y 5.
59

24/11/26, 18:58 Comunicación de Datos en PDF. El Santo Resumen
▾ ¿Qué medio elegís para una zona urbana con gran velocidad?
Final 04/04/2025
El ejemplo 2 del apunte es una organización madura en zona urbana con ancho de banda alto y
segurización, y usa fibra óptica en anillo. Fuente: apunte «Elección medio de acceso», páginas 4 y
5.
▾ ¿Qué medio elegís para una zona suburbana con gran velocidad?
Final 04/04/2025
El ejemplo 6 del apunte es una organización en zona suburbana con ancho de banda alto y
segurización, y usa fibra óptica en anillo. Fuente: apunte «Elección medio de acceso», páginas 4 y
5.
▾ ¿Qué medio elegís para una zona suburbana sin gran velocidad?
Final 04/04/2025
El ejemplo 4 del apunte es una organización en zona suburbana con ancho de banda bajo, con
espacio y sin segurización, y usa radio enlace. Con segurización, el ejemplo 5 suma satelital.
Fuente: apunte «Elección medio de acceso», páginas 4 y 5.
Los ejemplos tienen más datos que la consigna
El apunte agrega espacio físico y segurización, y la consigna no los menciona. Conviene decir
qué suposición hacés.
Qué practicar
Hacé los problemas de Ejercicios que dicen Final. Los de 2021 llevan la marca de plan viejo.
Este contenido se basa en el material disponible en el Drive de la carrera. No reemplaza bajo ningún concepto lo dado
por los docentes en cada aula, y los resúmenes no están verificados por ellos. Se recomienda fuertemente verificarlos
con el material que brindan tus profesores y adaptarlos para tu uso personal o grupal con el botón Editar, en la barra
de arriba de cada resumen.
60