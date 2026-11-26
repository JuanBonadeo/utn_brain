Ejercicio 1: Teoría de Colas
Imagina un router o conmutador que maneja el tráfico de datos en
una red. La llegada de paquetes de datos al router sigue una
distribución de Poisson (M), y el tiempo que tarda el router en
procesar cada paquete sigue una distribución exponencial (M). Solo
hay un procesador (1).
Datos del Problema:
1. Tasa de Llegada (λ): Los paquetes llegan al router a una tasa
promedio de 100 paquetes por segundo (paq/s).
2. Tasa de Servicio (μ): El router puede procesar los paquetes a
una tasa promedio de 125 paquetes por segundo (paq/s).
Objetivo
Calcular las principales métricas de rendimiento del router
utilizando el modelo de colas M/M/1.
Solución Paso a Paso
1. Definir los Parámetros Iniciales
 Tasa de Llegada (λ): λ=100 paq/s.
 Tasa de Servicio (μ): μ=125 paq/s.
2. Calcular el Factor de Utilización (ρ)
Representa el porcentaje de tiempo que el router está ocupado.
ρ=μ / λ
ρ = 125paq/seg / 100paq/s = 0.8 => p = 80%
Interpretación: El router está ocupado el 80% del tiempo.
3. Calcular la Longitud Promedio del Sistema (L)
Número promedio de paquetes en el sistema (cola + servicio).

4. Calcular la Longitud Promedio de la Cola (Lq)
Número promedio de paquetes esperando a ser atendidos.
paquetes
5. Calcular el Tiempo Promedio en el Sistema (W)
Tiempo total promedio que un paquete pasa desde que llega hasta
que se va (Retardo o Latencia total).
6. Calcular el Tiempo Promedio de Espera en la Cola (Wq)
Tiempo promedio que un paquete espera antes de ser procesado.
Cálculo del tiempo de servicio (1/μ): 1251=0.008 segundos (8 ms).

Resumen de Resultados
| Métrica                        | Símbolo Valor               | Unidad        |
| ------------------------------ | --------------------------- | ------------- |
| Factor de Utilización          | ρ  0.8 (80%)                | Adimensional  |
| Longitud Promedio del Sistema  | L  4                        | Paquetes      |
| Longitud Promedio de la Cola   | Lq  3.2                     | Paquetes      |
| Tiempo Promedio en el Sistema  | W  0.04 (40 ms)             | Segundos      |
| Tiempo Promedio en la Cola     | Wq  0.032 (32 ms) Segundos  |               |

Ejercicio 2
Una puerta de enlace (gateway) en una red de área local (LAN) se
comporta como un sistema de colas. La llegada de paquetes de datos
sigue una distribución de Poisson con una tasa promedio de 10
paquetes por segundo (λ). La puerta de enlace puede procesar (servir)
los paquetes siguiendo una distribución exponencial a una tasa
promedio de 15 paquetes por segundo (μ).
Calcular las siguientes métricas clave del rendimiento del sistema:
1. Factor de Utilización del Sistema (ρ): La proporción del tiempo
que la puerta de enlace está ocupada.
2. Longitud Promedio de la Cola (Lq): El número promedio de
paquetes esperando en la cola para ser procesados.
3. Longitud Promedio del Sistema (L): El número promedio de
paquetes en el sistema (tanto en la cola como siendo
procesados).
4. Tiempo Promedio de Espera en la Cola (Wq): El tiempo promedio
que un paquete pasa esperando en la cola.
5. Tiempo Promedio de Estancia en el Sistema (W): El tiempo
promedio que un paquete pasa en todo el sistema (espera +
servicio).
Solución Paso a Paso
El sistema descrito es un modelo de colas M/M/1, donde:
 M (Llegada): La llegada sigue una distribución de Poisson.
 M (Servicio): El tiempo de servicio sigue una distribución
exponencial.
 1: Hay un único servidor (la puerta de enlace).
Datos del Problema
 Tasa de Llegada (λ): 10 paquetes/segundo
 Tasa de Servicio (μ): 15 paquetes/segundo
1. Factor de Utilización del Sistema (ρ)
El factor de utilización (ρ) representa la probabilidad de que el
servidor esté ocupado. Debe ser menor a 1 para que el sistema sea
estable (λ<μ).

ρ= μ / λ
Cálculo:
Resultado: ρ≈∗∗0.67∗∗
Interpretación: La puerta de enlace está ocupada aproximadamente
el 67% del tiempo, o la probabilidad de que esté ocupada es de
0.67.
2. Longitud Promedio de la Cola (Lq)
La longitud promedio de la cola (Lq) es el número promedio de
paquetes que están esperando por el servicio.
Cálculo:
Resultado: Lq≈∗∗1.33 paquetes**
Interpretación: En promedio, hay 1.33 paquetes esperando en la
cola.
3. Longitud Promedio del Sistema (L)
La longitud promedio del sistema (L) es el número promedio de
paquetes en todo el sistema (esperando y siendo atendidos).

Cálculo usando la segunda fórmula (más directa para M/M/1):
Resultado: L= 2 paquetes
Interpretación: En promedio, hay 2 paquetes en la puerta de enlace
(incluyendo el que se está procesando y los que esperan).
4. Tiempo Promedio de Espera en la Cola (Wq)
El tiempo promedio de espera en la cola (Wq) es el tiempo que un
paquete pasa esperando para comenzar a ser procesado.
Cálculo:
Resultado: Wq≈∗∗0.133 segundos (o 133.3 milisegundos)**
Interpretación: Un paquete espera en la cola un promedio de 0.133
segundos antes de que comience su procesamiento.
5. Tiempo Promedio de Estancia en el Sistema (W)
El tiempo promedio de estancia en el sistema (W) es el tiempo
total que un paquete pasa en la puerta de enlace (espera más
servicio).

Cálculo usando la primera fórmula:

Resultado: W=∗∗0.2 segundos (o 200 milisegundos)**
Interpretación: Un paquete pasa en la puerta de enlace, desde su
llegada hasta su salida, un promedio de 0.2 segundos.

Resumen de Métricas
| Métrica               | Símbolo  | Valor  | Unidad        |
| --------------------- | -------- | ------ | ------------- |
| Tasa de Llegada       | λ        | 10     | paquetes/s    |
| Tasa de Servicio      | μ        | 15     | paquetes/s    |
| Utilización           | ρ        | 0.67   | (sin unidad)  |
| Longitud de Cola      | Lq       | 1.33   | paquetes      |
| Longitud del Sistema  | L        | 2      | paquetes      |
| Tiempo en Cola        | Wq       | 0.133  | segundos      |
| Tiempo en Sistema     | W        | 0.2    | segundos      |