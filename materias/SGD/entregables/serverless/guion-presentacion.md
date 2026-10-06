# Serverless — guion de la presentación

> Notas internas (no salen en el docx). Este archivo es la fuente de las notas
> del orador: `scripts/pptx-sgd-serverless/build.js` lo lee y pone cada bloque
> `## Lámina N` como nota de la diapositiva N. Si se cambia el texto acá, se
> regenera el pptx. Duración hablada: `.venv/bin/python scripts/guion-timing.py
> materias/SGD/entregables/serverless/guion-presentacion.md`.
> Ritmo de referencia: 145 palabras por minuto.

## Reloj y reparto

15 minutos, 14 láminas, 4 expositores. Cada uno tiene unos 3:30 y le pasa la
palabra al siguiente con una frase de pase, que ya está escrita al final de su
última lámina. El texto no es para leer: es lo que hay que decir, en el orden en
que conviene decirlo.

| Expositor | Bloque | Láminas | Tiempo | Acumulado |
|---|---|---|---|---|
| 1 | Qué es | 1–4 | 3:30 | 3:30 |
| 2 | Cómo funciona por dentro | 5–7 | 3:45 | 7:15 |
| 3 | Economía y datos | 8–10 | 3:50 | 11:05 |
| 4 | Límites y futuro | 11–14 | 3:30 | 14:35 |

El texto hablado dura unos 12:45 a 145 palabras por minuto; el resto es margen
para pausas, cambios de expositor y algún imprevisto. Los bloques 2 y
3 son los más técnicos: conviene que los tomen quienes mejor manejen el tema.

Si el tiempo se acorta, en este orden se recorta: la lámina 13 (se dice una
frase y se pasa al cierre), la parte de concurrencia de la lámina 5 y la
columna de isolates de la lámina 7.

## Lámina 1 — Portada

*Expositor 1 · 0:20*

Buenas. Somos el grupo que va a presentar serverless. Vamos a contar qué es,
cómo funciona por dentro, cuánto cuesta de verdad y, sobre todo, cuándo no
conviene usarlo. Somos cuatro y nos vamos a ir pasando la palabra por bloques.

## Lámina 2 — Serverless no significa sin servidores

*Expositor 1 · 1:00*

Arranquemos por el nombre, que es lo primero que confunde. Serverless no
significa que no haya servidores. Los servidores existen, están en un
datacenter y alguien los mantiene. La diferencia es que ese alguien no sos vos:
es el proveedor. Pasa lo mismo con wireless: los cables siguen existiendo, pero
no los tirás vos.

Y no es una moda de nicho. Lambda, el servicio serverless de Amazon, ejecuta
más de quince billones de invocaciones por mes, billones de los nuestros, diez a
la doce. Según el relevamiento de Datadog de 2025, el sesenta y cinco por
ciento de los clientes de AWS usa Lambda y el setenta por ciento de los de
Google Cloud usa Cloud Run. O sea, es algo que la mayoría de las empresas que
están en la nube ya usa en producción. Entonces, si los servidores existen,
¿qué es exactamente lo que cambia?

## Lámina 3 — Tres propiedades

*Expositor 1 · 1:00*

La definición que tomamos es la de la CNCF, la fundación que agrupa los
proyectos cloud native. Dice que serverless es construir y correr aplicaciones
que no requieren gestión de servidores, y que se ejecutan, escalan y facturan
según la demanda exacta del momento.

De ahí salen tres propiedades, y las usamos como criterio. Primera: no
administrás infraestructura. No elegís el tamaño de la máquina, no parcheás el
sistema operativo. Segunda: escala hasta cero. Si llegan mil pedidos levanta lo
necesario, y si no llega ninguno, no queda nada corriendo. Tercera: pagás por
uso real, por ejecución, no por tener algo encendido.

Si falta una, no es serverless. Un Kubernetes administrado por el proveedor
cumple la primera a medias, pero no la tercera: el pod cuesta plata aunque
nadie lo llame.

## Lámina 4 — La escalera de abstracción

*Expositor 1 · 1:10*

Para entender por qué apareció esto, sirve mirar la historia como una escalera.
En cada escalón el desarrollador se desentiende de una capa más.

Con bare metal comprás el servidor y te ocupás de todo. Con IaaS, por ejemplo
EC2, alquilás una máquina virtual por hora. Con PaaS subís tu aplicación y el
proveedor se ocupa del sistema operativo. Con contenedores empaquetás la
aplicación con sus dependencias. Y en el último escalón, FaaS, lo que desplegás
es una sola función.

Fíjense en la última fila: la unidad de cobro pasa de la hora al milisegundo.
Es la primera vez que el costo de cómputo puede ser cero cuando nadie usa el
sistema.

Abajo está la otra distinción importante. FaaS es tu código: funciones que se
disparan con eventos. BaaS son servicios que consumís por API, como la base, la
autenticación o el almacenamiento. En una aplicación serverless real, la mayor
parte es BaaS, y tus funciones son el pegamento entre esos servicios.

Pase al expositor 2: ahora que sabemos qué es, veamos qué pasa por dentro
cuando llega un pedido.

## Lámina 5 — Una función no corre: es invocada

*Expositor 2 · 1:20*

Una función serverless no está corriendo todo el tiempo esperando. Se invoca
cuando pasa algo: llega un pedido HTTP, alguien sube un archivo, entra un
mensaje a una cola o se cumple un horario.

La primera vez, la plataforma tiene que preparar el entorno. Esa fase se llama
INIT: crea una máquina virtual chiquita, descarga el código, arranca el runtime
y corre el código de inicialización, que es donde van los imports y la conexión
a la base. Después viene INVOKE, que ejecuta la función propiamente dicha. Al
terminar, el entorno no se destruye: se congela. Si llega otro pedido, se
reutiliza y se saltea todo el INIT. Si pasan entre cinco y quince minutos sin
pedidos, se apaga.

De esto salen dos consecuencias. La primera: el estado no se puede guardar en
memoria, porque no hay garantía de que dos pedidos caigan en el mismo entorno.
Es stateless por contrato. La segunda: en Lambda cada entorno atiende un pedido
a la vez. Si llegan cien por segundo y cada uno tarda dos décimas, necesitás
veinte entornos simultáneos. Si tarda dos segundos, necesitás doscientos.

## Lámina 6 — Cold start

*Expositor 2 · 1:10*

Esa primera invocación, la que tiene que pasar por INIT, es más lenta. Se llama
cold start y es el precio de poder escalar a cero: si no hay nada corriendo,
algo hay que arrancar.

Cuánto tarda depende mucho del lenguaje. Go o Rust, que son compilados,
arrancan en menos de cien milisegundos. Python anda entre doscientos y
cuatrocientos. Java sin optimizar puede tardar segundos. Si además la función
está dentro de una red privada, se suman unos cientos de milisegundos más.
Estos números son órdenes de magnitud reportados en 2026, no mediciones
nuestras.

Para bajarlo hay varias opciones. Provisioned Concurrency mantiene entornos
precalentados, pero se pagan por hora, así que se pierde parte del pago por
uso. SnapStart, en vez de arrancar de cero, restaura una foto de un entorno ya
inicializado: así Java baja a unos cien milisegundos. Y siempre ayuda tener un
paquete liviano, con pocas dependencias.

## Lámina 7 — El sandbox por dentro

*Expositor 2 · 1:15*

Ahora, el problema que tiene el proveedor es difícil: correr código de miles de
clientes distintos en la misma máquina física, sin que uno pueda ver al otro, y
arrancando en milisegundos. Los contenedores solos no alcanzan, porque
comparten el kernel. Las máquinas virtuales tradicionales son demasiado lentas.

Amazon lo resolvió con Firecracker, un monitor de máquinas virtuales escrito en
Rust y open source. Levanta una microVM con Linux en menos de ciento veinticinco
milisegundos y con unos cinco megas de memoria extra. Lo logra sacando todo lo
que una PC normal trae y una función no necesita. El aislamiento es por
hardware. Es la base de Lambda.

Cloudflare tomó el camino opuesto: isolates de V8, el motor de JavaScript de
Chrome. Un solo proceso aloja miles de funciones aisladas entre sí. Arrancan
unas cien veces más rápido que un proceso de Node, así que el cold start
prácticamente desaparece. El costo es que el aislamiento es por software y
solo corre JavaScript o WebAssembly.

Pase al expositor 3: todo esto tiene un costo, y ahí es donde serverless se
pone interesante.

## Lámina 8 — Se paga por milisegundo

*Expositor 3 · 1:15*

El modelo de cobro tiene dos partes. Una por cantidad de pedidos: veinte
centavos de dólar por millón. Otra por duración, medida en gigabyte-segundo,
que es la memoria que configuraste multiplicada por el tiempo que corrió la
función. Se cobra al milisegundo, y hay una capa gratuita todos los meses de
un millón de pedidos y cuatrocientos mil gigabyte-segundo.

Un detalle: la CPU que te dan es proporcional a la memoria. Si duplicás la
memoria, la función puede terminar en la mitad del tiempo y costar lo mismo.

Hicimos la cuenta con un caso concreto: una API con cinco millones de pedidos
por mes, doscientos milisegundos cada uno y medio giga de memoria. Descontando
la capa gratuita da unos dos dólares y medio por mes. Una máquina virtual chica
de Amazon, encendida todo el mes, cuesta unos quince. Para este caso serverless
sale seis veces más barato.

## Lámina 9 — El punto de cruce

*Expositor 3 · 1:20*

Pero el ejemplo anterior tiene trampa: esa API está ociosa casi todo el tiempo.
¿Qué pasa si la función corre sin parar?

El gráfico compara el costo de tener un procesador disponible durante una hora.
El servidor cuesta lo mismo esté ocupado o no: es la línea plana. Lambda, la
línea naranja, arranca en cero y crece con el uso. El problema es la
pendiente: normalizado por procesador, el vCPU-hora de Lambda cuesta unas tres
veces más que el de una instancia equivalente.

Las dos líneas se cruzan alrededor del treinta y cuatro por ciento de uso, un
tercio.
Debajo de eso gana serverless, y por mucho. Arriba, conviene un servidor.

Es la analogía del auto: alquilar un servidor es tener auto propio, lo pagás
aunque esté estacionado. Serverless es tomar un Uber: si no viajás no pagás,
pero el kilómetro sale más caro. Si viajás ocho horas por día, te conviene el
auto.

## Lámina 10 — Datos: apagar el cómputo sin perder la base

*Expositor 3 · 1:15*

Esto es lo que más se conecta con la materia. Para que una base de datos sea
serverless, tiene que poder apagar el cómputo sin perder los datos. El truco es
separar las dos cosas: los datos viven en un almacenamiento persistente, y los
nodos que procesan consultas se prenden y se apagan según la demanda. Así
funcionan Neon, Aurora Serverless y DynamoDB en modo on demand.

Pero hay un choque clásico. Una base relacional como Postgres soporta cientos
de conexiones, no miles. Si quinientas funciones corren a la vez y cada una
abre su conexión, la base se cae. Las soluciones son dos: poner un pooler en
el medio, como RDS Proxy o PgBouncer, que reutiliza pocas conexiones para
muchas funciones, o usar bases que se consultan por HTTP en lugar de mantener
conexiones abiertas.

Pase al expositor 4: con todo esto ya podemos decir cuándo conviene y cuándo
no.

## Lámina 11 — Cuándo sí y cuándo no

*Expositor 4 · 1:00*

Juntando todo lo anterior, serverless encaja cuando la carga es espigada o
impredecible, cuando el trabajo se dispara por eventos y cuando no hace falta
guardar estado entre pedidos. Por ejemplo, generar una miniatura cada vez que
alguien sube una foto, procesar datos de sensores o correr tareas programadas.
iRobot, el de la Roomba, procesa más de veinte millones de eventos por día así
y reporta un treinta por ciento menos de costo.

No encaja cuando la carga es constante, porque ya vimos que arriba de un
tercio de uso pierde. Tampoco cuando la latencia es crítica, por el cold
start, cuando hace falta estado o conexiones persistentes, o cuando el sistema
es una cadena larga de funciones muy acopladas. El caso más famoso de eso lo
contó el propio Amazon.

## Lámina 12 — Prime Video

*Expositor 4 · 1:00*

En 2023, el equipo de Prime Video publicó que había sacado un sistema de
serverless y había bajado el costo un noventa por ciento.

El sistema analizaba la calidad de cada stream que miraban los usuarios. Estaba
armado con funciones encadenadas, y por cada segundo de video había varias
transiciones entre funciones. Además, los datos pasaban de una etapa a otra
por la red. Lo que más costaba no era procesar: era mover datos. Lo
reescribieron como un solo proceso en contenedores, con todo junto en memoria.

La lección no es que serverless sea malo. Es que, cuando comunicar cuesta más
que computar, hay que juntar los componentes, no separarlos.

## Lámina 13 — 2026

*Expositor 4 · 0:50*

Y la industria tomó nota. En 2026 Amazon lanzó Lambda Managed Instances: las
mismas funciones, pero corriendo sobre servidores dedicados, pensado para
cargas estables. Es el propio proveedor reconociendo el punto de cruce. También
anunció microVMs con sesiones de hasta ocho horas y estado, que rompen dos de
los dogmas originales.

En paralelo, la inferencia de inteligencia artificial se está llevando al
edge, cerca del usuario. Y dos de cada tres empresas que usan funciones también
usan contenedores. El futuro es híbrido: cada carga va donde le conviene.

## Lámina 14 — Cierre

*Expositor 4 · 0:40*

Para cerrar, tres ideas. Serverless no es sin servidores: es no tener que
administrarlos. Se paga por uso, así que gana en cargas espigadas y pierde
cuando el uso es alto y constante. Y es un trade-off: se elige porque encaja
con el problema, no porque esté de moda. Gracias. ¿Preguntas?

## Preguntas probables

Respuestas cortas para tener a mano. Cada una indica qué expositor la toma.

| Pregunta | Quién | Respuesta corta |
|---|---|---|
| ¿Entonces no hay servidores? | 1 | Hay. No son tuyos y no los administrás. Como wireless. |
| ¿Es más barato? | 3 | Depende del uso. Debajo de un tercio de utilización (~34 %), sí y por mucho; arriba, no. |
| ¿Y si mi función tarda una hora? | 2 | No entra: Lambda corta a los 15 min. Hay que partirla, usar Cloud Run (hasta 60 min) o contenedores. |
| ¿Cómo se debuggea? | 2 | Es una debilidad real. Logs y tracing distribuido; el entorno local no reproduce la nube. |
| ¿Cómo manejo la conexión a la base? | 3 | Pooler (RDS Proxy, PgBouncer) o bases con API HTTP. Es la lámina 10. |
| ¿Me quedo atado a AWS? | 4 | En la función no tanto; en todo lo que la rodea (colas, base, auth), sí. Contenedores serverless y Knative lo mitigan. |
| ¿Sirve para machine learning? | 4 | Para inferencia liviana y tareas batch, sí. Para entrenar, no: timeout y falta de GPU. Está cambiando en 2026. |
| ¿Es seguro correr mi código al lado del de otro cliente? | 2 | Sí: el aislamiento es por virtualización de hardware (Firecracker + KVM + seccomp), no por confianza. |
| ¿Existe serverless fuera de la nube? | 4 | Sí: Knative y OpenFaaS sobre tu propio Kubernetes. Se gana el modelo de programación, no el ahorro, porque el clúster se paga igual. |
| ¿De dónde sale el 30 %? | 3 | Cálculo propio con precios oficiales: Lambda ≈ USD 0,106 por vCPU-hora contra ≈ USD 0,036 de una EC2 c7g.large. El cociente da ~34 %. |
