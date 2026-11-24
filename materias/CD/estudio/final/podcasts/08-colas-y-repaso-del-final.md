# Podcast CD 8 de 8 — Teoría de colas y repaso del final

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

Kendall, Little y el M/M/1 con el ejercicio de la sala de emergencias del final 2025 contado como historia, el punto de saturación del modelo cerrado y asignación de capacidad en breve. Terminá con las reglas para el examen en formato quiz: planteá la situación, esperá un momento y explicá qué conviene hacer.

## Contenido principal

### 9. Teoría de colas

*Fuentes: apunte Teoría de Colas, Ejercitación Teoría de cola y El Santo Resumen. Sale en 5 de cada 9 finales.*

#### 9.1 Elementos y notación

Pensá en una guardia con un solo médico. Los pacientes llegan al azar, esperan en la sala si el médico está ocupado, se atienden por orden de llegada y se van. Un sistema de colas tiene una **fuente** de usuarios, un **proceso de arribo** (Poisson: intervalos exponenciales), un **tiempo de servicio** (exponencial), una **capacidad**, una cantidad de **servidores** y una **disciplina** (FIFO, LIFO, prioridades).

**Kendall**: $A/B/c/k/n/Z$. $A$ es la distribución de los arribos, **$B$ la del servicio**, $c$ los servidores, $k$ la capacidad, $n$ la población y $Z$ la disciplina. **M** quiere decir exponencial. La forma corta $A/B/c$ supone cola sin límite, población infinita y FIFO.

> **Ojo:** la **segunda** M de M/M/1 es el **tiempo de servicio** exponencial. Lo decide la posición de la letra.

#### 9.2 M/M/1: fórmulas

| Símbolo | Significado | Fórmula |
|---|---|---|
| $\lambda$ | frecuencia media de arribos | $\lambda = 1/E[\tau]$ |
| $E[s]$ | tiempo medio de servicio | $E[s] = 1/\mu$ |
| $u$ | **intensidad de tráfico** [Erlang] | $u = E[s]/E[\tau] = \lambda E[s]$ |
| $\rho$ | **factor de utilización**: probabilidad de que el servidor esté ocupado | $\rho = u/c$; con un servidor, $\lambda E[s]$ |
| $W_q$ | tiempo medio **en cola** | $W_q = \rho\, E[s]/(1 - \rho)$ |
| $W$ | tiempo medio **en el sistema** | $W = W_q + E[s] = E[s]/(1 - \rho)$ |
| $L_q$, $L$ | usuarios medios en cola y en el sistema | $L_q = \lambda W_q$; $L = \lambda W$ (**Little**) |
| $\pi_q(90)$ | tiempo de cola que no supera el 90 % de los usuarios | $W \ln(10\rho)$ |

**Condición de estabilidad: $\rho < 1$.** Si no, la cola crece sin límite y las fórmulas no se aplican. La intensidad de tráfico da la **cantidad mínima de servidores**: con $E[s] = 15$ s y $E[\tau] = 10$ s, $u = 1{,}5$ Erlang, y hacen falta al menos 2.

Como $W = E[s]/(1 - \rho)$, la espera explota cuando $\rho \to 1$. Con $\rho = 0{,}5$ la espera en cola iguala al servicio; con $\rho = 0{,}9$ es 9 veces el servicio.

**Procedimiento:**

1. **Pasá $\lambda$ y $E[s]$ a la misma unidad.** "100 personas por día" se divide por los minutos **de atención**, no por 1440.
2. **Verificá $\rho < 1$.** Si no, decilo: hacen falta más servidores.
3. **Calculá** $W_q$, $W$, $L_q$ y $L$, **definiendo cada término**, con unidades.
4. **Concluí**: ¿la espera es aceptable?

> **Ojo:** la cátedra usa $\mu$ para la tasa de servicio y también para los niveles del multinivel. En colas trabajá con $E[s]$, que es lo que dan los enunciados.

#### 9.3 Ejercicio resuelto: final 2025

**Enunciado** (04/04/2025, igual al 20/11/2020 y al 17/12/2021). Una sala de emergencias es atendida por un doctor. Los pacientes llegan según un proceso de Poisson, uno cada media hora, y la atención es exponencial, de 20 minutos en promedio. Calcular a) el tiempo promedio que el paciente espera para ser atendido, b) el tiempo promedio en la sala de emergencias, c) el número promedio de pacientes en cola y d) el número promedio de pacientes en la sala.

**Datos**, en minutos: $\lambda = 1/30$ paciente/min; $E[s] = 20$ min.

1. **Utilización**: $\rho = \lambda E[s] = 20/30 = 0{,}667 < 1$. El sistema es estable y el doctor está ocupado el 66,7 % del tiempo.
2. **a) Tiempo en cola**:
$$W_q = \frac{\rho\, E[s]}{1 - \rho} = \frac{0{,}667 \cdot 20}{0{,}333} = \mathbf{40\ min}$$
3. **b) Tiempo en el sistema**, espera más atención: $W = 40 + 20 =$ **60 min**.
4. **c) Pacientes en cola**: $L_q = \lambda W_q = 40/30 =$ **1,33 pacientes**.
5. **d) Pacientes en el sistema**: $L = \lambda W = 60/30 =$ **2 pacientes**.
6. **Conclusión.** Con dos tercios de ocupación, la espera ya duplica el tiempo de atención. Extra: $\pi_q(90) = 60 \ln 6{,}67 = 113{,}8$ min.

**Criterio a declarar.** a) y b) se parecen mucho en la redacción. Se tomó a) como tiempo en cola y b) como tiempo total en emergencias; lo mismo para c) y d).

#### 9.4 Otras variantes

| Final | Qué cambia | Resultado |
|---|---|---|
| 19/11/2021, 18/12/2020 | caja única de 7 a 14 h, 100 personas por día, servicio de 3 min | $\lambda = 100/420 = 0{,}238$/min; $\rho = 0{,}714$; $W_q = 7{,}5$ min; $W = 10{,}5$ min; $L_q = 1{,}79$; $L = 2{,}5$ |
| 18/02/2011 (inverso) | $\lambda = 0{,}2$/min, $\mu = 0{,}25$/min, $W_q = 16$ min | $E[s] = 4$ min; $\rho = 0{,}8$ |
| Finales viejos (inverso) | dan $L_q$, $W$ y $\rho$ | sólo con Little: $\lambda W = L_q + \rho$ (esos datos no siempre son M/M/1) |
| Práctica (trampa) | 60 personas de 10 a 15 h, servicio de 5 min | $\rho = 1$: **saturado**, hacen falta 2 cajas |

#### 9.5 Punto de saturación (modelo cerrado)

Salió en dos finales de teoría. $N$ terminales comparten una CPU, y cada usuario alterna entre **pensar** (tiempo medio $E[t]$) y **ser atendido** ($E[s]$). Si se grafica el tiempo de respuesta $W$ contra $N$, con pocas terminales $W \approx E[s]$, y con muchas $W \approx N\,E[s] - E[t]$. Las dos asíntotas se cortan en el **punto de saturación**:

$$N^* = \frac{E[s] + E[t]}{E[s]}$$

Es el **número máximo de terminales que se pueden conectar sin interferencia mutua**. Ejemplo del apunte: $E[s] = 0{,}2$ s y $E[t] = 3$ s dan $N^* = 16$.

> **Ojo:** en el *multiple choice*, "el número **máximo** de usuarios con una **mínima** interferencia mutua". Un resumen de alumnos dice "número máximo de **servidores**": son terminales.

#### 9.6 Por las dudas: asignación de capacidad

No salió desde 2020. Hay una capacidad total $C$ (en bps) para repartir entre los enlaces de una red en estrella, buscando el menor retardo promedio (Kleinrock). Cada enlace es una **M/M/1** que recibe $\lambda_i$ mensajes/s de $1/\eta_i$ bits en promedio, con retardo $T_i = 1/(\eta_i C_i - \lambda_i)$: si $\lambda_i \to \eta_i C_i$, **el retardo crece sin límite**. La **regla de la raíz cuadrada** le da a cada enlace su tráfico mínimo $\lambda_i/\eta_i$ y reparte lo que sobra en proporción a $\sqrt{\lambda_i/\eta_i}$. La fórmula y un ejemplo resuelto están en `banco-ejercicios.md` (§9).

### 0.3 Reglas para el examen

1. **Si hay ambigüedad, escribí el criterio que usás.** Los casos conocidos:
   - ancho de banda de la trama: $B_w = 1/\tau$ (el de la cátedra) o $B = s/2$ (§7.3);
   - muestrear con $2f_{max}$ o con $2(f_{max} - f_{min})$ (§7.4);
   - si los pulsos de arranque y stop están dentro del total o se suman aparte (§3.2);
   - en colas, qué inciso es tiempo en cola y cuál tiempo en el sistema (§9.3);
   - en el medio de acceso, si hay espacio físico y si hace falta segurización (§8.2).
2. **En PCM y FDM piden siempre tres cosas**: la técnica, los gráficos y los cálculos con unidades.
3. **No redondees la información** $I$. Los niveles se redondean **para arriba**; la cantidad de señales que entran en un canal, **para abajo**.
4. **En colas, definí cada término** antes de calcularlo.
5. **En teoría vale la definición textual del apunte.** En los *multiple choice* las opciones difieren en una palabra.

## Preguntas reales de teoría de los finales, con su respuesta

### 9. Teoría de colas

#### 9.1 Punto de saturación de un sistema de cola cerrada
**Salió:** 19/11/2021 y 17/12/2021 (MC); FAQ ("Explique brevemente y grafique adecuadamente el punto de saturación de un sistema de cola cerrada").

**Respuesta.** Modelo **cerrado** de población finita: $N$ terminales interactúan con una CPU y cada usuario alterna entre "pensando" (tiempo medio $E[t]$), esperando y recibiendo servicio (tiempo medio $E[s]$). Se grafica el tiempo de respuesta medio $W$ en función de $N$:
- Con $N=1$ no hay cola: $W=E[s]$.
- Con **pocos terminales**, la interferencia mutua es mínima: cuando uno pide CPU los demás suelen estar pensando, y la cola se forma solo ocasionalmente. Asíntota horizontal $W=E[s]$.
- Con $N\to\infty$, la probabilidad de CPU libre $p_0\to0$ y la curva tiende a la recta $W=N\,E[s]-E[t]$.
- La intersección de las dos asíntotas da el **punto de saturación**:
$$N^{*}=\frac{E[s]+E[t]}{E[s]}$$
Es el **número máximo de terminales que se pueden conectar sin causar interferencia mutua** (con tiempos exactamente iguales a las medias). Por encima de $N^*$, cada terminal agregada aumenta $W$ en aproximadamente $E[s]$ sin mejorar casi el rendimiento.

```
  W │                                  ╱  W = N·E[s] − E[t]
    │                                ╱
    │                              ╱ ·
    │                            ╱ ·       ← curva real de W(N)
    │                          ╱·
    │                       · ╱
    │               ·  ·    ╱
  E[s]┼·──·──·──·─────────╳──────────────  W = E[s]
    │                    ╱│
    │                  ╱  │
    └────────────────╱────┼──────────────── N
                          N* = (E[s] + E[t]) / E[s]
```
**Ejemplo** (apunte): $E[s]=0{,}2$ s y $E[t]=3$ s → $N^*=3{,}2/0{,}2=16$ terminales. Pasar de 20 a 30 terminales sube las interacciones un 4,78 % a costa de un 150 % más de tiempo de respuesta.

**En el MC:** "el punto correspondiente al número **máximo** de usuarios que se pueden conectar con una **mínima** interferencia mutua".

(teoria/Teoría de Colas.md)

#### 9.2 Intensidad de tráfico y factor de utilización
**Salió:** 19/11/2021 y 17/12/2021 (MC).

**Respuesta.** La **intensidad de tráfico** $u$ es la relación entre el **tiempo de servicio promedio** $E[s]$ y el **intervalo promedio entre arribos** $E[\tau]$:
$$u=\frac{E[s]}{E[\tau]}=\lambda\,E[s]\qquad(\lambda=1/E[\tau]=\text{frecuencia de arribos})\quad[\text{Erlang}]$$
Determina la **cantidad mínima de servidores**: con $E[s]=15$ s y $E[\tau]=10$ s, $u=1{,}5$ → hacen falta al menos 2 servidores.
El **factor de utilización del servicio** es $\rho=u/c$ (intensidad de tráfico por servidor): la probabilidad de que un servidor esté ocupado. Con un solo servidor, $\rho=u$.

**En el MC:** "Respuestas **A y D** correctas". A es "tiempo de servicio promedio sobre el intervalo promedio entre arribos" y D es "tiempo de servicio promedio **por** la frecuencia de arribos": son la misma magnitud, porque $\lambda=1/E[\tau]$.

(teoria/Teoría de Colas.md)

#### 9.3 Notación de Kendall: ¿qué simboliza la segunda M de M/M/1?
**Salió:** FAQ.

**Respuesta.** La notación de Kendall es $A/B/c/k/n/Z$:
- $A$: distribución del **intervalo entre arribos**;
- $B$: distribución del **tiempo de servicio**;
- $c$: número de servidores;
- $k$: capacidad del sistema;
- $n$: tamaño de la población;
- $Z$: disciplina de la cola.

La forma corta $A/B/c$ supone cola sin límite, población infinita y disciplina FIFO. En **M/M/1**, la **segunda M** indica que el **tiempo de servicio tiene distribución exponencial** (Markoviana: servicio "aleatorio"), la primera M indica intervalos entre arribos exponenciales (arribos de Poisson), y el 1 indica un solo servidor.

(teoria/Teoría de Colas.md)
