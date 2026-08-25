Cola simple  SIN MEDIDAS DE RENDIMIENTO
Este modelo sirve para base de construcción de eventos del tipo arribo o partida en otros sistemas.
Lo que está escrito en este pseudocódigo base es lo necesario para que la simulación  corra. Según
las medidas de rendimiento que se necesitan y otras condiciones del sistema, se agregan más líneas
de codificación.
Diagrama de desencadenamiento de eventos

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

Variables de estado
Son variables internas del sistema y marcan el estado del mismo en un momento dado del mismo.
Participan en la generación de las variables endógenas:

T: tiempo total de la simulación (también indicado como Reloj al final de la simulación)
t :  tiempo

Otras variables de estado en el modelo
n : tamaño de la cola de clientes sin atender
S : estado del servidor [“D”: desocupado”O”: ocupado]
Reloj: tiempo de ocurrencia del evento que está corriendo actualmente.

Estructuras de datos involucradas
LEV: Lista de eventos. En ella se coloca una fila por cada evento que exista dentro del sistema, y se
guarda  como  mínimo  la  hora  en  que  va  a  ocurrir  dicho  evento.  Esta  hora  se  va  actualizando  a
medida que se produce la corrida.

LEV del ejercicio 1

Evento
Arribo = A
Partida= P

Hora
10:55
10:59

Nota importante:  como los algoritmos se presentan en pseudocódigo la sintaxis de la estructura se
reduce a solo su nombre, sin necesidad de mostrar el manejo de los subíndices o construcción de las
estructuras en sí.

Sara De Federico

               1

Algoritmo
El algoritmo se divide en diferentes módulos, uno por cada evento que participa en el sistema, un
bloque llamado Principal, en donde se concentran las llamadas a las diferentes rutinas, un módulo
llamado Tiempos que administra qué evento es llamado, y un módulo de salida llamado Informe
Principal
Inicialización

Simulación

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

Inicialización
Reloj=0
n=0                         número de clientes en cola
Generar tiempo de arribo   El Arribo es el evento que inicia el sistema (ver Diagrama de

          Desencadenamiento

Guardar en LEV(A, Tiempo de arribo)     el tiempo en que va a ocurrir el primer arribo se guarda en

Guardar en LEV(P, ∞)    la partida se pone en un nro muy grande (infinito) para que la rutina
     tiempos seleccione sí o sí al Arribo inicialmente

         la LEV

Arribo
Si S=’O’              Servidor está ocupado

Incrementar en 1 el nº de clientes en cola     n= n + 1
Sino

S=’O’
Generar Tiempo de servicio
Guardar en LEV (P, Reloj + tiempo de servicio)

Fin Si
Generar próximo arribo   El evento Arribo llama a sí mismo (ver Diagrama de Desencadenamiento)
Guardar en LEV (A, Reloj + tiempo de próximo arribo)

Partida
Si n=0

S=’D’
Guardar en LEV (P, )
Sino

Decrementar en 1 el nº de clientes en cola     n= n-1 (el primero de la cola entra al

Generar Tiempo de servicio     el cliente que entró al servidor va a ser atendido
Guardar en LEV (P, Reloj + tiempo de servicio)

 Servidor)

Fin Si
Reporte
Como no hay medidas de rendimiento no se muestra nada.

Sara De Federico

               2

