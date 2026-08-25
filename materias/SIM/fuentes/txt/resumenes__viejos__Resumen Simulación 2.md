# Simulación

## Índice

[Simulación](#_4vnles3yddni) 4

[Sistemas, modelos y simulación](#_hqbboksx8gcv) 4

[Experimentar con el sistema contra experimentar con el modelo](#_kbky8gf7wyq) 4

[Modelo físico contra modelo matemático](#_pd5dyix82tsz) 4

[Solución analítica contra simulación](#_2459uof63edg) 4

[Ventajas y desventajas de la simulación](#_jgvcfo5ibxlh) 5

[Ventajas](#_phxgiv5voj1h) 5

[Desventajas](#_gog0v0s2yob4) 5

[10 pasos para realizar un estudio de simulación](#_b51xdz7457p3) 6

[Simulación de eventos discretos](#_9rls4464xvso) 7

[Mecanismo de avance en el tiempo](#_hl286ukrilvp) 7

[Componentes y Organización de un modelo de simulación de eventos discretos](#_7t0w893jrkzq) 7

[M/M/1/∞/FIFO/∞](#_c1sc5pnsjiup) 9

[Medidas de desempeño](#_ltohze8sfxiv) 10

[Número medio de clientes en el sistema (L)](#_xakls8fov0lo) 10

[Número medio de clientes en cola (Lq)](#_wljupao741zu) 10

[Tiempo medio de espera en el sistema (W)](#_dwfg0xq8d3p8) 10

[Tiempo medio de espera en cola (Wq)](#_118704lz1f1) 10

[Algoritmos M/M/1](#_n2d7rwtein7d) 11

[Algoritmo principal](#_41kwgpq334ov) 11

[Tiempos](#_clxkx79q01ai) 11

[Inicialización](#_ve0mhhn3tjsr) 12

[Arribo](#_5nw2cpirj6dn) 12

[Partida](#_uuo3fr1u1kj7) 12

[Reporte](#_b66n1141sgs8) 12

[Análisis económico de los sistemas de colas](#_c70ygf628obf) 13

[Modelo y análisis del sistema de colas actual](#_r8g5b2i63t7q) 13

[Análisis de costos](#_swv2uecx1w4d) 13

[Simulación de un sistema de inventario](#_smms2n471bjn) 14

[Componentes](#_iufew1nm0fd5) 14

[Diagrama de flujo de las rutinas](#_t3rxux81ghxn) 14

[Modelo de desencadenamiento de eventos](#_evol3dn3xbae) 15

[Medidas de desempeño](#_hbly2zrthi8p) 15

[Algoritmos](#_uvvhk587r77q) 15

[Programa Principal](#_ux5pf443uu8n) 16

[Inicialización](#_gf2xe0w7giqo) 16

[Control de Inventario](#_yvt6lga7r0e) 16

[Acumular áreas](#_adbid1prglcf) 16

[Demanda](#_ksoakfgqrjnh) 16

[Arribo de Pedido](#_sfhd5yriad6q) 17

[Reporte Parcial](#_ha51i7acfhlh) 17

[Reporte Final](#_eh4i6ytvcq40) 17

[Control de Inventario II (no está)](#_27pno9uglig6) 17

[Análisis de resultados](#_1p1d1acipzgc) 17

[Comportamiento transiente y estado estacionario de un proceso estocástico](#_fqi01dm2i1nt) 17

[Tipos de simulación](#_rzsarhe5cjti) 17

[Análisis de resultados para simulaciones terminales](#_r9i7vhhrn49t) 18

[Obteniendo una precisión específica](#_wawj9grhewjp) 18

[Precisión absoluta](#_l50oar7ci36h) 18

[Precisión relativa](#_m1m3f1n941v) 18

[Determinación del sesgo inicial](#_dxkvqt6g9m5d) 18

[Media de lotes](#_lgfc46237v5i) 19

[Múltiples medidas de rendimiento](#_v4ykunfoqt1u) 19

[Números aleatorios comunes](#_5xvs12bgh0mr) 19

[Comparando sistemas alternativos](#_ee9vbnoi2o0v) 19

[Intervalos de confianza para la diferencia de medidas de rendimiento](#_1vzhzf2idwsy) 20

[Muestras apareadas](#_85poialkvxxq) 20

[Muestras independientes (Welch)](#_gzxoliyjtouq) 20

Z[Generador Congruencial Lineal](#_jqeqx2k81hnu) 20

[Tests para generadores de números aleatorios](#_mye508oh66q8) 21

[Test de chi-cuadrado](#_3osyjdlcwgv4) 21

[Test de serie (uniformidad)](#_wy8ieids2oyj) 21

[Test empírico de corridas (independencia)](#_75oycoe192m9) 22

[Naylor capítulo 4: Generación de variables estocásticas empleadas en simulación](#_pwbh4d612gs3) 22

[Método de transformación inversa](#_hyloh3gkdql7) 22

[Método de rechazo](#_iyq75frcmjk8) 22

[Método de composición](#_l6bq5bn7vuf4) 23

[Generación de valores de variables aleatorias con distribución continua](#_kyvjkej6ontn) 23

[Distribución uniforme](#_vpa9vwjhqogl) 23

[Distribución exponencial](#_lhe4cqj0rgul) 23

[Distribución Gamma](#_vzlh8zl09kd7) 23

[Distribución normal](#_1m1fyd5625jl) 24

[Distribución normal multivariada](#_32fujw8yhr5b) 24

[Distribución logarítimica normal](#_32fujw8yhr5b) 24

[Generación de valores de variables aleatorias con distribución discreta](#_145uzhp0y5z) 24

[Distribución geométrica](#_t8sna1dlj5b1) 24

[Distribución binomial](#_ottunwe0m1sp) 25

[Distribución hipergeométrica](#_rvpsv5150kne) 25

[Distribución de Poisson](#_dsaajhd73y8p) 25

[Distribuciones discretas empíricas](#_4il58aj9rb9b) 26

[Cadenas discretas de Markov](#_4il58aj9rb9b) 26

[Series de tiempo autocorrelacionadas](#_g66sgwbkk0cv) 26

##

## Simulación

### Sistemas, modelos y simulación

Un sistema es una colección de entidades que interactúan para lograr un objetivo lógico. Los sistemas pueden ser discretos, cuando sus variables cambian instantáneamente en puntos de tiempo separados, o continuos, cuando sus variables de estado cambian continuamente respecto del tiempo.

El estado del sistema es una colección de variables necesarias para describir el sistema en un momento particular.

La simulación es una técnica que permite analizar un modelo numérico en un periodo de tiempo y recolectar datos que permitan estimar el verdadero comportamiento del modelo. Se puede clasificar según 3 dimensiones:

* Discreta/Continua: Dependiendo el tipo de sistema que se quiera simular.
* Estática/Dinámica: La primera implica una representación del sistema en un momento particular, mientras que la segunda es de un sistema que evoluciona en el tiempo.
* Determinística/Estocástica: en la primera no hay ningún componente de entrada probabilístico mientras que en la segunda sí.

#### Experimentar con el sistema contra experimentar con el modelo

Si es posible y no costoso alterar el sistema físicamente y hacerlo operar bajo las nuevas condiciones, probablemente sea lo mejor. Sin embargo, esto pocas veces sucede. Generalmente es muy costoso o disruptivo intentar alterar el sistema, o incluso el sistema puede no existir en el mundo real todavía. Por eso, normalmente se usan los modelos.

#### Modelo físico contra modelo matemático

Muchas veces armar un modelo físico (o icónico) que intente replicar lo más cercanamente posible el sistema real puede ser útil, pero no es típicamente el tipo de modelo que se utilice en análisis de sistemas. La mayoría de los modelos son matemáticos, representando al sistema con relaciones lógicas y cuantitativas que se manipulan y cambian para entender cómo reacciona el modelo (y por consiguiente cómo reaccionaría el sistema, si está bien hecho el modelo).

#### Solución analítica contra simulación

Una vez construido el modelo matemático, debe usarse para responder las preguntas de interés sobre el sistema que supuestamente representa. Si el modelo es simple, pueden usarse métodos matemáticos para responder estas preguntas y así llegar a las llamadas soluciones analíticas. Por otro lado, cuando los sistemas son complejos y/o no hay métodos matemáticos que se pueda o convenga aplicar, el estudio debe darse a través de la simulación.

![](data:image/png;base64...)

### Ventajas y desventajas de la simulación

#### Ventajas

* No necesita llevar a cabo en la realidad los procesos para conocer su impacto.
* Mejora el conocimiento del proceso actual al permitir analizar su comportamiento en distintos escenarios.
* Puede utilizarse como medio de capacitación para la toma de decisiones.
* Es más económico realizar una simulación que cambiar procesos reales.
* Permite probar varios escenarios en busca de las mejores condiciones de trabajo de los procesos simulados.
* En problemas de gran complejidad la simulación permite generar una buena solución.

#### Desventajas

* Aunque muchas herramientas permiten obtener el mejor escenario a partir de una combinación de variaciones posibles, la simulación no es una herramienta de optimización.
* Puede ser costosa cuando se quiere emplearla en problemas sencillos, en lugar de utilizar soluciones analíticas.
* Se requiere bastante tiempo para realizar un buen estudio de simulación.
* Es preciso dominar la herramienta de simulación y tener sólidos conocimientos de estadística para interpretar los resultados.

### 10 pasos para realizar un estudio de simulación

1. **Definición del sistema bajo estudio**: Se definen las variables de decisión, las interacciones entre ellas y se establece el alcance y limitaciones del modelo.
2. **Generación del modelo de simulación base**: No es necesario que sea un modelo muy detallado, pero sí es necesario empezar a volcar el modelo conceptual a la computadora. También se define la manera en la que se van a visualizar las variables de decisión.
3. **Recolección y análisis de datos**: Consiste en recopilar información estadística de las variables aleatorias que se van a utilizar en el modelo, para poder determinar qué distribución se usará para generar los valores de cada una.
4. **Generación del modelo preliminar:** Se integra la información obtenida en el análisis de datos, los supuestos y otros datos para tener un modelo lo más cercano posible a la realidad del problema bajo estudio.
5. **Verificación del modelo:** Una vez que se han identificado las distribuciones y se han implantado los supuestos, se verifican los datos para comprobar que la programación y los parámetros usados funcionen correctamente.
6. **Validación del modelo**: Consiste en realizar una serie de pruebas al modelo, utilizando información de entrada real para observar su comportamiento y analizar los resultados.
7. **Generar el modelo final**: Con el modelo validado, el analista está listo para realizar la simulación y estudiar el comportamiento del proceso. Si se comparan escenarios diferentes, el generado aquí es el modelo raíz.
8. **Determinación de los escenarios**: Tras validar el modelo, se acuerdan con el cliente los escenarios a analizar. Una manera sencilla de determinarlos consiste en utilizar un escenario pesimista, uno intermedio y uno optimista.
9. **Análisis de sensibilidad**: Una vez que se obtienen los resultados de los escenarios es importante realizar pruebas estadísticas que permitan comparar los escenarios con los mejores resultados finales. Si dos intervalos de confianza de la misma variable se solapan, es estadísticamente incorrecto suponer que uno es mejor que el otro, por lo que habría que aumentar la cantidad de corridas y/o el tiempo de simulación de cada una.
10. **Documentación del modelo, sugerencias y conclusiones**: Una vez hecho análisis de resultados, es necesario documentar el modelo. Hay que incluir los supuestos del modelo, las distribuciones de las variables aleatorias, los alcances y limitaciones, y en general las consideraciones de programación. También se incluyen sugerencias sobre el uso del modelo y sobre los resultados obtenidos. Por último, se presentan conclusiones del proyecto.

##

## Simulación de eventos discretos

Un evento es una ocurrencia instantánea que puede cambiar el estado del sistema.

### Mecanismo de avance en el tiempo

Mientras la simulación proceda, debemos hacer un seguimiento del valor actual del tiempo simulado y necesitamos un mecanismo que permita avanzar este tiempo de un valor a otro. La variable que da el valor actual del tiempo se llama reloj de simulación, y para avanzarlo hay dos métodos:

* Avance en intervalos fijos.
* Avance al próximo evento: el reloj es inicializado en cero y se calculan los tiempos de ocurrencia de los eventos. Entonces, el reloj avanza al tiempo de ocurrencia del próximo evento, se actualiza el estado del sistema y se actualizan los tiempos de eventos futuros.

### Componentes y Organización de un modelo de simulación de eventos discretos

* Estados del sistema
* Reloj de simulación
* Lista de Eventos LEV: Contiene el próximo tiempo en el que cada evento ocurrirá.
* Contadores Estadísticos: Variables que almacenan información estadística del desempeño del sistema.
* Rutina de inicialización: Subprograma que inicializa el modelo en tiempo cero.
* Rutina de tiempo: Subprograma que determina el próximo evento en la lista de eventos y actualiza el reloj al tiempo de cuando ocurrirá.
* Rutina de eventos: Subprograma que actualiza el estado del sistema cuando un evento ocurre.
* Rutina de librería: Conjunto de subprogramas que generan observaciones aleatorias de probabilidad que fueron determinadas como parte del modelo.
* Generador de reportes: Computa estimadores de las medidas de desempeño deseadas y produce un reporte cuando la simulación termina.
* Programa principal: Invoca a la rutina de tiempos para determinar el próximo evento y transfiere el control a la rutina de evento para que actualice el estado del sistema. Al comprobar la terminación, invoca al generador de reportes.

![](data:image/png;base64...)

##

## M/M/1/∞/FIFO/∞

Sean las llegadas y los intervalos de tiempo de servicio variables aleatorias IID que siguen la ley de Poisson y exponencial respectivamente, un único servidor atendiendo, una población infinita, una disciplina de cola FIFO, y un número máximo de clientes en sistema infinito. Se establecen las siguientes hipótesis:

1. La probabilidad de que una unidad llegue al sistema en un intervalo de tiempo Δt es infinitamente pequeña y del orden de Δt. Esta probabilidad es λΔt.
2. La probabilidad de que se produzca un final de servicio en un intervalo de tiempo Δt es infinitamente pequeña y del orden de Δt. Esta probabilidad es µΔt.
3. La probabilidad de varias llegadas o servicios en el intervalo Δt es infinitamente pequeña y se despreciará.

*Nota: λ es la tasa de arribos mientras que µ es la tasa de servicio.*

Se formula además que λ/µ < 1, pues de lo contrario el sistema no sería estable.

La probabilidad Pn(t+Δt) de que haya n unidades en el sistema (con n>0) puede expresarse como la suma de las siguientes cuatro probabilidades:

1. Pn(t) . (1 - λΔt) . (1 - µΔt) *[había n, no llegó ni se fue ninguno]*
2. Pn-1(t) . (λΔt) . (1 - µΔt)  *[había n-1, llegó uno, no se fue ninguno]*
3. Pn+1(t) . (1 - λΔt) . (µΔt)  *[había n+1, no llegó ninguno, se fue uno]*
4. Pn(t) . (λΔt) . (µΔt) *[había n, llegó uno y se fue uno]*

Sumando las probabilidades se obtiene:

$P\_{n}(t+Δt)=P\_{n}(t)\*(1-λΔt-µΔt+2λµΔt^{2})+P\_{n-1}(t)\*(λΔt -λµΔt^{2})+P\_{n+1}(t)\*(µΔt-λµΔt^{2})$

$\frac{P\_{n}(t+Δt)-P\_{n}(t)}{Δt}=λP\_{n-1}(t) + µP\_{n+1}(t) - (λ+µ)P\_{n}(t) + λµΔt^{}[2P\_{n}(t)-P\_{n-1}(t)-P\_{n+1}(t)]$

Como Δt→0, el último término se desprecia.

$\frac{dP\_{n}(t)}{dt}=λP\_{n-1}(t)+µP\_{n+1}(t)-(λ+µ)P\_{n}(t); n>0$ → A

Ahora hay que agregar la ecuación correspondiente al caso en que haya 0 unidades en el sistema en el tiempo t+Δt, que es la suma de dos probabilidades:

1. P0(t) . (1 - λΔt)
2. P1(t) . (1 - λΔt) . (µΔt)

Sumando:

$P\_{0}(t+Δt)=P\_{0}(t)\*(1-λΔt)+P\_{1}(t)\*(µΔt)$

$\frac{P\_{0}(t+Δt)-P\_{0}(t)}{Δt}=λP\_{0}(t)+µP\_{1}(t)$

$\frac{dP\_{0}(t)}{dt}=-λP\_{0}(t)+µP\_{1}(t)$ →B

A y B constituyen un modelo para las colas con un servidor con llegadas poissoneanas y tiempos de servicio exponenciales.

En el caso de que Pn sea independiente de t, se dice que el proceso es estacionario y permanente. Pn(t) = Pn. Entonces, A y B quedan:

$A: λP\_{n-1}+µP\_{n+1}-(λ+µ)P\_{n}=0$

$B: -λP\_{0}+µP\_{1}=0$

Procediendo por recurrencia y teniendo en cuenta que por definición $\sum\_{n=0}^{\infty }P\_{n}=1$:

P0 = P0

P1 = λ/µ P0

P2 = (λ/µ)2 P0

En general, tenemos que $P\_{n}=(\frac{λ}{µ})^{n}\*P\_{0}--> C$

$\sum\_{n=0}^{\infty }(\frac{λ}{µ})^{n}\*P\_{0}=1$

La parte hasta P0 es una serie geométrica infinita que converge en $\frac{1}{1-λ/µ}$

$\frac{1}{1-λ/µ}\*P\_{0}=1=>P\_{0}=1-\frac{λ}{µ}; cuando \frac{λ}{µ}<1 --> D$

Sustituyendo D en C:

$P\_{n}=(\frac{λ}{µ})^{n}\*(1-\frac{λ}{µ}); cuando \frac{λ}{µ}<1--> Modelo General$

La intensidad de tráfico, ρ, se calcula como λ/µ y 0 < ρ < 1

### Medidas de desempeño

#### Número medio de clientes en el sistema (L)

$L=E(n)=\sum\_{n=0}^{\infty }n\*P\_{n}=\sum\_{n=0}^{\infty }n\*(\frac{λ}{µ})^{n}\*(1-\frac{λ}{µ})$

Esto es una serie geométrica infinita de la forma ar + 2ar2 + 3ar3+..., donde a = 1-λ/µ y r = λ/µ. Converge en $a\*\frac{r}{(1-r^{2})}$

Por lo tanto:

$L=(1-\frac{λ}{µ}) \* \frac{λ/µ}{1-(λ/µ)^{2}}=> L=\frac{λ}{µ-λ}$

#### Número medio de clientes en cola (Lq)

$L\_{q}=\sum\_{n=2}^{\infty }(n-1)\*P\_{n}=\sum\_{n=2}^{\infty }n\*P\_{n}-\sum\_{n=2}^{\infty }P\_{n}$

$L\_{q}=\sum\_{n=0}^{\infty }n\*P\_{n}-\sum\_{n=0}^{1}n\*P\_{n}-\sum\_{n=0}^{\infty }P\_{n}+\sum\_{n=0}^{1}P\_{n}=\frac{λ}{µ-λ}-P\_{1}-1+P\_{0}+P\_{1}^{}$

$L\_{q}=\frac{λ}{µ-λ}-\frac{λ}{µ}=\frac{λ^{2}}{µ\*(µ-λ)}$

#### Tiempo medio de espera en el sistema (W)

$W=\frac{L}{λ}=\frac{1}{µ-λ}$

#### Tiempo medio de espera en cola (Wq)

$W\_{q}=\frac{Lq}{λ}=\frac{λ}{µ\*(µ-λ)}$

### Algoritmos M/M/1

![](data:image/png;base64...)

Las medidas de rendimiento serán:

1. La demora promedio por cliente (definida como la demora total que hubo en cola dividido la cantidad de clientes atendidos).
2. El tamaño promedio de la cola (definido como el área bajo la curva de tamaño de cola en función del tiempo, dividido por el tiempo de simulación).
3. La utilización del servidor (definida como el área bajo la curva de utilización a través del tiempo, dividida por el tiempo total de simulación).

![](data:image/png;base64...)

#### Algoritmo principal

Inicialización

Mientras reloj < fin de simulación

Tiempos

Si evento seleccionado = "A" ir a Arribo

Sino ir a Partida

Fin Si

Fin Mientras

Reporte

#### Tiempos

Buscar en LEV el próximo evento

reloj = tiempo de próximo evento

#### Inicialización

Inicializar las variables AAQ, AAB, AAD, n, reloj, cli\_at, TUE, S, TIOS

Inicializar el vector de tiempos de arribo VTA y la lista de eventos LEV

Generar tiempo de arribo ta

Guardar en LEV (A, ta)

Guardar en LEV (P,infinito)

#### Arribo

Si S="O"

AAQ = AAQ + (reloj - TUE) . n

n = n + 1

Guardar en VTA el reloj

Sino

S="O"

TIOS = reloj

cli\_at = cli\_at + 1

Generar tiempo de partida tp

Guardar en LEV(P, reloj + tp)

Fin Si

Generar tiempo de arribo ta

Guardar en LEV (A, reloj + ta)

Guardar TUE

#### Partida

Si n=0

S="D"

Sino

AAQ=AAQ + (reloj - TUE) . n

AAB = AAB + (reloj - TIOS)

AAD = AAD + reloj - VTA(arribo del cliente)

cli\_at = cli\_at + 1

n = n - 1

Generar tiempo de partida tp

Guardar en LEV(P, reloj + tp)

Fin Si

Guardar TUE

#### Reporte

Mostrar AAQ/reloj, AAB/reloj, AAD/cli\_at

## Análisis económico de los sistemas de colas

Claramente, mientras más servidores haya mejor será el servicio. Sin embargo, cada servidor implica costos.

### Modelo y análisis del sistema de colas actual

Supongamos que se tiene un sistema de reparación de máquinas en una fábrica. El sistema es M/M/7 con µ=4 y λ=25. Luego de correr la simulación, se ve que el tiempo promedio en el sistema para un cliente es de 0.48 y la cantidad de clientes en el sistema es de 12.1.

Ahora, cuál es el número de servidores que convendría tener? Se prueban escenarios distintos con hasta 11 servidores para ver cómo evolucionan las variables.

![](data:image/png;base64...)

Ahora que se sabe cómo evolucionan las variables, lo que resta averiguar son los costos, para poder saber qué número de servidores (reparadores de máquinas) conviene tener.

### Análisis de costos

Hay dos costos que considerar:

1. Costo por reparadores: Costo por hora para cada reparador \* número de reparadores. Como ejemplo, digamos que el costo por hora para cada reparador es $50.
2. Costo por no producción: Costo por hora por máquina fuera de operación \* número promedio de máquinas fuera de operación. Como ejemplo, digamos que el costo por hora por una máquina no produciendo es de $100.

Con estos datos, se puede calcular el costo total (Costo por reparadores + Costo por no producción) en cada uno de los escenarios (de 7 a 11 reparadores) y elegir el menos costoso. Viendo la tabla, la mejor alternativa es tener 9 reparadores.

## Simulación de un sistema de inventario

### Componentes

* Tiempo entre demandas.
* Tamaño de demanda.
* Costo del pedido: K + i . Z; siendo K el costo base, i el costo incremental y Z la cantidad.
* Retardo del envío.
* Política estacionaria (s, S): define Z. Si I < s, Z = S-I; si I >= s, Z=0.
* I(t): Nivel de inventario.
* I+(t): Items en posesión en inventario. MAX (I(t), 0)
* I-(t): Items faltantes en inventario. MAX (-I(t), 0)
* h: Costo de mantenimiento de items por unidad de tiempo.
* Ī+: Items promedio para el n-ésimo período de tiempo. $Ī^{+}=\frac{1}{n}\*\int\_{0}^{n}I^{+}(t).dt$
* Promedio de costo de mantenimiento por unidad de tiempo: Ī+ . h
* π: Costo de faltante de items por unidad de tiempo.
* Ī-: Items faltantes promedio para el n-ésimo período de tiempo. $Ī^{-}=\frac{1}{n}\*\int\_{0}^{n}I^{-}(t).dt$
* Promedio de costo por faltantes por unidad de tiempo: π . Ī-

### Diagrama de flujo de las rutinas

![](data:image/png;base64...)

![](data:image/png;base64...)

### Modelo de desencadenamiento de eventos

Se aplica antes de construir el modelo de simulación. Tiene el propósito de visualizar el sistema a partir de sus eventos desde un alto nivel de abstracción, y descarta detalles del sistema que quedan fuera de lo que son los eventos y cómo se desencadenan unos a otros bajo determinadas condiciones. Los beneficios de aplicarlo son un modelado rápido y una clara derivación del diseño de rutinas.

![](data:image/png;base64...)

*Nota: Control de inventario se autorreferencia, y Demanda también.*

### Medidas de desempeño

CCP: Costo de Cantidad Pedida = ACP / reloj; ACP: Acumulado de Cantidad Pedida

CUI: Costo de Unidades en Inventario = AIP.h / reloj; AIP: Acumulado Inventario Positivo

CUP: Costo de Unidades Perdidas = AIN . π / reloj; AIN: Acumulado Inventario Negativo

CMP: Costo Mensual Promedio = CCP + CUI + CUP

### Algoritmos

#### Programa Principal

Inicialización

Mientras reloj <= fin de simulación

Tiempos

Ir a Evento Seleccionado

Fin Mientras

Reporte Parcial

Reporte Final

#### Inicialización

Setear variables iniciales AIP, AIN, ACP, CCP, CUI, CUP, TUE, reloj, I, i, h, k, π

Guardar en LEV (CI,0)

Generar tiempo entre demandas td

Guardar en LEV (D, td)

Guardar en LEV (AP,∞,0)

#### Control de Inventario

Si I < s

Calcular tamaño pedido Z = S - I

ACP = ACP + k + i . Z

Generar tiempo de AP tap

Guardar en LEV (AP, reloj + tap, Z)

Fin Si

Guardar en LEV (CI, reloj + 1)

#### Acumular áreas

Si I > 0

AIP = AIP + (reloj - TUE) . I

Sino si I < 0

AIN = AIN + (reloj - TUE) . I

Fin Si

#### Demanda

Acumular áreas

Generar cantidad de demandada cd

I = I - cd

Generar tiempo entre demandas ted

Guardar en LEV (D, reloj + ted)

Guardar TUE

#### Arribo de Pedido

Acumular Areas

I = I + Z

Guardar TUE

#### Reporte Parcial

Mostrar CMP = CCP + CUI + CUP

#### Reporte Final

Mostrar todos los promedios y terminar

### Control de Inventario II (no está)

## Análisis de resultados

Réplica o corrida es una ejecución del modelo en una ocasión. Como muy probablemente si se corre el modelo nuevamente los valores en las variables sean distintos, muchas veces es necesario efectuar un número de corridas independientes y obtener un intervalo de confianza sobre el cual, con un determinado grado de seguridad, esté el verdadero valor de la variable.

El estado transitorio se presenta al principio de la simulación, y es un período donde hay mucha variación entre los valores de las variables. Una vez pasado el estado transitorio, se llega al estado estable, donde los valores de las variables de decisión permanecen estables.

### Comportamiento transiente y estado estacionario de un proceso estocástico

Considerar la salida de un proceso estocástico y1, y2, …, yn. Sea Fi (Yi<=Y|I) para i: 1,2,..,n donde Y es un número real e I representa las condiciones iniciales utilizadas para comenzar la simulación en tiempo cero. Llamamos a Fi la distribución transiente de un proceso de salida en el tiempo discreto i para las condiciones iniciales I.

Si Fi(Y|I) ->F(y) cuando i->infinito para todo Y y cualquier condición I, F(y) es llamada distribución en estado estacionario de los procesos de salida y1, y2, …, yn.

En la práctica, el tiempo estacionario se dice que comienza en un tiempo K+1, a partir del cual las variables aleatorios yk+1, yk+2, …,yn tendrán aproximadamente la misma distribución.

### Tipos de simulación

* **Terminal:** Existe un evento natural que indica el fin de una fase, a partir del cual terminan las actividades del sistema. El desempeño del sistema depende fuertemente de las condiciones iniciales. Las medidas de desempeño están referidas a un tiempo de operación.
* **No terminal / Estacionaria**: El sistema real opera de forma continua, sin un evento que determina una fase. Las medidas de desempeño no están referidas a un tiempo específico, ni se ven muy afectadas por las condiciones iniciales.

### Análisis de resultados para simulaciones terminales

Sea n la cantidad de réplicas independientes a ejecutar. Se usan las mismas condiciones iniciales en cada una. Se asume una única medida de desempeño, como por ejemplo la demora promedio por cliente.

Sea xj una variable aleatoria definida para la réplica j siendo j: 1,2,...,n, las xj son IID.

Se desea obtener un punto de estimación y un intervalo de confianza para la media µ=E(x)

1. Simular las n réplicas independientes tomando x1,x2,…, xn como variables IID.
2. Calcular la media muestral y la varianza muestral.
3. Establecer un nivel de confianza de 100.(1-⍺)%

$IC: \overline{X}(n)\_{}\pm t\_{n-1;1-α/2}\*\sqrt{\frac{S^{2}(n)}{n}} --> Procedimiento de muestra de tamaño fijo$

Una desventaja de este método es que no se tiene control sobre la precisión de x̄(n)

### Obteniendo una precisión específica

#### Precisión absoluta

Si la estimación de x̄ es tal que |x̄-µ|=𝛃, entonces se dice que x̄ tiene un error de 𝛃 al estimar µ. El total de réplicas requeridas para tener un error absoluto de 𝛃 es:

$n\_{a}^{\*}(β)=Min\{i\geq n tal que t\_{i-1;1-α/2}\*\sqrt{\frac{S^{2}(n)}{i}}\leq β\}$

#### Precisión relativa $$

Si el estimador de x̄ es tal que (x̄-µ)/µ = j, entonces decimos que x̄ tiene un error relativo de j al estimar µ. El total de réplicas requeridas para obtener un error relativo de j es:

$n\_{r}^{\*}(j)=Min\{i\geq n / \frac{t\_{i-1;1-α/2}\*\sqrt{\frac{S^{2}(n)}{i}}}{x̄(n)}\leq j'\}$, donde $ j'=\frac{j}{1-j}$

El objetivo es tener un estimador de µ con un error relativo de j, siendo 0<= j <1 y con 100\*(1-⍺)% de confianza. Sea $δ(n,α)=t\_{n-1;1-α/2}\*\sqrt{\frac{S^{2}(n)}{i}}$ la semiamplitud del intervalo de confianza:

1. Realizar n0 réplicas y fijar n = n0.
2. Calcular x̄ y $δ(n,α)$a partir de los x1,x2,...,xn.
3. Si $\frac{δ(n,α)}{\overline{x}}\leq j',$ usar x̄ como estimador y parar. De lo contrario, incrementar en 1 la cantidad de réplicas y volver al paso 2.

### Determinación del sesgo inicial

Consiste en eliminar cierta cantidad de observaciones al inicio de cada corrida y utilizar las restantes para estimar µ. Se aplica a procesos estacionarios en los que es posible realizar corridas largas y el sistema bajo estudio es continuo.

### Media de lotes

Se basa en una corrida larga, por lo que el sesgo inicial se produce sólo una vez. Sea Y una variable IID con valores Y1, Y2, …, Yi; E(Yi)=µ. Se asume que las primeras l observaciones fueron eliminadas y se está trabajando con Yl+1, Yl+2,..., las cuales serán IID si l es lo suficientemente grande.

Se realiza una corrida de longitud m y se dividen las observaciones resultantes en n lotes de longitud K, o sea que m = n . k. Entonces el lote 1 consiste en Y1, Y2,...,Yk; el lote 2 consiste en Yk+1, Yk+2,...,Y2k, etc. Finalmente, se calcula el intervalo de confianza:

$\overline{\overline{Y}}(n,k)\pm t\_{n-1;1-α/2}\*\sqrt{\frac{S^{2}(n)}{n}}; S^{2}(n)=\sum\_{i=1}^{n}\frac{[\overline{Yi}(k)-\overline{\overline{Y}}(n,k)]^{2}}{n-1}$

### Múltiples medidas de rendimiento

Suponga que Is es un intervalo de confianza con el 100.(1-a)% de confianza para la medida de rendimiento µs (con s: 1,2,..,k), que puede ser de simulación terminal o no terminal. La probabilidad de que todos los k intervalos de confianza contengan simultáneamente a sus respectivas medidas de rendimiento satisface: $P(μ\_{s}ϵ I\_{s}; s:1,2,...,k)\geq 1-\sum\_{s=1}^{k}α\_{s}$donde las Is pueden ser independientes o no. Este resultado es conocido como inecuación de Bonferroni. Se recomienda que K<=10 y que $\sum\_{s=1}^{k}α\_{s}=α$, es decir que la confianza total de nuestro sistema sea la suma de las confianzas de todos los intervalos.

### Números aleatorios comunes

Si nuestro objetivo es determinar diferencias en la respuesta del sistema cuando cambia un parámetro, es razonable comparar las respuestas del sistema bajo las mismas condiciones. Esto implica que los números aleatorios a usar para generar los tiempos de arribo y de servicio deberían ser los mismos. Sea x̄1 el tiempo de espera medio de una simulación al tiempo de simulación 1; y sea x̄2 lo mismo para el tiempo 2; entonces la varianza de la diferencia será:

$Var(\overline{x1}-\overline{x2})=Var(\overline{x1})+Var(\overline{x2})-2\*Cov(\overline{x1},\overline{x2})$

Si se usan números aleatorios comunes, habrá correlación entre x̄1 y x̄2 y la varianza de su diferencia será reducida por tener covarianza positiva.

##

## Comparando sistemas alternativos

### Intervalos de confianza para la diferencia de medidas de rendimiento

Sean xi1, xi2,…,xin con i =1 a 2 una muestra de n.i observaciones para el sistema i y sea µi=E(xij) la esperanza matemática. Se desea construir un intervalo de confianza para$ζ$=µ1-µ2. Dependiendo de la independencia entre x1j y x2j se seleccionará el método de muestras apareadas o el de muestras independientes.

#### Muestras apareadas

Sean n1=n2 la cantidad de observaciones de los sistemas 1 y 2 (se pueden descartar observaciones de un sistema para que queden iguales). Es posible aparear estas observaciones x1j y x2j de manera zj=x1j-x2j, con j:1,2,...,n. Entonces Z es variable aleatoria IID y E(Z) = $ζ$. Para construir el intervalo de confianza t-apareado:

$\overline{Z}(n)=\sum\_{j=1}^{n}\frac{Zj}{n}; Var(Z(n))=\frac{\sum\_{j=1}^{n}[Zj-\overline{Z}(n)]^{2}}{n\*(n-1)}=> IC: \overline{Z}(n)\pm t\_{n-1;1-α/2}\*\sqrt{Var(Z(n))}$

Si la distribución de los Zj es normal, entonces el intervalo de confianza es exacto (es decir, cubre $ζ$ con una confianza de 1-$α$). De otra manera, tenemos que usar el teorema central del límite, usando n alto para que la distribución de los Z se aproxime a la distribución normal.

#### Muestras independientes (Welch)

Requiere que los X1j sean independientes de los x2j (además, x1j debe tener distribución normal). n1 puede ser distinto de n2.

$\overline{Xi}(ni)=\sum\_{j=1}^{ni}\frac{Xij}{ni}; Var(Xi(ni))=\frac{\sum\_{j=1}^{ni}[Xij-\overline{Xi}(ni)]^{2}}{(ni-1)}$

Ahora, calculamos los grados de libertad estimados:

$\hat{f}=\frac{[\frac{S\_{1}^{2}(n1)}{n1}+\frac{S\_{2}^{2}(n2)}{n2}]^{2}}{\frac{[S\_{1}^{2}(n1)]^{2}}{n1-1}+\frac{[S\_{2}^{2}(n2)]^{2}}{n2-1}}$

Y finalmente definimos el IC:

$IC: \overline{X1}(n1)-\overline{X2}(n2)\pm t\_{\hat{f},1-α/2}\*\sqrt{\frac{S\_{1}^{2}(n1)}{n1}+\frac{S\_{2}^{2}(n2)}{n2}}$

##

## Generador Congruencial Lineal

Teniendo los parámetros m (generalmente mayor a 109), a < m, c < m, y Z0 (llamado semilla) < m, se define el generador como:

$Z\_{i}=(a\*Z\_{i-1}+c) mod m$, y $U\_{i}=Z\_{i}/m$

Aunque es un método determinístico, a través de una cuidadosa selección de parámetros se puede inducir a los Zi a comportarse de forma tal que los Ui obtenidos parezcan variables aleatorias IID al ser sometidos a ciertos tests estadísticos. Es inevitable observar un comportamiento cíclico en los números generados debido a la naturaleza del generador. La longitud del ciclo, p, se denomina período y cuando p=m el generador es de período completo. Es deseable escoger valores de m, a y c para tener período completo y un m lo suficientemente grande como para evitar que haya ciclos en la cantidad deseada de números generados.

**Teorema**: Un GLC es de período completo si y sólo si cumple con las siguientes condiciones:

1. m y c tienen un único divisor común que es 1.
2. Si q es un número primo que divide a m, también tiene que dividir a a-1.
3. Si 4 divide a m, entonces también divide a a-1.

Un GLC puede ser de tres tipos:

1. Mixto: completo como el visto arriba.
2. Aditivo (a=1).
3. Multiplicativo (c=0).

### Tests para generadores de números aleatorios

#### Test de chi-cuadrado

Se divide el intervalo [0,1] en k subintervalos y se generan n números aleatorios. Como regla general, k>=100 y n/k >= 5.

Para j:1,2,..,k sea Fj la cantidad de números aleatorios que se encuentran en el subintervalo j. Sea:

$X^{2}=\frac{k}{n}\*\sum\_{j=1}^{k}(F\_{j}-\frac{n}{k})^{2}$

Entonces, para un valor grande de n, la distribución de X2 se aproxima a la distribución de chi-cuadrado con k-1 grados de libertad bajo la hipótesis nula de que Ui es variable aleatoria IID. Podemos descartar esta hipótesis a un nivel $α$si $X^{2}>X\_{k-1,1-α}^{2}$, donde $X\_{k-1,1-α}^{2}$es el valor crítico superior de la distribución de chi-cuadrado con k-1 grados de libertad.

#### Test de serie (uniformidad)

Es una generalización del test de chi-cuadrado para mayores dimensiones. Si los Ui fueran realmente variables aleatorias IID, las d-tuplas no superpuestas U1=(U1,U2,...,Ud), U2=(Ud+1, Ud+2,...,U2d), etc deberían ser vectores aleatorios uniformemente distribuidos en el hipercubo d-dimensional [0,1]d. Se divide el intervalo [0,1] en k subintervalos de igual amplitud y se generan los vectores U1, U2,...,Un (requiriendo generar entonces n.d números).

Sea Fj1,Fj2,...,Fjd el número de vectores U que tienen primer componente en el subintervalo j1, segundo componente en el intervalo j2, etc. Sea $X^{2}=\frac{k^{d}}{n}\*\sum\_{j1=1}^{d}\*\sum\_{j2=1}^{d}\*...\*\sum\_{jd=1}^{d}(F\_{j1,j2,...,jd}-\frac{n}{k^{d}})^{2}$, $X^{2}(d)$tendrá una distribución aproximada a la de chi-cuadrado con kd-1 grados de libertad (se recomienda n/kd >=5).

Este test se lleva a cabo de la misma forma que el de chi-cuadrado unidimensional.

#### Test empírico de corridas (independencia)

1. Generar los Ui con i=1,2,..,n, siendo n>=4000.
2. Examinar los Ui generados identificando subsecuencias crecientes y continuas de Ui de longitud máxima.
3. Calcular $r\_{i}=\frac{Cant de subsecuencias de longitud i}{Cant de subsecuencias de longitud \geq 6}; i:1,2,3,4,5$
4. Calcular la variable chi-cuadrado $R=\frac{1}{n}\*\sum\_{i=1}^{6}\*\sum\_{j=1}^{6}a\_{ij}\*(r\_{i}-n\*b\_{i})\*(r\_{j}-n\*b\_{j})$
5. Comparar $X^{2}$> $X\_{6,1-α}^{2}$, donde $X\_{6,1-α}^{2}$ es el valor de la tabla de chi-cuadrado con 6 grados de libertad y confianza de 1-$α$. Si la desigualdad se comprueba, entonces se rechaza la hipótesis nula de que los números aleatorios generados son independientes.

## Naylor capítulo 4: Generación de variables estocásticas empleadas en simulación

### Método de transformación inversa

Si queremos generar números aleatorios que sigan una distribución cuya función de densidad está dada por f(x), debemos obtener la función de distribución acumulativa F(x). F(x) va a estar definida entre 0 y 1, por lo que podemos generar un número aleatorio uniformemente distribuido entre 0 y 1, asignarlo a r = F(x), conseguir el valor de x correspondiente, y finalmente calcular f(x) para obtener el número definido por la distribución deseada.

r = F(x) = $\int\_{-\infty }^{x}f(t) dt$, x0 = F-1(r0)

Desafortunadamente, para muchas distribuciones resulta difícil o incluso imposible expresar a x en términos de F-1(r), por lo que este método en algunos casos no puede utilizarse, y en otros requiere hacer aproximaciones.

### Método de rechazo

Se puede usar si f(x) es acotada y x tiene un rango finito entre a y b. Los pasos son:

1. Normalizar f mediante un factor c, tal que c.f(x) <=1
2. Definir x como función lineal de r: x = a+(b-a).r
3. Generar parejas de números aleatorios (r1,r2)
4. Siempre que se satisfaga que r2<= c.f(a+(b-a).r1), el par será aceptado, siendo x = c.f(a+(b-a).r1) el valor generado.

Este método se basa en que P(r<=c.f(x)) = c.f(x)

Tocher demostró que la esperanza matemática del número de intentos necesarios para conseguir una pareja exitosa es de 1/c, por lo que este método puede resultar muy ineficiente en ocasiones.

### Método de composición

Consiste en expresar f(x) como una mezcla probabilística de n funciones de densidad gn(x), seleccionadas adecuadamente. f(x)=$\sum\_{}^{}gn.Pn$. Para elegir las gn(x), se considera la bondad de ajuste y el objetivo de minimizar $\sum\_{}^{}Tn.Pn$, siendo Tn el tiempo de computación esperado para generar valores a partir de gn(x).

### Generación de valores de variables aleatorias con distribución continua

#### Distribución uniforme

$f(x)=\{\frac{1}{b-a} si a\leq x\leq b; 0 si x está fuera del intervalo$

Entonces r = F(x) = $\int\_{a}^{x}\frac{1}{b-a} . dt=\frac{x-a}{b-a}; 0\leq F(x)\leq 1$

x = $F\_{}^{-1}(r)=r(b-a) + a; siendo 0\leq r\leq 1$

Se generan los números r para conseguir los valores x y luego se hace f(x) para conseguir el valor de la variable aleatoria con distribución uniforme.

#### Distribución exponencial

Suposiciones:

1. La probabilidad de que ocurra un evento en Δt es $αΔt$
2. $α$es constante y no depende de t ni ningún otro factor.
3. Se desprecia la probabilidad de que haya más de un evento en $Δt$.

Una variable aleatoria X tiene una distribución exponencial si su función de densidad f(x) = $α.e\_{}^{-αx}, con α>0 y x\geq 0$

La distribución acumulativa entonces es $F(x)=\int\_{0}^{x}α.e^{-αt}. dt =1- e^{-αt}$. Como la distribución es simétrica, F(x) = 1 - F(x) por lo que r = $1-(1-e^{-α}t)=e^{-αt}$. Consecuentemente, $F^{-1}(r)=x=-\frac{1}{α}. log(r)$

#### Distribución Gamma

Si un proceso consiste en k eventos sucesivos y el total de tiempo transcurrido es la suma de k valores independientes de la variable aleatoria con distribución exponencial (cada uno con su $α$), la distribución de esta suma será la de una distribución gamma con parámetros k y $α$. Si siempre es el mismo $α$, se llama distribución de Erlang.

$f(x) = \frac{α^{k}.x^{k-1}.e^{-αk}}{(k-1)!}, con α>0, k>0, y x>0$

Si k=1, la distribución es exponencial.

No hay función de distribución acumulativa F(x) para este caso, por lo que hay que usar métodos alternativos.

Si la distribución es de Erlang, se puede hacer la suma de los k valores con distribución exponencial, siendo entonces $x=\sum\_{i=1}^{K}x\_{i}=\frac{-1}{α}.\sum\_{i=1}^{K}log r\_{i}$

#### Distribución normal

Gracias al teorema del límite central, que dice que la suma de N valores igualmente distribuidos con media µi y varianza $σ\_{i}^{2}$tiene una distribución que se aproxima a la normal cuando N es grande, con $µ=\sum\_{i=1}^{N}µ\_{i} y σ^{2}=\sum\_{i=1}^{N}σ\_{i}^{2}$.

En esta distribución tampoco existe la función de distribución acumulariva F(x), así que se puede usar una interpretación del teorema del límite central y hacer una suma de K valores de variable aleatoria distribuidos uniformemente entre 0 y 1. Los $µ\_{i}$serán ½ y $σ\_{i}^{2}=\frac{1}{\sqrt{12}}$, por lo que $z=\frac{\sum\_{i=1}^{K}r\_{i}-K/2}{\sqrt{K/12}}$, pero como z tiene una distribución normal estándar, nos queda

$x=σ\_{x}.\left(\frac{12}{K}\right)^{1/2}.\left(\sum\_{i=1}^{K}r\_{i}-K/2\right)+µ\_{x}$.

Se recomienda que K sea 24 o mayor.

Existen también otros métodos, el procedimiento directo y el procedimiento rápido.

#### Distribución normal multivariada

#### Distribución logarítimica normal

### Generación de valores de variables aleatorias con distribución discreta

En estas probabilidades, $F(x)=P(X\leq x)=\sum\_{X=0}^{x}F(x)$, donde f(x) es la función de densidad de X definida por valores enteros: f(x) = P(X=x) con x=0, 1, 2,...

#### Distribución geométrica

Consiste en describir cuántos fracasos se observaron en una serie de ensayos de Bernoulli antes de que llegue el primer evento exitoso, teniendo una probabilidad de éxito p y una probabilidad de fracaso q = 1-p.

$f(x)=p.q^{x}, con x=0,1,2...,x$

$F(x)=\sum\_{X=0}^{x}p.q^{x}, con X=0,1,2,...,x$

Como P(X>x) = 1- F(x) => P(X>0) = q, y 1-F(x)=$q^{ x+1}$

r=$q^{x}=>x=\frac{log r}{log q}$

#### Distribución binomial

Variables aleatorias que definen el número de ensayos exitosos en una sucesión de n ensayos independientes de Bernoulli, cada uno con probabilidad de éxito p.

$f(x)=nCx.p^{x}.q^{n-x}$, siendo x=0,1,2,...,n y q=1-p

Se pueden generar de varios modos, siendo el más simple el del método de rechazo:

1. Fijar x0=0
2. Generar un ri, y si ri<=p entonces xi = xi - 1+1. Sino, xi = xi - 1.
3. Al llegar a n números generados, xn será el valor de la variable aleatoria con distribución binomial.

#### Distribución hipergeométrica

Si hay N elementos, dentro de los cuales N.p son de una clase (clase 1) y N.q son de otra (clase 2), siendo p+q=1, al tomar una muestra de n, el número de elementos que serán de clase 1 tendrá una distribución hipergeométrica.

$f(x)=\frac{\_{N.p}C\_{x} \*\_{N.q}C\_{n-x} }{\_{N}C\_{n}}, con 0\leq x\leq N.p y 0\leq n-x\leq N.q, siendo x,n y N enteros$

Para generarlos, se puede alterar el método que se usa para la distribución binomial, haciendo que p varíe según la iteración en la que está, haciendo $p\_{i}=\frac{n\_{i-1}\*p\_{i-1}- S}{N\_{i-1}-1}$

#### Distribución de Poisson

Si tomamos n ensayos de Bernoulli con p muy pequeña, a medida que n tiende a infinito, la probabilidad de x ocurrencias sigue la distribución de Poisson.

$f(x)=e^{-λ}. \frac{λ^{x}}{x!}, x=0,1,2... y λ>0, siendo λ=n.p$

Para generar una distribución de Poisson con parámetro $λ$, aprovechamos la relación entre la distribución de Poisson y la exponencial: si la ocurrencia de eventos es independiente a ocurrencias anteriores y la probabilidad de ocurrencia en $Δt$es $λΔt$ para todo t, entonces

1. $f(t)=λ.e^{-λt}$ (función de densidad del intervalo entre ocurrencias, de tipo exponencial)
2. $f(x)=e^{-λ t}. \frac{(λ . t)^{x}}{x!}$, para toda t y toda x

Entonces, si los eventos siguen una distribución de Poisson con valor esperado $λ$, el tiempo entre eventos sigue una distribución exponencial con valor esperado 1/$λ$.

Por lo tanto, para generar valores de variable aleatoria con distribución de Poisson, se generan intervalos ti con distribución exponencial con valor esperado = 1 y se suman hasta que la suma sea mayor a $λ$. Matemáticamente: $x tal que\sum\_{i=0}^{x}t\_{i} \leq λ < \sum\_{i=0}^{x+1}t\_{i}, donde t\_{i} =-log r\_{i}$

#### Distribuciones discretas empíricas

#### Cadenas discretas de Markov

### Series de tiempo autocorrelacionadas