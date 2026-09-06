# IPP — Material de cursada: lo que agrega al repaso

> Complemento de [`repaso-parcial.md`](repaso-parcial.md). **No lo reemplaza.** Todo lo que ya está ahí
> (banco de preguntas de los parciales 2022 y 2026, distractores reciclados, corrección del caso de
> junio 2026, plan cronometrado de Axure, checklist de entrega) no se repite acá.
>
> Este documento sale de tres fuentes que el repaso no tenía a la vista:
> el **PPT de teoría de la cátedra** (48 láminas), la **desgrabación de las clases del 13-04 y 20-04**,
> y una **auditoría de tus propias entregas** (EJ 3, 4, 5 y 6) contra las soluciones oficiales.
>
> Misma convención de origen:
> - **[CÁTEDRA]** = material de la cátedra (PPT, dicho por el docente en clase, soluciones oficiales).
> - **[NUESTRO]** = análisis propio, no verificado por la cátedra.

---

## 1. Lo que dijo el docente en clase

### 1.1 El formato del parcial, según él

**[CÁTEDRA]** El 13-04, repasando condiciones de aprobación:

> "Básicamente hay un parcial individual que no le vamos a poner teoría, sino va a ser hacer un modelo
> de BPM en el Visaggi [Bizagi] y hacer un prototipo de Ayur [Axure]."

⚠️ **AVISO — esto contradice `repaso-parcial.md` sección 1**, que documenta 10 preguntas multiple choice
en los formularios de 2022 y de 2026. **[NUESTRO]** Los parciales reales mandan sobre un comentario al
pasar de la primera clase: **seguí estudiando la teoría**. Lo que sí te dice esta cita es dónde está el
peso real de la nota: el modelado y el prototipo. Si tenés que repartir tiempo hoy, la teoría se contesta
rápido con los dos bancos; el modelado es lo que se corrige de verdad.

Lo demás del formato que dio en clase, y que el repaso no tenía:

- **Se hace todo el mismo día.** "Acá están puestos como dos temas, parcial de BPMN y parcial de
  prototipo, pero se hace todo junto el mismo día."
- **Remoto e individual.** "Lo vamos a hacer remoto, fíjense que acá sería imposible" (no hay máquinas
  en el aula). Individual "porque por reglamento tengo que tener alguna evaluación individual".
  **[NUESTRO]** Consecuencia operativa: **abrí Bizagi y Axure hoy**, no mañana. Si tu instalación falla,
  hay una **máquina virtual de la cátedra** con Bizagi que reparte a quien la pida (plan B).
- **Nivel de dificultad, textual:** "No son difíciles estos parciales, son hacer algo muy parecido a lo
  que venimos haciendo en clase."
- **El dato más accionable de toda la cursada:** "Hacemos dos clases de teoría, después empezamos a
  hacer ejercicios de complejidad sencilla, después vamos aumentando. **El parcial es muy parecido a
  esos ejercicios iniciales que hacemos.**"
  **[NUESTRO]** O sea: se parece a Requerimiento Organismo de Control / Gestión Evaluación /
  Publicación Artículos, **no** a Organizar Fiesta ni a Agencia de Viajes. Si el enunciado de mañana te
  parece un monstruo, releelo: probablemente lo estés complicando.
- **La advertencia sobre la herramienta**, que repitió: "Si nunca usaste el Visagi y el día del parcial
  lo querés usar, no te va a funcionar. Hay muchas cosas que uno las mira y dice 'ah, esto es re fácil',
  y después hay que sentarse un día y hacerlo."
- **Aprobación directa:** parcial individual aprobado + integrador grupal final. "En los últimos 3 años
  todos hicieron aprobación directa, todos los que se quedaron." El parcial no está pensado como filtro.
- **Fechas que dio en abril:** parcial comisión 1 el 3 de agosto, recuperatorio 5 de octubre, globalizador
  2 de noviembre. **[NUESTRO]** Ninguna coincide con el 7 de septiembre: o se corrió, o es instancia
  extra. El formato anunciado vale igual.

### 1.2 Qué NO entra (te ahorra tiempo de estudio)

**[CÁTEDRA]** Lo dijo explícitamente el 13-04:

| Tema | Cita | Alcance |
|---|---|---|
| Ejecución del BPMS | "Nosotros nos vamos a quedar en la anotación, no vamos a hacer la ejecución del BPMS" | no entra |
| Objetos de datos (la hojita doblada, la base de datos) | "No lo vamos a hacer porque lo complejiza sin mucho sentido" | **no se modelan**, pero sus definiciones sí están en el PPT (ver 2.3) |
| Diagramas de coreografía y de conversación | "Lo que vamos a hacer nosotros va a ser uno como este o eventualmente uno como este" (orquestación pública con la otra organización como caja negra, o colaboración con las dos abiertas) | no se modelan; **pueden aparecer nombrados en el multiple choice** |
| Eventos adjuntos NO interruptores | "O si no, si tienen líneas de trazos, que no interrumpan, pero eso es algo más raro que no lo vamos a usar" | para modelar usá siempre el interruptor (borde de línea llena); para el MC acordate: **punteado = NO interrumpe** |

### 1.3 Criterios de corrección — lo explícito

**[CÁTEDRA]** Cinco cosas que dijo con todas las letras. **[NUESTRO]** Es lo más parecido a una rúbrica
que se puede reconstruir:

1. **Los conectores tienen que quedar LIGADOS a los objetos.** Es lo único que marcó con la palabra
   "importante" sobre la herramienta: *"Es importante que queden conectados, así yo muevo la tarea y se
   mueve la línea."* **El test es ese:** antes de exportar, agarrá cada tarea y movela un centímetro.
   Si la flecha no la sigue, el conector está suelto.
2. **El diagrama tiene que entrar en la página.** *"Si en vez de usar el iconito directo de imprimir van
   al menú Archivo, Imprimir, tenemos la vista preliminar. Eso nos puede servir para ajustar a que entre
   en una sola parte."* Un diagrama cortado es un entregable defectuoso aunque el modelo esté bien.
3. **El paralelo se cierra sí o sí.** Ver 1.4, es el matiz que corrige la wiki.
4. **Compuerta compleja = compuerta + anotación.** *"Una compleja requiere una anotación y me tenés que
   explicar cómo se resuelve, por eso se llama compleja."* Sin la nota, está mal por definición.
5. **Actor de otra organización = pool aparte, nunca lane.** Lo respondió como pregunta directa de una
   alumna: *"Si yo quisiera representar al proveedor, lo tendría que poner como otro pool, no como una
   calle, porque pertenece a otra organización."*

**[NUESTRO]** Y tres implícitos que se deducen de cómo explicó:

6. **El ícono de la tarea tiene que corresponder a quién la ejecuta y con qué** (rúbrica completa en 1.5).
7. **El flujo de mensaje representa INFORMACIÓN.** Entrega física de mercadería entre pools no se dibuja
   como mensaje: *"Fíjense que este y este no se unen, porque no es flujo de información, esto es flujo
   de mercadería."*
8. **El diagrama cubre el proceso de negocio completo**, con una salida que tenga valor para el cliente,
   no un paso aislado: *"Reservar es un paso para comprar el pasaje. O si quieren una meta más amplia,
   que sería viajar."* / *"Evaluar candidato es un paso, el proceso de negocio es la selección de
   personal."* Si el enunciado te da un paso suelto, el modelo abarca el flujo completo.

**Contexto de corrección:** corrige él solo, de a uno, en secuencia — usó "corregir parciales" como
ejemplo de instancias múltiples secuenciales y contó que el año pasado corrigió 30, 40, 50 parciales.
**[NUESTRO]** Diagrama legible y prolijo. Nada para adivinar.

### 1.4 El énfasis teórico: qué explicó más y cómo

**[CÁTEDRA]**

**TOKEN — es el concepto que más veces explicó** (dos veces largas, una de ellas entera porque un alumno
preguntó "profe, ¿cómo dijiste que funcionan los tokens?"). Lo usó como herramienta para explicar
**todas** las compuertas:

| Compuerta | Cómo la explicó con tokens |
|---|---|
| Exclusiva | entra un token, sale **uno solo** por alguna de las ramas |
| Paralela | entra un token, salen **dos** que avanzan independientes "y en algún momento se tienen que volver a juntar" |
| Inclusiva | *"entra un token y sale al menos uno. No exactamente uno: al menos uno. Y pueden ser todos"* |
| Basada en eventos | entra un token y sale uno solo, **pero esperando** |

Y el cierre: *"Un evento de fin lo que hace es consumirse el token, y el token después no sigue más."*
**[NUESTRO]** Si en el multiple choice dudás de una compuerta, contá tokens. Es literalmente el método
que él usa.

**CIERRE DE COMPUERTAS — matiz que corrige la wiki** (ver 3.1). Lo dijo dos veces, aclarando "repito algo
que dije": *"De hecho siempre vos podés dibujar los rombos que cierran... pero en el caso de los OR, por
ejemplo el inclusivo, el que cierra es opcional, si querés lo hacés, si querés no lo hacés. **En el caso
del paralelismo hay que hacerlo sí o sí**, porque si no, no terminás de definir cómo funciona el
proceso."* Y sobre los TP: *"De experiencia, de todos los trabajos prácticos hay un 5% que cierran."*

**FLUJO DE DEFAULT** — no está ni en la wiki ni en el repaso, y es contenido de modelado **y** de MC:
*"Podés tener una de las ramificaciones con la barra: eso te implica cuál es la de default. Si no se
cumple ninguna condición, va a venir por acá."* Es la barrita cruzada sobre una salida de compuerta
exclusiva o inclusiva. El PPT además lo **recomienda explícitamente** para la inclusiva (lámina 36).

**COMPENSACIÓN = DESHACER.** Se detuvo en la terminología: *"Formalmente a esto se le llama compensación;
a mí me gusta más llamarlo deshacer, me parece que es más fácil de entender lo que significa: quiero
dejar de ejecutar algo, pero eso me implica tener que hacer una acción para volver a un estado
anterior."* Ejemplo: reservé vuelo y hotel, el vuelo falla, hay que cancelar el hotel — *"no es lo mismo
que apretar el escape y salgo, cancelar la reserva implica comunicarse con el hotel."*
**[NUESTRO]** Refuerza el distractor que el repaso ya tiene fichado ("Compensación representa la
ejecución de una instancia de una tarea" = FALSA).

**NO EXISTE EVENTO TEMPORIZADOR DE FIN**, y explicó por qué: *"Fíjense que no hay un evento temporal de
fin, porque sería como una contradicción: después del fin no podría haber más."* **[NUESTRO]** Sirve para
descartar opciones inventadas.

**ESCALAMIENTO:** *"Es cuando estás ejecutando un proceso y en algún momento lo elevás a un nivel
superior para que resuelva algo que requiere más autorización."* Y aclaró: *"Yo lo comento como nivel
superior pensando en un jefe, pero también puede ser un nivel superior de conocimiento, en el sentido de
un especialista"* (mesa de ayuda de primer nivel que escala al especialista). El escalamiento que sale
del subproceso como evento **intermedio** es "no lo pude resolver, que lo haga otro"; el que sale como
evento **final** interrumpe.

⚠️ **AVISO — el docente se equivocó acá.** En ese ida y vuelta dijo que el borde punteado *"interrumpe"*,
que es al revés del estándar y de lo que él mismo había dicho la clase anterior. **Para el multiple
choice quedate con el PPT: línea llena = interrupting, línea de puntos = NON-interrupting** (lámina 21).

**OTROS EVENTOS que explicó y no estaban en la wiki:**

- **Condicional**: *"Ocurre cuando se da determinada condición de la memoria interna del proceso: si el
  stock es menor de 100, hacé una orden de compra."* Es el inicio del caso Gestión de Compras (punto de
  pedido).
- **Señal**: *"Se puede transmitir entre procesos o subprocesos, sería parecido a una llamada de una
  subrutina."*
- **Link**: *"Cuando me quedo sin espacio en la hoja, hago un link de una hoja a la otra."*
- **Terminate**: *"Un cerrado más definitivo: si estoy dentro de un subproceso y cierra normal, es un
  retorno al proceso principal; con terminate se cierra totalmente la ejecución."*
- **Múltiple**: *"Cuando el flujo llega a ese lugar, dependiendo de qué tipo de evento es, va por una
  rama o por la otra."*
- **Error**: el de inicio *"no es inicio de proceso, sino inicio de SUBPROCESO — sería si yo especifico
  un subproceso para tratar errores"*; el intermedio es el error que aparece en el medio; el de fin
  *"da un código de error"*.
- **Sobre blanco vs sobre negro**: *"Si el sobrecito está en negro, es mensaje de salida; si está en
  blanco, es mensaje [de entrada]."* Aplica a eventos de inicio, intermedios y de fin.

**OR INCLUSIVO — el argumento de por qué existe**, que es lo que la cátedra evalúa: *"Cotizar vehículo,
cotizar hotel o cotizar vuelo: puede ser uno solo, dos o los tres, por eso OR inclusivo."* Y: *"Si no
tuviéramos el OR inclusivo, ¿qué hacíamos? Secuenciábamos rombos: ¿quiere reservar un vuelo? sí/no;
después otra tarea, ¿quiere reservar un hotel? sí/no. Esto me da más riqueza semántica y no necesito
hacer todo ese secuenciamiento de decisiones."*

**COMPUERTA BASADA EN EVENTOS:** *"El flujo llega al rombo y se queda esperando que ocurra algún evento
asociado con alguna de las ramificaciones."* La diferencia con las otras: *"en vez de estar basada en una
condición, tenés que esperar que ocurra un evento"*. Mostró **dos formas equivalentes de dibujarla**:
(a) del rombo salen eventos intermedios (sobre / reloj) y después la tarea; (b) del rombo salen
directamente las tareas con el iconito de recepción de mensaje. Y el patrón de negocio: *"Le envío la
propuesta y me quedo esperando: por un lado recibir la respuesta, por otro pasados siete días. En todos
los contextos de ventas esto es muy común, porque el cliente no está obligado a decirte 'no me
interesa', simplemente no contesta."*

**MARCADORES DE INSTANCIAS MÚLTIPLES — el porqué, no solo el qué**, con un ejemplo autorreferencial:
*"Tomar el parcial es una tarea, todos involucrados. Después paso a otra tarea que dice corregir
parciales, con instancias múltiples en secuencia. ¿Por qué es relevante? **Porque los tiempos son muy
distintos**: tomar el parcial es una hora y media, no importa si son treinta o noventa; corregir depende
de cuántos parciales sean."* La distinción clave: tarea que trabaja sobre el **conjunto** vs. tarea que
trabaja sobre **cada elemento** del conjunto. Y el ad-hoc ("el cosito de la ñ", la tilde ~) = varias
instancias **sin orden predeterminado**, ni paralelo ni secuencial.

**SUBPROCESOS:** el reusable *"se hace con este trazo más grueso"*; el embebido *"es para agrupar, para
estructurar ese proceso de negocio"* y vive solo ahí; el transaccional *"este que tiene la doble [línea]
es el rollback, como en base de datos"*.

**EVENTOS DE FIN MÚLTIPLES** — lo dijo en las dos clases como **la** diferencia con el diagrama de
actividad: *"Lo que nos permite BPMN es poner más de un evento de fin; formalmente en el diagrama de
actividad tenía que haber un único evento de fin."* Es una de las opciones tildadas del MC 2026.

**POOL vs LANE:** *"Cuando tengo organizaciones distintas, tengo que tener pools distintos."*

### 1.5 Tipos de tarea: la rúbrica del ejemplo de la biblioteca

**[CÁTEDRA]** Desmenuzó entero el caso Préstamo de libros, y es la mejor rúbrica que dio de tipos de
tarea. **[NUESTRO]** Ojo: es el mismo dominio que el CU de Axure "Pedir un libro", así que el vocabulario
te va a sonar.

| Tarea del caso | Tipo | Por qué (textual) |
|---|---|---|
| "Recibe solicitud y busca libro" | **Usuario** | la búsqueda la hace con una pantalla — *"si la búsqueda del libro fuera ir a mirar estanterías, ahí tendría que tener una manita"* |
| "Informar que el libro no está disponible" | **Manual** | *"es algo que le dice el bibliotecario oralmente, no interviene ningún sistema — si fuera apretar un botón para que le mande un mail, ahí sería usuario"* |
| (hipotético) buscar el libro y mandar el mail solo | **Script / Servicio** | *"si fuera automático... tendría el dibujito del script o del web service"* |
| "Registra el préstamo" | **Usuario** | |
| "Entrega el libro al socio" | **Manual** | |

Y el par que la cátedra intercambia en el MC, dicho en las dos clases:
**Servicio** = *"invoco un web service, un software externo"*. **Script** = *"es similar a la de
servicio, **la diferencia es que el script lo programo en el lenguaje del BPM, en la misma
herramienta**"*. **Usuario** = *"un usuario tecleando sobre una pantalla"*. **Manual** = *"un usuario
levantando cajas"*, *"una persona haciendo algo físico fuera del sistema"*.

**[NUESTRO]** El criterio único: **¿quién lo ejecuta y con qué?** Si el enunciado dice "a través de una
aplicación interna" o "el sistema envía", el ícono está pedido en el texto.

### 1.6 Bizagi operativo — lo que mostró en pantalla

**[CÁTEDRA]** El repaso da el checklist de entrega pero no el manejo de la herramienta. Esto es todo
nuevo:

- **Versión: Bizagi Modeler 2.6** en las máquinas del laboratorio. *"Hay más nuevas, pero requieren mucha
  memoria."* Coincide con el instalador que está en `fuentes/BPMN/Bizagi/`. Si usás la 3.6, los menúes
  están en otro lado.
- **El diagrama arranca con un pool ya puesto.** Los lanes se agregan desde el iconito de carriles del
  costado del pool.
- **La forma rápida y segura de dibujar** (evita el problema de conectores sueltos de raíz):
  *"Fíjense que cuando yo hago clic sobre un objeto, aparecen unos iconitos alrededor. Esto es por si yo
  quiero encadenar: tengo esta tarea y quiero poner otra tarea, hago clic acá y **ya me la crea junto con
  la línea**. Si le pongo un rombo, me crea el rombo y ya me lo liga. Es más rápido haciéndolo así."*
  **[NUESTRO]** Encadená siempre desde esos iconitos. Arrastrar desde la barra y después tirar la flecha
  a mano es exactamente cómo se te generó el conector roto del EJ 4 (ver sección 4).
- **Botón derecho es el menú de todo.** Sobre un **evento** → el tipo (mensaje, temporizador, error,
  señal, condición, escalamiento, compensación, terminate, múltiple). Sobre un **gateway** → el tipo de
  compuerta. Sobre una **tarea** → por un lado los marcadores (ciclo, instancias múltiples) y por otro el
  tipo de tarea (usuario, manual, servicio, script, envío, recepción). No lo busques en la barra de
  arriba.
- **Evento adjunto al borde:** botón derecho sobre la tarea o el subproceso → **"adjuntar evento"** →
  elegís el tipo. **Es la única forma de hacer el boundary event**: no se dibuja arrastrando un evento
  encima.
- **Subproceso (esto es lo que pide el parcial, las dos imágenes):** en vez de una tarea, arrastrás un
  subproceso; botón derecho → **Editar subproceso**. *"Fíjense que acá me quedan unos tabsitos abajo"*:
  el subproceso se abre como pestaña aparte al pie de la ventana, con su propio nombre; dibujás adentro
  (inicio, tareas, fin) y volvés al principal con el otro tab. **Cada tab exporta como una imagen
  distinta.**
- **Limitaciones de la 2.6** — no pierdas tiempo buscando lo que no está: en instancias múltiples *"no
  tiene paralelo ni secuencial, solo múltiples instancias"*; y los eventos intermedios no ofrecen los
  mismos tipos que los de inicio, *"en realidad lo que hace es validar cuál corresponde con cuál"*. Si un
  tipo no aparece en el menú, probablemente es porque no es legal en esa posición.
- **Exportación:** nunca con el botón directo de imprimir. **Archivo → Imprimir → vista preliminar**, y
  ajustá para que entre completo.
- **No improvises con otra herramienta.** *"Lo que tiene esto [Bizagi] es que está más adaptado a
  respetar la sintaxis; por ahí en Miro buscás alguna cosa y te queda algo medio mal, por eso usamos éste
  que es específico."*

---

## 2. Teoría BPMN — lo que el PPT agrega

⚠️ **Leé esto antes de usar la sección.** Las preguntas de abajo son **[NUESTRO]**: están **construidas
por nosotros a partir de las definiciones literales del PPT**, no tomadas de un parcial real. Sirven para
practicar el concepto y para reconocer el mecanismo del distractor. **No son preguntas confirmadas.** Las
que sí salieron en un parcial están en `repaso-parcial.md` sección 2.

**[CÁTEDRA] — el hallazgo que ordena todo lo demás:** el PPT es la **fuente literal** de casi todas las
opciones correctas del banco. Las frases de los parciales 2022 y 2026 son copy-paste de las láminas 15,
20, 21, 24, 31, 35, 36, 37, 39, 43, 47 y 58. **La hipótesis de trabajo del repaso queda verificada:**
memorizá esas láminas y tenés las opciones correctas escritas palabra por palabra. Y el mecanismo del
distractor es casi siempre el mismo: **la definición textual del elemento vecino de la misma lámina, con
el sujeto cambiado.**

### 2.1 Canales, objetos de flujo y de conexión (láminas 14-16)

**[CÁTEDRA]** Definiciones literales:

- **Actividades**: "Representan el trabajo a ser realizado en un proceso. Atómicas: **Tareas**.
  Compuestas: **Subproceso**."
- **Compuertas**: "Representan la división y unión de flujos."
- **Objetos de flujo** = Actividades, Eventos y Compuertas. **Cerrado.** El Pool y el Lane son
  **canales**, no objetos de flujo; el flujo de secuencia y el de mensaje son **objetos de conexión**.
- **Contenedor (Pool)**: "Representa un **participante (organización)** en un proceso."
- **Carril (Lane)**: "Usada para organizar actividades asociadas con un **rol o unidad
  organizacional**."
- **Flujo de mensaje**: "Usado para representar el flujo de mensajes entre dos participantes que están
  preparados para enviar y recibir mensajes."
- **Asociación**: "usada para asociar artefactos con objetos de flujo." **Asociación de dato**: "usada
  para asociar datos con objetos de flujo."

**Preguntas de práctica [NUESTRO]**

**Respecto de un Contenedor (Pool)**
- [x] Representa un participante (organización) en un proceso
- [ ] Es usada para organizar actividades asociadas con un rol o unidad organizacional → *es el Lane*
- [ ] Agrupación de actividades para propósitos de documentación o análisis → *es el Grupo (artefacto)*
- [ ] Es uno de los objetos de flujo del proceso → *es un canal*

**Son Objetos de Flujo**
- [x] Actividades
- [x] Eventos
- [x] Compuertas
- [ ] Flujo de Secuencia → *objeto de conexión: conecta objetos de flujo*
- [ ] Contenedor (Pool) → *canal*

**Respecto de las Actividades**
- [x] Representan el trabajo a ser realizado en un proceso
- [x] Las actividades atómicas son las Tareas
- [x] Las actividades compuestas son los Subprocesos
- [ ] Las compuertas son un tipo de actividad → *categoría hermana; además no representan trabajo*

**Respecto de un Flujo de Secuencia** (versión completa del PPT, amplía la del repaso 2.3)
- [x] Es usado para representar el orden de ejecución de las actividades en un proceso
- [x] El origen y el destino deben ser uno de los objetos de flujo: Eventos, Actividades y Compuertas
- [x] **No** puede cruzar los límites de un Contenedor (Pool)
- [ ] Usado para asociar artefactos con objetos de flujo → *es la Asociación*
- [ ] Es usado para representar el flujo de mensajes entre dos participantes → *es el Flujo de Mensaje*

### 2.2 Artefactos (lámina 16) — cero preguntas en el banco actual

**[CÁTEDRA]** Los artefactos son **solo dos**: **Grupo** ("agrupación de actividades para propósitos de
documentación o análisis") y **Anotación / Text Annotation** ("usada para proveer información adicional a
un diagrama"). Definición de la familia: **"No tienen efecto directo en la semántica del flujo de
secuencia o de mensajes."**

**[NUESTRO]** Nota práctica: **el cuadro donde va tu apellido en el diagrama de Bizagi ES una
Anotación.**

**Son Artefactos en BPMN [NUESTRO]**
- [x] Grupo
- [x] Anotación (Text Annotation)
- [x] No tienen efecto directo en la semántica del flujo de secuencia o de mensajes
- [ ] Objeto de Dato (Data Object) → *el PPT lo pone en la categoría **Datos**, no en Artefactos*
- [ ] Flujo de Mensaje → *objeto de conexión*

### 2.3 Datos (lámina 17) — no se modelan, pero las definiciones existen

**[CÁTEDRA]** Cinco definiciones cortas, todas intercambiables entre sí como distractores:

| Concepto | Definición textual |
|---|---|
| **Objeto de Dato** | "información que las actividades requieren para ser ejecutadas y/o que producen" |
| **Entrada de Dato** | "información **requerida para ejecutar** un proceso" |
| **Salida de Dato** | "información **producida por** un proceso" |
| **Almacén de Dato** | "información recuperada o actualizada por actividades y que **persistirá por fuera del alcance de las instancias** del proceso" |
| **Propiedades** | "propiedades que se agregan y definen en procesos, actividades o eventos. **No son visibles en diagramas**" |

**[NUESTRO]** La marca del **Data Store** es "por fuera del alcance de las instancias". La de
**Propiedades**, "no son visibles en diagramas". Con esas dos frases descartás el resto.

### 2.4 Eventos de inicio (lámina 24) — la mitad simétrica que faltaba

**[CÁTEDRA]** El banco tiene el bloque de Eventos de fin. Este es el espejo, textual:

- "Indica dónde comienza el flujo de secuencia del proceso."
- **"No debe tener ningún flujo de secuencia de ENTRADA."**
- "Pueden definirse varios eventos de inicio para un proceso."
- "**Genera** un token que debe ser consumido por un evento de fin."
- "Cuando el disparador (trigger) ocurre, una instancia del proceso es creada y tokens son generados para
  cada flujo de secuencia de salida del evento."

⚠️ **[NUESTRO] El distractor obvio, y el favorito de la cátedra: cruzar entrada con salida.**
El **inicio** no tiene **entrada**; el **fin** no tiene **salida**. El banco solo cubre la del fin.

**Respecto de los Eventos de Inicio [NUESTRO]**
- [x] Indica dónde comienza el flujo de secuencia del proceso
- [x] No debe tener ningún flujo de secuencia de entrada
- [x] Pueden definirse varios eventos de inicio para un proceso
- [x] Genera un token que debe ser consumido por un evento de fin
- [ ] No debe tener ningún flujo de secuencia de salida → *es el de fin*
- [ ] Consume un token generado desde un evento de inicio → *es el de fin*

### 2.5 Interrupting vs. non-interrupting (lámina 21) — no está en el banco

**[CÁTEDRA]** "Los eventos pueden ser: **Interrupting** si interrumpe el proceso (**línea llena**).
**Non-interrupting** si NO interrumpe el proceso (**líneas de punto**)."

**Respecto de los eventos interrupting y non-interrupting [NUESTRO]**
- [x] Interrupting = interrumpe el proceso, línea llena
- [x] Non-interrupting = no interrumpe, líneas de punto
- [ ] El non-interrupting se representa con línea llena y el interrupting con puntos → *inversión pura*
- [ ] Indican cómo un proceso puede ser interrumpido o demorado → *definición de los **Eventos
  Intermedios** (lámina 27): cambio de sujeto*

### 2.6 Taxonomía de eventos: las definiciones intercambiables

**[CÁTEDRA]** Todas textuales. **[NUESTRO]** Están puestas juntas a propósito: la cátedra arma el
distractor tomando la definición del vecino de la misma lámina.

**De inicio (láminas 25-26)**

| Tipo | Definición |
|---|---|
| Sin especificar | no se especifica ningún comportamiento en particular para iniciar |
| Mensaje | "un proceso inicia cuando un **mensaje es recibido**" |
| Temporización | "un proceso inicia **cada ciclo de tiempo o en una fecha específica**" |
| Condición | "un proceso inicia cuando una **condición de negocio se cumple**" |
| Señal | "el proceso inicia cuando se captura una **señal lanzada desde otro proceso**. Tenga en cuenta que una señal **no es un mensaje**: un mensaje tiene claramente definido un destinatario, la señal no" |
| Múltiple | "existen muchas formas de iniciar el proceso y al cumplirse una de ellas se iniciará" |

**Intermedios (láminas 28-30)**

| Tipo | Definición |
|---|---|
| Sin especificar | algo que ocurre dentro del proceso; **solo dentro de la secuencia del flujo** |
| Mensaje | puede enviarse o recibirse; **si es de recepción, el proceso no continúa hasta que el mensaje llegue** |
| Temporización | "indica una **espera** dentro del proceso; dentro del flujo de secuencia = espera entre actividades; **adjunto a los límites de una actividad = flujo de excepción**" |
| Condición | "esperar que una condición de negocio se cumpla" |
| Señal | enviar o recibir señales |
| Múltiple | "puede ser activado por muchas causas" |
| **Escalable** | "el proceso debe pasar a un **nivel más alto de responsabilidad**; dentro del flujo para lanzarlo, adjunto a los límites de una actividad para capturarlo" |
| **Cancelación** | "usado en **subprocesos transaccionales**; se diagrama a los límites del subproceso transaccional indicando un flujo alternativo cuando es cancelado" |
| **Error** | "usada para **capturar errores**; se diagrama a los límites de una actividad" |
| **Compensación** | dentro del flujo = lanza compensación; adjunto al borde (siempre de captura) = esa actividad se compensará |
| **Enlace (Link)** | "**permite conectar dos secciones del proceso**" |

**De fin (láminas 32-33)**

| Tipo | Definición |
|---|---|
| Sin especificar | "indica que **un camino** del flujo llegó al fin" |
| Mensaje | envía un mensaje al finalizar |
| **Terminación (Terminal)** | "el proceso es terminado: **cuando algún camino llega a este fin el proceso termina completamente, sin importar que existan más caminos pendientes**" |
| Señal | envía una señal al finalizar |
| Múltiple | "varios resultados pueden darse al finalizar un flujo" |
| **Cancelación** | "envía una excepción de cancelación. **Sólo se utiliza en subprocesos transaccionales**" |
| Error | envía una excepción de error |
| Compensación | indica que es necesaria una compensación al finalizar |
| Escalable | un escalamiento se realiza al finalizar el flujo |

**Preguntas de práctica [NUESTRO]** (una por trampa)

**Respecto del Evento de Inicio de Señal**
- [x] El proceso inicia cuando se captura una señal lanzada desde otro proceso
- [x] Una señal no es un mensaje: el mensaje tiene destinatario definido, la señal no
- [ ] Un proceso inicia cuando un mensaje es recibido → *inicio de Mensaje*
- [ ] Un proceso inicia cuando una condición de negocio se cumple → *inicio de Condición*

**Respecto del Evento Intermedio de Temporización**
- [x] Indica una espera dentro del proceso
- [x] Dentro del flujo indica espera entre actividades; adjunto al borde indica flujo de excepción
- [ ] Indica que un proceso inicia cada ciclo de tiempo o en una fecha específica → *es el de **inicio**:
  mismo símbolo, distinta categoría*
- [ ] Se utiliza para esperar que una condición de negocio se cumpla → *intermedio de Condición*

**Respecto del Evento Intermedio de Escalamiento**
- [x] Indica que el proceso debe pasar a un nivel más alto de responsabilidad
- [x] Dentro del flujo lanza el evento; adjunto a los límites de una actividad lo captura
- [ ] Es un marcador de actividad que representa la ejecución del nivel siguiente → *distractor ya usado
  en 2022: escalamiento es un **evento***
- [ ] Se utiliza para esperar que una condición de negocio se cumpla → *intermedio de Condición*

**Respecto del Evento Intermedio de Enlace (Link)**
- [x] Permite conectar dos secciones del proceso
- [ ] Se utiliza para enviar o recibir señales → *de Señal*
- [ ] Es usada para capturar errores y se diagrama a los límites de una actividad → *de Error*
- [ ] Indica que puede ser activado por muchas causas → *Múltiple*

**Respecto del Evento Intermedio de Cancelación**
- [x] Es usado en subprocesos Transaccionales
- [x] Se diagrama a los límites del subproceso transaccional, con un flujo alternativo para cuando se
  cancela
- [ ] Es usada para capturar errores y se diagrama a los límites de una actividad → *de Error*
- [ ] Puede utilizarse en cualquier actividad o subproceso, sea transaccional o no → *el PPT lo restringe
  explícitamente a transaccionales*

**Respecto del Evento de Fin de Terminación**
- [x] Cuando algún camino llega a este fin el proceso termina completamente, sin importar que existan
  más caminos pendientes
- [ ] Indica que un camino del flujo llegó al fin → *fin sin especificar*
- [ ] Indica que varios resultados pueden darse al finalizar → *fin Múltiple*
- [ ] Permite enviar un mensaje al finalizar → *fin de Mensaje*

**Respecto del Evento de Fin de Cancelación**
- [x] Permite enviar una excepción de cancelación al finalizar el flujo
- [x] Sólo se utiliza en subprocesos transaccionales
- [ ] Permite enviar una excepción de error al finalizar → *fin de Error*
- [ ] Indica que es necesaria una compensación al finalizar → *fin de Compensación*

### 2.7 Compuertas — lo que el banco no cubría

**[CÁTEDRA]** Definiciones textuales que faltaban:

- **Exclusiva como UNIÓN** (el banco solo trabaja la división): "Una compuerta exclusiva con varios
  flujos de secuencia de **entrada** es utilizada como una **unión de caminos alternativos mutuamente
  excluyentes**."
- **Inclusiva como UNIÓN**: "espera todos los tokens que han sido producidos en los caminos. **No
  requiere que todos los caminos hayan producido un token**." Y: "**Se recomienda la definición del
  camino por defecto.**"
- **Compleja** (lámina 38, entera): "Creado para tratar casos complejos. **Pueden ser usados para dividir
  y unir flujos.** Puede ser usado para manejar todas las situaciones, pero la mejor práctica es evitar
  usarlas, ya que hace que los modelos de proceso sean menos legibles." Ejemplo del PPT: "3 flujos
  convergen y la actividad siguiente es habilitada una vez que 2 flujos hayan finalizado."
- **Basada en eventos** (lámina 39): "el **destino de los caminos alternativos es una tarea de recepción
  o bien un evento intermedio**". Y las dos variantes: una para "caminos alternativos basados en eventos
  al inicio del proceso, pero **sólo uno** se ejecutará", otra para "un proceso puede iniciarse cuando
  ocurren **varios eventos en paralelo**".

**Respecto de la Compuerta Compleja [NUESTRO]**
- [x] Creada para tratar casos complejos
- [x] **Pueden ser usados para dividir y unir flujos** ← ver el aviso de la sección 3.1
- [x] Puede manejar todas las situaciones, pero la mejor práctica es evitarla porque hace los modelos
  menos legibles
- [ ] Un punto donde la selección de caminos está basada en la ocurrencia de eventos → *es la basada en
  eventos; además la Compleja es basada en **datos***

**Respecto de la Compuerta Exclusiva [NUESTRO]**
- [x] Un punto donde el flujo puede tomar dos o más caminos alternativos mutuamente excluyentes; sólo uno
  será seleccionado
- [x] Con varios flujos de entrada, es una unión de caminos alternativos mutuamente excluyentes
- [ ] Cada camino es independiente y todas las combinaciones pueden ocurrir, desde cero a todos → *la
  Inclusiva*
- [ ] Usado para crear y sincronizar flujos paralelos → *la Paralela*

**Respecto de la Compuerta Inclusiva utilizada como unión [NUESTRO]**
- [x] Espera todos los tokens que han sido producidos en los caminos
- [x] No requiere que todos los caminos hayan producido un token
- [x] Se recomienda la definición del camino por defecto
- [ ] Todas las rutas deben completarse antes de que el proceso continúe → *la Paralela, textual*
- [ ] Es utilizada como unión de caminos alternativos mutuamente excluyentes → *la Exclusiva, textual*

**Respecto de la Compuerta Basada en Eventos [NUESTRO]**
- [x] El destino de los caminos alternativos es una tarea de recepción o bien un evento intermedio
- [x] Hay una variante para caminos alternativos al inicio del proceso, donde sólo uno se ejecutará
- [x] Hay una variante para que el proceso se inicie cuando ocurren varios eventos en paralelo
- [ ] El destino de los caminos alternativos es una tarea de envío o una compuerta → *inversión: es
  recepción; y una compuerta jamás es destino válido*

### 2.8 Subprocesos (láminas 43-44, 52)

**[CÁTEDRA]** Textual:

| Tipo | Definición |
|---|---|
| **Embebido** | "definido dentro de un proceso pero **NO puede ser reusado** en el contexto de actividades de otro proceso. Usado para definir un **alcance**: visibilidad, manejo de transacciones, excepciones, eventos o compensaciones. Colapsado o expandido" |
| **Reusable (Call Activity)** | "representa la **invocación**, en un proceso, a **otro proceso predefinido**. La invocación resulta en la **transferencia de control** al proceso llamado" |
| **De Evento** | "puede ser **iniciado como consecuencia de un evento de inicio asociado al mismo**. **No es parte del flujo de secuencia normal del proceso padre: no tiene flujos de secuencia de entrada y salida.** Puede o no ocurrir mientras el padre está en ejecución, y es posible que ocurra varias veces" |
| **Transaccional** | "el comportamiento es expresado a través de un **protocolo de transacción**" |

**Las tres salidas del transaccional (lámina 52):**
1. **Con éxito.**
2. **Con falla (Cancelación)**: las actividades dentro de la transacción quedan sujetas a acciones de
   cancelación. *Ejemplo del PPT: al hacer las reservas no encuentra disponibilidad en el vuelo.*
3. **Excepción (Error)**: error grave, no es posible una terminación exitosa ni con falla. *Ejemplo:
   caída de servicio, error de conexión.*

**[NUESTRO]** "Con compensación" y "con escalamiento" **no** son salidas del transaccional: la
compensación es el mecanismo que se dispara **desde** la salida de cancelación.

**Respecto del Subproceso de Evento [NUESTRO]**
- [x] Puede ser iniciado como consecuencia de un evento de inicio asociado al mismo
- [x] No tiene flujos de secuencia de entrada ni de salida
- [x] Puede o no ocurrir mientras el padre está en ejecución, y puede ocurrir varias veces
- [ ] Representa la invocación a otro proceso predefinido → *el Reusable*
- [ ] Usado para definir un alcance dentro de un proceso → *el Embebido: la misma frase que en el banco
  va tildada bajo "embebido", acá es distractor por cambio de sujeto*

**Respecto del Subproceso Reusable (Call Activity) [NUESTRO]**
- [x] Representa la invocación, en un proceso, a otro proceso predefinido
- [x] La invocación resulta en la transferencia de control al proceso llamado
- [ ] Es un subproceso definido dentro de un proceso pero no puede ser reusado en otro → *el Embebido:
  el mismo par que la cátedra recicla desde 2022, dado vuelta*
- [ ] El comportamiento es expresado a través de un protocolo de transacción → *el Transaccional*

⚠️ **[NUESTRO]** El distractor del embebido que ya está fichado en el repaso es **literalmente la lámina
43 con el "no" borrado**. Igual que el del flujo de secuencia: **leé si la opción está negada** antes de
tildar.

### 2.9 Marcadores, compensación y excepciones (láminas 47-51)

**[CÁTEDRA]** Definiciones:

- **Loop**: "ejecución repetida de una tarea en forma secuencial."
- **Instancias Múltiples**: "ejecución de múltiples instancias de la tarea."
- **Ad-Hoc**: "las actividades no son ejecutadas en un orden particular."
- **Compensación**: "deshacer la acción de una actividad previa que fue realizada y **finalizada en forma
  exitosa**, pero cuyos resultados y efectos no son más deseados y requieren ser revertidos."

**Lámina 48 — el matiz que el banco no tiene:**

| Marcadores de **TAREA** (3) | Marcadores de **SUBPROCESO** (4) |
|---|---|
| Loop, Múltiple Instancia, Compensación | Loop, Múltiple Instancia, Compensación **+ Ad-Hoc** |

⚠️ **[NUESTRO]** **Ad-Hoc NO es marcador de tarea.** Si la pregunta acota el sujeto a "marcadores de
**tareas**", Ad-Hoc pasa a ser distractor válido; si dice "marcadores de **actividad**" o "de
**subproceso**", va tildado. Es exactamente el cambio-de-sujeto que usa la cátedra. El repaso los trata
como una sola lista.

**Compensación en profundidad (lámina 50)** — repetida dos veces en el PPT, señal fuerte de material de
examen:
- "Si una actividad está **aún activa, no puede ser compensada**: para ello debe ser primero
  **cancelada**."
- "Es ejecutada por un **manejador de compensación**, que contiene los pasos necesarios para revertir los
  efectos."
- (Lámina 51) Las actividades de compensación "están **fuera del flujo de secuencia normal**", "**no
  tienen flujos de secuencia de entrada o de salida**", y el evento intermedio de compensación "no tiene
  un flujo de secuencia de salida, sino que tiene una **asociación de salida dirigida**" (línea punteada,
  no flecha llena).

**Manejo de excepciones (lámina 49):** "Eventos intermedios asociados a una actividad representan
**triggers que pueden interrumpir la actividad**. Todo el trabajo que se esté realizando será
interrumpido y el flujo procederá desde el evento."

**[NUESTRO]** La distinción que se evalúa: **excepción interrumpe algo en curso; compensación revierte
algo ya terminado.**

**Son tipos de marcadores de TAREAS [NUESTRO]**
- [x] Loop
- [x] Múltiple Instancia
- [x] Compensación
- [ ] Ad-Hoc → *solo de subproceso*
- [ ] Escalamiento → *no es marcador de nada: es un evento*

**Respecto de las actividades de compensación [NUESTRO]**
- [x] Están fuera del flujo de secuencia normal, asociadas por un Evento Intermedio de Compensación
- [x] No tienen flujos de secuencia de entrada ni de salida
- [x] El evento intermedio de compensación sale por una asociación dirigida, no por flujo de secuencia
- [ ] Se conectan a la actividad a compensar mediante un flujo de secuencia → *contradice la lámina 51*

### 2.10 Tipos de tarea: son SIETE, no seis

**[CÁTEDRA]** Lámina 58, textual. El banco registra seis; falta **Regla de Negocio**:

| Tarea | Definición |
|---|---|
| Envío (Send) | "el **envío** de un mensaje a un participante externo. Cuando el mensaje fue enviado, la tarea finaliza" |
| Recepción (Receive) | "la **espera del arribo** de un mensaje desde un participante externo. Cuando se recibe, la tarea finaliza" |
| Usuario (User) | "una persona ejecuta la tarea **con** la asistencia de una aplicación de software" |
| Manual | "ejecutada **sin** la asistencia de una aplicación" |
| **Regla de negocio (BusinessRule)** | "la ejecución de una **regla de negocio por una máquina de reglas de negocio**" |
| Servicio (Service) | "un **servicio automatizado provisto por una aplicación**" |
| Script | "un script ejecutado por una **máquina de proceso de un BPMS**. El script se define en el **lenguaje de script provisto por el BPMS**" |

**[NUESTRO]** Los siete son Envío, Recepción, Usuario, Manual, Regla de Negocio, Servicio y Script.
**Cualquier octavo nombre en una opción es invención.** Y la definición de Script confirma por qué
"Script: sin la asistencia de una aplicación" es falso: es lo **más** automatizado de todos.

### 2.11 Lo que este PPT NO cubre

⚠️ **[NUESTRO] Aviso de alcance.** El PDF del PPT **arranca en la lámina 14**. No cubre: tipos de
diagrama (orquestación privada/pública, colaboración, coreografía, conversación), ni pool caja negra vs.
caja blanca, ni esa terminología. Si esos temas existen en la materia, están en las láminas 1 a 13, que
no están en el archivo. **No armes preguntas de coreografía a partir de esta fuente.** El docente sí los
nombró en clase (ver 1.2): coreografía y conversación **no se modelan**, pero pueden aparecer nombrados
en el multiple choice.

---

## 3. Correcciones a lo que ya teníamos

### 3.1 Al repaso (`repaso-parcial.md`)

**⚠️ CORRECCIÓN 1 — la más cara del documento. Sección 2.2, "Compuerta Basada en Eventos".**

El repaso explica que *"Pueden ser usados para dividir y unir flujos"* es falsa bajo *Compuerta Basada en
Eventos* **"porque esa solo divide: para converger hay que usar otra compuerta"**. Esa racionalización es
**[NUESTRO]** y **no está en el PPT**. El mecanismo real es el de siempre: esa frase es **textual de la
Compuerta COMPLEJA** (lámina 38: "Pueden ser usados para dividir y unir flujos"). Es un **cambio de
sujeto**, no un juicio semántico.

- **La respuesta no cambia**: bajo *basada en eventos*, sigue destildada.
- **Pero si mañana la pregunta viene encabezada "Respecto de la Compuerta Compleja", esa misma frase VA
  TILDADA.**

**⚠️ CORRECCIÓN 2 — sección 2.2, "Son Tipos de Compuertas basada en datos" (2022).**

El repaso registra `[x] Inclusiva [x] Exclusiva [x] Paralela [ ] Recursiva`. **[CÁTEDRA]** La lámina 34
clasifica **CUATRO** compuertas como basadas en datos: **Exclusiva (XOR), Inclusiva (OR), Paralela (AND)
y COMPLEJA**. Si mañana aparece "Compleja" como opción bajo *compuertas basada en datos*, **va tildada**.
El repaso lo dice de refilón en un comentario ("la Compleja existe pero es basada en datos"), enterrado
en la nota de 2026. Que quede arriba:

| Basadas en **datos** (4) | Basadas en **eventos** (2) |
|---|---|
| Exclusiva, Inclusiva, Paralela, **Compleja** | Exclusiva, Paralela |

**⚠️ CORRECCIÓN 3 — sección 1, formato del parcial.** El docente dijo en clase que el parcial *"no le
vamos a poner teoría"*. Ver 1.1: **no dejes de estudiar la teoría**, pero sabé que él lo concibe como
esencialmente práctico.

**⚠️ MATIZ — sección 2.6, marcadores.** El repaso los trata como una lista única de "marcadores de
actividad". El PPT separa **tarea (3)** de **subproceso (4, con Ad-Hoc)**. Ver 2.9.

**Lo que el PPT CONFIRMA del repaso** (no cambies nada de esto):

- ✅ **"Todas las combinaciones de caminos pueden ocurrir, desde cero a todos"** es **textual de la
  Inclusiva** (lámina 36). El aviso del repaso ("si aparece *desde cero*, va tildada igual") queda
  ratificado por la fuente. La wiki, que dice "uno o más", pierde: **manda el PPT**.
- ✅ **"Requiere que todos los caminos hayan producido un token"** es distractor de la exclusiva porque el
  PPT lo enuncia **negado** para la inclusiva. Y **"Todas las rutas deben completarse antes de que el
  proceso continúe"** es textual de la **Paralela** (lámina 37).
- ✅ **"Un evento de fin genera un Token"** es falsa: el inicio genera (lámina 20 y 24), el fin consume
  (lámina 31).
- ✅ El distractor del **subproceso embebido** es la lámina 43 con el "no" borrado.
- ✅ **"Escalamiento" no es marcador de actividad**: en el PPT aparece siempre como tipo de **evento**.

**Convivencia, no contradicción:** la regla "todos los tokens deben ser consumidos por un evento de fin"
(lámina 31) y el **Fin de Terminación** (lámina 32, "el proceso termina completamente sin importar que
existan más caminos pendientes") **conviven**. Como opciones de multiple choice, las dos pueden ir
tildadas. No las trates como contradicción.

### 3.2 A la wiki (`IPP.md`, Unidad 1)

**⚠️ CORRECCIÓN 4 — la más importante para el modelado. "Gateway que abre, gateway que cierra, del mismo
tipo".**

**[CÁTEDRA]** El docente es más laxo, y lo dijo dos veces: *"En el caso de los OR, el que cierra es
**opcional**, si querés lo hacés, si querés no lo hacés. **En el caso del paralelismo hay que hacerlo sí
o sí**, porque si no, no terminás de definir cómo funciona el proceso."*
**Traducción para mañana:** cerrá **siempre** el paralelo — es el único obligatorio y el único que
descuenta. Cerrar el exclusivo/inclusivo suma prolijidad pero no es exigible. Si vas corto de tiempo,
sabés qué sacrificar.

**⚠️ CORRECCIÓN 5 — caso 3 (Publicación Artículos), variante B.**

La wiki dice: *"B: diseño solo si el artículo tiene ilustración → gateway **inclusivo** (O)"*, y remata
*"la trampa es resolver B con un exclusivo"*. **Es al revés.** **[CÁTEDRA]** La solución oficial
(`Caso_Articulos.pdf`, en fuentes) resuelve B con **paralela que abre → exclusiva con salto en la rama de
diseño → paralela que cierra**. No hay ninguna inclusiva. Tu propia entrega del EJ 3 coincide casi
elemento por elemento con la oficial. **Si mañana sale este caso, hacelo como lo hiciste vos, no como
dice la wiki.**

Además: el enunciado de ese caso es **acumulativo** (B es "el mismo proceso anterior" que A, y C que B),
así que el diagrama final tiene las tres cosas: paralelo redacción/diseño (A) + decisión "¿Tiene
ilustración?" sobre la rama de diseño (B) + exclusiva de tres salidas con loop (C).

**⚠️ CORRECCIÓN 6 — "No hay resoluciones de los 7 casos en el material" (sección Dudas/pendientes).**

Falso: **sí hay dos soluciones oficiales** en fuentes, `Caso_Articulos.pdf` (procesos A, B y C resueltos)
y `Caso_Reclamo.pdf`. **[NUESTRO]** Ese par es el único contraste válido contra la cátedra que tenés. Usá
esos, no la wiki, como patrón de referencia.

**⚠️ CORRECCIÓN 7 — "el actor externo va en pool aparte y COLAPSADO: no se modela su proceso interno".**

**[CÁTEDRA]** El PPT no respalda eso **como regla de sintaxis**: en Gestión de Compras (lámina 57) los
dos pools, Compras y Proveedor, están **expandidos**, cada uno con su proceso completo, unidos por flujos
de mensaje punteados.
**[NUESTRO]** Reconciliación práctica: sigue siendo el mejor criterio de **economía** para el parcial —
las dos soluciones oficiales de la cátedra tampoco modelan el interior de los participantes externos, y a
vos los pools externos abiertos son justo lo que se te rompe (sección 4). Pero **no es sintaxis**: no
descartes un modelo por tener el pool externo abierto. Lo que **sí** es sintaxis es que ningún flujo de
secuencia cruce la frontera de un pool.

**⚠️ FALTANTE 8 — el camino por defecto (default flow).** La wiki no lo menciona. **[CÁTEDRA]** El PPT lo
dibuja en la exclusiva (lámina 35) y en la inclusiva (lámina 36), y para la inclusiva lo **recomienda
explícitamente**. El docente lo explicó en clase (ver 1.4). Es la barrita cruzada sobre una de las
salidas. Vale como punto a favor en el modelado de mañana.

**⚠️ MATIZ 9 — "todo camino termina en un evento de fin".** Sigue siendo la regla operativa, pero el
**Fin de Terminación** es la excepción explícita del PPT. No modeles con terminate salvo que el enunciado
lo pida; sabelo para el MC.

**⚠️ CLASIFICACIÓN 10 — artefactos.** El PPT pone los **Datos** como categoría propia (lámina 17),
separada de los **Artefactos**, que son **solo Grupo y Anotación** (lámina 16). En BPMN 2.0 del OMG los
data objects a veces se cuentan entre los artefactos: **para el parcial manda el PPT**.

---

## 4. Tus errores recurrentes

**[NUESTRO]** Esto sale de auditar **tus propias entregas** (EJ 3 Publicación Artículos, EJ 4 Quejas y
Reclamos, EJ 5 Selección de Personal, EJ 6 Organizar Fiesta), abriendo los `.bpm`/XPDL además de los jpg,
y contrastando contra las dos soluciones oficiales. Solo se listan los hallazgos confirmados por dos de
tres verificadores. **Es la sección más importante del documento**: son errores que ya cometiste y que
tenés a mano repetir mañana.

### 4.1 Los cinco patrones

**PATRÓN 1 — EL BORDE DEL PROCESO ES TU PUNTO CIEGO.** Es el número uno y aparece en **los cuatro
ejercicios**. El núcleo lógico siempre está bien resuelto; lo que se te rompe es **el primer elemento, el
último, y todo lo que toca un pool externo**. Inventario:

| Ejercicio | Qué quedó roto en el borde |
|---|---|
| EJ 3 v1 | "Enviar artículo" en el pool Autor, sin salida ni evento de fin |
| EJ 3 v2 | evento de inicio de mensaje sin flujo de mensaje entrante |
| EJ 4 | conector del evento de inicio sin destino → la primera tarea sin entrada |
| EJ 6 | el pool Cliente termina en un lanzamiento de mensaje, sin evento de fin |
| EJ 6 | falta la última tarea del enunciado ("Enviar factura al cliente") |

**Cinco errores, todos en los extremos.** → **Para mañana: cuando termines el diagrama, tocá con el dedo
el evento de inicio y el evento de fin de CADA pool, incluidos los externos.**

**PATRÓN 2 — LOS POOLS EXTERNOS LOS AGREGÁS PERO NO LOS TERMINÁS, Y NO SOS CONSISTENTE.** En EJ 3
modelaste el pool Autor expandido y le mandaste mensaje desde "Enviar correcciones" pero **no** desde
"Notificar rechazo al autor" (el autor se entera fuera del modelo). En EJ 6 dejaste el pool Cliente
expandido y colgado, mientras que el pool Banda lo dejaste colapsado y bien. En EJ 5 directamente no
pusiste el pool Candidato, aunque el enunciado tiene al candidato aceptando o rechazando.
→ **Regla para mañana: pool externo SIEMPRE colapsado. Si un actor externo recibe algo, lo recibe por
flujo de mensaje, sin excepciones.** Es lo que hacen las dos soluciones oficiales.

**PATRÓN 3 — NO HACÉS LA PASADA DE VERIFICACIÓN FINAL.** Cinco de los hallazgos (la unión exclusiva sobre
un split paralelo en EJ 6, el evento colgado en EJ 3, el conector sin destino en EJ 4, el flujo duplicado
en EJ 3, el inicio de mensaje huérfano en EJ 3 v2) se detectan **en menos de un minuto** con dos
preguntas:

1. ¿Cada elemento tiene al menos un flujo de entrada y uno de salida?
2. ¿Cada compuerta que abre cierra con una del mismo tipo? (al menos las paralelas — ver 3.2)

**El problema no es que no sepas**: en el **mismo** diagrama del EJ 6 tenés dos pares paralelos
perfectamente cerrados. El problema es que **no releés**.

**PATRÓN 4 — LO QUE NO SE VE EN EL JPG SE TE ESCAPA.** Dos de los tres errores de sintaxis (el conector
sin destino de EJ 4 y el flujo duplicado de EJ 3) son **invisibles en la imagen exportada** y solo
aparecen abriendo el `.bpm`. Era irrelevante hasta 2022, pero **desde 2026 la cátedra pide el `.bpm`
además de las dos imágenes**. Tu hábito de validar mirando el jpg ya no alcanza.
→ **El test del docente resuelve los dos de una:** mové cada elemento un centímetro antes de exportar; si
una flecha no lo sigue, está desconectada.

**PATRÓN 5 — NOMBRÁS BIEN LAS TAREAS Y MAL LOS EVENTOS, Y ENCIMA REGRESIONASTE.** De unas 35 tareas hay
**una sola** con verbo conjugado: eso está resuelto. Los eventos no: en junio (EJ 6) los tenías todos en
participio, impecables ("La invitación ha sido enviada", "Semana de espera transcurrida", "La banda ha
respondido"), y en septiembre (EJ 3 y EJ 4) volviste al infinitivo en **seis** eventos ("Enviar
correcciones", "Recibir artículo corregido", "Recibir respuesta del cliente"…).
→ Es **el mismo ítem que el repaso ya marca como error del diagrama del compañero** (4.2, error #2): es
un descuento que podés cobrar **dos veces** mañana. **Tarea = infinitivo + sustantivo. Evento = hecho
narrado (participio o sustantivo).**

### 4.2 Los errores confirmados, uno por uno

| # | Ejercicio | Qué está mal | Gravedad | Corrección |
|---|---|---|---|---|
| 1 | **EJ 6** | El proceso abre las dos ramas principales (lugar / música) con una **paralela (+)** y las cierra con una **exclusiva** (rombo vacío). La exclusiva no sincroniza: deja pasar el primer token y después el segundo, así que **toda la cola del proceso se ejecuta dos veces** (Ordenar comida → ¿Contrataron banda? → temporizador → Validar fiesta → fin). Es justo el concepto que la cátedra evalúa con el distractor "Requiere que todos los caminos hayan producido un token". | sintaxis | Cambiar ese rombo a **paralela (+)**. **Regla operativa: apenas ponés un +, poné inmediatamente su + de cierre, antes de dibujar nada adentro de las ramas.** |
| 2 | **EJ 3** | Pool Autor: inicio → evento intermedio de mensaje "Enviar artículo" → **nada**. Grado de salida cero, rama colgada. Y el pool tiene **dos inicios sueltos**, o sea dos fragmentos desconectados. | sintaxis | Evento de fin después de "Enviar artículo". Mejor todavía: **colapsar el pool Autor** y dejar solo los flujos de mensaje, como hace la cátedra. |
| 3 | **EJ 4** | El flujo entre el inicio y "Registrar reclamo" está roto en el `.bpm`: la transición tiene `From` y **no tiene `To`**. La flecha **se dibuja en el jpg**, pero el modelo está partido y lo levanta el validador de Bizagi. | sintaxis | Soltarla y volver a tirarla **del centro** del evento al **centro** de la tarea (no al borde). |
| 4 | **EJ 3** | El flujo "Realizar diseño" → compuerta de unión está **duplicado**: dos transiciones idénticas superpuestas. La unión queda con grado de entrada 3 cuando son 2. Invisible en el jpg. | sintaxis | Seleccionar la flecha, moverla, borrar la que queda debajo. |
| 5 | **EJ 6** | Falta **"Enviar factura al cliente"**: el enunciado termina con "Después de esto, la factura es enviada al cliente" y el proceso corta en "Validar fiesta". Es el último requisito explícito. | fidelidad | Agregarla después de "Validar fiesta", con flujo de mensaje al pool Cliente, y recién ahí el fin. |
| 6 | **EJ 5** | "Publicar la oferta" está en el lane **Director de RRHH**. El enunciado dice textual: "Una vez la información está completa **el Profesional de Selección** publica la oferta". | fidelidad | Moverla al lane correcto. **Método: subrayá el sujeto de cada oración del enunciado antes de dibujar, y usá ese sujeto como lane.** |
| 7 | **EJ 5** | "**Verifica** integridad de la solicitud": verbo conjugado. Única excepción en 35 tareas, pero es exactamente el error que el repaso ya tiene fichado. | estilo | "Verificar integridad de la solicitud". |

**Dos avisos más [NUESTRO]:**

- **Rama de compuerta basada en eventos apuntando a un evento intermedio NONE.** Está así en el TP grupal
  del Caso Hotel ("El cliente llegó a tiempo"). Una event-based **solo** puede apuntar a eventos de
  **captura** (mensaje, timer, señal, condicional) o a **receive tasks**. Un none ahí es error de
  sintaxis. Es lo mismo que el repaso (4.2) elogia como bien hecho en el diagrama del compañero: sabé
  hacerlo bien vos también.
- **Errores de tipeo visibles en el jpg entregado** (EJ 4: "¿Resulatado aceptado?", "Generar reporte
  vacio", lane "Logistica"). Menor, pero es lo primero que lee el corrector y cuesta cero.

### 4.3 Tus fortalezas — no las toques

**[NUESTRO]** Breve, para que sepas qué **no** revisar mañana y dónde no perder tiempo:

- **Etiquetado de compuertas: 100% en los cuatro ejercicios.** Las quince exclusivas tienen todas sus
  salidas etiquetadas, y ninguna paralela ni event-based está etiquetada — que es lo correcto. **Es el
  error #1 que el repaso marca en el diagrama del compañero y vos no lo cometés nunca.**
- **Cero flujos de secuencia cruzando pools, en los cuatro ejercicios.** Verificado en el XPDL. El error
  que "nunca se perdona" no aparece una sola vez. (Saltos entre lanes del mismo pool hay muchos, y es
  legal.)
- **Las compuertas nunca hacen trabajo:** la tarea que consigue el dato va siempre antes del rombo, y el
  rombo está nombrado como pregunta. Lo tenés automatizado.
- **La compuerta basada en eventos la tenés dominada**, que es lo que más pesa: en EJ 4 la usaste
  exactamente donde va (el formulario vuelve en dos semanas vs. vence el plazo), con las dos salidas
  apuntando a eventos de captura y sin etiquetar. En EJ 6 la volviste a usar con tres salidas.
- **Los loops de reproceso te salen bien y en cantidad:** los tres del EJ 5, el del EJ 3, el del EJ 4,
  los dos del EJ 6. Ninguno queda colgado.
- **Detalles finos que no son obvios y están:** "Generar reporte" tipada como **Script** en EJ 4 (el
  enunciado dice "procesado automáticamente", y la cátedra hace lo mismo); entender que el reporte vacío
  **no** termina el proceso; el subproceso **colapsado** con el "+" en EJ 5 donde el enunciado dice "no
  detallado"; y la fuga "si no encuentran banda a tiempo cambian a CD's" del EJ 6, que es la parte más
  difícil de ese caso.
- **Asignación de tareas a lanes casi perfecta** (EJ 4: 7 de 7; EJ 5: 6 de 7) y **tareas en infinitivo +
  sustantivo: 34 de 35**.

**[NUESTRO] Conclusión honesta:** modelás bien. Lo que te cuesta la nota no es el criterio, es la
**terminación**: bordes, cierres y relectura. Los tres minutos finales valen más que los últimos tres
elementos que agregues.

---

## 5. Cómo leer un enunciado de esta cátedra

### 5.1 Los dos formatos, y cuál esperar mañana

**[CÁTEDRA]** Los TP **grupales** vienen como **"Minuta de reunión"** (Caso Hotel, Porta 2016) o
**"ART MIN — Minuta Reunión N"** (Caso Alquiler de Autos, 2020): encabezado fijo (Tema / Fecha / Horario
/ Participantes) y el cuerpo en **prosa narrada por el entrevistado**, partido en secciones con título
(Reserva, Check-In, Check-Out, Servicios). **Nunca dice "modele el proceso": hay que extraerlo.**

⚠️ **[NUESTRO] El parcial probablemente NO use ese formato.** El caso de junio 2026 (`repaso-parcial.md`
4.1) viene como **consigna numerada 1..6**, un punto por paso, con las palabras clave servidas al vuelo
("subproceso", "loop", "plazo determinado", "puede ser cancelada"). El estilo minuta es el del TP grupal,
con dos o tres reuniones sucesivas y semanas de trabajo. **No le dediques tiempo de estudio.** Lo que
sigue se lee en dos minutos y solo lo usás si mañana cae un texto narrado.

### 5.2 Receta minuta → proceso, en el orden en que funciona

**[NUESTRO]**

1. **La sección "Procesos de Negocio" te da los procesos raíz ya listos.** El Caso Hotel dice textual
   "Reserva de Habitación - Check-in - Check-out" y "Gestión de los Servicios": **ese es el nombre del
   diagrama principal y del subproceso.** No se inventa nada.
2. **La sección "Problemática Excluida"** (Hotel) o el párrafo "Estarán excluidas…" (Autos) **define el
   alcance**: todo lo listado ahí **no se modela**. Es lo que más tiempo ahorra y lo que más se ignora.
3. **Los títulos de sección son las actividades de alto nivel.** La sección con varios párrafos y
   decisiones adentro es **candidata a subproceso**.
4. **Los "Participantes" del encabezado + los sujetos de las oraciones dan los lanes** ("el recepcionista
   ingresa", "el cliente informa").

### 5.3 Disparadores léxicos — la traducción frase → notación

**[NUESTRO]** Es el 80% del trabajo:

| Lo que dice el enunciado | Lo que se dibuja |
|---|---|
| "se verifica / se confirma la disponibilidad" | tarea **+ gateway exclusivo inmediatamente después** (la tarea consigue el dato, el rombo decide) |
| "si el cliente acepta… / puede no aceptar y se finaliza el proceso" | exclusivo con **dos fines** |
| "**pueden ocurrir cuatro eventos diferentes**" | **gateway basado en eventos**, una rama por evento. Es la frase más cara: está escrita casi en BPMN |
| "antes de las 15 hs", "pasadas 6 horas", "24 horas", "30 días corridos" | **evento temporizador** |
| "**en cualquier momento anterior a**" | **evento adjunto al borde** (boundary) |
| "se le ofrecen otras alternativas… el cliente puede aceptar y se continúa" | **loop** de vuelta al gateway anterior |
| "no forma parte de este proceso" | subproceso aparte, o directamente **fuera del alcance** |
| "a través de una aplicación interna" / "el sistema envía" / "procesado automáticamente" | el **tipo de tarea** está pedido en el texto (usuario / servicio / script) |

### 5.4 Dos avisos sobre la lectura

**[NUESTRO]**

- **Las minutas son incrementales y se pisan.** La minuta 2 del Hotel repite "Datos de las habitaciones"
  y le agrega capacidad; agrega medios de pago; agrega el camino de "no hay disponibilidad" que la 1 no
  cubría; agrega late check-out. **La minuta más nueva gana y AMPLÍA, no reemplaza.** Si un enunciado
  trae dos textos, leé los dos completos **antes** de dibujar: el segundo mete ramas nuevas en un flujo
  que en el primero parecía cerrado. (Mismo criterio que el enunciado acumulativo del caso Artículos:
  ver corrección 5.)
- **La minuta trae ruido que no es proceso.** Listas de atributos (datos personales del cliente, campos
  del comprobante, los 8 estados del auto, los datos del conductor) son **modelo de datos, no flujo**: en
  BPMN no se dibujan. Sirven para el prototipo de Axure y para el modelo de dominio.

### 5.5 Convenciones validadas en el TP grupal

**[CÁTEDRA]** (entrega del grupo, sin devolución del docente: **precedente, no verdad**). Confirman con
un segundo caso lo que `repaso-parcial.md` 4.3 ya daba por aceptable:

- **Cuatro diagramas, no dos**: un principal más tres subprocesos, y **cada subproceso con su propio pool
  y sus propios lanes**, distintos del padre. No pierdas tiempo mañana intentando que el subproceso
  comparta los lanes del pool padre.
- **Gateways nombrados como pregunta y con signos**, todos sin fallar uno: "¿Hay disponibilidad?",
  "¿Cliente acepta?", "¿Está demorado?", "¿Desea extender su estadía?". Copiá este patrón.
- **Tareas en infinitivo + sustantivo, y largas cuando hace falta**: "Informar al cliente el número de
  habitación y entregar llave", "Generar factura de estadía y entrega al cliente". **La cátedra tolera
  nombres largos y con dos verbos coordinados**: no te frenes buscando el nombre corto perfecto.
- **Eventos narrados como hecho**, no en infinitivo: "Cliente cancela reserva", "Llega las 15hs del día
  de la reserva y el cliente no se presentó", "Termina la estadía". La frase larga en el nombre del timer
  es aceptada.
- **El cliente fue como LANE, no como pool**, y el `.bpm` no tiene ningún flujo de mensaje — mientras que
  en EJ 3 y EJ 4 el mismo grupo lo puso en pool aparte. **Los dos criterios pasaron.** Lo que se corrige
  de verdad es que **ningún flujo de secuencia cruce la frontera de un pool**: si lo ponés como pool,
  **todo** lo que entra y sale va por flujo de mensaje punteado.

**[NUESTRO] Relación con el CU de Axure "Reservar habitación": reuso casi nulo.** La minuta describe un
hotel con reserva **telefónica** operada por un recepcionista; el CU de Axure es un cliente **logueado**
eligiendo entre varios hoteles en una web. Ni el actor ni el canal ni el alcance coinciden. Lo único
común es el vocabulario (fecha de entrada/salida, cantidad de personas, precio por día) y el cálculo
costo = precio × días, que ya está resuelto en la wiki. **No abras esos PDF mañana.**

---

## Log de este documento

- 2026-09-06: creado. Ingesta del PPT de teoría de la cátedra (48 láminas), desgrabación de las clases
  del 13-04 y 20-04, y auditoría de las entregas propias (EJ 3, 4, 5, 6) contra las soluciones oficiales
  `Caso_Articulos.pdf` y `Caso_Reclamo.pdf`. Complementa `repaso-parcial.md`; no lo reemplaza.
