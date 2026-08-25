Capítulo 1: Modelado de Simulación Básico (Law & Kelton)

La naturaleza de la simulación

Sistema: empresa o proceso de interés a modelizar.
Modelo: representación del sistema en términos de relaciones cuantitativas y lógicas.
Aplicaciones:
  Diseño y análisis de sistemas de fabricación.
  Evaluar requerimientos de hardware y software para un sistema informático.
  Evaluar nuevos sistemas de armas o tácticas militares.
  Determinar políticas de pedidos para un sistema de inventarios.
  Diseñar sistemas de comunicaciones y protocolos de mensajes para ellos.
  Diseñar y operar instalaciones de transporte.
  Evaluar diseños para organizaciones de servicios.
  Analizar sistemas financieros o económicos.

Sistemas, modelos y simulación

Un  sistema  se  define  como  una  colección  de  entidades  que  actúan  e  interactúan  juntos
hacia el cumplimiento de un fin lógico. Definimos el estado de un sistema como una colección
de variables necesarias para describir un sistema en un momento determinado, relativos a los
objetivos de estudio.

Los  sistemas  se  categorizan  en  dos  tipos:  discretos  o  continuos.  Un  sistema  discreto  es
aquel  en  el  que  las  variables  de  estado  cambian  instantáneamente  en  puntos  separados  del
tiempo. En un sistema continuo en cambio las variables de estado cambian continuamente con
respecto al tiempo.

Diferentes maneras en que un sistema puede ser estudiado:
  Experimentos  con  el  sistema  real  vs.  Experimentos  con  un  modelo  del  sistema:  si  es
posible alterar el sistema físico y luego dejar que opere bajo las nuevas condiciones, es
probable que sea conveniente hacerlo, porque en este caso no hay duda acerca de si
lo que estudiamos es relevante. Sin embargo, rara vez es posible hacer esto. Por esto,
es  necesario  construir  un  modelo  como  una  representación  del  modelo  y  estudiarlo
como un sustituto del sistema real.

  Modelos  físicos  vs.  Modelos  matemáticos:  los  modelos  físicos  son  construcciones  en
escala  reducida  o  simplificada  del  sistema  real  para  estudiar  en  ellos  su
comportamiento.  Los  modelos  matemáticos  representan  un  sistema  en  términos  de
relaciones  lógicas  y  cuantitativas  que  son  luego  manipuladas  y  modificadas  para  ver
como el sistema reacciona

  Solución  analítica  vs.  Simulación:  si  las  relaciones  que  componen  el  modelo  son
suficientemente simples, puede ser posible utilizar métodos matemáticos para obtener
información  exacta  sobre  cuestiones  de  interés,  lo  que  se  llama  solución  analítica.
Muchos  sistemas  son  demasiados  complejos  para  ser  estudiados  analíticamente,  y
deben  ser  estudiados  por  medio  de  la  simulación.  En  una  simulación,  usamos  la
computadora para evaluar un modelo numéricamente, y los datos se recogen con el fin
de estimar las características del modelo.

Clasificación de los modelos de simulación:
  Estáticos vs. Dinámicos: un modelo de simulación estático es una representación de un
sistema en un momento determinado, o  uno  que  puede ser utilizado  para representar
un  sistema  en  el  que  el  tiempo  simplemente  no  juega  ningún  papel.  Un  modelo  de
simulación dinámica representa un sistema a medida que evoluciona en el tiempo.
  Estocásticos vs. Determinísticos: Si un modelo de simulación no contiene componentes
probabilísticas (es decir aleatorias) se conoce como determinístico, en estos modelos la
salida se “determina” una vez que se especifica el conjunto de relaciones (ecuaciones)
y  los  valores  de  entrada.  En  cambio  los  modelos  estocásticos  contienen  variables
aleatorias de entrada sujetas a una distribución probabilística de algún tipo.

  Continuos  vs.  Discretos:  definimos  los  modelos  de  simulación  discreta  y  continua  de
manera  análoga  a  la  forma  en  que  los  sistemas  discretos  y  continuos  se  definieron
anteriormente.

Simulación de Eventos Discretos:

La  simulación  de  eventos  discretos  comprende  el  modelado  de  un  sistema  a  medida  que
este evoluciona a través del tiempo por medio de una representación en la cual las variables de
estado  cambian  instantáneamente  en  puntos  separados  en  el  tiempo.  Estos  puntos  en  el
tiempo  son  aquellos  en  los  cuales  un  evento  ocurre,  donde  un  evento  se  define  como  una
ocurrencia instantánea que puede cambiar el estado del sistema.

Mecanismo de Avance del Tiempo
Debido  a  la  naturaleza  dinámica  de  los  modelos  de  simulación  de  eventos  discretos,
tenemos que realizar un seguimiento del valor actual del tiempo simulado a medida que avanza
la  simulación,  y  también  necesitamos  un  mecanismo  para  avanzar  el  tiempo  simulado  de  un
valor  a  otro.  Llamamos  reloj  de  la  simulación  a  la  variable  de  un  modelo  de  simulación  que
contiene  el  valor  actual  del  tiempo  simulado.  La  unidad  del  reloj  nunca  se  enuncia
explícitamente y se asume que está en las mismas unidades que los parámetros de entrada.

Existen dos enfoques para el mecanismo de avance del tiempo:
  Avance del tiempo al siguiente evento: Con este enfoque el reloj de la simulación se
inicializa a cero y se determinan los tiempos de ocurrencia de eventos futuros, luego el
reloj se avanza al tiempo de ocurrencia del evento futuro más próximo, en este punto el
estado  del  sistema  se  actualiza  para  determinar  que  un  evento  ha  ocurrido  y  los
tiempos de futuros eventos también se actualizan. Este proceso continua hasta que se
cumple con una condición de parada pre especificada.

  Avance del tiempo a incrementos fijos: La diferencia con el método anterior es que
este enfoque no saltea periodos de inactividad en el sistema, lo que supone una mayor
cantidad de cómputo.

Componentes y organización de un modelo de simulación de eventos discretos
  Estado  del  sistema:  el  conjunto  de  variables  de  estado  necesarias  para  describir  el

sistema en un momento dado.

  Reloj de simulación: una variable que indica el valor actual del tiempo simulado.
  Lista de eventos: una lista que contiene la próxima vez en el que cada tipo de evento

ocurrirá.

  Contadores  estadísticos:  variables  usadas  para  almacenar  información  estadística

sobre el rendimiento del sistema.

  Rutina  de  inicialización: un sub-programa que inicializa el modelo de simulación en  el

tiempo cero.

  Rutina  de  tiempo:  un  sub-programa  que  determina  el  siguiente  evento  de  la  lista  de
eventos y luego avanza el reloj de simulación al momento en que ocurre ese evento.
  Rutina de evento: un sub-programa que actualiza el estado del sistema cuando un tipo

particular de evento ocurre (hay una rutina de evento por cada tipo de evento).

  Rutinas  de  biblioteca:  un  conjunto  de  sub-programas  utilizados  para  generar
observaciones  aleatorias  a  partir  de  distribuciones  de  probabilidad  que  fueron
determinadas como parte del modelo de simulación.

  Generador de informes: un sub-programa que calcula estimaciones de las medidas de

rendimiento deseadas y elabora un informe cuando la simulación finaliza.

  Programa principal: un sub-programa que invoca la rutina de tiempo para determinar el
siguiente evento y luego transfiere el control a la correspondiente rutina de evento para
actualizar  el  estado  del  sistema  apropiadamente.  También  controla  la  terminación  e
invoca al generador de informes cuando la simulación acaba.

Simulación de un Sistema de Colas de un solo Servidor (M/M/1):

En un sistema de colas de un solo servidor, los tiempos entre arribos A1, A2,…, An (de cada
cliente  al  sistema)  son  variables  aleatorias  IID  (independientes  e  idénticamente  distribuidas).
Un  cliente  que  arriba  y  encuentra  al  servidor  desocupado  se  atiende  inmediatamente,  y  los
tiempos  de  servicio  S1,  S2,…,  Sn  (de  cada  cliente)  son  también  variables  aleatorias  IID
independientes de los tiempos de arribo. Si un cliente arriba y encuentra al servidor ocupado se
une al final de cola. Al producirse una partida (un cliente completa el servicio) el servidor elige
un  cliente  de  la  cola  según  la  disciplina  FIFO.  La  simulación  comenzará  sin  clientes  en  el
sistema y el servidor en estado desocupado. El sistema se simula hasta que un número fijo (n)
de clientes hayan completados sus demoras en cola, es decir cuando el n-esimo cliente entre
en servicio.

Medidas  de  Rendimiento:  Para  medir  el  rendimiento  de  este  sistema  observamos  las

estimaciones de tres parámetros (más un parámetro opcional que es w(n)):
  Demora promedio esperada en cola de los n clientes. Llamada d(n).
  Número de clientes promedio esperado en la cola. Denotado por q(n).
  Utilización del servidor. Denominada u(n).
  Demora promedio esperada en el sistema de los n clientes. Llamada w(n).
Demora promedio esperada en cola de los “n-clientes”:
La  demora  promedio  en  una  corrida  determinada  de  la  simulación  es  considerada
propiamente  como  una  variable  aleatoria  en  sí.  Lo  que  queremos  estimar,  d(n),  es  el  valor
esperado  para  esta  variable  aleatoria.  d(n)  es  el  promedio  de  una  gran  numero  de  demoras
promedio  de  n  clientes.  A  partir  de  una  sola  corrida  de  la  simulación  podemos  estimar  este
parámetro a través de:

𝑑̂(𝑛) =

𝑛
∑ 𝐷𝑖
𝑖=1
𝑛

Esta fórmula es el promedio de las n demoras que fueron obtenidas durante la simulación.
Este  estimador  está  basado  en  una  muestra  de  tamaño  1  ya  que  estamos  haciendo
solamente  una  sola  corrida  de  la  simulación.  Un  estimador  de  este  tipo  no  tendrá  demasiada
precisión, pues el sistema seguramente se encuentra en estado transitorio.

Es un ejemplo de una estadística de tiempo discreto.

Número de clientes promedio esperado en la cola:

Este promedio se toma sobre el periodo de tiempo necesarios para observar las n demoras
que definen nuestra regla de parada. Esta es una clase diferente de promedio que el anterior,
ya que se toma sobre el tiempo (continuo) en lugar de los clientes (discreto).

Definimos Q(t) como el número de clientes en cola en el momento t (para cualquier t ≥ 0) y
T(n)  como  el  tiempo  requerido  para  observar  n  demoras  en  cola.  Para  cualquier  momento  t
entre  0  y T(n), Q(t) es no  negativo.  Si llamamos pi a la  proporción esperada (entre 0  y  1) del
tiempo en que Q(t) es igual a i, una definición de q(n) seria:

∞

𝑞(𝑛) = ∑ 𝑖𝑝𝑖

𝑖=0

Para  estimar  q(n)  en  una  simulación,  simplemente  reemplazamos  pi  con  sus  respectivas

estimaciones y obtenemos:

∞

Donde  𝑝̂𝑖  es  la  proporción  observada  del  tiempo  en  que  hubo  i  clientes  en  la  cola  (en  la

𝑞̂(𝑛) = ∑ 𝑖𝑝̂𝑖

𝑖=0

simulación).

Sin  embargo  una  manera  más  sencilla  de  obtener  𝑞̂(𝑛)  es  mediante  algunas
consideraciones  geométricas.  Si  llamamos  Ti  al  tiempo  total  durante  la  simulación  en  que  la
cola es de tamaño i, luego:
𝑛
𝑖=0 = 𝑇0 + 𝑇1 + 𝑇2 + ⋯ + 𝑇𝑛 y 𝑃𝑖 = 𝑇𝑖 𝑇(𝑛)

⁄

𝑇(𝑛) = ∑ 𝑇𝑖
Y el estimador puede escribirse como:

𝑞̂(𝑛) =

∞
∑ 𝑖𝑇𝑖
𝑖=0
𝑇(𝑛)

La sumatoria en el numerador de la ecuación anterior es solo el área bajo la curva de Q(t),

que puede escribirse como una integral de 0 hasta T(n), quedando finalmente la expresión:

𝑞̂(𝑛) =

𝑇(𝑛)
∫
0

𝑄(𝑡)𝑑𝑡

𝑇(𝑛)

Es un ejemplo de una estadística de tiempo continuo.

Utilización esperada del servidor:

La  utilización  esperada  del  servidor  es  la  proporción  esperada  de  tiempo  durante  la
simulación en que el servidor está ocupado y por eso es un número entre 0 y 1. El estimador
𝑢̂(𝑛)  es  la  proporción  observada  de  tiempo  durante  la  simulación  en  que  el  servidor  está
ocupado. Para esto definimos la “función ocupado” B(t).

𝐵(𝑡) = {

 1 𝑠𝑖 𝑒𝑙 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟 𝑒𝑠𝑡á 𝑜𝑐𝑢𝑝𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜 𝑡
 0 𝑠𝑖 𝑒𝑙 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟 𝑒𝑠𝑡á 𝑑𝑒𝑠𝑜𝑐𝑢𝑝𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜 𝑡

De esta manera 𝑢̂(𝑛) puede expresarse como la proporción de tiempo en que B(t) es igual a

1.

𝑢̂(𝑛) =

𝑇(𝑛)
∫
0

𝐵(𝑡)𝑑𝑡

𝑇(𝑛)

El  numerador  puede  ser  visto  como  el  área  bajo  la  función  B(t)  durante  el  curso  de  la

simulación.

𝑢̂(𝑛)  es  el  promedio  continuo  de  la  función  B(t).  La  integral  de  B(t)  puede  fácilmente  ser
acumulada  por  la  suma  de  las  áreas  de  los  rectángulos.  Las  estadísticas  de  uso  son  muy
informativos en la identificación de cuellos de botella o exceso de capacidad.

Es un ejemplo de una estadística de tiempo continuo.

Demora o Tiempo de espera promedio esperado en el sistema (cola + servidor):

Esta medida se define como el intervalo de tiempo desde el instante que un cliente arriba a

la cola hasta el instante en que el cliente completa el servicio y parte.

El estimador usual de w(n) seria:
𝑛
∑ 𝐷𝑖
𝑖=1
𝑛

𝑛
∑ 𝑆𝑖
𝑖=1
𝑛
Donde Si es el tiempo de espera de los n clientes en el servidor y 𝑆̅(𝑛) es el promedio de los
n tiempos de servicio de los clientes.  Ya que el tiempo de servicio medio o esperado E(S) es
conocido un estimador alternativo seria  𝑤̃(𝑛) = 𝑑̂(𝑛) + 𝐸(𝑆)

= 𝑑̂(𝑛) + 𝑆̅(𝑛)

𝑤̂(𝑛) =

+

En casi todas las simulaciones de colas 𝑤̃(𝑛) será mejor que 𝑤̂(𝑛). Ambos son estimadores

no sesgados.

Eventos y variables de estado: Los eventos de este sistema son el arribo de un cliente y la
partida de un cliente. Las variables de estado necesarias para estimar d(n), q(n) y u(n) son el
estado del servidor, el número de clientes en cola, el tiempo de arribo de cada cliente en cola y
el tiempo del ultimo evento.

Observaciones:
  El elemento clave in la dinámica de una simulación es la interacción entre el reloj de la

simulación y la lista de eventos.

  Mientras se procesa un evento, no transcurre el tiempo de simulación.
  A veces es fácil pasar por alto las contingencias que parecen fuera de lo común, pero

que sin embargo hay que tener en cuenta.

  En  algunas simulaciones puede suceder que  2 o más entradas en  la  lista de  eventos
empatan  en  menor,  y  deba  incorporarse  una  regla  de  decisión  para  romper  empates,
que afectará el resultado de la simulación.

Reglas de interrupción alternativas

La simulación puede terminar:
  Cuando el número de clientes atendidos llega a una determinada cantidad fija. El valor

final del reloj de la simulación es una variable aleatoria.

  Cuando el reloj llega a una cantidad fija de tiempo. El número de clientes atendidos es

una variable  aleatoria.

Determinando los eventos y variables

En  el  método  de  eventos  gráficos,  los  eventos  propuestos,  cada  uno  representado  por  un
nodo,  están  conectados  por  arcos  dirigidos  que  representan  cómo  los  eventos  se  pueden
programar  de  otros  eventos  y  de  ellos  mismos.  Los  eventos  gráficos  conectan  el  conjunto
propuesto de eventos por los arcos que indican el tipo de programación de eventos que pueden
ocurrir. Las flechas lisas gruesas indican que un evento al final de la flecha se puede programar
desde  el  evento  en  el  comienzo  de  la  flecha  en  una  cantidad  no  nula  de  tiempo,  y  la  flecha
dentada delgada indica que el evento en su extremo está programado inicialmente.

Uno  de  los  usos  de  los  gráficos  de  eventos  es  simplificar  la  estructura  de  eventos  de  una
simulación mediante la eliminación de eventos innecesarios. Hay varias reglas que permiten la
simplificación, y una de ellas es que si un nodo de evento tiene arcos entrantes que son todos

delgados  y  lisos,  este  evento  puede  ser  eliminado  del  modelo  y  su  acción  integrada  en  los
eventos que se programan en tiempo cero.

Otra  regla  tiene  que  ver  con  la  inicialización.  El  gráfico  de  eventos  se  descompone  en
componentes  fuertemente  conectados,  dentro  de  cada  uno  de  los  cuales  es  posible  viajar
desde cada nodo a todos los demás nodos siguiendo los arcos en sus direcciones indicadas.
La  regla  de  inicialización  establece  que  en  cualquier  componente  fuertemente  conectado  de
nodos  que  no  tenga  arcos  entrantes  de  otros  nodos  de  eventos  fuera  del  componente,  debe
haber al menos un nodo que se programa inicialmente.

Simulación distribuida

En  los  últimos  años  la  tecnología  informática  ha  permitido  que  las  computadoras  o
procesadores  individuales  se  asocien  entre  sí  en  entornos  de  computación  paralela  o
distribuida.  En  estos  tipos  de  entornos,  puede  ser  posible  distribuir  diferentes  partes  de  una
tarea computacional  a través de procesadores individuales que operan al mismo tiempo y por
lo tanto reducir el tiempo total para completar la tarea.

Hay  muchas  formas  posibles  de  dividir  una  simulación  dinámica  para  distribuir  su  trabajo

sobre diferentes procesadores:

  Asignar  las  distintas  funciones  de  apoyo  a  diferentes  procesadores.  La  lógica  de
ejecución  de  la  simulación  sigue  siendo  secuencial,  pero  el  programa  principal  de  la
simulación  puede  delegar
funciones  de  soporte  a  otros
la  ejecución  de
procesadores y seguir adelante con su trabajo.

las

  Descomponer  el  modelo  en  distintos  sub-modelos,  que  luego  son  asignados  a
diferentes procesadores para la ejecución. Los procesadores deben comunicarse entre
sí siempre que sea necesario para mantener las relaciones lógicas correctas entre los
sub-modelos.

Pasos en un estudio de simulación

1.  Formular  el  problema  y  planificar  el  estudio:  todo  estudio  debe  comenzar  con  una
declaración  clara  de  los  objetivos  generales  del  estudio  y  las  cuestiones  específicas
que se abordarán.

2.  Recolectar  datos  y  definir  un  modelo:  información  y  datos  deben  recolectarse  del
sistema  de  interés  y  utilizarse  para  especificar  los  procedimientos  operativos  y
distribuciones de probabilidad de las variables aleatorias utilizadas en el modelo.

3.  Validar: en la construcción del modelo,  es imperativo para  los modeladores  involucrar
en el estudio a las personas que están íntimamente familiarizadas con las operaciones
del sistema real.

4.  Construir un programa de computación y verificar: el modelador de la simulación debe
decidir  si  se  debe  programar  el  modelo  en  un  lenguaje  de  propósito  general  o  en  un
lenguaje de simulación de diseño especial.

5.  Hacer corridas piloto: se hacen pruebas piloto del modelo verificado.
6.  Validar: las pruebas piloto pueden usarse para probar la sensibilidad de las salidas del

modelo a pequeños cambios en un parámetro de entrada.

7.  Diseñar  experimentos:  hay  que  decidir  qué  diseño  de  sistema  simular  si  hay  más  de

una alternativa que pueda razonablemente simularse.

8.  Hacer corridas de producción: se hacen corridas de producción para proporcionar datos

de rendimiento sobre los diseños de los sistemas de interés.

9.  Analizar  los  datos  de  salida:  se  usan  técnicas  estadísticas  para  analizar  los  datos  de

salida de las corridas.

10.  Documentar  presentar  e  implementar  los  resultados:  es  importante  documentar  los

supuestos que entraron en el modelo, así como el propio programa informático.

Otros tipos de simulación

  Simulación  continua:  se  refiere  a  la  modelización  a  lo  largo  del  tiempo  de  un  sistema
por una representación en la que las variables de estado cambian continuamente con
respecto  al  tiempo.  Involucra  ecuaciones  diferenciales  que  dan  las  relaciones  de  las
tasas de variación de las variables de estado con el tiempo.

  Simulación  combinada  discreta-continua:  puesto  que  algunos  sistemas  no  son  ni
completamente  discretos  ni  completamente  continuo,  puede  surgir  la  necesidad  de
construir un modelo con aspectos tanto de simulación de eventos discretos y continuos.

  Simulación de  Monte Carlo: es un esquema de empleo de números aleatorios que se
utiliza para solucionar determinados problemas estocásticos o deterministas en donde
el paso del tiempo no juega ningún papel sustantivo.

Ventajas, desventajas y dificultades de la simulación

Ventajas:
  Muchos sistemas complejos no pueden describirse con precisión mediante un modelo
matemático  que  puede  evaluarse  analíticamente.  Por  lo  tanto,  una  simulación  es  a
menudo el único tipo de investigación posible.

  Permite estimar el rendimiento de un sistema existente bajo un conjunto de condiciones

de operación proyectados.

  En  una  simulación  podemos  mantener  mejor  control  sobre

  Diseños  alternativos  del  sistema  propuesto  se  pueden  comparar  a  través  de  la
simulación para poder ver los que mejor se adaptan a los requerimientos especificados.
las  condiciones
experimentales  de  lo  que  generalmente  sería  posible  cuando  experimentamos  con  el
propio sistema.

  Permite estudiar un sistema con un horizonte temporal largo en tiempo comprimido, o
bien estudiar los pormenores del funcionamiento de un sistema en tiempo expandido.

Desventajas:
  Cada corrida de un modelo de simulación estocástico produce solo estimaciones de las
verdaderas  características  del  modelo  para  un  conjunto  particular  de  parámetros  de
entrada.

  Los  modelos  de  simulación  suelen  ser  costosos  y  requieren  mucho  tiempo  para

desarrollarlos.

  El  gran  volumen  de  números  producidos  por  un  estudio  de  simulación  o  el  impacto
persuasivo  de  una  animación  realista  crea  a  menudo  una  tendencia  a  poner  mayor
confianza en los resultados de un estudio que la que se justifica.

