#PREGUNTA 1

    Describa los costos asociados a un modelo de simulación de
inventarios

    - I-.π: costo promedio mensual por ítems adeudados. donde π: costo
por ítem por mes de atraso en la entrega

    - I+.h: costo promedio mensual por ítems en existencia. donde h:costo
por item por mes de inventario

    - Costo de la orden: K + i.Z; donde K es el costo fijo, i es el costo
por unidad y Z es la cantidad de
unidades pedidas.

#PREGUNTA 2

    Enuncie y demuestre el Algoritmo de la Transformada Inversa para la
generación de variables aleatorias continuas y aplíquelo para generar una
variable aleatoria con distribución uniforme.

    Proposición: Sea U una variable aleatoria uniƒormeen (0. 1). Para
cualquier función de distribución continua E invertible, la variable
aleatoria X definida como
                    X = F^-1(U)

    tiene distribución F. [F^-1 se define como el valor de x tal que F(x)
= u.]

    Demostración: Sea FX la función de distribución de X = F^-1(U).
Entonces

                    Fx(x) = P{F(F^-1(U) <= F(x)}
                          = P{U <= F(x)}    pues F(F^-1(U)) = U
                          = F(x)            pues U es uniforme en (0,1).

    La proposición anterior muestra entonces que para generar una
variable aleatoria X a partir de la función de distribución continua F,
generamos un número aleatorio U y hacemos entonces X = F^-1(U).

#PREGUNTA 3

    Dada la fórmula de generación de números aleatorios xn = axn−1 modulo
m, explique cuáles son las condiciones deseables para a y m

    En general. las constantes a y m deben satisfacer tres criterios:

    1. Para cualquier semilla inicial, la sucesión resultante tiene la
“apariencia” de ser una sucesión de variables aleatorias independientes y
uniformes en (0, 1).

    2. Para cualquier semilla inicial, el número de variables que se
pueden generar

antes de que comience la repetición es grande.
    3. Los valores se pueden calcular de manera eficiente en una
computadora digital.

    Las condiciones deseables son que m sea un numero primo de tamaño
aproximado al tamaño de la palabra del sistema de simulacion, para una
palabra de tamaño 32 se suele elegir m = 2^31-1 y a = 7^5 = 16807.

#PREGUNTA 4

    Qué condiciones debe cumplir un proceso de Poisson homogéneo?

    (a) N(0) = 0.

    (b) El número de eventos que ocurren en intervalos de tiempo
distintos son independientes.
    (c) La distribución del número de eventos que ocurren en un intervalo
dado depende solamente de la longitud del intervalo y no de su posición.
    (d) y (e) establecen que en un pequeño
intervalo de longitud h, la probabilidad de que ocurra un evento es
aproximadamente
lambda.h, mientras que la probabilidad de dos o más es aproximadamente 0.

#PREGUNTA 5

    Desarrolle los siguientes pasos a) y b), en la realización de un
estudio de simulación:

a) la determinación de los escenarios para el análisis, b) la
documentación del modelo, sugerencias y conclusiones

     a) Tras validar el modelo es necesario acordar con el cliente los
escenarios que se quiere analizar. Una manera muy sencilla de
determinarlos consiste en utilizar un escenario pesimista, uno optimista
y uno intermedio para la variable de respuesta mas importante.
       Por su parte el analista tambien puede contribuir a la seleccion
de escenarios, sugiriendo aquellos que considere mas importantes.

     b) Una vez realizado el analisis de los resultados, es necesario
efectuar toda la documentacion del modelo. Esta documentacion es muy
importante, pues permitira el uso del modelo generado en caso de que se
requieran ajustes futuros. Tambien es importante incluir sugerencias
tanto del uso del modelo como sobre los resultados obtenidos, con el
proposito de realizar un reporte mas completo. Por ultimo, deberan
presentarse asimismo las conclusiones del proyecto de simulacion, a
partir de las cuales es posible obtener los reportes ejecutivos para la
presentacion final.

#PREGUNTA 6

    Cuál es la diferencia entre un modelo analítico y una simulación?

    Si el modelo es bastante simple, puede ser posible trabajar con sus
relaciones y cantidades para obtener una solución exacta y analítica.

    Pero algunas soluciones analíticas pueden llegar a ser
extraordinariamente complejas, requiriendo vastos recursos informáticos.
Si una solución analítica a un modelo matemático están disponibles y es
computacionalmente eficiente, generalmente es deseable estudiar el modelo
de esta manera en lugar de a través de un simulación. Sin embargo, muchos
sistemas son altamente complejos, lo que impide cualquier posibilidad de
una solución analítica. En este caso, se debe estudiar el modelo mediante
simulación, es decir, ejercitando numéricamente el modelo para las
entradas en cuestión para ver cómo afectan a las medidas de rendimiento
de la producción.

#PREGUNTA 7

    En un modelo de colas, establezca la relación matemática entre la
tasa de servicio (o número promedio de clientes atendidos por unidad de
tiempo), y estas dos medidas de rendimiento: Tiempo promedio de espera en
la cola - Tiempo promedio en el sistema. Exprese dicha relación
simbólicamente (señalando el significado de cada símbolo que utilice)

    W = Wq + (1/u)

    donde:

    u = tasa de servicio

    1/u = tiempo promedio de servicio por cliente

    Wq = tiempo promedio en cola

    W= tiempo promedio en el sistema

#PREGUNTA 8

    Explique y aplique el Método de la Transformada Inversa para generar
el valor de una variable aleatoria discreta X con la siguiente función de
masa de probabilidad: P(X=1) = 1/6, P(X=2) = 1/3, P(X=3) = 1/3, P(X=4) =
1/6 (observe que 1/6 + 1/3 + 1/3 + 1/6 = 1)

    Generamos U y hacemos lo siguiente:
    - Si U < 1/6 hacemos X = 1 y terminamos
    - Si U < 1/2 hacemos X = 2 y terminamos
    - Si U < 5/6 hacemos X = 3 y terminamos
    - En caso contrario, hacemos X = 4

    Después de generar un número aleatorio U determinamos el valor de X
hallando el intervalo (F(xj-1), F(xj)) en el que está U [o, de forma
equivalente, hallando la inversa de F( U)]. Es por esta razón que el
anterior se llama método de la transformada inversa discreta para generar
X.

#PREGUNTA 9

    Cuáles son las condiciones para un modelo M/M/1?

    1. Una poblacion de clientes infita.
    2. Un proceso de llegada en el que los clientes se presentan de
acuerdo con un proceso de Poisson con una tasa promedio de lambda
clientes por unidad de tiempo.
    3. Un proceso de colas que consiste en una sola linea de espera de
capacidad infinita, con una disciplina de colas PEPS.
    4. Un proceso de servicio que consiste en un solo servidor que
atiende a los clientes de acuerdo con una distribucion exponencial con un
promedio de u clientes por unidad de tiempo.

    Para que este sistema alcance una condicion de estado estable, la
tasa de servicio promedio u debe ser mayor que la tasa de llegadas
promedio lambda.

#PREGUNTA 10

    Enuncie la fórmula y explique bajo qué condiciones hablamos de una
variable aleatoria hipergeométrica   (pag 32 Ross)

    Consideremos una urna con N+M bolas, de las cuales N tienen color
claro y M color oscuro. Si se elige una nuestra de tamano n de manera
aleatoria (en el sentido de que cada subconjunto de tamano n tiene la
misma probabilidad de ser elegido), entoces X, el numero de bolas de
color claro elegidas, tiene la funcion de masa de probabilidad:

                                /N\/ M \
                                \i/\n-1/
                       P[X=i] = ----------
                                 /N-M\
                                 \ n /

#PREGUNTA 11

    Cual es la diferencia entre un modelo del sistema y un experimento
con el sistema real?

    Si es posible (y rentable) alterar el sistema físicamente y luego
déjelo operar bajo las nuevas condiciones, probablemente sea deseable
hacerlo, porque en este caso no hay duda sobre si lo que estudiamos es
relevante. Sin embargo, rara vez es factible hacer esto, porque tal
experiencia, generalmente sería demasiada costosa o demasiada perjudicial
para el sistema.
    Por estas razones, generalmente es necesario construir un modelo.
como una representación del sistema y estudiarlo como un sustituto del
sistema. Cuando se utiliza un modelo, siempre existe la pregunta de si
refleja con precisión el sistema a los efectos de las decisiones que
deben tomarse.

#PREGUNTA 12

    Explique la diferencia entre un proceso de Poisson homogeneo y uno no
homogeneo.

    Un proceso de Poisson homogeneo, a diferencia de uno no homogeneo,
cumple con la condicion llamada hipótesis de incremento estacionario,
esto es, que la distribucion del numero de eventos que ocurren en un
intervalo dado depende solamente de la longitud del intervalo y no de su
posicion.

#PREGUNTA 13

    Explique la formula y el concepto de variable aleatoria exponencial.
Para que usamos esta formula en un modelo de colas?

    Una variable aleatoria continua con funcion de de densidad de
probabilidad
                f(x)= lambda.e^(-lambda.x) , 0<x<infinito
    para cierta lambda>0 es una variable aleatoria exponencial con
parametro lambda.

    En un modelo de colas mm1 tanto los tiempos de arribo como los
tiempos de servicios siguen una distribucion exponencial.

#PREGUNTA 14

    Luego de la definicion del sistema bajo estudio y la generacon del
modelo de simulacion base, se debe efectuar: a) la recoleccion y el
analisis de datos, y b) la generacion del modelo preliminar. Desarrolle
los pasos a) y b) de un estudio de simulacion.

    a)Recoleccion y analisis de los datos: en este paso se recopila y
analiza la informacion estadistica necesaria para determinar las
distribuciones de probabilidad de cada una de las variables aleatorias
del modelo.

    b)Generacion del modelo preliminar: en esta etapa se integra toda la
informacion obtenida hasta el momento para lograr un modelo lo mas
cercano posible al sistema en estudio.

#PREGUNTA 15

    Dada una cola finita de tamaño n en un sistema de una cola y un
servidor. Como se calcula la probabilidad de que un cliente no pueda
entrar a la cola?(Denegacion de servicio)

    Para un sistema con una cola de tamaño finito n-1 y un servidor, la
capacidad maxima de dicho sistema es n, contando a un cliente en
servicio. Por lo tanto la probabilidad de denegacion de servicio Pd es
igual a la sumatoria de las probabilidades de que hayan mas de n clientes
en el sistema. Entonces
            Pd = Pn+1 + Pn+2 + Pn+3....
    O bien se podria restar a 1 la sumatoria de probabilidades de que
hayan entre 0 y n clientes en el sistema
            Pd = 1 - (P0+P1+P2+...+Pn)

#PREGUNTA 16

    En el modelo de simulacion de inventarios desarrollado en clase,
describa el significado, las formulas que los involucran, y como varian
en el tiempo los niveles de inventario: I(t), I^+(t) e I^-(t)

    I(t): nivel de inventario al momento t (puede ser positivo, negativo
o cero)
    I +(t): número de unidades que realmente están en existencia.
    I –(t): número de unidades demandadas y no entregadas, por falta de
stock.

    I- = [integral entre 0 y n de I-(t).dt] / n
    I+ = [integral entre 0 y n de I+(t).dt] / n

    I+.h: costo promedio mensual por items en existencia , h:costo por
item por mes de inventario
    I-.π: costo promedio mensual por ítems adeudados ,     π: costo por
ítem por mes de atraso en la entrega.

