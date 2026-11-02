# Modelado de Simulación y Análisis - Averill M. Law

## Capítulo 1 - Modelado de Simulación Básico

### 1.1 Naturaleza de la Simulación

La **simulación** consiste en el uso de computadoras para imitar el funcionamiento de sistemas o procesos reales. Para estudiarlos científicamente se construyen **modelos**, basados en relaciones matemáticas o lógicas, que representan el comportamiento del sistema.

A pesar de su utilidad, enfrenta algunos **impedimentos**:

* Complejidad de los modelos (programación extensa y difícil).
* Alto costo y tiempo computacional (ha disminuido gracias a la tecnología).
* Percepción errónea de que la simulación es solo programar y correr un modelo una vez, sin un análisis riguroso.

Estas limitaciones resaltan la importancia de una **metodología** adecuada, que asegure conclusiones válidas a partir de los modelos simulados.![](imagen)

### 1.2 Sistemas, Modelos y Simulación

Un **sistema** es un conjunto de entidades que interactúan para alcanzar un objetivo. En la práctica, la definición del sistema depende de los objetivos del estudio.

El **estado** de un sistema se describe mediante la colección de variables necesarias para describir el sistema en un determinado momento.

Los sistemas se **clasifican** en:

* **Discretos**: las variables de estado cambian en momentos específicos (cliente llega o se va).
* **Continuos**: las variables de estado cambian de manera continua en el tiempo (posición y velocidad de avión).

En la práctica, pocos sistemas son completamente discretos o continuos, pero suele haber un tipo predominante que permite clasificarlos.

En el gráfico se pueden ver diferentes **formas** en las que se puede **estudiar un sistema**:

* **Experimentar con Sistema Real**: ideal si es posible y no resulta costoso ni riesgoso, aunque rara vez lo es.
* **Experimentar con Modelo del Sistema**: más habitual, evita costos o interrupciones. Siempre está la pregunta si el modelo refleja correctamente el sistema.
* **Modelos Físicos**: representaciones tangibles, como maquetas o simuladores. Son poco comunes en investigación de operaciones o análisis de sistemas.
* **Modelos Matemáticos**: representaciones mediante relaciones lógicas o cuantitativas, que luego son manipulados para ver cómo el sistema reacciona. Son los más usados.
* **Solución Analítica**: se obtiene una respuesta exacta a partir de fórmulas. Es útil si el modelo es simple. En caso de poder resolverlo de esta manera, hacerlo.
* **Simulación**: necesaria cuando los modelos son demasiado complejos y no permiten solución analítica. Ejercitar el modelo para las entradas en cuestión para ver cómo afectan la salida.

Para estudiar un **modelo de simulación** es útil **clasificarlo** en tres dimensiones:

* **Estáticos**: representan un sistema en un instante.
* **Dinámicos**: representan la evolución del sistema en el tiempo.
* **Determinísticos**: no incluyen componentes probabilísticos, como variables aleatorias, los resultados se determinan sólo con los datos de entrada.
* **Estocásticos**: incorporan aleatoriedad, por lo que los resultados son estimaciones y esa es la principal desventaja (modelos de colas, inventarios).
* **Continuos**: describen cambios con ecuaciones diferenciales (flujo de tráfico).
* **Discretos**: se enfocan en eventos puntuales (autos individuales en la autopista).

***Nota***: un modelo discreto no siempre se usa para modelar un sistema discreto, y viceversa. La decisión de utilizar un modelo continuo o discreto depende de los objetivos del estudio.

### 1.3 Simulación de Eventos Discretos

La **simulación de eventos discretos** consiste en modelar un sistema que evoluciona en el tiempo mediante una representación en la cual las variables de estado cambian en instantes separados en el tiempo (solamente en un número contable de momentos en el tiempo).

**Evento**: suceso instantáneo que puede (o no) modificar el estado del sistema.

***Ejemplo***: sistema con un solo servidor (barbería o mesa de información)

**Objetivo**: estimar el tiempo promedio de espera en la cola (intervalo desde el instante que llega hasta que es atendido)

**Variables de estado**:

* **Estado del servidor** (ocupado o libre): permite determinar si, al llegar un cliente, puede ser atendido inmediatamente o no.
* **Número de clientes en la cola**: se usa para decidir si, al finalizar un servicio, el servidor queda libre o atiende al siguiente cliente en espera.
* **Tiempos de arribo de los clientes en cola**: permiten calcular la demora (tiempo de inicio de servicio - tiempo de arribo).

**Eventos**:

* **Llegada de un cliente**: puede hacer que el servidor pase de libre a ocupado, o que aumente la cola en 1.
* **Salida** (fin del servicio): puede hacer que el servidor pase de ocupado a libre, o que disminuya la cola en 1.

En el ejemplo, ambos eventos cambian el estado del sistema, pero en algunas simulaciones de eventos discretos no siempre ocurre. Un **evento** también puede servir para finalizar la simulación en un instante dado o programar decisiones en determinados momentos.

### 1.3.1 Mecanismos de Avance de Tiempo

En un modelo de **simulación de eventos discretos**, como los estados cambian en el tiempo, es necesario llevar el registro del tiempo simulado, se hace con la variable **reloj de simulación**. El tiempo simulado no está relacionado con el tiempo real que tarda la computadora en correr la simulación.

También se necesita un método para **avanzar el reloj** de un valor a otro:

* **Siguiente Evento**: es el más utilizado en la mayoría del software de simulación. El reloj comienza en cero y se calculan los tiempos de los eventos futuros. El reloj se avanza hasta el evento más próximo, actualizando el estado del sistema y recalculando los tiempos futuros. Este proceso continúa hasta que se cumpla una condición de parada preestablecida. Los periodos de inactividad se omiten, lo que hace a la simulación más eficiente. Los saltos del reloj no siempre son iguales en tamaño.
* **Incremento Fijo**: caso especial del anterior. No omite los periodos de inactividad, lo que puede consumir más tiempo de cómputo. El tiempo avanza en intervalos iguales.

***Ejemplo***: método de siguiente evento para un sistema de un solo servidor (cola)

*ti* = tiempo de arribo del cliente *i* (*t0* = 0)

*Ai* = *ti* - *ti - 1* = tiempo entre arribos entre el cliente *i - 1* e *i*

*Si* = tiempo de servicio del cliente *i*

*Di* = tiempo en cola del cliente *i*

*ci* = *ti* + *Di* + *Si* = tiempo en el que el cliente *i* completa su servicio y se va

*ei* = tiempo de ocurrencia del evento *i* (valor que toma el reloj en ese evento)

Cada una de estas variables generalmente será aleatoria. Se asume que los tiempos entre arribos *A1* , *A2* , … y los tiempos de servicio *S1* , S*2* , … son conocidos y tienen funciones de distribución acumuladas *FA* y *FS* respectivamente.

1. **Inicio**. En *e0* = 0, el servidor está inactivo. El primer tiempo de llegada *t1* se obtiene generando *A1* de *FA* y sumándolo a 0. El reloj avanza de *e0* al tiempo del siguiente evento *e1* = *t1 .*
2. **Primera Llegada**. Primer cliente llega en *t1* . Como el servidor está inactivo, comienza a ser atendido inmediatamente (*D1* = 0) y el servidor pasa a ocupado. El tiempo en que este cliente termina el servicio *c1* se calcula como *S1* + *t1* , *S1* generado de *FS* .
3. **Segunda Llegada**. Segundo cliente llega en *t2* = *t1* + *A2* . Si *t2* < *c1* , el reloj avanza de *e1* a *e2* = *t2* . Dado que el servidor está ocupado, el número de clientes en cola pasa de 0 a 1. No se genera el tiempo de servicio *S2* en este momento.
4. **Tercera Llegada**. El tiempo de llegada del tercer cliente va a ser *t3* = *t2* + *A3 .*
5. **Cambio de eventos**. Si *c1* < *t3* , el reloj avanza de *e2* a *e3* = *c1* . En ese instante, el primer cliente termina el servicio y se va, el segundo cliente comienza su servicio, y se calcula su retraso en la cola *D2* = *c1* - *t2* y su tiempo de salida *c2* = *c1* + *S2* . El número de clientes en la cola se reduce en 1.
6. **Fin**. La simulación puede terminar cuando se alcanza un número específico de observaciones de retrasos de los clientes.

![](imagen)

### 1.3.2 Componentes de un Modelo de Simulación de Eventos Discretos

En los modelos que usan el **método de avance por siguiente evento**, suelen aparecer los siguientes elementos:

* **Estado del Sistema**: conjunto de variables necesarias para describir el sistema en un tiempo determinado.
* **Reloj de Simulación**: variable que indica el valor actual del tiempo simulado.
* **Lista de Eventos**: lista que contiene el próximo tiempo en que ocurrirá cada tipo de evento.
* **Contadores Estadísticos**: variables que almacenan información sobre el desempeño del sistema.
* **Rutina de Inicialización**: subprograma que inicializa la simulación en tiempo 0.
* **Rutina de Temporización**: subprograma que determina el siguiente evento de la lista y avanza el reloj hacia el tiempo en el que ocurre.
* **Rutinas de Eventos**: subprograma que actualiza el estado del sistema cuando ocurre un tipo de evento determinado (hay una rutina de evento para cada tipo de evento).
* **Rutinas de Librería**: conjunto de subprogramas usados para generar observaciones aleatorias a partir de distribuciones de probabilidad definidas en el modelo.
* **Generador de Reportes**: subprograma que calcula estimaciones de desempeño y produce un reporte al finalizar la simulación.
* **Programa Principal**: subprograma que invoca la rutina de temporización para determinar el próximo evento y transfiere el control a la rutina correspondiente. Además, revisa la finalización de la simulación e invoca el generador de reportes.

El **flujo de control** con el método del **siguiente evento**.

1. **Programa Principal**.

* Invoca a la rutina de inicialización.

1. **Rutina de Inicialización**.

* Se pone en 0 el reloj de la simulación.
* Inicializa el estado del sistema y los contadores estadísticos.
* Inicializa la lista de eventos.

1. **Programa Principal** (Repetidamente)

* Invoca a la rutina de temporización.

**Rutina de Temporización**.

* Determina el siguiente tipo de evento, *i.*
* Avanza el reloj de la simulación.
* Invoca la rutina de evento *i*.

**Rutina de Evento *i***.

* Actualiza el estado del sistema.
* Actualiza los contadores estadísticos.
* Genera futuros eventos y los agrega a la lista de eventos

Cuando finaliza la simulación:

1. **Generador de Reportes**.

* Calcula las estimaciones de interés.
* Escribe el reporte.

![](imagen)

## 1.4 Simulación de un Sistema de Cola con un Solo Servidor

### 1.4.1 Planteo del Problema

![](imagen)

* Consideremos un **sistema de colas** con un **solo servidor**:
* **Tiempos entre Arribos**: *A1* , *A2* , … son variables aleatorias independientes e idénticamente distribuidas (IID).
* **Tiempos de Servicio**: *S1* , S*2* , … son IID y son independientes de los arribos.

**IID**: significa que tienen la misma distribución probabilística.

* Un cliente que llega y encuentra el servidor libre entra en servicio inmediatamente. Si está ocupado, se une al final de la cola FIFO (primero en entrar, primero en salir).
* La simulación comienza en estado vacío e inactivo (sin clientes y con el servidor libre).
* El primer arribo ocurre después del primer tiempo entre arribos *A1 .*
* La simulación se ejecuta hasta que *n* clientes hayan completado su demora en cola y entren en servicio.
* El tiempo de fin es una variable aleatoria, depende de los arribos y tiempos de servicio.

Para **medir el desempeño** del sistema, miramos los estimados de tres cantidades:

* *d*(*n*) **tiempo promedio en cola**: promedio del tiempo que los *n* clientes esperaron en la cola antes de ser atendidos. Depende de los valores aleatorios de llegadas y servicios, es una variable aleatoria. Lo que se busca es su valor esperado, el promedio teórico si se repitiera el experimento muchas veces.
   donde *Di* es el tiempo de espera en cola del cliente *i*.

No se excluyen en el promedio los valores *D* = 0, cuando llega y encuentra el sistema vacío, ayuda a reflejar el buen desempeño del sistema.

* *q*(*n*) **número promedio de clientes en cola**: es el promedio del número de clientes esperando en la cola durante el tiempo que duró la simulación (hasta que *n* clientes fueron atendidos). A diferencia de *d*(*n*), que es un promedio por cliente, *q*(*n*) es un promedio en el tiempo. Para definirlo:
* *Q*(*t*): número de clientes en la cola en el tiempo *t* (*t* ≥ 0).
* *T*(*n*): tiempo total para que *n* clientes completen sus demoras en cola.
* *pi* : proporción de tiempo que hubo *i* clientes en la cola.

promedio ponderado, se puede estimar observando su simulación

donde *Ti* es el tiempo total en el cual hubo *i* clientes en cola

* *u*(*n*) **utilización esperada del servidor**: proporción esperada de tiempo, entre 0 y *T*(*n*), en la que el servidor está ocupado, no inactivo. Su valor está entre 0 y 1.

Definimos la función de ocupación

![](imagen)

Entonces es la proporción de tiempo en que *B*(*t*) = 1.

Utilización cercana al 100%, significa colas largas y posibles cuello de botella. Mientras que la utilización baja conlleva un exceso de capacidad, recursos no aprovechados.

***Ejemplo***: trayectoria temporal de *Q*(*t*) en este sistema para el caso *n* = 6.

* **Llegadas**: ocurren en los tiempos 0.4, 1.6, 2.1, 3.8, 4.0, 5.6, 5.8 y 7.2.
* **Salidas**: ocurren en los tiempos 2.4, 3.1, 3.3, 4.9 y 8.6.
* La simulación termina en *T*(6) = 8.6.

Para calcular , primero se obtienen los tiempos *Ti* , que representan cuánto tiempo la cola tuvo longitud *i*. Sumar todos los tiempos en los que la cola fue de *i* (ver gráfico).

*T0* = (1.6 - 0.0) + (4.0 - 3.1) + (5.6 - 4.9) = 3.2

*T1* = (2.1 - 1.6) + (3.1 - 2.4) + (4.9 - 4.0) + (5.8 - 5.6) = 2.3

*T2* = (2.4 - 2.1) + (7.2 - 5.8) = 1.7

*T3* = (8.6 - 7.2) = 1.4

*Ti* = 0 para todo *i* ≥ 4

La suma ponderada es

Entonces

![](imagen)

Podemos observar, la suma es el área bajo la curva *Q*(*t*) desde el inicio al fin de la simulación. entonces

***Ejemplo***: sistema para el caso *n* = 6.

Mirando el gráfico calculamos el tiempo en el que el servidor estuvo ocupado:

(3.3 - 0.4) + (8.6 -3.8) = 7.7

Entonces la utilización del servidor es

Podemos observar que se puede representar con la integral .

![](imagen)

***Ejemplo***: sistema de cola de un solo servidor.

* **Tiempos entre arribos**: *A1* = 0.4, *A2* = 1.2 , *A3* = 0.5 , *A4* = 1.7 , *A5* = 0.2, *A6* = 1.6, *A7* = 0.2 , *A8* = 1.4, *A9* = 1.9, …
* **Tiempos de servicio**: *S1* = 2.0, *S2* = 0.7, *S3* = 0.2, *S4* = 1.1, *S5* = 3.7, *S6* = 0.6, …

***t* = 0, inicialización**.

* El reloj se inicia en *t* = 0.
* El servidor está libre (estado = 0) y la cola se encuentra vacía.
* Todos los contadores estadísticos comienzan en 0.
* La siguiente llegada *A* queda programada en 0 + *A1* = 0.4.
* La siguiente salida aún no existe, por lo que se fija en ∞.
* Al ser el inicio, no hay área acumulada todavía *Q*(*t*) = 0 y *B*(*t*) = 0.

![](imagen)

***t* = 0.4, llegada del primer cliente**.

* Encuentra el servidor vacío (estado = 0), por lo que entra directamente al servicio.
* Su demora en cola es *D1* = 0, se actualiza la cantidad de tiempos en colas completados a 1 y el tiempo total en cola a 0.
* El servidor cambia a ocupado (estado = 1).
* La siguiente llegada se programa en 0.4 + *A2* = 1.6.
* La siguiente salida será cuando el cliente termine su servicio 0.4 + *S1* = 2.4.
* *B*(*t*) = 0 x (0.4 - 0) = 0
* *Q*(*t*) = 0 x (0.4 - 0) = 0

![](imagen)

***t* = 1.6, llegada del segundo cliente.**

* Encuentra el servidor ocupado (estado = 1), por lo que debe esperar en la primera posición de la cola. El número en cola aumenta a 1 y se guarda su tiempo de arribo.
* La siguiente llegada queda programada en 1.6 + *A3* = 2.1.
* La siguiente salida sigue siendo la del cliente 1 en *t* = 2.4.
* Como ningún cliente sale de la cola en este instante, la cantidad de tiempos en colas completados y el tiempo total en cola no cambian.
* *B*(*t*) = 0 x 0.4 + (1.6 - 0.4) x 1 = 1.2
* *Q*(*t*) = 0 x 1.6 = 0

![](imagen)

**t = 2.1, llegada del tercer cliente**.

* Encuentra el servidor ocupado (estado = 1), por lo que entra en la cola. El número en cola aumenta a 2, y se guarda su tiempo de arribo.
* La siguiente llegada queda programada en 2.1 + *A4* = 3.8.
* La siguiente salida sigue siendo la del cliente 1 en *t* = 2.4.
* Como ningún cliente sale de la cola en este instante, la cantidad de tiempos en colas completados y el tiempo total en cola no cambian.
* *B*(*t*) = 0 x (0.4 - 0) + 1 x (2.1 - 0.4) = 1.7
* *Q*(*t*) = 0 x (1.6 - 0) + 1 x (2.1 - 1.6) = 0.5

![](imagen)

**t = 2.4, salida del primer cliente**.

* Como hay clientes esperando, el servidor toma al cliente 2 de la cola y comienza a atenderlo inmediatamente. El número en cola disminuye a 1 (queda el cliente 3).
* Se calcula su demora en cola: *D*2 = 2.4 − 1.6 = 0.8.
* Se actualizan la cantidad de tiempos en colas completados = 2 y el tiempo total en cola = 0 + 0.8 = 0.8.
* La siguiente salida pasa a ser el fin de servicio del cliente 2, en 2.4 +*S2* = 3.1.
* *B*(*t*) = 0 x (0.4 - 0) + 1 x (2.4 - 0.4) = 2
* *Q*(*t*) = 0 x (1.6 - 0) + 1 x (2.1 - 1.6) + 2 x (2.4 - 2.1) = 1.1

![](imagen)

### 1.4.3 Organización y Lógica del Programa

**Evento de Llegada**

1. Programar el siguiente evento de llegada.
2. ¿El servidor está ocupado?

* **Sí**:

1. Agregar 1 al número en cola.
2. Está la cola llena?

* **Sí**: Escribir mensaje de error y detener la simulación.
* **No**: Guardar la hora de llegada de ese cliente.
* **No**:

1. Fijar el tiempo en cola = 0 para este cliente y recopilar estadísticas.
2. Incremenentar en 1 el número de clientes que completaron la cola.
3. Poner el servidor en estado ocupado.
4. Programar un evento de salida para este cliente.
5. Retorna.

**Evento de Salida**

1. ¿Está la cola vacía?

* **Sí**:

1. Poner el servidor en estado inactivo.
2. Eliminar el evento de salida de consideración.

* **No**:

1. Restar 1 al número de clientes en cola.
2. Calcular el tiempo en cola del cliente que entra en servicio y recopilar estadísticas.
3. Incrementar en 1 el número de clientes que completaron tiempo en cola.
4. Programar un evento de salida para este cliente.
5. Mover cada cliente en cola, si hay, un lugar hacia delante.
6. Retorna.

## 1.5 Simulación de un Modelo de Inventarios

### 1.5.1 Planteo del Problema

En estos problemas buscamos comparar diferentes **políticas de pedido** (ordering policies). Consideramos que una empresa vende un solo producto y su **objetivo** es decidir cuántos ítems tener en inventario durante los próximos *n* meses.

* **Tiempo entre Demandas**: son variables aleatorias independientes e idénticamente distribuidas (IID), con distribución exponencial y una media de 0.1 meses.
* **Tamaño de la Demanda** (*D*): también es una variable aleatoria IID (independiente del momento en que ocurre la demanda), con la siguiente distribución:

wp es la probabilidad ![](imagen)

Al comienzo de cada mes, la empresa revisa su nivel de inventario y decide cuántos artículos pedir al proveedor. Si la empresa pide *Z* artículos, incurre en un costo de *K* + *iZ*, donde *K* es el

costo fijo de pedido e *i* es el costo por artículo pedido. Si *Z* = 0, no se incurre en ningún costo.

Cuando se hace una orden, tenemos un **Tiempo de Entrega** (lead time), que es una variable aleatoria uniforme entre 0.5 y 1 mes. La empresa utiliza un **Política de Reordenamiento** (*s*, *S*) para decidir cuánto pedir:

![](imagen)

Donde *I* es el nivel de inventario al comienzo del mes.

Si hay suficiente inventario, la demanda se satisface de inmediato. Si la demanda supera el inventario disponible, la demanda excedente se pone en espera (**backlog**) y se cubre con futuras entregas. Esto puede hacer que el inventario sea negativo.

Cuando llega un pedido, se utiliza primero para cubrir cualquier backlog y luego el resto (si queda) se agrega al inventario.

Además del **costo de pedido**, el sistema de inventario también incurre en:

* *h* **Costo de Almacenamiento** (holding cost): incluye alquiler del almacén, seguros, impuestos, mantenimiento y el costo de oportunidad del capital inmovilizado.
* *p* **Costo por Faltantes** (shortage cost): representa costos administrativos y pérdida de buena voluntad de los clientes.

*I*(*t*): nivel de inventario en el instante *t* (puede ser positivo, cero o negativo).

* *I +*(*t*) = max{*I*(*t*), 0} artículos en existencia física en el tiempo *t*
* *I -* (*t*) = max{-*I*(*t*), 0} cantidad en backlog en el tiempo *t*

El **número promedio** (por mes) de **artículos almacenados** en el inventario durante el período de *n* meses es:

por lo que el **costo promedio de almacenamiento** por mes es *h*  ​

El **número promedio de artículos en retraso** es

por lo que el **costo promedio de retraso** es π

![](imagen)

Resumen de costos asociados a un modelo de simulación de inventarios

* **Costo por pedido:** Cp = *K* + *iZ*.
* **Costo de Almacenamiento** **(h)** o costo de mantenimiento de ítems por mes de inventario.
* **Costo de por faltante (p o ℼ)** o costo por ítem por mes de atraso en la entrega.
* **Costo promedio de almacenamiento:**  ⇒
* **Costo promedio de retraso:** ⇒

### 1.5.2 Organización y Lógica del Programa

**Evento de Llegada de Pedido**

1. Incrementar el nivel de inventario en la cantidad previamente pedida.
2. Eliminar el evento de llegada de pedido de la consideración.
3. Retornar.

**Evento de Demanda**

1. Generar el tamaño de esta demanda.
2. Disminuir el nivel de inventario en ese tamaño de demanda.
3. Programar el siguiente evento de demanda.
4. Retornar.

**Evento de Evaluación de Inventario**

1. Evaluar *I*(*t*) < *s*

* En caso que **sí**:

1. Determinar la cantidad a pedir [*S - I*(*t*)].
2. Incluir el costo de pedido y recopilar estadísticas.
3. Programar el evento de llegada de pedido para esta orden.
4. Programar el siguiente evento de evaluación de inventario.
5. Retornar.

**Actualizar Acumuladores Estadísticos de Tiempo Promedio**

1. Fue *I*(*t*) durante el intervalo anterior: negativo, cero o positivo?

* **Negativo**:

1. Actualiza el área debajo de *I -* (*t*)

* **Positivo**:

1. Actualiza el área debajo de *I +* (*t*)
2. Retorna.

## 1.7 Pasos en una Simulación

1. **Formular el problema y planificar el estudio**
2. El problema es planteado por el gerente, pero puede no estar bien definido. Puede ser un proceso iterativo.
3. Reuniones iniciales con gerente, analistas y expertos (SMEs) para definir:

* Objetivos generales y preguntas específicas
* Métricas de desempeño
* Alcance del modelo y configuraciones del sistema a modelar
* Cronograma y recursos necesarios

1. Seleccionar software de simulación.
2. **Recopilar datos y definir el modelo**
3. Reunir información sobre la estructura y operación del sistema:

* Ninguna persona o documento por sí solo es suficiente
* Puede haber información errónea, identificar a los verdaderos expertos
* Los procedimientos pueden no estar formalizados

1. Obtener datos para parámetros del modelo y distribuciones de probabilidad.
2. Redactar un documento de supuestos que detalle datos y estructuras.
3. Si es posible, recopilar datos del sistema actual para futura validación.
4. Elegir nivel de detalle del modelo considerando:

* Objetivos y métricas
* Disponibilidad de datos
* Credibilidad
* Opiniones de los expertos
* Limitaciones técnicas y recursos

1. No debe haber una correspondencia uno a uno entre cada elemento del modelo y cada elemento del sistema.
2. Empezar con un modelo simple y aumentarlo si es necesario.
3. Mantener interacción constante con los responsables del proyecto.
4. **Validar el documento de supuestos**
5. Revisión estructurada del documento ante gerentes, analistas y expertos:

* Asegura la corrección y completitud.
* Fomenta participación y apropiación del modelo.
* Debe realizarse antes de programar para evitar reprocesos.

1. **Construir y verificar el programa**
2. Programar el modelo en lenguaje o software de simulación.
3. Verificar el programa (debugging), asegurar que corre correctamente.
4. **Realizar corridas piloto**
5. Ejecuciones preliminares para preparar la validación del modelo.
6. **Validar el modelo programado**
7. Si existe un sistema real, comparar resultados del modelo con los datos reales.
8. Revisión del modelo por parte de analistas y expertos.
9. Realizar análisis de sensibilidad para identificar factores críticos del modelo.
10. **Diseñar experimentos**
11. Definir para cada configuración:

* Duración de la simulación
* Periodo de calentamiento (si aplica)
* Número de repeticiones independientes (diferentes números aleatorios).

1. **Realizar corridas de producción**
2. Corridas completas del modelo para análisis formal.
3. **Analizar los datos de salida**
4. Evaluar desempeño absoluto de configuraciones del sistema y la comparación relativa entre configuraciones alternativas.
5. **Documentar, presentar y utilizar resultados**
6. Documentar supuestos, programa, resultados.
7. Presentar resultados:

* Usar animaciones para comunicar a audiencias no técnicas.
* Explicar el proceso de modelado y validación para ganar credibilidad.
* Usar resultados en la toma de decisiones, si son válidos y creíbles.

## 1.8 Ventajas, Desventajas y Riesgos de la Simulación

**Ventajas**

* Permite representar sistemas complejos del mundo real con elementos estocásticos que no se pueden modelar correctamente con modelos matemáticos o analíticos.
* Permite estimar el desempeño de un sistema bajo diferentes condiciones operativas.
* Comparar diseños o políticas operativas para ver cuál cumple mejor con los requisitos.
* Control mucho mayor sobre las condiciones experimentales que en pruebas reales.
* Permite un horizonte temporal largo en un tiempo comprimido o estudiar detalles en tiempo expandido.

**Desventajas**

* Cada simulación produce estimaciones, se requieren varias corridas independientes para obtener resultados confiables.
* No es tan eficaz para optimización como un modelo analítico válido.
* Suelen ser costosos y requieren mucho tiempo para desarrollarse.
* Riesgo de exceso de confianza en resultados aunque el modelo no sea una representación válida.

En algunos estudios, tanto la simulación como los modelos analíticos pueden ser útiles:

* La simulación verifica la validez de los supuestos necesarios en un modelo analítico.
* Un modelo analítico sugiere alternativas para investigar en un estudio de simulación.

**Riesgos** que pueden afectar el éxito de un estudio de simulación:

* **Planificación y Comunicación**:
* Objetivos mal definidos al inicio.
* Nivel inapropiado de detalle del modelo.
* No involucrar a todo el equipo del proyecto desde el principio.
* Falta de comunicación con la gerencia.
* **Conocimiento y Enfoque**:
* Tratar el estudio como solo programación.
* Falta de personal con conocimiento en simulación y estadística.
* No recopilar buenos datos del sistema real.
* **Software y Herramientas**:
* Uso de software inapropiado o con macros poco documentadas.
* Creer que un software fácil no requiere conocimiento técnico.
* Mal uso de la animación.
* **Datos y Aleatoriedad**:
* No considerar correctamente las fuentes de aleatoriedad del sistema real.
* Usar distribuciones arbitrarias (normal, uniforme, triangular) como entradas.
* No establecer un período de calentamiento para el estado estable.
* **Análisis y Resultados**:
* Basar el análisis en una sola corrida o replicación.
* Comparar diseños con una sola replicación por diseño.
* Medidas de desempeño incorrectas.

## Apéndice 1A. Avance de Tiempo en Incrementos Fijos

El otro enfoque para avanzar un reloj en una simulación de eventos discretos es por **incrementos fijos**, donde se avanza el reloj en exactamente Δ*t* unidades de tiempo.

Después de cada actualización del reloj, se revisa si algún evento ocurrió durante ese intervalo. Si había eventos programados, se considera que ocurrieron al final del intervalo.

Como varios eventos pueden considerarse simultáneos, es necesario definir reglas para determinar el orden en que se procesan.

Las principales **desventajas** son:

* Introduce errores al procesar eventos al final del intervalo en el que ocurren.
* Necesidad de decidir qué evento procesar primero cuando eventos que no son simultáneos se tratan como simultáneos.

Se pueden solucionar eligiendo un Δ*t* más chico, pero esto aumenta el número de revisiones y el tiempo de ejecución. Por esto, no se suele usar el método de avance de tiempo para modelos donde los tiempos entre eventos varían mucho.

El principal **uso** es para sistemas donde los eventos ocurren en tiempos múltiplos *n* Δ*t* . Por ejemplo, si los datos sólo están disponibles anualmente.

![](imagen)

## Apéndice 1B. Introducción a los Sistemas de Colas

Un **sistema de colas** consiste en uno o más servidores que brindan servicio a clientes que llegan. Los clientes que al llegar encuentran todos los servidores ocupados, se unen a una o más colas en frente de los servidores.

### 1B.1 Componentes de un Sistema de Colas

Un **sistema de colas** se caracteriza por tres **componentes**:

* **Proceso de Llegada**: describe cómo los clientes llegan al sistema. Si los tiempos de arribos *A1* , *A2* , … son variables aleatorias IID, el **tiempo promedio** (o esperado) **entre llegadas** es *E*(*A*) y la **tasa de llegada** de clientes .
* **Mecanismo de Servicio**: se define especificando el número de servidores *s*, si hay una cola para cada servidor o una única cola para todos, y la distribución de probabilidad de los tiempos de servicio de los clientes. Si *S1* , *S2* … son variables aleatorias IID, el **tiempo promedio de servicio** es *E*(*S*) y la **tasa de servicio** de un servidor
* **Disciplina de la Cola**: regla que determina qué cliente de la cola (si hay) se atiende cuando un servidor queda libre. Las más utilizadas son:
* **FIFO**: primero en entrar, primero en salir.
* **LIFO**: último en entrar, primero en salir.
* **Prioridad**: según importancia o requerimientos de servicio.

### 1B.2 Notación para Sistemas de Colas

Algunos sistemas de colas son tan comunes en la práctica que se han desarrollado notaciones estándar. Por ejemplo, consideremos un sistema con:

* *s* servidores en paralelo con una cola FIFO que los alimenta.
* *A1* , *A2* , … son variables aleatorias IID
* *S1* , *S2* … son variables aleatorias IID
* Los *Ai* y *Si* son independientes

A este sistema se lo llama *GI*/*G*/*s* donde:

* *GI* (general independent): distribución de los tiempos entre arribos *Ai*
* *G* (general): distribución de los tiempos de servicio *Si*

Si se conocen las distribuciones específicas, se usan los símbolos en lugar de *GI* y *G*

* *M*: distribución exponencial
* *Ek* : distribución k-Erlang
* *D*: tiempos determinísticos o constantes

Un sistema de un solo servidor con tiempos exponenciales entre llegadas y de servicio, y disciplina FIFO, se denomina *M*/*M*/*1*.

Para cualquier *GI*/*G*/*s* definimos el **factor de utilización** del sistema se define como: donde es la tasa de arribos y es la tasa de servicio del sistema cuando todos los servidores están ocupados. Mide qué tan intensamente se utilizan los recursos del sistema.

### 1B.3 Medidas de Desempeño de un Sistema de Colas

Hay muchas **medidas de desempeño** para los sistemas de colas, las más comunes:

* *Di* = tiempo que el cliente *i* pasó en cola
* *Wi* = *Di* + *Si* = tiempo de espera en el sistema del cliente *i*
* *Q*(*t*) = número de clientes en cola en el tiempo *t*
* *L*(*t*) = número de clientes en el sistema en el tiempo *t* [*Q*(*t*) + número de clientes en servicio]
* = demora promedio en estado estacionario
* = tiempo de espera promedio en estado estacionario.

Para sistemas de colas donde estas medidas existen, las siguientes ecuaciones de conservación se cumplen:

* El número promedio de clientes en la cola es igual a la tasa de llegada multiplicada por el retraso promedio *.*
* El número promedio de clientes en el sistema es igual a la tasa de llegada multiplicada por el tiempo de espera promedio  *.*

También se cumple donde *E*(*S*) es el tiempo esperado de servicio.

Para una cola *M*/*M*/*1*, se puede mostrar que el número promedio de clientes en el sistema en estado estacionario es:

donde ρ es la tasa de utilización del sistema.

# Simulación - Darío Weitz

## 1.5 Pasos para Realizar un Estudio de Simulación

1. **Definición del Sistema Bajo Estudio**:

* Establecer objetivos y supuestos del estudio
* Definir variables de decisión, sus interacciones y alcances
* Desarrollar modelo conceptual con fronteras, elementos, flujos y variables clave

1. **Generación del Modelo Base**:

* Traducir modelo conceptual a lenguaje de simulación
* Incluir interrelaciones entre subsistemas
* Definir animaciones si son necesarias
* Incorporar variables aleatorias y sus distribuciones

1. **Recolección y Análisis de Datos**:

* Recopilar información estadística de variables aleatorias
* Validar calidad y formato de datos
* Realizar estudios estadísticos si la información es insuficiente
* Identificar distribuciones de probabilidad apropiadas

1. **Generación del Modelo Preliminar**:

* Integrar análisis de datos, supuestos e información requerida
* Estimar rangos de variación o valores constantes para nuevos procesos
* Sugerir distribuciones basadas en experiencia
* Preparar modelo para verificación

1. **Verificación del Modelo**:

* Comprobar correcta programación del modelo
* Validar funcionamiento de parámetros
* Detectar errores de programación o alimentación de datos
* Actualizar supuestos si han cambiado durante el desarrollo

1. **Validación del Modelo**

* Probar modelo con información real o condiciones actuales de operación
* Validar comportamiento con expectativas del cliente
* Justificar comportamientos contrarios a experiencias de especialistas
* Para nuevos procesos, usar escenarios sugeridos por el cliente

1. **Generación del Modelo Final**

* Modelo validado listo para simulación
* Será el modelo base para comparar escenarios

1. **Definición de Escenarios**

* Acordar con cliente escenarios a analizar
* Usar comúnmente: pesimista, optimista e intermedio
* Considerar múltiples variables de respuesta
* Utilizar herramientas de simulación para múltiples réplicas
* Sugerir escenarios clave para reducir combinaciones posibles

1. **Análisis de Sensibilidad**

* Comparar estadísticamente los mejores escenarios
* Analizar intersección de intervalos de confianza
* Realizar más réplicas o incrementar tiempo de simulación si hay traslape
* Acortar intervalos de confianza para diferenciar soluciones

1. **Documentación y Conclusiones**

* Documentar completamente el modelo para uso futuro
* Incluir: supuestos, distribuciones, alcances, limitaciones
* Agregar sugerencias de uso y sobre resultados
* Presentar conclusiones del proyecto
* Elaborar reportes ejecutivos para presentación final

## 13. Modelos de Colas

### 13.1 Características de un Sistema de Colas

**Población de Clientes**

* **Infinita**: número de clientes muy grande en comparación con la capacidad del sistema (clientes en un supermercado).
* **Finita**: número limitado de clientes (4 máquinas en un taller). El análisis es más complejo.

**Tiempos entre Llegadas**

* **Determinístico**: los clientes llegan en intervalos de tiempo fijos y conocidos.
* **Probabilístico**: los tiempos entre llegadas son inciertos y se modelan con distribuciones de probabilidad. Usualmente se utiliza la exponencial.

**Proceso de Espera en Cola**

* **Cantidad de Colas**: puede existir una única cola o varias colas.
* **Número de Espacios en Cola**: puede ser limitado (finito) o ilimitado (infinito).
* **Disciplina de Cola**: regla que determina qué cliente recibe servicio primero (FIFO, LIFO, Prioridad).

**Proceso de Servicio**

* **Tipo de Servidores**:
* **Idénticos**: todos atienden a la misma velocidad ( usual en los modelos básicos).
* **No idénticos**: los servidores difieren en su rapidez de atención.
* **Cantidad de Servidores**: puede haber un único o múltiples servidores en paralelo.

Cualquier sistema de colas tiene dos fases:

* **Fase Transitoria**: periodo inicial de un sistema donde se observan los efectos de las condiciones iniciales.
* **Estado Estable**: condición del sistema después que se han eliminado las condiciones iniciales.

### 13.2 Medidas de Rendimiento

* número promedio de llegadas por unidad de tiempo
* número promedio de clientes atendidos por unidad de tiempo en una estación
* tiempo promedio de servicio
* número promedio de clientes en el sistema
* tiempo promedio de espera
* tiempo promedio en el sistema
* número promedio de clientes en cola
* probabilidad de que no haya clientes en el sistema
* probabilidad de que un cliente que llega tenga que esperar
* probabilidad de que haya *n* clientes en el sistema
* utilización, tiempo promedio que un servidor está ocupado
* intensidad de tráfico

**Modelo M/M/1**:

* Población de clientes finita.
* Los clientes llegan de acuerdo con un proceso de Poisson con tasa promedio de clientes por unidad de tiempo. Para que el sistema alcance un estado estable se tiene que dar que
* Proceso de colas con una sola línea con disciplina FIFO.
* Un sólo servidor que atiende con cliente de acuerdo con una distribución exponencial con una cantidad promedio de clientes por unidad de tiempo.

**Modelo M/M/c**:

* Población de clientes infinita.
* Los clientes llegan de acuerdo con un proceso de Poisson con tasa promedio de clientes por unidad de tiempo. Condición de estado estable
* Proceso de colas con una sola línea con disciplina FIFO.
* C servidores idénticos, cada uno atiende a los clientes con una distribución exponencial con una cantidad promedio de clientes por unidad de tiempo.

###

### 13.5 Análisis Económico de los Sistemas de Colas

Para evaluar el **costo de un sistema de colas** se necesitan:

* Costo por servidor por unidad de tiempo *cs* .
* Costo por unidad de tiempo por cliente esperando en el sistema *cw* .
* Número promedio de clientes en el sistema *L*.

![](imagen)

En el caso de un sistema *M*/*M*/*c* con capacidad de espera limitada *M*/*M*/*c*/*K* necesitamos:

* Costo total de los servidores = costo por servidor x número de servidores
* Costo total de espera = costo de la espera x número clientes en el sistema
* Costo total por negación = costo por negación x número de llegadas x probabilidad de negación (asociado a la pérdida de un cliente)

Entonces, el costo total = costo servidores + costo espera + costo negación de servicio

# Simulación - Sheldon M. Ross

## Capítulo 2 - Elementos de Probabilidad

### 2.1 Espacio Muestral y Eventos

*S* es el **espacio muestral** del experimento, el conjunto de todos los resultados posibles. *S* = { }

*A* es un **evento**, subconjunto del espacio muestral formado por resultados posibles del experimento.

Para dos eventos *A* y *B* definimos el nuevo evento la **unión** *A* ∪ *B*, los resultados están en *A, B* o ambos. Definimos la **intersección** *AB*, los resultados están en *A* y en *B*.

La **unión** de los eventos *A1 , A2 , … , An* denotado por ∪ni=1 está formado por todos los resultados que están en cualquiera de los *Ai* . La **intersección** de *A1 , A2 , … , An* denotado por *A1 A2 … An* está formado por todos los resultados que están en todos los *Ai* .

Para cualquier evento *A* definimos *AC*, el **complemento** de *A*, como todos los resultados del espacio muestral *S* que no están en *A* (*AC* ocurre ↔ *A* no ocurre). *SC* es el conjunto vacío o ∅

Si *AB* = ∅, *A* y *B* no pueden ocurrir a la vez, decimos que estas son **mutuamente excluyentes**.

### 2.2 Axiomas de Probabilidad

Supongamos que para cada evento *A* de un experimento con espacio muestral *S* hay un número, *P*(*A*) y llamado la probabilidad del evento *A*, que cumple los **tres axiomas**:

**Axioma 1**. 0 ≤ *P*(*A*) ≤ 1

La probabilidad de que el resultado del experimento esté en *A* es un número entre 0 y 1.

**Axioma 2**. *P*(*S*) = 1

Con probabilidad 1, este resultado es un elemento del espacio muestral.

**Axioma 3**. Para cualquier secuencia de eventos mutuamente excluyentes *A1* , *A2* , …

Para cualquier conjunto de eventos mutuamente excluyentes, la probabilidad de que al menos uno ocurra es igual a la suma de sus probabilidades respectivas.

Con los axiomas anteriores llegamos a que la probabilidad de que no ocurra un evento es 1 menos la probabilidad de que ocurra. Como *A* y *AC* son eventos mutuamente excluyentes, y como *A* ∪ *AC* = *S* tenemos que 1 = *P*(*S*)= *P*(*A* ∪ *AC*) = *P*(*A*)+ *P*(*AC*) entonces *P*(*AC*) = 1 - *P*(*A*)

### 2.3 Probabilidad Condicional e Independencia

La **probabilidad condicional** de *A* dado que *B* ha ocurrido es

En el caso de que decimos que *A* y *B* son independientes y entonces también se da que . Esta relación es simétrica, siempre que *A* sea independiente de *B*, *B* es independiente de *A.*

###

### 2.4 Variables Aleatorias

Las cantidades numéricas determinadas por los resultados del experimento se conocen como **variables aleatorias**. La función de distribución *F* de la variable aleatoria *X* se define para cualquier número real *x* como *F*(*x*) = *P*(*X* ≤ *x*)

Una variable aleatoria si asume un número finito de valores es **discreta**. Para estas, la función de masa de probabilidad *p*(*x*) = *P*(*X* = *x*) y si toma uno de los posibles valores *x1 , x2 , …* entonces

La variable aleatoria *X* es **continua** si existe una función no negativa *f*(*x*) definida para todo número real *x*, el conjunto de valores posibles es un intervalo, sea *C* un conjunto de reales

### 2.5 Esperanza

Si *X* es una variable aleatoria **discreta** que toma uno de los valores *x1 , x2 , …* , entonces la **esperanza** o **valor esperado** de *X* es

Si *X* es **continua** con función de densidad de probabilidad *f*, entonces

Si *a* y *b* son constantes, entonces *E*[*aX* + *b*] = *a E*[*X*] + *b*

Cualesquiera variables aleatorias *X1* y *X2* entonces *E*[*X1* + *X2*] = *E*[*X1*] + *E*[*X2*], se generaliza como

### 2.6 Varianza

*E*[*X*] es el valor esperado de la variable aleatoria *X*, un promedio ponderado de los valores posibles de la misma. La variación de tales valores se puede medir considerando el promedio del cuadrado de la diferencia entre *X* y *E*[*X*].

Si *X* es una variable aleatoria con media μ, entonces la **varianza** de *X*, es

También podemos expresarla como

Sean dos constantes *a* y *b* por definición

por definición

### 2.7 Desigualdad de Chebyshev y Leyes de los Grandes Números

**Desigualdad de Markov**. Si *X* sólo toma valores no negativos, para cualquier valor *a* > 0

. Para demostrarlo definimos una variable aleatoria *Y* como![](imagen)

Tomando estos valores, la **esperanza** se expresa como

Como *X* ≥ 0, entonces *X* ≥ *Y*. Utilizando la expresiones anteriores

**Desigualdad de Chebyshev**. Si *X* es una variable aleatoria que tiene media μ y varianza σ2, entonces para cualquier valor *k* > 0

Creamos una variable aleatoria entonces

por definición de varianza de *X*

Entonces, para la **Desigualdad de Markov** nos queda

si cambiamos a por y a por entonces obtenemos

multiplicamos dentro de a ambos términos por

aplicamos raíz cuadrada solamente a la parte positiva y por Markov sabemos que entonces y la ecuación queda

**Ley Débil de los Grandes Números**. Sea *X1 , X2 , …* una sucesión de variables aleatorias independientes e idénticamente distribuidas con media μ. Entonces, para cada > 0

cuando

Creamos una variable , entonces

si

*n* veces

Como

si son independientes

como

*n* veces

entonces el desvío = (desvío muestral)

Por desigualdad de Chebyshev reemplazando con variable y desvío

llamamos entonces por lo que

cuando *n* tiende infinito el lado derecho tiende a 0

Para un epsilon pequeño el promedio de la variables se acerca a la media muestral.

**Ley Fuerte de los Grandes Números**. A largo plazo, el promedio de una sucesión de variables independiente e idénticamente distribuidas convergerá a su media.

### 2.8 Algunas Variables Aleatorias Discretas

**Variables Aleatorias Binomiales**

Se realizan *n* ensayos independientes, cada uno con una **probabilidad de éxito** de *p* y de **fracaso** 1 - *p*. Sea *X* el número de éxitos en esos *n* ensayos, entonces:

![](imagen)

**Función de Masa de Probabilidad**:

![](imagen)es el **coeficiente binomial**, número de subconjuntos distintos de *i* elementos que se pueden elegir de un conjunto de *n* elementos

Una **Bernoulli** es un caso particular de binomial con *n* = 1: ![](imagen)

*p*

*1 - p*

Una **variable binomial** *X* puede expresarse como la suma de *n* variables de Bernoulli independientes e idénticamente distribuidas IID:

entonces

**Variables Aleatorias Poisson**

Una variable aleatoria *X* que toma los valores 0, 1, 2, … se dice que es una **variable de Poisson** con parámetro λ (donde λ > 0) si su función de masa de probabilidad está dada por:

**Función de Masa de Probabilidad**:

Las variables de Poisson se utilizan para aproximar la distribución del número de éxitos en un gran número de ensayos *n*, donde cada ensayo tiene una probabilidad de éxito *p*. Consideremos una variable binomial y definimos . Entonces:

desarrollando los factoriales

la *i* estaría entre el 1 y la *n* por lo que podemos

Cuando *n* grande y *p* pequeña, la binomial se transforma en una Poisson, y se cumplen las siguientes aproximaciones cuando *n* tiende a ∞:

Entonces

Dado que para una variable binomial se tiene:

para *p* pequeña

Entonces para una **variable de Poisson** *X* con parámetro :

**Variables Aleatorias Geométricas**

Considere una secuencia de ensayos independientes, cada uno con una probabilidad de éxito *p*. Cuántos intentos hasta lograr el primer éxito. Si *X* representa el número del primer ensayo que resulta en un éxito, entonces:

Una variable aleatoria con esta función de masa de probabilidad se denomina **variable geométrica** con parámetro *p*.

**Variable Aleatoria Binomial Negativa**

Supongamos que *X* representa el número de ensayos necesarios para obtener *r* éxitos, donde cada ensayo es independiente y tiene una probabilidad de éxito *p*. Entonces, *X* es una **variable aleatoria binomial negativa** (o Pascal).

![](imagen)

**Función de Masa de Probabilidad**:

### 2.9 Variables Aleatorias Continuas

**Variables Aleatorias Uniformemente Distribuidas**

Una variable aleatoria *X* está distribuida **uniformemente** en el intervalo (*a*, *b*), donde *a* < *b*, si su función de densidad de probabilidad es:

![](imagen)

*X* está distribuida uniformemente en (*a*, *b*) si coloca toda su masa en ese intervalo y tiene la misma posibilidad de estar cerca de cualquier punto de ese intervalo.

la integral de x es x2/2

Entonces

![](imagen)

**Variables Aleatorias Normales**

Una variable aleatoria *X* se distribuye **normalmente** con media y varianza si su función de densidad de probabilidad es:

La curva tiene forma de campana y es simétrica alrededor de

Si *X* es normal con media y varianza cualesquiera constantes *a* y *b*, *aX* + *b* está distribuida normalmente con media y varianza .

También, siendo

*Z* tiene una distribución normal y se llama estandarizada, con media y varianza . Esto lo podemos demostrar aplicando las propiedades:

*E*[*aX* + *b*] = *a E*[*X*] + *b*

Sea la función de distribución de una variable aleatoria normal estándar:

Como entonces podemos expresar la función de distribución de como:

**Teorema Central del Límite**

Sea *X1* , *X2* , … una sucesión de variables aleatorias independientes e idénticamentes distribuidas con media finita y varianzafinita . Entonces

**Variables Aleatorias Exponenciales**

Una variable aleatoria continua *X* sigue una distribución **exponencial** con parámetro λ > 0 si su función de densidad de probabilidad es:

Su distribución acumulativa está dada por

### Proceso Poisson

Sea *N*(*t*) el número de eventos que ocurren en el intervalo [*0, t*]. Estos eventos constituyen un **proceso de Poisson** con razón λ > 0 si:

1. **Condición Inicial**: comienza en el instante 0, *N*(0) = 0
2. **Incremento Independiente**: el número de eventos en intervalos de tiempo disjuntos son independientes.
3. **Incremento Estacionario**: (diferencia si es homogéneo o no) la distribución del número de eventos en un intervalo determinado depende solo de su longitud, no de su posición en el tiempo. Todos los intervalos tienen la misma probabilidad.
4. En un intervalo pequeño de longitud *h*, la probabilidad de que ocurra exactamente un evento es aproximadamente *h*

1. En un intervalo pequeño de longitud *h*, la probabilidad de que ocurran dos o más evento es aproximadamente 0

### Proceso Poisson No Homogéneo

El **proceso de Poisson homogéneo** asume que los eventos ocurren con la misma probabilidad en cualquier intervalo de igual longitud. Esto no siempre es realista, por lo que se introduce el **proceso de Poisson no homogéneo**, que permite que la tasa de ocurrencia varíe en el tiempo.

Sea *N*(*t*) el número de eventos ocurridos hasta el instante *t*, entonces {*N*(*t*), *t ≥ 0*} es un proceso de Poisson no homogéneo con función de intensidad λ(*t*), si:

1. **Condición Inicial**: comienza en el instante 0, *N*(0) = 0
2. **Incremento Independiente**: el número de eventos en intervalos de tiempo distintos son independientes.
3. *P* {exactamente 1 evento entre *t* y *t + h*}/*h* = λ(*t*)
4. *P* {2 o más eventos entre *t* y *t + h*}/*h* = 0

En el proceso no homogéneo tenemos λ(*t*) varía con el tiempo, permitiendo modelar situaciones donde la tasa de ocurrencia de eventos cambia a lo largo del tiempo.

# 7.1 Números Pseudoaleatorios

El objetivo de los generadores aleatorios es construir sucesiones de números independientes que se comporten como observaciones de una distribución Uniforme(0,1).

## Números Verdaderamente Aleatorios

* Son no determinísticos, es decir, imposibles de predecir.
* Se basan en fenómenos físicos con un grado de aleatoriedad inherente:
* **Procesos cuánticos** (teóricamente impredecibles).
* **Procesos caóticos** (prácticamente impredecibles).

**Ejemplos**:

* **random.org**: genera números a partir de ruido atmosférico.
* **ERNIE**: utiliza ruido térmico en transistores, aplicado en loterías del Reino Unido.
* **RAND** Corporation (1955): publicó una tabla de un millón de números aleatorios obtenidos con una ruleta electrónica.

**Ventajas**: genuinamente aleatorios.

**Desventajas**: costosos, lentos, y no reproducibles.

## Números Pseudoaleatorios

* Son generados mediante algoritmos determinísticos.
* Aunque no son verdaderamente aleatorios, buscan imitar sus propiedades estadísticas.
* Se definen a partir de:

1. **Semilla** (seed): estado inicial que determina toda la secuencia.
2. **Función de transición**: actualiza el estado del generador.
3. **Función de salida**: produce los bits o números finales.

**Características deseables**:

* No deben mostrar patrones o regularidades.
* Deben tener un periodo largo (cantidad de valores que se generan antes de repetirse).
* Ser rápidos de calcular y reproducibles (útiles para simulaciones y pruebas).

## Métodos Tempranos

**Método de la Parte Media del Cuadrado** (Von Neumann, 1946)

* Se eleva al cuadrado la semilla inicial y se toman los dígitos centrales como nuevo valor.
* **Problema**: cae en ciclos muy cortos (ejemplo, aparición de ceros perpetuos).
* Mejoras posteriores lograron secuencias más largas (ejemplo: Metrópolis, 750.000 números distintos), pero sigue siendo un método poco confiable.

**Función rand en Matlab**

* Usó hasta 1995 un generador congruencial de la forma:
* Generaba números que, a primera vista, parecían Uniforme(0,1).

**RANDU** (muy usado en los 60–70s)

* Definido como:
* **Problema**: al graficar ternas los puntos caían en unos pocos planos, mostrando una fuerte correlación no deseada.
* Se considera un mal generador.

## Generadores Congruenciales Lineales (GCL)

* Definidos por la recurrencia:
* Parámetros:
* módulo
* multiplicador
* incremento
* semilla

**Propiedades**:

* Periodo máximo
* Para lograr periodo completo en un GCL mixto :

1. y deben ser primos relativos
2. divisible por todos los factores de
3. Si es múltiplo de 4, entonces debe ser divisible por 4

**Problemas**: aunque rápidos y fáciles de implementar, los GCL presentan defectos estructurales. En dimensiones altas, los puntos generados se distribuyen en pocos hiperplanos.

Los GCL son eficientes cuando m es potencia de 2 (por el truncamiento de bits)

## Generador Mersenne-Twister

* Desarrollado en 1997 por Matsumoto y Nishimura
* Periodo extremadamente largo: 2¹⁹⁹³⁷ - 1
* Pasa múltiples pruebas de aleatoriedad
* Implementado en: Python, R, Ruby, C++, Excel, Matlab

**Ventajas sobre GCL**

* Mejor distribución multidimensional
* Periodo más extenso
* Mayor calidad en las pruebas estadísticas

## Pruebas de Aleatoriedad

Dado que el ojo humano no distingue bien la aleatoriedad, se utilizan pruebas estadísticas.

**Tipos de Pruebas**

* **Empíricas**: aplicadas directamente sobre las secuencias generadas.
* **Teóricas**: basadas en propiedades matemáticas de la regla de recurrencia.

**Ejemplos**:

* Prueba X2 de bondad de ajuste
* Prueba de uniformidad k-dimensional

## Resumen

* Los números aleatorios verdaderos son impredecibles, pero poco prácticos.
* Los números pseudoaleatorios son determinísticos, eficientes y reproducibles, aunque requieren buenos algoritmos para evitar patrones indeseados.
* Los GCL marcaron un inicio importante, pero presentan limitaciones.
* El Mersenne Twister es actualmente uno de los generadores más usados y confiables.
* Para evaluar generadores, es indispensable aplicar pruebas estadísticas de aleatoriedad más allá de simples inspecciones visuales.

# Capítulo 4 - Generación de valores de variables estocásticas en simulación

## Contexto y Objetivos

El término Monte Carlo se asocia con la simulación de procesos estocásticos, aunque originalmente también se aplicaba a problemas determinísticos.

La **simulación estocástica** permite resolver problemas complejos donde los métodos numéricos o analíticos tradicionales son poco prácticos.

## Métodos de Generación

* **Transformación Inversa**: usa la función de distribución acumulada (FDA) y su inversa para obtener valores a partir de números aleatorios uniformes.
* **Método de Rechazo**: genera candidatos y acepta o rechaza valores según la densidad objetivo. Útil cuando no existe forma cerrada de la inversa.
* **Método de Composición** (mezclas): combina varias distribuciones más simples para construir la deseada.

## Distribuciones Continuas

Se presentan fórmulas, propiedades, diagramas de flujo y subrutinas para:

* Uniforme: la más simple, útil en errores de redondeo.
* Exponencial: modela tiempos entre eventos independientes.
* Gamma y Ji-cuadrada: aplicables en tiempos de espera y procesos de cola.
* Normal y Normal multivariada: fundamentales en estadística; se generan por métodos como el del límite central o transformaciones (Box-Muller).
* Normal logarítmica: usada en fenómenos multiplicativos.

## Distribuciones Discretas

* Geométrica
* Pascal (binomial negativa)
* Binomial
* Hipergeométrica
* Poisson

## Casos Especiales

* **Distribuciones Empíricas**: cuando no existe un modelo teórico, se utilizan tablas de probabilidades observadas.
* **Procesos de Markov**: simulación basada en matrices de transición de estados.
* **Variables Autocorrelacionadas**: necesarias en modelos donde los valores no son independientes.

## Consideraciones Prácticas

El empleo de computadoras digitales agiliza el cálculo, pero los métodos son aplicables también manualmente. Se enfatiza la simplicidad de las subrutinas y la reutilización de funciones de librería como logaritmos, exponenciales y generadores uniformes. La elección del método depende del equilibrio entre eficiencia computacional, precisión y facilidad de programación.

# The Art of Process-Centric Modeling

## M/M/1/∞/∞ (Servidores Cola Simple)![](imagen)

Cuando la capacidad del sistema y el tamaño de la población que llama son infinitos, podemos omitirlos de la notación de colas, M/M/1/∞/∞ es lo mismo que M/M/1.

La notación M/M/1/∞/∞ significa que este sistema tiene las siguientes **características**:

* Tiempo entre llegadas = exponencial
* Tiempo de servicio = exponencial
* Número de servidores en paralelo = 1
* Capacidad del sistema = ∞
* Población que llama = ∞

Las **fórmulas** para un sistema de colas M/M/1/∞/∞ son:

Incluimos estas fórmulas para mostrar cómo se pueden calcular soluciones exactas, con el objetivo de compararlas con los resultados de las simulaciones.

Las tasas de arribos y los tiempos de servicio se modelan como un **proceso de Poisson**, con tiempos entre arribos **distribuidos exponencialmente**. La principal característica del proceso de Poisson es que cada arribo ocurre de manera independiente, sin influir en los demás.

En contraste, usar la distribución exponencial para los tiempos de servicio no es realista. La razón principal para utilizar esta distribución en sistemas de colas clásicos es que tiene propiedades matemáticas que facilitan la obtención de una solución cerrada.

En los tiempos de servicio, la **distribución exponencial** se emplea más por conveniencia matemática que por realismo, permite soluciones cerradas en los modelos clásicos de colas. Al igual que las llegadas, es una distribución sin memoria: el tiempo de servicio de un cliente no depende del estado actual del servidor.

La **distribución exponencial** es la única distribución continua aleatoria sin memoria, donde el pasado no tiene influencia sobre el futuro.

### AnyLogic

Si se quiere modelar y analizar un sistema de colas M/M/1 (llegadas y servicios exponenciales, 1 servidor, capacidad y población infinita) se puede utilizar AnyLogic, construyendo un modelo con bloques básicos de la Process Modeling Library.

* **Llegadas**: se configura un bloque Source con tiempos entre llegadas definidos por una distribución exponencial (exponential(15, 0)), modelando un proceso de Poisson con una tasa de 15 entidades por segundo.
* **Servicio**: el tiempo de servicio se modela con un bloque Delay usando una distribución exponencial (exponential(20, 0)), con una tasa de servicio de 20 entidades por segundo.
* **Cola y Servidor**: implementados con Seize (captura recurso), Delay (tiempo de servicio) y Release (libera recurso). La capacidad se controla con un ResourcePool.
* **Métricas**:
* **Tiempo en el Sistema y en Cola**: se usan pares de bloques TimeMeasureStart y TimeMeasureEnd para registrar los tiempos totales en el sistema y los tiempos de espera en la cola.
* **Número de Entidades en el Sistema y en Cola**: se emplean variables y objetos de Statistics para calcular y trackear en tiempo real el número promedio de entidades en el sistema y en la cola. El código para actualizar estas estadísticas se coloca en los eventos On enter y On exit de los bloques Source, Sink y Seize.
* **Visualización**: se generan histogramas de las distribuciones de tiempo en el sistema y en la cola, mostrando sus medias.

# Preguntas Parciales

| ¿Cuáles son algunas características de los **generadores aleatorios verdaderos**?   1. Solo generan conjuntos finitos de números. 2. En general son menos prácticos que otros generadores. 3. El tiempo de generación es más importante que la calidad de los conjuntos generados. 4. Están basados en algoritmos procesados en computadoras.   **Respuesta**: b)  **Nota:** [7.1 Números pseudoaleatorios | Estadística Computacional](https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html) ⟶ “*La desventaja de éstos métodos es que son costosos, tardados y no reproducibles.*” |
| --- |

| La **frecuencia relativa** es una medida estadística que se calcula como la suma de la **frecuencia absoluta de algún valor de la población** o muestra entre el total de valores que **componen la población** o muestra.   1. Verdadero 2. Falso   **Respuesta**: b)  **Nota**: Para que sea verdadero, debería ser el total de observaciones de ese valor que están presentes en la población. |
| --- |

| ¿Cuáles son los **tipos de pruebas de aleatoriedad** que pueden aplicarse a un conjunto de números pseudoaleatorios?   1. Empíricas. 2. Poker. 3. Prueba de bondad de ajuste. 4. Tests de Cooper. 5. Subidas y bajadas. 6. Teóricas. 7. Prueba de espera.   **Respuesta**: a) y f)  **Nota**: [Pruebas de aleatoriedad](https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html#pruebas-de-aleatoriedad) ⟶ “*Hay dos tipos de pruebas: empíricas y teóricas…*”  La prueba de espera es una prueba, **no** un tipo de prueba.  **ORIGINAL-108-Simulation-Modeling-and-Analysis-Averill-M.-Law-Edisi-5-2014 (1).pdf** | **Pág. 428**  There are two quite different kinds of tests, which we discuss separately in Secs. 7.4.1 and 7.4.2.   * **Empirical tests** are the usual kinds of statistical tests and are based on the actual Ui’s produced by a generator. Chi-square test, serial test, runs test, Kolmogorov-Smirnov, birthday spacings test, * **Theoretical tests** are not tests in the statistical sense, but use the numerical parameters of a generator to assess it globally without actually generating any Ui’s at all. |
| --- |

| En matemáticas y estadística, la **media** o **promedio** es una medida de tendencia central. La media aritmética es un promedio estándar que a menudo se denomina promedio.   1. Verdadero 2. Falso   **Respuesta**: a) |
| --- |

| La **programación orientada a objetos** no es imprescindible para realizar simulaciones.   1. Verdadero 2. Falso   **Respuesta**: a)  **Nota**: Página 182-183 del libro (201-202 del PDF) de [ORIGINAL-108-Simulation-Modeling-and-Analysis-Averill-M.-Law-Edisi-5-2014 (1).pdf - Google Drive](https://drive.google.com/file/d/19NAXRa3XQNj6l8Kp-C3VaKy4HSmgvYwo/view?hl=es)  The programming languages C++ and Java are object-oriented (see Sec. 3.6), which is of considerable importance to many analysts and programmers, such as those in the defense industry. **On the other hand, most simulation packages are not truly object-oriented.** |
| --- |

| Si la **tasa de arribos** es mayor que la **tasa de servicio** no es posible realizar la simulación.   1. Verdadero 2. Falso   **Respuesta**: b)  **Nota**: Es posible realizar la simulación, pero no el cálculo teórico. La simulación mostrará un 100% de utilidad del servicio.  Simulation Modeling and Analysis, FIFTH EDITION  **Pág. 335**  **“If the arrival rate of customers is close to the service rate, the system will be congested and the Xi ’s will be highly positively correlated”**  **Si la tasa de arribos es cercana a la tasa de servicio, el sistema se congestiona y las demoras (Xi) se vuelven altamente correlacionadas**, pero no se dice que no sea posible realizar la simulación. La simulación puede hacerse igual, aunque el sistema no sea estable (en ese caso las colas crecerán indefinidamente). |
| --- |

| **GIS** es un sistema geográfico monocapa para analizar cuestiones concretas de una zona particular.   1. Verdadero 2. Falso   **Respuesta**: b)  **Nota**: <https://anylogic.help/anylogic/gis/gis-map.html>  “With the GIS Map shape you **can display layers of both map types, superimposed one over another**. On a map you can also add points, routes, and regions.” |
| --- |

| ¿Cuáles **paradigmas de simulación** son los explicados en **AnyLogic en 3 días**?   1. Basado en agentes 2. Peatones 3. Eventos discretos 4. Sistemas dinámicos 5. Caminos 6. Sistemas en tiempo real 7. GIS   **Respuesta**: a), c) y d)  **Nota**: Página 13 del apunte de “*Anylogic in 3 days*”. Se dice que “In simulation modeling, a method is a framework we use to map a real-world system to its model. You can think of a method as a type of language or a sort of "terms and conditions" for model building. There are three methods: System Dynamics Discrete, Event Modeling and Agent-Based Modeling “  ![](imagen) |
| --- |

| Los eventos a tratar en el **modelo de cola simple** son el paradigma de simulación basado en eventos son:   1. Poner el servidor en ocupado/desocupado 2. Inicio 3. Arribo 4. Partida 5. Finalización   **Respuesta**: c) y d) |
| --- |

| La **solución analítica** es exacta:   * Verdadero * Falso   **Respuesta**: a) |
| --- |

| El conjunto de **números pseudoaleatorios** generados se espera que tengan un "comportamiento" similar a los conjuntos de números aleatorios verdaderos.   1. Verdadero 2. Falso   **Respuesta**: a) |
| --- |

| Un **modelo** es un recorte de características observables de la realidad y solo puede ser usado si está totalmente testeado.   1. Verdadero 2. Falso   **Respuesta**: b) |
| --- |

| Para la construcción de **modelos** es necesario herramientas informáticas siempre.   1. Verdadero 2. Falso   **Respuesta**: b)  **Nota**: Falso, podrían existir modelos físicos que nos permitan simular el comportamiento del sistema. Ejemplos son, una maqueta, una tiza que se cae para calcular la velocidad. |
| --- |

| Realizar test de los valores generados por un generador de números pseudoaleatorios es obligatorio antes de ser empleados en **simulación**.   1. Verdadero 2. Falso   **Respuesta**: a)  **Nota**: Es necesario realizar tests sobre los valores generadores por el generador para verificar que sea lo suficientemente aleatorio como necesitemos. Es común que generadores básicos caigan en patrones redundantes o ciclos de valores. |
| --- |

| El método de la **parte media del cuadrado** es un método vigente para la generación de números pseudoaleatorios   1. Verdadero 2. Falso   **Respuesta**: b)  **Nota**: <https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html> ⟶ Bajo el título de “Ejemplo: método de la parte media del cuadrado” se expresa que “*el método del valor medio no es considerado un método bueno por lo común de los ciclos cortos.*” |
| --- |

| Los **números pseudoaleatorios** se generan de manera secuencial con un algoritmo determinístico.   1. Verdadero 2. Falso   **Respuesta**: a) |
| --- |

| Los **números pseudoaleatorios** pueden generarse con cualquier computadora a altas velocidades.   1. Verdadero 2. Falso   **Respuesta**: a) |
| --- |

| Se denomina **ciclo completo** cuando el conjunto de números pseudoaleatorios generados repite siempre el mismo número, luego de generar un gran conjunto de números distintos.   1. Verdadero 2. Falso   **Respuesta**: b) |
| --- |

| Los modelos de la cola simple y de inventario empleados durante los TPI de clase…   * Son modelos simples que pueden ser simulados y que también se cuenta con la solución analítica de los mismos. * Solo pueden ser simulados si se tiene la solución analítica. * La solución analítica puede ser comparada con las respuestas obtenidas de las simulaciones. * Las respuestas obtenidas mediante simulaciones son generalmente similares al de la solución analítica.   **Respuesta**: ni idea XD (Ponele que a), c) y d)) |
| --- |

| Para poder **simular** es necesario contar con información de funcionamiento de la realidad o estimaciones del mismo.   1. Verdadero 2. Falso   **Respuesta**: a) |
| --- |

| La **simulación** por computadora surgió en los últimos 30 años.   1. Verdadero 2. Falso   **Respuesta**: b) |
| --- |

| La **simulación** reemplaza a la solución analítica como método de resolución de problemas complejos con solución.   1. Verdadero 2. Falso   **Respuesta**: b) |
| --- |

| **Frecuencia absoluta** de un evento es el número de veces en que dicho evento se repite durante un experimento o muestra estadística.   1. Verdadero 2. Falso   **Respuesta**: a) |
| --- |

| Sobre los **números pseudoaleatorios**...   1. Se generan de manera secuencial con un algoritmo determinístico. 2. Se denomina de ciclo completo cuando el conjunto de números pseudoaleatorios generados repite siempre el mismo número, luego de generar un gran conjunto de números distintos. 3. EI método de la parte media del cuadrado es un método vigente para la generación de números pseudoaleatorios. 4. Los números pseudoaleatorios pueden generarse con cualquier computadora a altas velocidades.   **Respuesta**: a) y d) |
| --- |

| **Verdaderos números aleatorios**.   1. Es preferible en simulaciones de alto rendimiento usar un conjunto de números aleatorios y no pseudoaleatorios. 2. En general los números aleatorios se basan en alguna fuente de aleatoriedad física que puede ser teóricamente impredecible (cuántica) o prácticamente impredecible (caótica).   Respuesta: b) |
| --- |

| **Latex** es un sistema de composición de textos, orientado a la creación de documentos escritos que presenten una alta calidad tipográfica. Por sus características y posibilidades, es usado de forma especialmente intensa en la generación de artículos y libros científicos que incluyen, entre otros elementos, expresiones matemáticas.   1. Verdadero 2. Falso   **Respuesta**: a) |
| --- |

# Preguntas Extra (inventadas por nosotros)

| El **Mersenne Twister** se destaca porque:   1. Tiene un periodo extremadamente largo. 2. Fue diseñado en 1946 por Von Neumann. 3. Es más lento que los GCL. 4. Está implementado en lenguajes como Python, R y Excel.   **Respuesta**: a) y d) |
| --- |

| Una característica deseable en un **generador de números pseudoaleatorios** es:   1. Corto período. 2. Mostrar patrones claros para depuración. 3. Alta velocidad de cálculo. 4. No ser reproducible.   **Respuesta**: c) |
| --- |

| ¿Qué problema presentaba el generador **RANDU** usado en los 60s-70s?   1. Generaba siempre ceros perpetuos. 2. Los puntos tridimensionales caían en pocos planos, mostrando correlación no deseada. 3. Tenía un periodo infinito pero lento. 4. No se podía reproducir la secuencia.   **Respuesta**: b) |
| --- |

| El **método de rechazo** se utiliza cuando:   1. La inversa de la función de distribución acumulada no existe en forma cerrada. 2. La función de densidad objetivo es uniforme. 3. Queremos reducir el tiempo de cómputo. 4. Todas las anteriores.   **Respuesta**: a) |
| --- |

| El **método de composición**:   1. Siempre se basa en transformaciones trigonométricas. 2. Consiste en combinar distribuciones simples para formar una más compleja. 3. Es lo mismo que la Transformación Inversa. 4. Se usa solo para distribuciones exponenciales.   **Respuesta**: b) |
| --- |

| La distribución **Exponencial**:   1. Se usa para modelar tiempos entre eventos independientes. 2. Tiene la propiedad de ser “sin memoria”. 3. Es la única distribución continua con esa propiedad. 4. Se usa solo en tiempos de servicio realistas.   **Respuesta**: a), b) y c) |
| --- |

| ¿Cuál de estas distribuciones es **discreta**?   1. Normal 2. Binomial 3. Poisson 4. Hipergeométrica   **Respuesta**: b), c) y d) |
| --- |

| La **Normal** puede generarse en simulación mediante:   1. Transformación Inversa. 2. Método de Box-Muller. 3. Teorema del Límite Central. 4. Método de rechazo.   **Respuesta**: b) y c) |
| --- |

| En un sistema de colas M/M/1, la **condición de estabilidad** es:   1. λ > μ 2. λ < μ 3. λ = μ 4. Ninguna, siempre es estable.   **Respuesta**: b) |
| --- |

| En AnyLogic, el bloque **Source**:   1. Genera llegadas al sistema. 2. Simula la cola de espera. 3. Libera recursos. 4. Mide el tiempo total en el sistema.   **Respuesta**: a) |
| --- |

| Para medir el **tiempo en el sistema** de una entidad en AnyLogic se usan:   1. TimeMeasureStart y TimeMeasureEnd. 2. ResourcePool. 3. Delay con histogramas. 4. Sink.   **Respuesta**: a) |
| --- |

| El bloque **Seize** en AnyLogic:   1. Genera llegadas al sistema. 2. Registra tiempos de espera. 3. Captura un recurso (servidor). 4. Libera al servidor.   **Respuesta**: c) |
| --- |

| La simulación de **Monte Carlo** se asocia principalmente con:   1. Procesos determinísticos. 2. Procesos estocásticos complejos. 3. Modelos GIS. 4. Modelos orientados a objetos.   **Respuesta**: a) |
| --- |

| Una ventaja de los **números pseudoaleatorios** frente a los verdaderamente aleatorios es que:   1. Son más realistas. 2. Son reproducibles y eficientes computacionalmente. 3. No requieren semilla. 4. Nunca muestran patrones indeseados.   **Respuesta**: b) |
| --- |

| Los **procesos de Markov** en simulación se representan con:   1. Tablas de frecuencias relativas. 2. Matrices de transición de estados. 3. Distribuciones uniformes. 4. Simulación GIS.   **Respuesta**: b) |
| --- |

| En simulación, se recomienda que un buen **generador de pseudoaleatorios** sea:   1. Lento pero muy preciso. 2. Rápido, reproducible y con buen comportamiento estadístico. 3. Basado siempre en fenómenos físicos. 4. Limitado a periodos cortos para mayor control.   **Respuesta**: b) |
| --- |

| ¿Cuál es una característica de los **números verdaderamente aleatorios**?   1. Son generados por algoritmos determinísticos. 2. Son reproducibles a partir de una semilla. 3. Se basan en fenómenos físicos como procesos cuánticos. 4. Presentan siempre ciclos cortos.   **Respuesta**: c) |
| --- |

| ¿Qué condición NO es necesaria para que un **Generador Congruencial Lineal** (GCL) mixto tenga período completo?   1. El módulo y el incremento deben ser primos relativos. 2. El módulo debe dividir a todos los factores de (a − 1). 3. Si el módulo es múltiplo de 4, entonces (a − 1) debe ser divisible por 4. 4. El multiplicador debe ser siempre un número primo.   **Respuesta**: d) |
| --- |

| El método de **Transformación Inversa** se utiliza cuando:   1. La inversa de la función de distribución acumulada (FDA) es fácil de obtener. 2. La distribución no tiene forma cerrada para la inversa. 3. Queremos mezclar varias distribuciones simples. 4. Se requiere aceptar o rechazar valores candidatos.   **Respuesta**: a) |
| --- |

##

| ¿Cuáles son algunas características de los **generadores aleatorios verdaderos**?   1. Solo generan conjuntos finitos de números. 2. En general son menos prácticos que otros generadores. 3. El tiempo de generación es más importante que la calidad de los conjuntos generados. 4. Están basados en algoritmos procesados en computadoras.   **Respuesta**: b)  **Nota:** [7.1 Números pseudoaleatorios | Estadística Computacional](https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html) ⟶ “*La desventaja de éstos métodos es que son costosos, tardados y no reproducibles.*” |
| --- |

Resolución de parciales anteriores

# Parcial 2024

![](imagen)

1)

Modelo físico vs Modelo Matemático:

A la hora de experimentar con un modelo del sistema, es posible utilizar dos tipos de modelos: Modelos físicos o modelos matemáticos. En el caso de los modelos físicos, se tratan de maquetas o simuladores (realizados con objetos del plano físico). Por otro lado, los modelos matemáticos utilizan relaciones lógicas o cuantitativas que existen entre las variables del sistema en estudio para poder analizar lo que ocurre en ellos y su posible variabilidad.

Solución analítica vs Simulación:

La solución analítica busca valores exactos con base en ecuaciones matemáticas que, de manera determinística, obtienen valores de salida. Mientras que las simulaciones tienen en cuenta la variabilidad del entorno del sistema para no depender completamente de los valores de entrada.

2)

…

3)

Paso 6: Validar el modelo programado

La idea es comparar los resultados con los resultados posibles de un sistema real para ver si la simulación arroja valores factibles. Se contrastan las situaciones con el cliente para comprobar que los resultados arrojados sean factibles en el contexto, con la disponibilidad del analista que debería poder explicar cualquier funcionamiento contrario a lo común.

Paso 7: Generación del modelo final

El modelo queda terminado y listo para usar. El analista puede comenzar con su estudio y su revisión de casos.

Paso 8: Determinación de los escenarios finales para el análisis

Se determina el caso estándar (base) y los casos alternativos. Una buena técnica es utilizar tres casos: optimista, intermedio y pesimista. Puede charlar con el cliente para ver qué otros casos serán incluidos en las pruebas.

4)

5)

La notación de Kendall permite describir y clasificar sistemas de colas. La notación simplificada se expresa de la siguiente manera:

*A/B/c*

Donde:

* A: es la distribución de tiempos de llegada
* B: es la distribución de tiempos de servicio
* c: Es la cantidad de servidores que trabajan en forma paralela.

El caso más clásico, *M/M/1*, implica que tanto la distribución de tiempos de llegada como la de tiempos de servicio es Markoviana (es decir, de Poisson). Y que hay un único servidor trabajando para la cola.

6)

Dado el concepto de la esperanza la cual es el valor esperado, matemáticamente expresado como el promedio ponderado de los valores posibles de la variable aleatoria. La varianza vendría a ser el promedio del cuadrado de las distancias de las observaciones con respecto a la media:

7)

Las variables binomiales se definen como la cantidad de experimentos de Bernoulli independientes que resultaron con éxito en un conjunto de n experimentos. Se determina que cada experimento:

Siendo la cantidad de experimentos a realizar y la probabilidad de éxito de cada experimento. Entendemos que los ensayos de Bernoulli son independientes unos de otros, y que un experimento resulte en éxito o fracaso no afecta a la probabilidad de éxito de los otros.

8)

Las condiciones que hacen que la ocurrencia de un evento pueda ser descrito a través de una distribución de Poisson son las siguientes:

* En el instante 0, no se deben producir eventos:
* Los eventos que ocurran en tiempos disjuntos son independientes.
* La distribución del número de eventos que ocurre en un periodo está determinado únicamente por el largo del período, no la ubicación
* En un instante la probabilidad de que ocurra un evento es
* En un instante la probabilidad de que ocurran dos o más eventos es

El **proceso de Poisson homogéneo** asume que los eventos ocurren con la misma probabilidad en cualquier intervalo de igual longitud. Esto no siempre es realista, por lo que se introduce el **proceso de Poisson no homogéneo**, que permite que la tasa de ocurrencia varíe en el tiempo.

x)

Dado un evento que puede ocurrir reiteradas veces en un periodo. Si dividieramos el periodo (por ejemplo, una hora) en ranuras o “slots”, podríamos pensarlo como una Binomial. Donde un ensayo de Bernoulli se realizaría en cada slot para ver si el evento ocurrió durante ese slot o no.

![](imagen)

Evidentemente, la

Para ello, definimos un tal que :

![](imagen) y ![](imagen)

![](imagen)![](imagen)![](imagen)![](imagen)
