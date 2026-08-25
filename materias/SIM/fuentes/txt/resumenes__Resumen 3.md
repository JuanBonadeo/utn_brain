Simulación
Índice
Simulación 4
Sistemas, modelos y simulación 4
Experimentar con el sistema contra experimentar con el modelo 4
Modelo físico contra modelo matemático 4
Solución analítica contra simulación 4
Ventajas y desventajas de la simulación 5
Ventajas 5
Desventajas 5
10 pasos para realizar un estudio de simulación 6
Simulación de eventos discretos 7
Mecanismo de avance en el tiempo 7
Componentes y Organización de un modelo de simulación de eventos discretos 7
M/M/1/∞/FIFO/∞ 9
Medidas de desempeño 10
Número medio de clientes en el sistema (L) 10
Número medio de clientes en cola (Lq) 10
Tiempo medio de espera en el sistema (W) 10
Tiempo medio de espera en cola (Wq) 11
Algoritmos M/M/1 11
Algoritmo principal 11
Tiempos 12
Inicialización 12
Arribo 12
Partida 12
Reporte 13
Análisis económico de los sistemas de colas 13
Modelo y análisis del sistema de colas actual 13
Análisis de costos 13
Simulación de un sistema de inventario 14
Componentes 14
Diagrama de flujo de las rutinas 14
Modelo de desencadenamiento de eventos 15
Medidas de desempeño 15
Algoritmos 16
Programa Principal 16
1 de 25

Inicialización 16
Control de Inventario 16
Acumular áreas 16
Demanda 16
Arribo de Pedido 17
Reporte Parcial 17
Reporte Final 17
Control de Inventario II (no está) 17
Análisis de resultados 17
Comportamiento transiente y estado estacionario de un proceso estocástico 17
Tipos de simulación 17
Análisis de resultados para simulaciones terminales 18
Obteniendo una precisión específica 18
Precisión absoluta 18
Precisión relativa 18
Determinación del sesgo inicial 19
Media de lotes 19
Múltiples medidas de rendimiento 19
Números aleatorios comunes 19
Comparando sistemas alternativos 20
Intervalos de confianza para la diferencia de medidas de rendimiento 20
Muestras apareadas 20
Muestras independientes (Welch) 20
ZGenerador Congruencial Lineal 21
Tests para generadores de números aleatorios 21
Test de chi-cuadrado 21
Test de serie (uniformidad) 21
Test empírico de corridas (independencia) 22
Naylor capítulo 4: Generación de variables estocásticas empleadas en simulación 22
Método de transformación inversa 22
Método de rechazo 22
Método de composición 23
Generación de valores de variables aleatorias con distribución continua 23
Distribución uniforme 23
Distribución exponencial 23
Distribución Gamma 23
Distribución normal 24
Distribución normal multivariada 24
Distribución logarítimica normal 24
Generación de valores de variables aleatorias con distribución discreta 24
Distribución geométrica 24
2 de 25

Distribución binomial 24
Distribución hipergeométrica 25
Distribución de Poisson 25
Distribuciones discretas empíricas 25
Cadenas discretas de Markov 25
Series de tiempo autocorrelacionadas 25
3 de 25

Simulación
Sistemas, modelos y simulación
Un sistema es una colección de entidades que interactúan para lograr un objetivo
lógico. Los sistemas pueden ser discretos, cuando sus variables cambian instantáneamente en
puntos de tiempo separados, o continuos, cuando sus variables de estado cambian
continuamente respecto del tiempo.
El estado del sistema es una colección de variables necesarias para describir el sistema
en un momento particular.
La simulación es una técnica que permite analizar un modelo numérico en un periodo
de tiempo y recolectar datos que permitan estimar el verdadero comportamiento del modelo. Se
puede clasificar según 3 dimensiones:
● Discreta/Continua: Dependiendo el tipo de sistema que se quiera simular.
● Estática/Dinámica: La primera implica una representación del sistema en un momento
particular, mientras que la segunda es de un sistema que evoluciona en el tiempo.
● Determinística/Estocástica: en la primera no hay ningún componente de entrada
probabilístico mientras que en la segunda sí.
Experimentar con el sistema contra experimentar con el modelo
Si es posible y no costoso alterar el sistema físicamente y hacerlo operar bajo las
nuevas condiciones, probablemente sea lo mejor. Sin embargo, esto pocas veces sucede.
Generalmente es muy costoso o disruptivo intentar alterar el sistema, o incluso el sistema
puede no existir en el mundo real todavía. Por eso, normalmente se usan los modelos.
Modelo físico contra modelo matemático
Muchas veces armar un modelo físico (o icónico) que intente replicar lo más
cercanamente posible el sistema real puede ser útil, pero no es típicamente el tipo de modelo
que se utilice en análisis de sistemas. La mayoría de los modelos son matemáticos,
representando al sistema con relaciones lógicas y cuantitativas que se manipulan y cambian
para entender cómo reacciona el modelo (y por consiguiente cómo reaccionaría el sistema, si
está bien hecho el modelo).
Solución analítica contra simulación
Una vez construido el modelo matemático, debe usarse para responder las preguntas
de interés sobre el sistema que supuestamente representa. Si el modelo es simple, pueden
usarse métodos matemáticos para responder estas preguntas y así llegar a las llamadas
soluciones analíticas. Por otro lado, cuando los sistemas son complejos y/o no hay métodos
matemáticos que se pueda o convenga aplicar, el estudio debe darse a través de la simulación.
4 de 25

Ventajas y desventajas de la simulación
Ventajas
● No necesita llevar a cabo en la realidad los procesos para conocer su impacto.
● Mejora el conocimiento del proceso actual al permitir analizar su comportamiento en
distintos escenarios.
● Puede utilizarse como medio de capacitación para la toma de decisiones.
● Es más económico realizar una simulación que cambiar procesos reales.
● Permite probar varios escenarios en busca de las mejores condiciones de trabajo de los
procesos simulados.
● En problemas de gran complejidad la simulación permite generar una buena solución.
Desventajas
● Aunque muchas herramientas permiten obtener el mejor escenario a partir de una
combinación de variaciones posibles, la simulación no es una herramienta de
optimización.
● Puede ser costosa cuando se quiere emplearla en problemas sencillos, en lugar de
utilizar soluciones analíticas.
● Se requiere bastante tiempo para realizar un buen estudio de simulación.
● Es preciso dominar la herramienta de simulación y tener sólidos conocimientos de
estadística para interpretar los resultados.
5 de 25

10 pasos para realizar un estudio de simulación
1. Definición del sistema bajo estudio: Se definen las variables de decisión, las
interacciones entre ellas y se establece el alcance y limitaciones del modelo.
2. Generación del modelo de simulación base: No es necesario que sea un modelo
muy detallado, pero sí es necesario empezar a volcar el modelo conceptual a la
computadora. También se define la manera en la que se van a visualizar las variables
de decisión.
3. Recolección y análisis de datos: Consiste en recopilar información estadística de las
variables aleatorias que se van a utilizar en el modelo, para poder determinar qué
distribución se usará para generar los valores de cada una.
4. Generación del modelo preliminar: Se integra la información obtenida en el análisis
de datos, los supuestos y otros datos para tener un modelo lo más cercano posible a la
realidad del problema bajo estudio.
5. Verificación del modelo: Una vez que se han identificado las distribuciones y se han
implantado los supuestos, se verifican los datos para comprobar que la programación y
los parámetros usados funcionen correctamente.
6. Validación del modelo: Consiste en realizar una serie de pruebas al modelo, utilizando
información de entrada real para observar su comportamiento y analizar los resultados.
7. Generar el modelo final: Con el modelo validado, el analista está listo para realizar la
simulación y estudiar el comportamiento del proceso. Si se comparan escenarios
diferentes, el generado aquí es el modelo raíz.
8. Determinación de los escenarios: Tras validar el modelo, se acuerdan con el cliente
los escenarios a analizar. Una manera sencilla de determinarlos consiste en utilizar un
escenario pesimista, uno intermedio y uno optimista.
9. Análisis de sensibilidad: Una vez que se obtienen los resultados de los escenarios es
importante realizar pruebas estadísticas que permitan comparar los escenarios con los
mejores resultados finales. Si dos intervalos de confianza de la misma variable se
solapan, es estadísticamente incorrecto suponer que uno es mejor que el otro, por lo
que habría que aumentar la cantidad de corridas y/o el tiempo de simulación de cada
una.
10. Documentación del modelo, sugerencias y conclusiones: Una vez hecho análisis de
resultados, es necesario documentar el modelo. Hay que incluir los supuestos del
modelo, las distribuciones de las variables aleatorias, los alcances y limitaciones, y en
general las consideraciones de programación. También se incluyen sugerencias sobre
el uso del modelo y sobre los resultados obtenidos. Por último, se presentan
conclusiones del proyecto.
6 de 25

Simulación de eventos discretos
Un evento es una ocurrencia instantánea que puede cambiar el estado del sistema.
Mecanismo de avance en el tiempo
Mientras la simulación proceda, debemos hacer un seguimiento del valor actual del
tiempo simulado y necesitamos un mecanismo que permita avanzar este tiempo de un valor a
otro. La variable que da el valor actual del tiempo se llama reloj de simulación, y para avanzarlo
hay dos métodos:
● Avance en intervalos fijos.
● Avance al próximo evento: el reloj es inicializado en cero y se calculan los tiempos de
ocurrencia de los eventos. Entonces, el reloj avanza al tiempo de ocurrencia del próximo
evento, se actualiza el estado del sistema y se actualizan los tiempos de eventos
futuros.
Componentes y Organización de un modelo de simulación de eventos
discretos
● Estados del sistema
● Reloj de simulación
● Lista de Eventos LEV: Contiene el próximo tiempo en el que cada evento ocurrirá.
● Contadores Estadísticos: Variables que almacenan información estadística del
desempeño del sistema.
● Rutina de inicialización: Subprograma que inicializa el modelo en tiempo cero.
● Rutina de tiempo: Subprograma que determina el próximo evento en la lista de eventos
y actualiza el reloj al tiempo de cuando ocurrirá.
● Rutina de eventos: Subprograma que actualiza el estado del sistema cuando un evento
ocurre.
● Rutina de librería: Conjunto de subprogramas que generan observaciones aleatorias de
probabilidad que fueron determinadas como parte del modelo.
● Generador de reportes: Computa estimadores de las medidas de desempeño deseadas
y produce un reporte cuando la simulación termina.
● Programa principal: Invoca a la rutina de tiempos para determinar el próximo evento y
transfiere el control a la rutina de evento para que actualice el estado del sistema. Al
comprobar la terminación, invoca al generador de reportes.
7 de 25

8 de 25

M/M/1/∞/FIFO/∞
Sean las llegadas y los intervalos de tiempo de servicio variables aleatorias IID que
siguen la ley de Poisson y exponencial respectivamente, un único servidor atendiendo, una
población infinita, una disciplina de cola FIFO, y un número máximo de clientes en sistema
infinito. Se establecen las siguientes hipótesis:
1.  La probabilidad de que una unidad llegue al sistema en un intervalo de tiempo Δt es
infinitamente pequeña y del orden de Δt. Esta probabilidad es λΔt.
2.  La probabilidad de que se produzca un final de servicio en un intervalo de tiempo Δt es
infinitamente pequeña y del orden de Δt. Esta probabilidad es µΔt.
3.  La probabilidad de varias llegadas o servicios en el intervalo Δt es infinitamente
pequeña y se despreciará.
Nota: λ es la tasa de arribos mientras que µ es la tasa de servicio.
  Se formula además que λ/µ < 1, pues de lo contrario el sistema no sería estable.
  La probabilidad P (t+Δt) de que haya n unidades en el sistema (con n>0) puede
n
expresarse como la suma de las siguientes cuatro probabilidades:
1.  P n (t) . (1 - λΔt) . (1 - µΔt)         [había n, no llegó ni se fue ninguno]
2.  P n-1 (t) . (λΔt) . (1 - µΔt)          [había n-1, llegó uno, no se fue ninguno]
3.  P (t) . (1 - λΔt) . (µΔt)         [había n+1, no llegó ninguno, se fue uno]
n+1
4.  P (t) . (λΔt) . (µΔt)                [había n, llegó uno y se fue uno]
n
  Sumando las probabilidades se obtiene:
𝑃 (𝑡+𝛥𝑡) = 𝑃 (𝑡)∗(1−𝜆𝛥𝑡−µ𝛥𝑡+2𝜆µ𝛥𝑡2)+𝑃 (𝑡)∗(𝜆𝛥𝑡 −𝜆µ𝛥𝑡2)+𝑃 (𝑡)∗(µ𝛥𝑡
| 𝑛   |     | 𝑛   |     |     |     |     | 𝑛−1 |     |     | 𝑛+1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−𝜆µ𝛥𝑡2)
| 𝑃 (𝑡+𝛥𝑡)−𝑃 |     | (𝑡) |             |     |              |     |            |     |           |       |       |
| ---------- | --- | --- | ----------- | --- | ------------ | --- | ---------- | --- | --------- | ----- | ----- |
| 𝑛          |     | 𝑛   |             |     |              |     |            |     |           |       |       |
|            |     | =   | 𝜆𝑃 (𝑡) + µ𝑃 |     | (𝑡) − (𝜆+µ)𝑃 |     | (𝑡) + 𝜆µ𝛥𝑡 |     | [2𝑃 (𝑡)−𝑃 | (𝑡)−𝑃 | (𝑡)]  |
|            | 𝛥𝑡  |     | 𝑛−1         |     | 𝑛+1          |     | 𝑛          |     | 𝑛         | 𝑛−1   | 𝑛+1   |
  Como Δt→0, el último término se desprecia.
𝑑𝑃𝑛(𝑡)
| =   | 𝜆𝑃  | (𝑡)+µ𝑃 | (𝑡)−(𝜆+µ)𝑃 |     | (𝑡); 𝑛 | > 0 → A  |     |     |     |     |     |
| --- | --- | ------ | ---------- | --- | ------ | -------- | --- | --- | --- | --- | --- |
|     | 𝑛−1 |        | 𝑛+1        |     | 𝑛      |          |     |     |     |     |     |
𝑑𝑡
  Ahora hay que agregar la ecuación correspondiente al caso en que haya 0 unidades en
el sistema en el tiempo t+Δt, que es la suma de dos probabilidades:
1.  P 0 (t) . (1 - λΔt)
2.  P 1 (t) . (1 - λΔt) . (µΔt)
  Sumando:
|          |            |     | 𝑃 (𝑡+𝛥𝑡) |            | = 𝑃 (𝑡)∗(1−𝜆𝛥𝑡)+𝑃 |     |           | (𝑡)∗(µ𝛥𝑡)  |      |     |     |
| -------- | ---------- | --- | -------- | ---------- | ----------------- | --- | --------- | ---------- | ---- | --- | --- |
|          |            |     | 0        |            | 0                 |     |           | 1          |      |     |     |
|          |            |     |          | 𝑃 (𝑡+𝛥𝑡)−𝑃 |                   | (𝑡) |           |            |      |     |     |
|          |            |     |          | 0          | 0                 |     |           |            |      |     |     |
|          |            |     |          |            |                   | =   | 𝜆𝑃 (𝑡)+µ𝑃 |            | (𝑡)  |     |     |
|          |            |     |          |            | 𝛥𝑡                |     | 0         | 1          |      |     |     |
| 𝑑𝑃0(𝑡) = | −𝜆𝑃 (𝑡)+µ𝑃 |     | (𝑡) →B   |            |                   |     |           |            |      |     |     |
|          | 0          |     | 1        |            |                   |     |           |            |      |     |     |
𝑑𝑡
A y B constituyen un modelo para las colas con un servidor con llegadas poissoneanas
y tiempos de servicio exponenciales.
En el caso de que P  sea independiente de t, se dice que el proceso es estacionario y
n
| permanente. P |     | (t) = P | . Entonces, A y B quedan:  |       |        |         |     |      |     |     |     |
| ------------- | --- | ------- | -------------------------- | ----- | ------ | ------- | --- | ---- | --- | --- | --- |
|               |     | n       | n                          |       |        |         |     |      |     |     |     |
|               |     |         |                            | 𝐴: 𝜆𝑃 | +µ𝑃    | −(𝜆+µ)𝑃 |     | = 0  |     |     |     |
|               |     |         |                            |       | 𝑛−1    | 𝑛+1     |     | 𝑛    |     |     |     |
|               |     |         |                            |       | 𝐵: −𝜆𝑃 | +µ𝑃     | =   | 0    |     |     |     |
0 1
Procediendo por recurrencia y teniendo en cuenta que por definición ∑∞
|     |     |     |     |     |     |     |     |     |     |     | 𝑃 = 1:  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |
𝑛=0 𝑛
P 0  = P 0
9 de 25

P = λ/µ P
1 0
P = (λ/µ)2 P
2 0
En general, tenemos que 𝑃 = ( 𝜆 )𝑛 ∗𝑃 −−> 𝐶
𝑛 0
µ
∞
𝜆
∑ ( )𝑛 ∗𝑃 = 1
µ 0
𝑛=0
1
La parte hasta P es una serie geométrica infinita que converge en
0
1−𝜆/µ
1 𝜆 𝜆
∗𝑃 = 1 => 𝑃 = 1− ; 𝑐𝑢𝑎𝑛𝑑𝑜 < 1 −−> 𝐷
1−𝜆/µ 0 0 µ µ
Sustituyendo D en C:
𝜆 𝜆 𝜆
𝑃 = ( )𝑛 ∗(1− ); 𝑐𝑢𝑎𝑛𝑑𝑜 < 1−−> 𝑀𝑜𝑑𝑒𝑙𝑜 𝐺𝑒𝑛𝑒𝑟𝑎𝑙
𝑛 µ µ µ
La intensidad de tráfico, ρ, se calcula como λ/µ y 0 < ρ < 1
Medidas de desempeño
Número medio de clientes en el sistema (L)
∞ ∞
𝜆 𝜆
𝐿 = 𝐸(𝑛)= ∑ 𝑛∗𝑃 = ∑ 𝑛∗( )𝑛 ∗(1− )
𝑛 µ µ
𝑛=0 𝑛=0
Esto es una serie geométrica infinita de la forma ar + 2ar2 + 3ar3+..., donde a = 1-λ/µ y r = λ/µ.
𝑟
Converge en 𝑎∗
(1−𝑟2)
Por lo tanto:
𝜆 𝜆/µ 𝜆
𝐿 = (1− ) ∗ => 𝐿 =
µ 1−(𝜆/µ)2 µ−𝜆
Número medio de clientes en cola (Lq)
∞ ∞ ∞
𝐿 = ∑ (𝑛−1)∗𝑃 = ∑ 𝑛∗𝑃 − ∑ 𝑃
𝑞 𝑛 𝑛 𝑛
𝑛=2 𝑛=2 𝑛=2
∞ 1 ∞ 1
𝜆
𝐿 = ∑ 𝑛∗𝑃 −∑ 𝑛∗𝑃 −∑ 𝑃 + ∑ 𝑃 = −𝑃 −1+𝑃 +𝑃
𝑞 𝑛 𝑛 𝑛 𝑛 µ−𝜆 1 0 1
𝑛=0 𝑛=0 𝑛=0 𝑛=0
𝜆 𝜆 𝜆 2
𝐿 = − =
𝑞 µ−𝜆 µ µ∗(µ−𝜆)
Tiempo medio de espera en el sistema (W)
𝐿 1
𝑊 = =
𝜆 µ−𝜆
10 de 25

Tiempo medio de espera en cola (Wq)
𝐿𝑞 𝜆
𝑊 = =
𝑞 𝜆 µ∗(µ−𝜆)
Algoritmos M/M/1
Las medidas de rendimiento serán:
1. La demora promedio por cliente (definida como la demora total que hubo en cola
dividido la cantidad de clientes atendidos).
2. El tamaño promedio de la cola (definido como el área bajo la curva de tamaño de cola
en función del tiempo, dividido por el tiempo de simulación).
3. La utilización del servidor (definida como el área bajo la curva de utilización a través del
tiempo, dividida por el tiempo total de simulación).
Algoritmo principal
Inicialización
Mientras reloj < fin de simulación
Tiempos
Si evento seleccionado = "A" ir a Arribo
Sino ir a Partida
Fin Si
Fin Mientras
Reporte
11 de 25

Tiempos
Buscar en LEV el próximo evento
reloj = tiempo de próximo evento
Inicialización
Inicializar las variables AAQ, AAB, AAD, n, reloj, cli_at, TUE, S, TIOS
Inicializar el vector de tiempos de arribo VTA y la lista de eventos LEV
Generar tiempo de arribo ta
Guardar en LEV (A, ta)
Guardar en LEV (P,infinito)
Arribo
Si S="O"
AAQ = AAQ + (reloj - TUE) . n
n = n + 1
Guardar en VTA el reloj
Sino
S="O"
TIOS = reloj
cli_at = cli_at + 1
Generar tiempo de partida tp
Guardar en LEV(P, reloj + tp)
Fin Si
Generar tiempo de arribo ta
Guardar en LEV (A, reloj + ta)
Guardar TUE
Partida
Si n=0
S="D"
Sino
AAQ=AAQ + (reloj - TUE) . n
AAB = AAB + (reloj - TIOS)
AAD = AAD + reloj - VTA(arribo del cliente)
cli_at = cli_at + 1
n = n - 1
Generar tiempo de partida tp
Guardar en LEV(P, reloj + tp)
Fin Si
Guardar TUE
12 de 25

Reporte
Mostrar AAQ/reloj, AAB/reloj, AAD/cli_at
Análisis económico de los sistemas de colas
Claramente, mientras más servidores haya mejor será el servicio. Sin embargo, cada
servidor implica costos.
Modelo y análisis del sistema de colas actual
Supongamos que se tiene un sistema de reparación de máquinas en una fábrica. El
sistema es M/M/7 con µ=4 y λ=25. Luego de correr la simulación, se ve que el tiempo promedio
en el sistema para un cliente es de 0.48 y la cantidad de clientes en el sistema es de 12.1.
Ahora, cuál es el número de servidores que convendría tener? Se prueban escenarios
distintos con hasta 11 servidores para ver cómo evolucionan las variables.
Ahora que se sabe cómo evolucionan las variables, lo que resta averiguar son los
costos, para poder saber qué número de servidores (reparadores de máquinas) conviene tener.
Análisis de costos
Hay dos costos que considerar:
1. Costo por reparadores: Costo por hora para cada reparador * número de reparadores.
Como ejemplo, digamos que el costo por hora para cada reparador es $50.
2. Costo por no producción: Costo por hora por máquina fuera de operación * número
promedio de máquinas fuera de operación. Como ejemplo, digamos que el costo por
hora por una máquina no produciendo es de $100.
Con estos datos, se puede calcular el costo total (Costo por reparadores + Costo por no
producción) en cada uno de los escenarios (de 7 a 11 reparadores) y elegir el menos costoso.
Viendo la tabla, la mejor alternativa es tener 9 reparadores.
13 de 25

Simulación de un sistema de inventario
Componentes
● Tiempo entre demandas.
● Tamaño de demanda.
● Costo del pedido: K + i . Z; siendo K el costo base, i el costo incremental y Z la cantidad.
● Retardo del envío.
● Política estacionaria (s, S): define Z. Si I < s, Z = S-I; si I >= s, Z=0.
● I(t): Nivel de inventario.
● I+(t): Items en posesión en inventario. MAX (I(t), 0)
● I-(t): Items faltantes en inventario. MAX (-I(t), 0)
● h: Costo de mantenimiento de items por unidad de tiempo.
● Ī+: Items promedio para el n-ésimo período de tiempo. Ī+ = 1 ∗∫ 𝑛 𝐼+(𝑡).𝑑𝑡
𝑛 0
● Promedio de costo de mantenimiento por unidad de tiempo: Ī+ . h
● π: Costo de faltante de items por unidad de tiempo.
● Ī-: Items faltantes promedio para el n-ésimo período de tiempo. Ī− = 1 ∗∫ 𝑛 𝐼−(𝑡).𝑑𝑡
𝑛 0
● Promedio de costo por faltantes por unidad de tiempo: π . Ī-
Diagrama de flujo de las rutinas
14 de 25

Modelo de desencadenamiento de eventos
Se aplica antes de construir el modelo de simulación. Tiene el propósito de visualizar el
sistema a partir de sus eventos desde un alto nivel de abstracción, y descarta detalles del
sistema que quedan fuera de lo que son los eventos y cómo se desencadenan unos a otros
bajo determinadas condiciones. Los beneficios de aplicarlo son un modelado rápido y una clara
derivación del diseño de rutinas.
Nota: Control de inventario se autorreferencia, y Demanda también.
Medidas de desempeño
CCP: Costo de Cantidad Pedida = ACP / reloj; ACP: Acumulado de Cantidad Pedida
CUI: Costo de Unidades en Inventario = AIP.h / reloj; AIP: Acumulado Inventario Positivo
CUP: Costo de Unidades Perdidas = AIN . π / reloj; AIN: Acumulado Inventario Negativo
CMP: Costo Mensual Promedio = CCP + CUI + CUP
15 de 25

Algoritmos
Programa Principal
Inicialización
Mientras reloj <= fin de simulación
Tiempos
Ir a Evento Seleccionado
Fin Mientras
Reporte Parcial
Reporte Final
Inicialización
Setear variables iniciales AIP, AIN, ACP, CCP, CUI, CUP, TUE, reloj, I, i, h, k, π
Guardar en LEV (CI,0)
Generar tiempo entre demandas td
Guardar en LEV (D, td)
Guardar en LEV (AP,∞,0)
Control de Inventario
Si I < s
Calcular tamaño pedido Z = S - I
ACP = ACP + k + i . Z
Generar tiempo de AP tap
Guardar en LEV (AP, reloj + tap, Z)
Fin Si
Guardar en LEV (CI, reloj + 1)
Acumular áreas
Si I > 0
AIP = AIP + (reloj - TUE) . I
Sino si I < 0
AIN = AIN + (reloj - TUE) . I
Fin Si
Demanda
Acumular áreas
Generar cantidad de demandada cd
I = I - cd
Generar tiempo entre demandas ted
Guardar en LEV (D, reloj + ted)
Guardar TUE
16 de 25

Arribo de Pedido
Acumular Areas
I = I + Z
Guardar TUE
Reporte Parcial
Mostrar CMP = CCP + CUI + CUP
Reporte Final
Mostrar todos los promedios y terminar
Control de Inventario II (no está)
Análisis de resultados
Réplica o corrida es una ejecución del modelo en una ocasión. Como muy
probablemente si se corre el modelo nuevamente los valores en las variables sean distintos,
muchas veces es necesario efectuar un número de corridas independientes y obtener un
intervalo de confianza sobre el cual, con un determinado grado de seguridad, esté el verdadero
valor de la variable.
El estado transitorio se presenta al principio de la simulación, y es un período donde hay
mucha variación entre los valores de las variables. Una vez pasado el estado transitorio, se
llega al estado estable, donde los valores de las variables de decisión permanecen estables.
Comportamiento transiente y estado estacionario de un proceso
estocástico
Considerar la salida de un proceso estocástico y , y , …, y . Sea F (Y<=Y|I) para i:
1 2 n i i
1,2,..,n donde Y es un número real e I representa las condiciones iniciales utilizadas para
comenzar la simulación en tiempo cero. Llamamos a F la distribución transiente de un proceso
i
de salida en el tiempo discreto i para las condiciones iniciales I.
Si F(Y|I) ->F(y) cuando i->infinito para todo Y y cualquier condición I, F(y) es llamada
i
distribución en estado estacionario de los procesos de salida y , y , …, y .
1 2 n
En la práctica, el tiempo estacionario se dice que comienza en un tiempo K+1, a partir
del cual las variables aleatorios y , y , …,y tendrán aproximadamente la misma distribución.
k+1 k+2 n
Tipos de simulación
● Terminal: Existe un evento natural que indica el fin de una fase, a partir del cual
terminan las actividades del sistema. El desempeño del sistema depende fuertemente
de las condiciones iniciales. Las medidas de desempeño están referidas a un tiempo de
operación.
17 de 25

●  No terminal / Estacionaria: El sistema real opera de forma continua, sin un evento que
determina una fase. Las medidas de desempeño no están referidas a un tiempo
específico, ni se ven muy afectadas por las condiciones iniciales.
Análisis de resultados para simulaciones terminales
Sea n la cantidad de réplicas independientes a ejecutar. Se usan las mismas
condiciones iniciales en cada una. Se asume una única medida de desempeño, como por
ejemplo la demora promedio por cliente.
Sea x una variable aleatoria definida para la réplica j siendo j: 1,2,...,n, las x son IID.
j j
Se desea obtener un punto de estimación y un intervalo de confianza para la media
µ=E(x)
1.  Simular las n réplicas independientes tomando x 1 ,x 2 ,…, x n  como variables IID.
2.  Calcular la media muestral y la varianza muestral.
3.  Establecer un nivel de confianza de 100.(1-⍺)%
𝑆2(𝑛)
∗√
| 𝐼𝐶: 𝑋(𝑛) | ±𝑡        |  −−>  𝑃𝑟𝑜𝑐𝑒𝑑𝑖𝑚𝑖𝑒𝑛𝑡𝑜 𝑑𝑒 𝑚𝑢𝑒𝑠𝑡𝑟𝑎 𝑑𝑒 𝑡𝑎𝑚𝑎ñ𝑜 𝑓𝑖𝑗𝑜  |     |     |
| -------- | --------- | ---------------------------------------------- | --- | --- |
|          | 𝑛−1;1−𝛼/2 | 𝑛                                              |     |     |

Una desventaja de este método es que no se tiene control sobre la precisión de x̄(n)
Obteniendo una precisión específica
Precisión absoluta
Si la estimación de x̄ es tal que |x̄-µ|=𝛃, entonces se dice que x̄ tiene un error de 𝛃 al
estimar µ. El total de réplicas requeridas para tener un error absoluto de 𝛃 es:
𝑆2(𝑛)
|     | 𝑛∗(𝛽)= | 𝑀𝑖𝑛{𝑖 ≥ 𝑛 𝑡𝑎𝑙 𝑞𝑢𝑒  𝑡 | ∗√        | ≤ 𝛽}  |
| --- | ------ | -------------------- | --------- | ----- |
|     | 𝑎      |                      | 𝑖−1;1−𝛼/2 |       |
𝑖
Precisión relativa
Si el estimador de x̄ es tal que (x̄-µ)/µ = j, entonces decimos que x̄ tiene un error relativo
de j al estimar µ. El total de réplicas requeridas para obtener un error relativo de j es:
|               | 𝑡𝑖−1;1−𝛼/2∗√𝑆2 | (𝑛)                 |     |     |
| ------------- | -------------- | ------------------- | --- | --- |
| 𝑛∗(𝑗) = 𝑀𝑖𝑛{𝑖 | ≥ 𝑛 /          | 𝑖 ≤ 𝑗′}, donde  𝑗′= | 𝑗   |     |
𝑟
|     | 𝑥̄ (𝑛) |     | 1−𝑗 |     |
| --- | ------ | --- | --- | --- |
El objetivo es tener un estimador de µ con un error relativo de j, siendo 0<= j <1 y con
𝑆2(𝑛)
100*(1-⍺)% de confianza. Sea 𝛿(𝑛,𝛼)= 𝑡 ∗√  la semiamplitud del intervalo de
𝑛−1;1−𝛼/2
𝑖
confianza:
| 1.  Realizar n                            |  réplicas y fijar n = n | .         |     |     |
| ----------------------------------------- | ----------------------- | --------- | --- | --- |
|                                           | 0                       | 0         |     |     |
| 2.  Calcular x̄ y 𝛿(𝑛,𝛼)a partir de los x |                         | ,x ,...,x | .   |     |
1 2 n
18 de 25

𝛿(𝑛,𝛼)
3. Si ≤ 𝑗′, usar x̄ como estimador y parar. De lo contrario, incrementar en 1 la
𝑥̄
cantidad de réplicas y volver al paso 2.
Determinación del sesgo inicial
Consiste en eliminar cierta cantidad de observaciones al inicio de cada corrida y utilizar
las restantes para estimar µ. Se aplica a procesos estacionarios en los que es posible realizar
corridas largas y el sistema bajo estudio es continuo.
Media de lotes
Se basa en una corrida larga, por lo que el sesgo inicial se produce sólo una vez. Sea Y
una variable IID con valores Y , Y , …, Y; E(Y)=µ. Se asume que las primeras l observaciones
1 2 i i
fueron eliminadas y se está trabajando con Y , Y ,..., las cuales serán IID si l es lo
l+1 l+2
suficientemente grande.
Se realiza una corrida de longitud m y se dividen las observaciones resultantes en n
lotes de longitud K, o sea que m = n . k. Entonces el lote 1 consiste en Y , Y ,...,Y ; el lote 2
1 2 k
consiste en Y , Y ,...,Y , etc. Finalmente, se calcula el intervalo de confianza:
k+1 k+2 2k
𝑆2(𝑛)
𝑛 [𝑌𝑖(𝑘)−𝑌(𝑛,𝑘)]2
𝑌(𝑛,𝑘)±𝑡 ∗√ ; 𝑆2(𝑛) = ∑
𝑛−1;1−𝛼/2 𝑛 𝑛−1
𝑖=1
Múltiples medidas de rendimiento
Suponga que I es un intervalo de confianza con el 100.(1-a)% de confianza para la
s
medida de rendimiento µ (con s: 1,2,..,k), que puede ser de simulación terminal o no terminal.
s
La probabilidad de que todos los k intervalos de confianza contengan simultáneamente a sus
respectivas medidas de rendimiento satisface: 𝑃(𝜇 𝜖 𝐼 ; 𝑠:1,2,...,𝑘) ≥ 1−∑𝑘 𝛼 donde las I
𝑠 𝑠 𝑠=1 𝑠 s
pueden ser independientes o no. Este resultado es conocido como inecuación de Bonferroni.
Se recomienda que K<=10 y que ∑𝑘 𝛼 = 𝛼, es decir que la confianza total de nuestro
𝑠=1 𝑠
sistema sea la suma de las confianzas de todos los intervalos.
Números aleatorios comunes
Si nuestro objetivo es determinar diferencias en la respuesta del sistema cuando cambia
un parámetro, es razonable comparar las respuestas del sistema bajo las mismas condiciones.
Esto implica que los números aleatorios a usar para generar los tiempos de arribo y de servicio
deberían ser los mismos. Sea x̄ el tiempo de espera medio de una simulación al tiempo de
1
simulación 1; y sea x̄ lo mismo para el tiempo 2; entonces la varianza de la diferencia será:
2
𝑉𝑎𝑟(𝑥1−𝑥2) = 𝑉𝑎𝑟(𝑥1)+𝑉𝑎𝑟(𝑥2)−2∗𝐶𝑜𝑣(𝑥1,𝑥2)
Si se usan números aleatorios comunes, habrá correlación entre x̄1 y x̄2 y la varianza
de su diferencia será reducida por tener covarianza positiva.
19 de 25

Comparando sistemas alternativos
Intervalos de confianza para la diferencia de medidas de rendimiento
  Sean x , x ,…,x  con i =1 a 2 una muestra de n.i observaciones para el sistema i y sea
|     | i1  | i2  | in  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
µ=E(x i ij ) la esperanza matemática. Se desea construir un intervalo de confianza para𝜁=µ 1 -µ 2 .
Dependiendo de la independencia entre x 1j  y x 2j  se seleccionará el método de muestras
apareadas o el de muestras independientes.
Muestras apareadas
  Sean n =n  la cantidad de observaciones de los sistemas 1 y 2 (se pueden descartar
1 2
observaciones de un sistema para que queden iguales). Es posible aparear estas
observaciones x  y x  de manera z=x -x , con j:1,2,...,n. Entonces Z es variable aleatoria IID y
|     |     | 1j 2j |     | j 1j 2j |     |     |     |     |
| --- | --- | ----- | --- | ------- | --- | --- | --- | --- |
E(Z) = 𝜁. Para construir el intervalo de confianza t-apareado:
𝑛
|       |     |             |     | ∑𝑛 [𝑍𝑗−𝑍(𝑛)]2 |     |                |     |              |
| ----- | --- | ----------- | --- | ------------- | --- | -------------- | --- | ------------ |
|       |     | 𝑍𝑗          |     | 𝑗=1           |     |                |     |              |
| 𝑍(𝑛)= | ∑   | ; 𝑉𝑎𝑟(𝑍(𝑛)) |     | =             |     | =>  𝐼𝐶: 𝑍(𝑛)±𝑡 |     | ∗√𝑉𝑎𝑟(𝑍(𝑛))  |
𝑛−1;1−𝛼/2
|     |     | 𝑛   |     | 𝑛∗(𝑛−1) |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- |
𝑗=1
Si la distribución de los Z es normal, entonces el intervalo de confianza es exacto (es
j
decir, cubre 𝜁 con una confianza de 1-𝛼). De otra manera, tenemos que usar el teorema central
del límite, usando n alto para que la distribución de los Z se aproxime a la distribución normal.
Muestras independientes (Welch)
  Requiere que los X  sean independientes de los x  (además, x  debe tener distribución
|            |                          |     | 1j             |     |                    | 2j  | 1j  |     |
| ---------- | ------------------------ | --- | -------------- | --- | ------------------ | --- | --- | --- |
| normal). n |  puede ser distinto de n |     |                | .   |                    |     |     |     |
|            | 1                        |     |                | 2   |                    |     |     |     |
|            |                          |     |                |     | ∑𝑛 𝑖 [𝑋𝑖𝑗−𝑋𝑖(𝑛𝑖)]2 |     |     |     |
|            |                          | ∑𝑛𝑖 | 𝑋𝑖𝑗            |     | 𝑗= 1               |     |     |     |
|            | 𝑋𝑖(𝑛𝑖) =                 |     | ; 𝑉𝑎𝑟(𝑋𝑖(𝑛𝑖))= |     |                    |     |     |     |
|            |                          | 𝑗=1 | 𝑛𝑖             |     | (𝑛𝑖−1)             |     |     |     |
Ahora, calculamos los grados de libertad estimados:
|     |     |     |     | 𝑆2(𝑛1) |     | 𝑆2(𝑛2) |     |     |
| --- | --- | --- | --- | ------ | --- | ------ | --- | --- |
|     |     |     |     | [      | 1 + | 2 ]2   |     |     |
𝑛1 𝑛2
|     |     |     |     | 𝑓̂ =      |     |           |     |     |
| --- | --- | --- | --- | --------- | --- | --------- | --- | --- |
|     |     |     |     | [𝑆2(𝑛1)]2 |     | [𝑆2(𝑛2)]2 |     |     |
|     |     |     |     | 1         | +   | 2         |     |     |
|     |     |     |     | 𝑛1−1      |     | 𝑛2−1      |     |     |
Y finalmente definimos el IC:
|     |     |     |                     |     |          | 𝑆2(𝑛1) | 𝑆2(𝑛2) |     |
| --- | --- | --- | ------------------- | --- | -------- | ------ | ------ | --- |
|     |     |     |                     |     |          | ∗√ 1   | 2      |     |
|     |     |     | 𝐼𝐶: 𝑋1(𝑛1)−𝑋2(𝑛2)±𝑡 |     | 𝑓̂,1−𝛼/2 |        | +      |     |
|     |     |     |                     |     |          | 𝑛1     | 𝑛2     |     |
|     |     |     |                     |     |          |        |        |     |
20 de 25

Generador Congruencial Lineal
Teniendo los parámetros m (generalmente mayor a 109), a < m, c < m, y Z (llamado
0
semilla) < m, se define el generador como:
𝑍 = (𝑎∗𝑍 +𝑐) 𝑚𝑜𝑑 𝑚, y 𝑈 = 𝑍 /𝑚
𝑖 𝑖−1 𝑖 𝑖
Aunque es un método determinístico, a través de una cuidadosa selección de
parámetros se puede inducir a los Zi a comportarse de forma tal que los Ui obtenidos parezcan
variables aleatorias IID al ser sometidos a ciertos tests estadísticos. Es inevitable observar un
comportamiento cíclico en los números generados debido a la naturaleza del generador. La
longitud del ciclo, p, se denomina período y cuando p=m el generador es de período completo.
Es deseable escoger valores de m, a y c para tener período completo y un m lo suficientemente
grande como para evitar que haya ciclos en la cantidad deseada de números generados.
Teorema: Un GLC es de período completo si y sólo si cumple con las siguientes
condiciones:
1. m y c tienen un único divisor común que es 1.
2. Si q es un número primo que divide a m, también tiene que dividir a a-1.
3. Si 4 divide a m, entonces también divide a a-1.
Un GLC puede ser de tres tipos:
1. Mixto: completo como el visto arriba.
2. Aditivo (a=1).
3. Multiplicativo (c=0).
Tests para generadores de números aleatorios
Test de chi-cuadrado
Se divide el intervalo [0,1] en k subintervalos y se generan n números aleatorios. Como
regla general, k>=100 y n/k >= 5.
Para j:1,2,..,k sea Fj la cantidad de números aleatorios que se encuentran en el
subintervalo j. Sea:
𝑘
𝑘 𝑛
𝑋2 = ∗∑ (𝐹 − )2
𝑛 𝑗 𝑘
𝑗=1
Entonces, para un valor grande de n, la distribución de X2 se aproxima a la distribución
de chi-cuadrado con k-1 grados de libertad bajo la hipótesis nula de que Ui es variable aleatoria
IID. Podemos descartar esta hipótesis a un nivel 𝛼si 𝑋2 > 𝑋2 , donde 𝑋2 es el valor
𝑘−1,1−𝛼 𝑘−1,1−𝛼
crítico superior de la distribución de chi-cuadrado con k-1 grados de libertad.
Test de serie (uniformidad)
Es una generalización del test de chi-cuadrado para mayores dimensiones. Si los Ui
fueran realmente variables aleatorias IID, las d-tuplas no superpuestas U1=(U1,U2,...,Ud),
U2=(Ud+1, Ud+2,...,U2d), etc deberían ser vectores aleatorios uniformemente distribuidos en el
21 de 25

hipercubo d-dimensional [0,1]d. Se divide el intervalo [0,1] en k subintervalos de igual amplitud y
se generan los vectores U1, U2,...,Un (requiriendo generar entonces n.d números).
Sea F ,F ,...,F el número de vectores U que tienen primer componente en el
j1 j2 jd
subintervalo j1, segundo componente en el intervalo j2, etc. Sea 𝑋2 =
𝑘𝑑
∗∑𝑑 ∗∑𝑑 ∗
𝑛 𝑗1=1 𝑗2=1
...∗∑𝑑 (𝐹 − 𝑛 )2, 𝑋2(𝑑)tendrá una distribución aproximada a la de chi-cuadrado con
𝑗𝑑=1 𝑗1,𝑗2,...,𝑗𝑑 𝑘𝑑
kd-1 grados de libertad (se recomienda n/kd >=5).
Este test se lleva a cabo de la misma forma que el de chi-cuadrado unidimensional.
Test empírico de corridas (independencia)
1. Generar los Ui con i=1,2,..,n, siendo n>=4000.
2. Examinar los Ui generados identificando subsecuencias crecientes y continuas de Ui de
longitud máxima.
𝐶𝑎𝑛𝑡 𝑑𝑒 𝑠𝑢𝑏𝑠𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎𝑠 𝑑𝑒 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 𝑖
3. Calcular 𝑟 = ; 𝑖:1,2,3,4,5
𝑖
𝐶𝑎𝑛𝑡 𝑑𝑒 𝑠𝑢𝑏𝑠𝑒𝑐𝑢𝑒𝑛𝑐𝑖𝑎𝑠 𝑑𝑒 𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 ≥ 6
4. Calcular la variable chi-cuadrado 𝑅 = 1 ∗∑6 ∗∑6 𝑎 ∗(𝑟 −𝑛∗𝑏 )∗(𝑟 −𝑛∗𝑏 )
𝑛 𝑖=1 𝑗=1 𝑖𝑗 𝑖 𝑖 𝑗 𝑗
5. Comparar 𝑋2> 𝑋2 , donde 𝑋2 es el valor de la tabla de chi-cuadrado con 6 grados
6,1−𝛼 6,1−𝛼
de libertad y confianza de 1-𝛼. Si la desigualdad se comprueba, entonces se rechaza la
hipótesis nula de que los números aleatorios generados son independientes.
Naylor capítulo 4: Generación de variables estocásticas
empleadas en simulación
Método de transformación inversa
Si queremos generar números aleatorios que sigan una distribución cuya función de
densidad está dada por f(x), debemos obtener la función de distribución acumulativa F(x). F(x)
va a estar definida entre 0 y 1, por lo que podemos generar un número aleatorio uniformemente
distribuido entre 0 y 1, asignarlo a r = F(x), conseguir el valor de x correspondiente, y finalmente
calcular f(x) para obtener el número definido por la distribución deseada.
𝑥̄
r = F(x) = ∫ 𝑓(𝑡) 𝑑𝑡, x = F-1(r )
−∞ 0 0
Desafortunadamente, para muchas distribuciones resulta difícil o incluso imposible
expresar a x en términos de F-1(r), por lo que este método en algunos casos no puede
utilizarse, y en otros requiere hacer aproximaciones.
Método de rechazo
Se puede usar si f(x) es acotada y x tiene un rango finito entre a y b. Los pasos son:
1. Normalizar f mediante un factor c, tal que c.f(x) <=1
2. Definir x como función lineal de r: x = a+(b-a).r
3. Generar parejas de números aleatorios (r1,r2)
4. Siempre que se satisfaga que r2<= c.f(a+(b-a).r1), el par será aceptado, siendo x =
c.f(a+(b-a).r1) el valor generado.
22 de 25

Este método se basa en que P(r<=c.f(x)) = c.f(x)
Tocher demostró que la esperanza matemática del número de intentos necesarios para
conseguir una pareja exitosa es de 1/c, por lo que este método puede resultar muy ineficiente
en ocasiones.
Método de composición
Consiste en expresar f(x) como una mezcla probabilística de n funciones de densidad
g (x), seleccionadas adecuadamente. f(x)=∑ 𝑔𝑛.𝑃𝑛. Para elegir las g (x), se considera la
n n
bondad de ajuste y el objetivo de minimizar ∑ 𝑇𝑛.𝑃𝑛, siendo Tn el tiempo de computación
esperado para generar valores a partir de g (x).
n
Generación de valores de variables aleatorias con distribución continua
Distribución uniforme
1
𝑓(𝑥) = { 𝑠𝑖 𝑎 ≤ 𝑥 ≤ 𝑏; 0 𝑠𝑖 𝑥 𝑒𝑠𝑡á 𝑓𝑢𝑒𝑟𝑎 𝑑𝑒𝑙 𝑖𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜
𝑏−𝑎
𝑥̄ 1 𝑥̄−𝑎
Entonces r = F(x) = ∫ .𝑑𝑡 = ; 0 ≤ 𝐹(𝑥) ≤ 1
𝑎 𝑏−𝑎 𝑏−𝑎
x = 𝐹−1(𝑟) = 𝑟(𝑏−𝑎) + 𝑎; 𝑠𝑖𝑒𝑛𝑑𝑜 0 ≤ 𝑟 ≤ 1
Se generan los números r para conseguir los valores x y luego se hace f(x) para
conseguir el valor de la variable aleatoria con distribución uniforme.
Distribución exponencial
Suposiciones:
1. La probabilidad de que ocurra un evento en Δt es 𝛼𝛥𝑡
2. 𝛼es constante y no depende de t ni ningún otro factor.
3. Se desprecia la probabilidad de que haya más de un evento en 𝛥𝑡.
Una variable aleatoria X tiene una distribución exponencial si su función de densidad
f(x) = 𝛼.𝑒−𝛼𝑥̄,𝑐𝑜𝑛 𝛼 > 0 𝑦 𝑥 ≥ 0
La distribución acumulativa entonces es 𝐹(𝑥) = ∫ 𝑥̄ 𝛼.𝑒−𝛼𝑡.𝑑𝑡 = 1− 𝑒−𝛼𝑡. Como la
0
distribución es simétrica, F(x) = 1 - F(x) por lo que r = 1−(1−𝑒−𝛼𝑡) = 𝑒−𝛼𝑡.
Consecuentemente, 𝐹−1(𝑟) = 𝑥 = − 1 .𝑙𝑜𝑔(𝑟)
𝛼
Distribución Gamma
Si un proceso consiste en k eventos sucesivos y el total de tiempo transcurrido es la
suma de k valores independientes de la variable aleatoria con distribución exponencial (cada
uno con su 𝛼), la distribución de esta suma será la de una distribución gamma con parámetros
k y 𝛼. Si siempre es el mismo 𝛼, se llama distribución de Erlang.
𝛼 𝑘.𝑥𝑘−1.𝑒−𝛼𝑘
𝑓(𝑥) = ,𝑐𝑜𝑛 𝛼 > 0,𝑘 > 0,𝑦 𝑥 > 0
(𝑘−1)!
Si k=1, la distribución es exponencial.
23 de 25

No hay función de distribución acumulativa F(x) para este caso, por lo que hay que usar
métodos alternativos.
Si la distribución es de Erlang, se puede hacer la suma de los k valores con distribución
−1
| exponencial, siendo entonces 𝑥 |     |     |     | =   | ∑𝐾  | 𝑥 = .∑𝐾 | 𝑙𝑜𝑔 𝑟  |
| ------------------------------ | --- | --- | --- | --- | --- | ------- | ------ |
|                                |     |     |     |     | 𝑖=1 | 𝑖       | 𝑖=1 𝑖  |
𝛼
Distribución normal
  Gracias al teorema del límite central, que dice que la suma de N valores igualmente
distribuidos con media µ y varianza 𝜎2tiene una distribución que se aproxima a la normal
|                           |     |     | i   |     | 𝑖   |              |       |
| ------------------------- | --- | --- | --- | --- | --- | ------------ | ----- |
|                           |     |     |     | ∑𝑁  |     |    𝑦   𝜎2 ∑𝑁 | 𝜎2.   |
| cuando N es grande, con µ |     |     |     | =   | µ   | =            |       |
|                           |     |     |     | 𝑖=1 | 𝑖   |              | 𝑖=1 𝑖 |
  En esta distribución tampoco existe la función de distribución acumulariva F(x), así que
se puede usar una interpretación del teorema del límite central y hacer una suma de K valores
1
de variable aleatoria distribuidos uniformemente entre 0 y 1. Los µ serán ½ y 𝜎2 = , por lo
𝑖 𝑖
√12
|     | ∑𝐾 𝑟𝑖−𝐾/2 |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- |
que 𝑧 = 𝑖=1 , pero como z tiene una distribución normal estándar, nos queda
√𝐾/12
1/2
| 𝑥   | =𝜎 .( 12 ) | .(∑𝐾 | 𝑟   | −𝐾/2)+µ | .   |     |     |
| --- | ---------- | ---- | --- | ------- | --- | --- | --- |
|     | 𝑥̄         | 𝑖=1  | 𝑖   |         | 𝑥̄  |     |     |
𝐾
  Se recomienda que K sea 24 o mayor.
  Existen también otros métodos, el procedimiento directo y el procedimiento rápido.
Distribución normal multivariada
Distribución logarítimica normal
Generación de valores de variables aleatorias con distribución discreta
  En estas probabilidades, 𝐹(𝑥) = 𝑃(𝑋 ≤ 𝑥) = ∑𝑥̄ 𝐹(𝑥), donde f(x) es la función de
𝑋=0
densidad de X definida por valores enteros: f(x) = P(X=x) con x=0, 1, 2,...
Distribución geométrica
  Consiste en describir cuántos fracasos se observaron en una serie de ensayos de
Bernoulli antes de que llegue el primer evento exitoso, teniendo una probabilidad de éxito p y
una probabilidad de fracaso q = 1-p.
|     |     |     |     |     | 𝑓(𝑥) = | 𝑝.𝑞𝑥̄,𝑐𝑜𝑛 𝑥 | = 0,1,2...,𝑥  |
| --- | --- | --- | --- | --- | ------ | ----------- | ------------- |
𝑥̄
|     |     |     |     | 𝐹(𝑥) | = ∑ | 𝑝.𝑞𝑥̄,𝑐𝑜𝑛 𝑋 | = 0,1,2,...,𝑥  |
| --- | --- | --- | --- | ---- | --- | ----------- | -------------- |
𝑋=0
Como P(X>x) = 1- F(x) => P(X>0) = q, y 1-F(x)=𝑞 𝑥̄+1
𝑙𝑜𝑔 𝑟
| r=𝑞𝑥̄ | => 𝑥 = |     |     |     |     |     |     |
| ----- | ------ | --- | --- | --- | --- | --- | --- |
𝑙𝑜𝑔 𝑞
Distribución binomial
  Variables aleatorias que definen el número de ensayos exitosos en una sucesión de n
ensayos independientes de Bernoulli, cada uno con probabilidad de éxito p.
𝑛𝐶𝑥.𝑝𝑥̄.𝑞𝑛−𝑥̄, siendo x=0,1,2,...,n y q=1-p
𝑓(𝑥) =
24 de 25

  Se pueden generar de varios modos, siendo el más simple el del método de rechazo:
| 1.  Fijar x 0 =0                       |     |                          |              |     |     |     |
| -------------------------------------- | --- | ------------------------ | ------------ | --- | --- | --- |
| 2.  Generar un r, y si r<=p entonces x | i i | i  = x i - 1 +1. Sino, x | i  = x i - 1 | .   |     |     |
3.  Al llegar a n números generados, x  será el valor de la variable aleatoria con distribución
n
binomial.
Distribución hipergeométrica
  Si hay N elementos, dentro de los cuales N.p son de una clase (clase 1) y N.q son de
otra (clase 2), siendo p+q=1, al tomar una muestra de n, el número de elementos que serán de
clase 1 tendrá una distribución hipergeométrica.
|        | 𝐶  ∗       | 𝐶          |                     |     |       |     |
| ------ | ---------- | ---------- | ------------------- | --- | ----- | --- |
|        | 𝑁.𝑝 𝑥̄ 𝑁.𝑞 | 𝑛−𝑥̄       |                     |     |       |     |
| 𝑓(𝑥) = |            | ,    𝑐𝑜𝑛 0 | ≤ 𝑥 ≤ 𝑁.𝑝    𝑦    0 |     | ≤ 𝑛 − | 𝑥   |
𝐶
𝑁 𝑛
≤ 𝑁.𝑞,   𝑠𝑖𝑒𝑛𝑑𝑜 𝑥,𝑛 𝑦 𝑁 𝑒𝑛𝑡𝑒𝑟𝑜𝑠
  Para generarlos, se puede alterar el método que se usa para la distribución binomial,
|     |     |     |     | 𝑛   | ∗𝑝 − 𝑆 |     |
| --- | --- | --- | --- | --- | ------ | --- |
haciendo que p varíe según la iteración en la que está, haciendo 𝑝 = 𝑖−1 𝑖−1
𝑖
|     |     |     |     |     | 𝑁 −1 |     |
| --- | --- | --- | --- | --- | ---- | --- |
𝑖−1
Distribución de Poisson
  Si tomamos n ensayos de Bernoulli con p muy pequeña, a medida que n tiende a
infinito, la probabilidad de x ocurrencias sigue la distribución de Poisson.
𝜆𝑥̄
𝑒−𝜆.
| 𝑓(𝑥) | = , 𝑥 | = 0,1,2...    𝑦  𝜆 | > 0, | 𝑠𝑖𝑒𝑛𝑑𝑜 𝜆 | = 𝑛.𝑝  |     |
| ---- | ----- | ------------------ | ---- | -------- | ------ | --- |
𝑥!
  Para generar una distribución de Poisson con parámetro 𝜆, aprovechamos la relación
entre la distribución de Poisson y la exponencial: si la ocurrencia de eventos es independiente a
ocurrencias anteriores y la probabilidad de ocurrencia en 𝛥𝑡es 𝜆𝛥𝑡 para todo t, entonces
=𝜆.𝑒−𝜆𝑡      (función de densidad del intervalo entre ocurrencias, de tipo
1.  𝑓(𝑡)
exponencial)
(𝜆 .𝑡)𝑥
| 𝑓(𝑥) = | 𝑒−𝜆 𝑡. |     |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- | --- |
2.  , para toda t y toda x
𝑥̄!
Entonces, si los eventos siguen una distribución de Poisson con valor esperado 𝜆, el
tiempo entre eventos sigue una distribución exponencial con valor esperado 1/𝜆.
  Por lo tanto, para generar valores de variable aleatoria con distribución de Poisson, se
generan intervalos t con distribución exponencial con valor esperado = 1 y se suman hasta que
i
la suma sea mayor a 𝜆. Matemáticamente: 𝑥 𝑡𝑎𝑙 𝑞𝑢𝑒∑𝑥̄  𝜆 < ∑𝑥̄+1
|     |     |     | 𝑡  ≤  |     | 𝑡 , 𝑑𝑜𝑛𝑑𝑒 𝑡 |  =  |
| --- | --- | --- | ----- | --- | ----------- | --- |
|     |     |     | 𝑖=0 𝑖 | 𝑖=0 | 𝑖           | 𝑖   |
−𝑙𝑜𝑔 𝑟
𝑖
Distribuciones discretas empíricas
Cadenas discretas de Markov
Series de tiempo autocorrelacionadas
25 de 25