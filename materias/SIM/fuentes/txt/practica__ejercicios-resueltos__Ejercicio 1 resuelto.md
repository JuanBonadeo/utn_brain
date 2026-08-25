Ejercicio 1 parte a)
Diagrama de desencadenamiento de eventos
Representa los eventos involucrados en el sistema y la secuencia de ocurrencia de los eventos entre
sí, es decir, qué evento cuya ocurrencia provoca que suceda otro evento, qué eventos se llaman a sí
mismos, qué evento inicia el sistema, etc.

Simulación

Si S=’D’

Si n>0

A

P

S: servidor
‘D’: Desocupado
n: tamaño de la cola

Eventos
A: Arribo
P: Partida

Variables exógenas
Son  las  variables  aleatorias  que  pertenecen  al  sistema  y  están  involucradas  en  los  eventos  que
ocurren  dentro  del  mismo.  De  estas  variables  se  debe  saber  su  distribución  y  medidas  (valor
esperado,  varianza)  para  la  construcción  o  elección  de  los  generadores.  En  este  caso  las  variables
son:

  Tiempo de arribo: Tiempo en que llegan los clientes al sistema.
  Tiempo de servicio: Tiempo que tarda el servidor en atender a un cliente

Variables endógenas
También  llamadas  de  respuesta  o  medidas  de  rendimiento,  son  las  medidas  que  se  desea  que  el
modelo de simulación emita como resultado de su ejecución, en este ejercicio son:

Tamaño promedio en el tiempo de la cola:

Utilización del servidor:

Demora promedio en el tiempo:

Variables de estado
Son variables internas del sistema y marcan el estado del mismo en un momento dado del mismo.
Participan en la generación de las variables endógenas:

T: tiempo total de la simulación (también indicado como Reloj al final de la simulación)
t :  tiempo
cli_at : cantidad de clientes atendidos en toda la simulación
q  :  Acumulada  de  las  áreas  de  la  cola  (también  q).  Es  la  suma  de  las  áreas  formadas  por  los
rectángulos en la gráfica del tamaño de cola en el tiempo en una corrida del programa.  Se calcula el
área  formada  con  altura  =  tamaño  de  la  cola  (n)  y  base=  tiempo  que  n  tuvo  un  valor  constante.
Cada vez que n cambia de valor (porque llega un cliente a la cola, o un cliente entra al servidor y se
va de la cola), se calcula el área antes de actualizar a n a su nuevo valor. La base se calcula entre el
tiempo “Ahora” (Reloj) y la última vez que n cambió de valor (TUE).

S. De Federico

               1

TqtqTtt0)(TbtbTtt0)(atclidatclidTtt_)_(0

b : Acumulada de las áreas de la utilización del servidor (también b). Las áreas están  formadas
por el rectángulo con altura 1 (servidor ocupado en la computadora) y base igual al tiempo en que
el estado del servidor estuvo constante.
d : Acumulada de las demoras. Se suman los tiempos de cada cliente que hizo cola desde que llega
a  la  misma  (el  momento  del  arribo  y  ver  que  el  servidor  está  ocupado  y  se  guarda  en  un  vecto
llamado “Tiempos de arribo”) hasta que entra al servidor.

Simulación

Otras variables de estado en el modelo
n : tamaño de la cola de clientes sin atender
S : estado del servidor [“D”: desocupado”O”: ocupado]
Reloj: tiempo de ocurrencia del evento que está corriendo actualmente.
TUE: Tiempo del último evento. Es el tiempo en que se hizo algún movimiento

Estructuras de datos involucradas
VTA: vector “Tiempos de Arribo” donde se guardan los tiempos de arribo al sistema e ingreso a la
cola porque el servidor está ocupado
LEV: Lista de eventos. En ella se coloca una fila por cada evento que exista dentro del sistema, y se
guarda  como  mínimo  la  hora  en  que  va  a  ocurrir  dicho  evento.  Esta  hora  se  va  actualizando  a
medida que se produce la corrida.

LEV del ejercicio 1

C
Arribo = A
Partida= P

Hora
10:55
10:59

       VTA

8:23
8:45
9:00
9:12
……

Nota importante:  como los algoritmos se presentan en pseudocódigo la sintaxis de las estructura se
reduce a solo su nombre, sin necesidad de mostrar el manejo de los subíndices o construcción de las
estructuras en sí.

Algoritmo
El algoritmo se divide en diferentes módulos, uno por cada evento que participa en el sistema, un
bloque llamado Principal,  en donde se concentran las llamadas a las diferentes rutinas, un módulo
llamado Tiempos que administra qué evento es llamado, y un módulo de salida llamado Informe

Principal
Inicialización

Mientras reloj <=Fin simulación

Tiempos
Si evento seleccionado =’A’ ir a Arribo

Sino ir a Partida

Fin Si

Fin mientras

Reporte

Tiempos
Buscar en la LEV el evento con menor tiempo de ocurrencia
Guardar en el Reloj este tiempo      Reloj = Tiempo en LEV

S. De Federico

               2

Simulación

Inicialización
Reloj=0
q=0
b=0
d=0
cli_at=0                  número de clientes atendidos
n=0                         número de clientes en cola
Generar tiempo de arribo   El Arribo es el evento que inicia el sistema (ver Diagrama de

          Desencadenamiento

Guardar en LEV(A, Tiempo de arribo)     el tiempo en que va a ocurrir el primer arribo se guarda en

         la LEV

Guardar en LEV(P, ∞)    la partida se pone en un nro muy grande (infinito) para que la rutina
     tiempos seleccione sí o sí al Arribo inicialmente

Crear vector de tiempos de arribo en  VTA=0
TUE=0           Tiempo de último evento es para ir acumulando las áreas

Arribo
Si S=’O’              Servidor está ocupado

Acumular área de la cola                       q = q + (Reloj-TUE) * n
Incrementar en 1 el nº de clientes en cola     n= n + 1
Guardar en VTA el reloj
Sino

S=’O’
TIOS= Reloj     Tiempo en que el servidor empieza a estar ocupado
cli_at = cli_at + 1      Aumenta en 1 la cantidad de clientes  atendidos, o sea que
                                    entraron al servidor
Generar Tiempo de servicio
Guardar en LEV (P, Reloj + tiempo de servicio)

Fin Si
Generar próximo arribo   El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A, Reloj + tiempo de próximo arribo)
Guardar TUE    Tiempo de último evento para el cálculo de la próxima área   TUE=Reloj

Partida
Si n=0

S=’D’
Acumular área del servidor                  b = b + (Reloj-TIOS)
Guardar en LEV (P, )
Sino

Acumular área de la cola                       q=q + (Reloj-TUE) *n
Decrementar en 1 el nº de clientes en cola     n= n-1 (el primero de la cola entra al

 Servidor)

Acumular la demora                              d=d + (Reloj – VTA (tiempo de ingreso de

cli_at = cli_at + 1
Generar Tiempo de servicio     el cliente que entró al servidor va a ser atendido
Guardar en LEV (P, Reloj + tiempo de servicio)

  ese cliente))

Fin Si
Guardar TUE        Tiempo de último evento para el cálculo de la próxima área

Reporte
Mostrar todas las medidas de rendimiento con las fórmulas tal como se describió más  arriba.

S. De Federico

               3

