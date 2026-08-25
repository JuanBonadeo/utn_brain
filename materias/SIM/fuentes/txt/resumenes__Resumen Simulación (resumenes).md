Resumen Simulación

Low-Kelton

Capítulo 1 – Modelado Básico por Simulación

1.1  Naturaleza Básica de la Simulación

Sistema: Es la instalación o proceso de interés que estudiamos. Para estudiarlo
científicamente, hay que hacer suposiciones lo más realistas posibles
(hipótesis) de cómo funciona.

Estas suposiciones toman forma de relaciones lógicas o matemáticas,
constituyen un modelo, que se usa para tratar de entender el comportamiento
del sistema.

•  Si el sistema es simple -> podemos usar métodos matemáticos para

obtener información exacta del sistema; a esto se le llama una solución
analítica. El modelo es un Modelo Matemático.

•  Si el sistema es complejo (la mayoría de los sistemas reales) -> deben
ser estudiados por simulación a través de computadoras donde en vez
de darme una solución exacta me devuelve estimaciones.

¿A qué se puede aplicar la simulación?

•  Diseño y análisis de sistemas de fabricación.
•  Evaluar requerimientos de hardware y software para un sistema informático.
•  Evaluar nuevos sistemas de armas o tácticas militares.
•  Determinar políticas de pedidos para un sistema de inventarios.
•  Diseñar sistemas de comunicaciones y protocolos de mensajes para ellos.
•  Diseñar y operar instalaciones de transporte.
•  Evaluar diseños para organizaciones de servicios.
•  Analizar sistemas financieros o económicos

1.2  Sistemas, Modelos y Simulación

Sistema: Es una colección de entidades, que actúan e interactúan juntos para
lograr un objetivo lógico.

Estado de un Sistema: Es una colección de variables necesarias para
describirlo, en un momento dado, en relación con los objetivos de estudios.

Clasificación de Sistemas: Discretos vs Continuos

1.2.1

1.2.2

Discretos: Es aquel en el que las variables de estado (V.E) cambian
instantáneamente en puntos de tiempo separados.
Ejemplo: Un Banco, donde el número de clientes cambia cuando un cliente
arriba al banco o finaliza su atención y parte.
Continuos: Es aquel para el cual las V.E cambian continuamente respecto al
tiempo.
Ejemplo: Un avión, donde las variables de la posición y la velocidad cambian
continuamente con respecto al tiempo.

En la práctica pocos sistemas son completamente discretos o continuos.

Maneras de estudiar un Sistema:

Sistema

Experimentar
con el Sistema
Real

Experimentar
con un Modelo
del Sistem

Modelo Físico

Modelo
Matemático

Solucion
Analítica

Simulación

Experimentar con el sistema real: Si es posible (y rentable), alterar el sistema
físicamente y luego dejarlo operar bajo las nuevas condiciones, aunque tal
experimento costaría demasiado o perjudicaría al sistema.

Experimentar con un modelo del sistema: Construir un modelo como
representación del sistema y estudiarlo como reemplazo del sistema real.

Modelo físico: son construcciones en escala reducida o simplificada del sistema
real para estudiar en ellos su comportamiento, pero no se utiliza tanto.

Modelo matemático: representan a un sistema en términos de relaciones
lógicas y cuantitativas que luego son manipuladas y cambiadas para ver cómo el
modelo reacciona.

Solucion analítica: Una vez que construimos el modelo matemático, si el
modelo es simple, podría ser posible trabajar con sus relaciones y cantidades
para obtener una solución exacta, analítica.

Simulación: Si el modelo es complejo el mismo debe ser estudiado mediante la
simulación, trabajando numéricamente con las entradas para ver cómo afectan
las medidas de desempeño de la salida.

Clasificación los modelos de simulación:

•  Estáticos vs. Dinámicos:

Estático: representación del sistema en un momento determinado o un sistema en el que
el tiempo no interviene.
Dinámico: representación del sistema con el avance del tiempo.

•  Determinísticos vs. Estocásticos:

Determinísticos: no contiene ningún componente probabilístico o aleatorio o determinista.
los valores de los parámetros utilizados se saben con anterioridad, y están dados por
alguna ecuación estática, que no cambia con el tiempo.
Estocásticos: hay, al menos, algún componente de entrada aleatorio y producen salidas
aleatorias.
las variables están dadas por distintas distribuciones de probabilidad, en las cuales el valor
que se utilizará durante la simulación es aleatorio, correspondiente con la distribución. Por
lo tanto no es posible saber el valor con anterioridad.

•  Continuos vs. Discretos:

Discretos: las variables de estado cambian constantemente en el tiempo.
Continuos: las variables de estado cambian constantemente en el tiempo.

Los modelos que vamos a estudiar en la materia son:

−  DINAMICOS
−  ESTOCASTICOS
−  DISCRETOS

1.3  Simulación de Eventos Discretos

Es el modelado de un sistema mientras evoluciona en el tiempo donde las variables de
estado cambian en puntos separados en el tiempo (cuando ocurre un evento).

Un evento se define como un suceso instantáneo que cambia el estado del sistema.

La simulación de eventos discretos puede hacerse a mano, pero es recomendable
hacer en computadora.

1.3.1  Mecanismos de avance en el tiempo

Reloj de simulación: a variable que da el valor actual del tiempo simulado. Su unidad
de tiempo no se establece explícitamente.

Dos métodos para avanzar el reloj de simulación:

1.  Avance al próximo evento, el reloj es inicializado en cero y se calculan los

tiempos de ocurrencia de los eventos. Entonces, el reloj avanza al tiempo de
ocurrencia del próximo evento, se actualiza el estado del sistema y se
actualizan los tiempos de eventos futuros. Este proceso continua hasta que se
cumple con una condición de parada preespecificada.

Reloj de simulación absoluto: parte de 0 y termina en un tiempo total de simulación
definido.

2.  Avance a incrementos fijos, difiere del anterior ya que no saltea periodos de
inactividad en el sistema, lo que supone una mayor cantidad de cómputo.

Reloj de simulación relativo: solo considera los lapsos de tiempo que transcurre
entre dos eventos.

1.3.2  Componentes y organización de un modelo de

simulación de eventos discretos

Componentes:

1

2
3
4

5

6

7

8
9

10

Estado del Sistema: Colección de V.E necesarias para describir el Sistema en un
momento determinado.
Reloj de Simulación: variable que da el valor actual del tiempo simulado.
Lista de Eventos: Lista que contiene la próxima vez que ocurre un evento.
Contadores Estadísticos: Variables utilizadas para almacenar información
estadística sobre el desempeño del sistema.
Rutina de inicialización: subprograma que inicializa el modelo de simulación al
tiempo cero.
Rutina de avance en el tiempo: subprograma que determina el próximo evento
de la lista de eventos y luego actualiza el reloj de simulación al tiempo del
evento.
Rutina de eventos: subprograma que actualiza el estado del sistema cuando
ocurre un tipo particular de evento.
Biblioteca de rutinas: subprogramas usados para generar observaciones.
Generador de informes: Subprograma que calcula estimaciones a partir de los
Contadores Estadísticos.
Programa principal: Subprograma que invoca a la Rutina de avance en el tiempo
para determinar el próximo evento.

Organización de un modelo de eventos discretos:

1.  Modelo de un Sistema de Espera (1.4)
2.  Modelo de un Sistema de Inventario (1.5)

1.3.3  Diagrama de flujo del mecanismo de avance al

próximo evento

1.4  Simulación de un Sistema de

Espera Formado por una sola Cola
con un solo Servidor.

1.4.1  Planteo del problema

Diagramas

 Servidor

   Cliente en Servicio

Clientes en Cola

    Cliente que llega

    Cliente que se retira

Supuestos o Hipótesis:

•  Los tiempos entre arribos A1,A2,…, son V.A independientes y distribuidas de

manera idéntica (V.A.I.I) (Ai=ti-ti-1).

•  Un cliente que llega y encuentra al servidor desocupado, entra y empieza a ser

atendido (s1,s2,… son VAII)

t=0 -> servidor inactivo

t1>0

•  Cuando llega un cliente y el servidor esta ocupado, espera en la cola y los

clientes son atendidos en FIFO.

•  Cuando el n-esimo cliente completo la cola o cuando haya pasado un tiempo T,

se finaliza la simulación. (T= tiempo prefijado de antemano.)

Medidas de Desempeño o Rendimiento

Las medidas de desempeño o rendimiento son V.A

1.  Demora promedio de cola esperada por los n clientes que completaron su

demora durante la simulación.

𝑑̂(𝑛) =

𝑛
∑ 𝐷𝑖
𝑖=1
𝑛

Esta fórmula es el promedio de las n demoras (D) que fueron obtenidas durante la
simulación.

Está basado en una muestra de tamaño 1 ya que estamos haciendo solamente una
sola corrida de la simulación. Un estimador de este tipo no tendrá demasiada
precisión, pues el sistema seguramente se encuentra en estado transitorio.

Es un ejemplo de una estadística de tiempo discreto.

2.  Numero promedio de clientes esperando en cola.

Para definir esta medida utilizaremos los valores:

•  𝑄(𝑡): el número de clientes en cola en el tiempo t.
•  𝑇(𝑛): el tiempo requerido para observar las 𝑛 demoras en cola.

Para cualquier momento 0 ≤ 𝑡 ≤ 𝑇(𝑛) , Q(t) es no negativo.

i= número de clientes.

Ti= tiempo en el que hay i clientes en cola.

T(n)=T0+T1+T2+…+ Tn

Pi= proporción de tiempo total en el que hay i clientes en cola

𝑃𝑖 =

𝑇𝑖
𝑇(𝑛)

∞
𝑞̂(𝑛) = ∑ 𝑖. 𝑃𝑖 =
𝑖=0

∞
(∑ 𝑖. 𝑇𝑖
𝑖=0
𝑇(𝑛)

)

=

𝑇(𝑛)
∫
0

𝑄(𝑡). 𝑑𝑡

𝑇(𝑛)

Es un ejemplo de una estadística de tiempo continuo.

3.  Proporción de tiempo que el servidor está ocupado. Definimos la función

“ocupado”:

𝐵(𝑡) = {

1 𝑠𝑖 𝑒𝑙 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟 𝑒𝑠𝑡𝑎 𝑜𝑐𝑢𝑝𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜 𝑡
0 𝑠𝑖 𝑒𝑙 𝑠𝑒𝑟𝑣𝑖𝑑𝑜𝑟 𝑒𝑠𝑡𝑎 𝑑𝑒𝑠𝑜𝑐𝑢𝑝𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜 𝑡

Entonces:

𝑢̂(𝑛) =

𝑇(𝑛)
∫
0

𝐵(𝑡). 𝑑𝑡

𝑇(𝑛)

Es un ejemplo de una estadística de tiempo continuo.

1.5  Simulación de un Sistema de

Inventario

El objetivo de esta simulación es decidir cuántos items deben tenerse en inventario los
próximos meses para minimizar los costos. Es decir, elegir la mejor política de inventario.

•
•

La empresa vende un solo producto.
Los tiempos entre demandas son V.A exponenciales independiente e idénticamente
distribuidas (IID) con una media de 0,1 mes.

•

Las probabilidades de la cantidad demandada son:

Eventos:

Llegada de un pedido desde el proveedor a la empresa.

•
•  Demanda de productos por parte de un cliente.
•  Evaluación de inventario al inicio del mes.

Pedido al proveedor: tiene una demora de entrega representada por una variable aleatoria
uniformemente distribuida entre 0,5 y 1 mes.

Costo por pedido:

Cp = K + i.Z   donde

−  K es el costo fijo
−
−  Z es la cantidad de productos pedidos.

i es el costo por unidad

Política de pedidos: es una política estacionaria (s,S) con ‘s’ siendo el nivel mínimo deseado de
mercadería en existencia y ‘S’ el nivel máximo.

Siendo I el nivel real de inventario al momento de hacer un pedido (Final de cada periodo
(mes)).

Valores y variables:

I(t): nivel de inventario al momento t (puede ser positivo, negativo o cero)
I+(t): número de unidades que realmente están en existencia. MAX (I(t), 0)
I–(t): número de unidades demandadas y no entregadas. MAX (-I(t), 0)

•
•
•
•  h: Costo de mantenimiento de items por mes de inventario.
•  π: costo por ítem por mes de atraso en la entrega (por faltantes en el mes).

Número de ítems en el inventario para el 𝑛-ésimo período de tiempo.

Número de ítems faltantes en el inventario para el 𝑛-ésimo período de tiempo.

•
•

𝐼̅+h: costo promedio mensual por ítems en existencia (por mantenimiento).
𝐼̅−π: costo promedio mensual por ítems adeudados o faltantes.

Rutinas:

Ventajas y desventajas de una
Simulación

Ventajas:

•  Buena herramienta para conocer el impacto de los cambios sin necesidad de llevarlos

a cabo en la realidad

•  Mejora el conocimiento del proceso actual al evaluarlo ante distintos escenarios
•  Puede utilizarse como medio de capacitación para toma de decisiones
•  Es más económico frente a cambios reales
•  Permite estudiar varios escenarios buscando mejores condiciones
•  Permite generar buenas soluciones en problemas de más complejidad
•  Es posible ver como se comportará un proceso una vez sea mejorado.

Deventajas

•  No es una herramienta de optimización
•  Puede ser costoso

•  Se requiere bastante tiempo para realizar un buen estudio de simulación
•  Requiere conocimiento y dominio de los paquetes de simulación y de estadística para

interpretar resultados.

Pasos para realizar un estudio de
simulación

1)  Definición del sistema en estudio: las variables de decisión, la interacción entre
ellas y los alcances y limitaciones del modelo. El objetivo de la simulación.
2)  Generación de un modelo de simulación base: creación de un modelo no muy

detallado con la información que se tiene.

3)  Recolección y análisis de datos: se recopila y analiza la información estadística
necesaria para determinar las distribuciones de probabilidad de cada una de las
variables aleatorias del modelo.

4)  Generación del modelo preliminar: se integra toda la información obtenida

para lograr un modelo lo más cercano posible al sistema en estudio.
5)  Verificación del modelo: se comprueba que todos los parámetros usados

funcionen correctamente y que el comportamiento del modelo sea cercano a lo
que se esperaba.

6)  Validación del modelo:  realizar una serie de pruebas utilizando información
real en la entrada para observar cómo se comporta y analizar los resultados.

Verificacion:  se analiza si el comportamiento y si sus parámetros son correctos
(se ajusta a la realidad)
Luego de realizar la verificación, se realiza la validación, consiste en ingresar
valores reales para ver si se comporta de la manera adecuada, para poder
generar un modelo final.

7)  Generación del modelo final: modelo resultante luego de validar y verificar el

preliminar.

8)  Determinación de los escenarios: junto con el cliente, se determinan los
escenarios que se quieren analizar. definir un escenario pesimista, uno
optimista y uno intermedio para la variable de respuesta más importante
9)  Análisis de sensibilidad: realización de pruebas estadísticas para comparar los
escenarios con los mejores resultados finales para determinar el ganador. Si
dos escenarios tienen resultados similares será necesario comparar sus
intervalos de confianza respecto de la variable de respuesta final. También
puede ser necesario realizar más réplicas (Análisis de resultados).

10) Documentación del modelo, sugerencias y conclusiones: se incluye toda la

información recolectada, sugerencias de uso del modelo y de los resultados y,
por último, las conclusiones de la simulación.

13. Modelo de Colas

Sistemas de colas:  Sistema en el que los productos (o los clientes) llegan a una
estación, esperan en una fila (cola), obtienen algún tipo de servicio y luego salen del
sistema.

13.1 Características de un sistema de colas

•  Población de clientes:  conjunto de todos los clientes posibles, cuando el

número es grande, se considera infinita.

•  Proceso de llegada: Forma en la que los clientes llegan a solicitar un servicio. La

característica más importante es el tiempo entre llegadas, que puede ser
determinístico o probabilístico.

•  Proceso de colas: Forma en la que los clientes esperan los servicios.  Puede
importar la cantidad de colas (una o varias), si la cola es infinita o finita y la
disciplina de colas (PEPS, UEPS, prioridad, etc.).

•  Disciplina de colas: Forma en la que los clientes son elegidos para dar el

servicio.

•  Proceso de servicio: Forma y rapidez con la que es atendido el cliente.
•  Proceso de salida: Forma en la que los clientes abandonan el sistema de colas.

13.1.1 Población de clientes

Dos tamaños posibles

•  Finita-> banco/supermercado
•

Infinita->fabrica con numero de máquinas que se descomponen.

13.1.2 El proceso de llegada

Tiempo entre llegadas: intervalo de tiempo que existe entre dos llegadas sucesivas de
clientes a un sistema de colas.

•  Determinístico: los clientes sucesivos llegan en un mismo intervalo de tiempo,

fijo y conocido.

•  Probabilístico: el tiempo entre llegadas sucesivas es incierto y variable. Los

tiempos entre llegadas se describen mediante distribuciones de probabilidad.

Distribución de Poisson:
λ =tasa de arribos= N° de clientes / Unidades de tiempo
1 /λ = tiempo entre arribos promedio
μ= tasa de servicio
1/ μ

13.1.4 El proceso de colas

Tipos:

•  Sistema de colas de una sola línea-> los clientes esperan en una sola línea para

tener acceso al servicio.

•  Sistema de colas de líneas múltiples-> los clientes que llegan pueden elegir una

de varias líneas en la cual esperar el servicio.

Características:

Numero de espacios de espera de cada fila:

•  Finito
•

Infinito

Disciplinas de las colas:

•  Primero en entrar, Primero en salir (PEPS)-> los clientes son atendidos en orden

que llegan

•  Primero en entrar, ultimo en salir (VEPS)-> el cliente que ha llegado mas

recientemente es el primero en ser atendido.

•  Selección de prioridad (ejemplo hospital por gravedad)-> a cada cliente se le da

una prioridad y de acuerdo con esta son atendidos.

13.1.4 El proceso de servicio

Características:

Cantidad de estaciones de trabajo:

•  Sist. Col. De canal múltiple -> varias estaciones (con servicios idénticos o

distintos)

•  Sist. Col. De canal sencillo-> 1 estación.

Número de clientes atendidos por estación:

•  1 cliente a la vez-> super/banco/etc.
•  Grupo de clientes a la vez-> pasajeros de autobús

Si tiene o no prioridad:

•  Prioridad-> proceso de servicio en el cual un servidor puede interrumpir el

servicio que esta proporcionando para dar lugar a un nuevo cliente.

Tipo de servicio:

•  Determinístico: los clientes son atendidos en el mismo intervalo de tiempo, fijo

y conocido.

•  Probabilístico: el tiempo de servicio es incierto y variable. Se describen

mediante distribuciones de probabilidad.

1.3.5 Clasificación de los modelos de colas

Se supone población infinita, una sola cola de espera y espacio en cola infinito.

El proceso de llegada -> dist. Entre t de llegadas

•  D: t. determinístico
•  M: t. probabilísticos, con distribución exponencial.
•  G: t. probabilísticos, con distribución diferente a la exponencial.

El proceso de servicio -> dist. de t de servicio

•  D: t. determinístico
•  M: t. probabilísticos, con distribución exponencial.
•  G: t. probabilísticos, con distribución diferente a la exponencial.

El proceso de colas:

•  C: representa cuantas estaciones de servicio en paralelo existen en el sistema.

Si el espacio de espera y/o el tamaño de la población son finitos:

•  K: número máximo de clientes que pueden estar en el sistema en cualquier

momento

•  L: número total de clientes de la población.

13.2 Medidas de rendimiento de un sistema de colas

Cualquier sistema de colas tiene dos fases:

•

La fase transitoria-> el periodo inicial de un sistema de colas donde se conservan los
efectos de las condiciones iniciales.

•  estado estable-> condición del sistema después que se han eliminado las condiciones

iniciales.

1-  Cuando inicia el sistema no hay cola por lo que el primer cliente es atendido de

manera inmediata (sin hacer cola), luego van llegando más clientes y la cola se va
agrandando, por lo que aumenta el tiempo de espera en cola.

2-  A medida que avanza el tiempo, el tiempo d espera en cola comienza a estabilizarse,

por lo que los clientes nuevos esperan casi el mismo tiempo.

Condición de estado estable -> 1/ 𝜇 < 1/𝜆

ρ = 𝝀 / 𝝁 < 1

13.2.1 Medidas de rendimiento

Son valores numéricos que se utilizan para evaluar cómo funciona un sistema de colas en
estado estable.

Para obtener las diferentes medidas de rendimiento es necesario conocer los siguientes
parámetros, correspondientes a los procesos de llegada y de servicio.

•  Tiempo promedio de espera en cola (𝑊𝑞)
•  Tiempo promedio en el sistema (𝑊)
•
Longitud media de la cola (𝐿𝑞)
•  Número medio de clientes en el sistema (𝐿)
•  Probabilidad de bloqueo (𝑃𝑤): probabilidad de que un cliente que llega tenga que

esperar a ser atendido.

•  Utilización del servidor (𝑈): tiempo, en promedio, que un servidor está ocupado.
•  Probabilidad de negación de servicio (𝑃𝑖): probabilidad de que un cliente que llega no

pueda entrar debido a que la cola está llena.

•  Distribución de probabilidad de estado: probabilidad de que se encuentren 𝑛 clientes

en el sistema

13.2.2 Relaciones entre medidas de rendimiento

Cola M/M/1

Siendo:

𝜆 = número promedio de llegadas por unidad de tiempo

𝜇 = número promedio de clientes atendidos por unidad de tiempo en una estación

•  Para que el sistema alcance un estado estable se tiene que dar que μ > λ.
•  Población: infinita
•
•  Cola: única, con capacidad infinita. Disciplina PEPS.
•  Servicio: distribución exponencial. (μ)

Llegadas: proceso de Poisson (λ)

ρ = 𝝀 / 𝝁 (“intensidad de tráfico”).

Número promedio en fila:

Tiempo promedio de espera en la cola:

Tiempo promedio de espera en el sistema:

Número promedio en el sistema:

Probabilidad de que no haya clientes en el sistema:

Probabilidad de que un cliente que llegue espere:

Probabilidad de que haya n clientes en el sistema:

Utilización (del servidor):

Cola M/M/C

Tiene las mismas características que el M/M/1 (población infinita, disciplina de cola PEPS y
capacidad de cola infinita) solo que en lugar de un servidor puede haber varios.

Condición de estado estable ->  ρ = 𝝀 / 𝝁. c < 1

Donde c = cantidad de servidores en paralelo.

También es válido -> c.μ > λ

Condiciones de un Modelo M/M/c:

1.  La población de clientes es infinita.
2.  Proceso de llegada con distribución de Poisson de λ clientes por unidad de tiempo.
3.  Proceso de cola de una sola fila de espera de capacidad infinita con una disciplina de

primero en entrar, primero en salir.

4.  Proceso de servicio de c servidores idénticos, cada uno con una distribución

exponencial 𝝁 de atención de clientes por unidad de tiempo.

13.5 Análisis económico de los sistemas de colas

13.5.2 Análisis de costos del sistema de colas

En un sistema de colas donde se puede controlar el número de servidores o su tasa de servicio,
para conocer el costo total por unidad de tiempo, es necesario saber:

•  El costo por servidor por unidad de tiempo (Cs).
•  El costo por unidad de tiempo por cliente esperando en el sistema (Cw).
•  El número promedio de clientes por unidad de tiempo en el sistema (L).

Luego, Costo total por unidad de tiempo para c servidores = (𝐶𝑠 . 𝑐) + (𝐶𝑤. L)

13.6 Análisis de otros modelos de colas usando la
computadora

13.6.1 Un sistema M/M/c con una población de clientes finitas
(M/M/c/K)

Población de clientes finita (M/M/c/k)

En estos casos la tasa de llegadas disminuye a medida que aumenta el número de clientes en
el sistema porque existen menos clientes que aún no llegaron. El proceso de llegada se

describe considerando la tasa de llegada de cada cliente individual. No se puede describir
mediante una tasa fija.

13.6.1 Un sistema M/M/c con capacidad de espera limitada
(M/M/c/K) (capacidad cola ≠ ∞)

Para poder realizar el análisis de costos, es necesario conocer la probabilidad de negación del
servicio (Pd) = probabilidad de que un cliente que llega no pueda entrar debido a que la cola
está llena.

Entonces, para el cálculo del costo total por unidad de tiempo:

•  Costo por servidor (Cs)
•  Costo por esperar (Cw)
•  Costo asociado a la pérdida de un cliente (Cd).

𝐶𝑜𝑠𝑡𝑜 𝑡𝑜𝑡𝑎𝑙 𝑝𝑜𝑟 𝑢𝑛𝑖𝑑𝑎𝑑 𝑑𝑒 𝑡𝑖𝑒𝑚𝑝𝑜 = (𝐶𝑠. 𝑐) + (𝐶𝑤. 𝐿) + (𝐶𝑑. 𝜆. 𝑃𝑑)

13.6.3 Un sistema de colas con una distribución de tiempo de
servicio general (M/G/c)

En este tipo de sistemas para calcular las medidas de rendimiento es necesario conocer,
además de la tasa promedio de llegadas (λ), el tiempo promedio por servicio y la desviación
estándar del tiempo de servicio. Si la desviación estándar es igual a 0, es determinístico.

Consideraciones gerenciales complementarias

•  Elección del modelo adecuado: puede que el sistema en cuestión no se adapte a los
modelos conocidos. En estos casos se pueden hacer algunas suposiciones para
aproximarlo a dichos modelos.

•  Sistema de colas adicionales: pueden existir sistemas con características distintas a las

estudiadas, como, por ejemplo:

−  Sistema con clientes que llegan en lotes.
−  Sistema con clientes que esperan en múltiples filas.
−  Sistema con atención en grupo.
−  Sistema con diferentes disciplinas de atención.
−  Sistema con clientes que pueden renunciar a esperar.
−  Sistema con red de estaciones de trabajo.

•  Análisis de sensibilidad: consiste en calcular repetidamente las medidas de

rendimiento y los análisis económicos para el modelo, cambiando en cada caso los
datos de interés (cantidad de servidores, tasa de llegada, tasa de servicio, etc.) para
encontrar la mejor solución.

•  Análisis de equilibrio: hace referencia a la elección de los parámetros del sistema en la
búsqueda de valores en particular para ciertas medidas de rendimiento y cómo eso
afecta a otras. Por lo tanto, es necesario hacerlo procurando obtener valores
aceptables para todas las medidas de rendimiento.

Libro ROSS

S= espacio muestral -> todos los resultados posibles al hacer el experimento

A= eventos (sucesos)

2.2 Axiomas de la probabilidad

P(A) = probabilidad de cualquier evento

1)  0≤P(A)≤1
2)  P(S)=1

3)

2.3 Probabilidad condicional e
Independencia

Probabilidad condicional. Saber la probabilidad de que ocurra A habiendo
ocurrido B.

2.3 Variable aleatoria

La función de distribución F de la variable aleatoria X se define para cualquier número real
x como:

Para una variable aleatoria discreta X, definimos su función de masa de probabilidad p(x)
como:

Propiedad:

Para especificar la relación entre dos variables aleatorias, definimos la función de
distribución de probabilidad acumulativa conjunta de X y Y como

Si tanto X como Y son variables aleatorias discretas, entonces definimos la función de masa
de probabilidad conjunta de X y Y como

X y Y son conjuntamente continuas, con función de densidad de probabilidad conjunta
ƒ(x,y), Si para cualesquiera conjuntos de números reales C y D

2.4 Esperanza

Si X es una variable aleatoria discreta que toma uno de los posibles valores x1, x2, ….,
entonces la esperanza o valor esperado de X, también llamado media de X y denotado por
E[X], Se define como:

Si X es una variable aleatoria continua con función de densidad de probabilidad f,
entonces, definimos la esperanza de X como:

2.5 Varianza

Si X es una variable aleatoria con media 𝝁 entonces la varianza de X, denotada por Var(X),
se define como:

La varianza es la esperanza de los desvíos al cuadrad -> refleja el alejamiento de los valores
con respecto a la media.

Obtenemos una fórmula alternativa para Var(X) como sigue:

La varianza de una ctte es igual a 0

Demostración que V[aX]=a2V[X]

La covarianza de dos variables aleatorias X y Y, denotada Cov(X, Y), se define como:

Desarrollando el lado derecho de la ecuación:

Como

vemos que

la varianza de la suma de variables aleatorias independientes es igual a la suma de sus
varianzas.

2.6 Desigualdad de Chebyshev y las
leyes de los grandes números

Desigualdad de Chebyshev

Teorema: La ley débil de los grandes números

2.7 Algunas variables aleatorias

discretas

1.  VARIABLES ALEATORIAS BINOMIALES o BERNOULLI

Supongamos que se realizan n ensayos independientes, cada uno de los cuales
produce un “éxito” con probabilidad p. Si X representa el número de éxitos que
ocurren en los n ensayos, entonces X es una variable aleatoria binomial con
parámetros (n. p). Su función de masa de probabilidad:

2.  VARIABLES ALEATORIAS POISSON

Se utilizan cuando se quiere saber el número de éxitos que ocurren en varios
experimentos independientes.

Tiene relación con la variable binomial

Dada la relación entre las variables aleatorias binomial y Poisson para una variable
aleatoria Poisson X con parámetro 𝝀:

3.  VARIABLES ALEATORIAS GEOMÉTRICAS

VAI que siguen una distribución de Poisson.
Se utiliza para saber la probabilidad de que después de varios experimentos
independientes se tenga un éxito. Para que ocurra un éxito en el experimento n,
deben ocurrir n-1 fracasos.

4.  VARIABLE ALEATORIA BINOMIAL NEGATIVA o PASCAL

5.  VARIABLES ALEATORIAS HIPERGEOMÉTRICAS

Una variable hipergeométrica se utiliza cuando se debe elegir un valor aleatorio dentro de
distintas categorías.

N es el número de elementos de una categoría

M es el número de elementos de otra categoría distinta,

n es el tamaño de la muestra

i es el número de elementos de la categoría que se elige

2.8 Variables aleatorias continuas

1.  VARIABLES ALEATORIAS UNIFORME

2.  VARIABLES ALEATORIAS NORMALES

3.  VARIABLES ALEATORIAS EXPONENCIALES

Es equivalente

3Números aleatorios

la capacidad de generar números aleatorios, que representan el valor de una variable aleatoria
distribuida uniformemente en (0, 1).

En general, los números aleatorios surgen de alguna fuente de aleatoriedad física
impredecible. Generar números pseudoaleatorios implica generar secuencias de números que
“parezcan” aleatorias (variable aleatoria IID).

Características de un buen generador de números aleatorios

−  Que no muestre ningún patrón o regularidad aparente desde un punto de vista

estadístico.

−  Que, dada una semilla inicial, se puedan generar muchos valores antes de repetir el

ciclo.

Método congruencial multiplicativo

Uno de los métodos más comunes para generar números pseudoaleatorios comienza con un
valor inicial x0, llamado semilla, y luego se calcula de manera recursiva los valores sucesivos
con n>=1,

a y m son enteros positivos dados y deben satisfacer tres criterios:

𝑋𝑛 = 𝑎.𝑋𝑛-1  𝑚𝑜𝑑 (𝑚)

1.  La sucesión resultante tiene la “apariencia” de ser una sucesión de variables aleatorias

independientes y uniformes en (0, 1).

2.  El número de variables que se pueden generar antes de que comience la repetición es

grande.

3.  Los valores se pueden calcular de manera eficiente en una computadora digital.

Generador congruencial lineal o mixto (GCL)

Tiene la forma:

Parámetros:

𝑋𝑛+1 = (𝑎.𝑋𝑛 + 𝐶) 𝑚𝑜𝑑 (𝑚)

•  Módulo: m (>0)
•  Multiplicador: a (0 < a < m)
•
Incremento: c (≤ X0 < m)
•  Semilla: X0 (0 ≤ X0 < m)

En cada iteración, el número aleatorio generado es:

Características importantes

•

La longitud del ciclo depende de m ya que el generador no puede producir más de
m elementos.

•  El tamaño de m influye en la velocidad del generador porque m muy grande puede

•

requerir mucha capacidad de cómputo.
La longitud del ciclo (p) se denomina período y cuando p = m el generador es de
“período completo”.

G.C.L. sea de período completo

•  M y c tienen que ser primos relativos (único divisor común --> 1)
•  Si q es un número primo que divide a m, también tiene que dividir a “a – 1”.
•  Si 4 divide a m, entonces también divide a “a – 1”.

ANÁLISIS DE RESULTADOS

muchas veces es necesario efectuar un número de corridas independientes y obtener un
intervalo de confianza sobre el cual, con cierto grado de seguridad, esté el verdadero valor de
la variable.

