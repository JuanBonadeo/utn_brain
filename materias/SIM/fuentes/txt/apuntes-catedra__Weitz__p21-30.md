# Apunte de cátedra (Weitz) — transcripción páginas 21–30 del PDF

Fuente: `materias/SIM/fuentes/apuntes-catedra/Apunte Weitz con hojas rotadas y acotado.pdf`
Texto original en inglés (Law & Kelton, *Simulation Modeling and Analysis*), fotocopiado en el apunte de cátedra.

---

--- pág. 21 del PDF --- (contiene: página impresa 60 [izquierda, sin número visible] y página impresa 61 [derecha]; numeración manuscrita del apunte al pie: **[MANUSCRITO] 19**)

### [Página izquierda — libro pág. 60]

**1.4.7 Simulation Output and Discussion**

The output (in a file named mm1.out if the FORTRAN or C program above was used) is shown in Fig. 1.37; since the same method for random-number generation was used for the programs in all three languages, they produced identical results. In this run, the average delay in queue was 0.430 minute, there was an average of 0.418 customer in the queue, and the server was busy

```
Single-server queueing system

Mean interarrival time            1.000 minutes

Mean service time                 0.500 minutes

Number of customers               1000


Average delay in queue            0.430 minutes

Average number in queue           0.418

Server utilization                0.460

Time simulation ended          1027.915 minutes
```

FIGURE 1.37
Output report, queueing model.

### [Página derecha — libro pág. 61]

**BASIC SIMULATION MODELING  61**

46 percent of the time. It took 1027.915 simulated minutes to run the simulation to the completion of 1000 delays, which seems reasonable since the expected time between customer arrivals was 1 minute. (It is not a coincidence that the average delay, average number in queue, and utilization are all so close together for this model; see App. 1B.)

Note that these particular numbers in the output were determined, at root, by the numbers the random-number generator happened to come up with this time. If a different random-number generator were used, or if this one were used in another way (with another "seed" or "stream," as discussed in Chap. 7), then different numbers would have been produced in the output. Thus, these numbers are not to be regarded as "The Answers," but rather as estimates (and perhaps poor ones) of the expected quantities we want to know about, $d(n)$, $q(n)$, and $u(n)$; the statistical analysis of simulation output data is discussed in Chaps. 9 through 12. Also, the results are functions of the input parameters, in this case the mean interarrival and service times, and the $n = 1000$ stopping rule; they are also affected by the way we initialized the simulation (empty and idle).

In some simulation studies, we might want to estimate *steady-state* characteristics of the model (see Chap. 9), i.e., characteristics of a model after the simulation has been running a very long (in theory, an infinite) amount of time. For the simple $M/M/1$ queue we have been considering, it is possible to compute *analytically* the steady-state average delay in queue, the steady-state time-average number in queue, and the steady-state server utilization, all of these measures of performance being 0.5 [see, for example, Ross (1989, p. 352)]. Thus, if we wanted to determine these steady-state measures, our estimates based on the stopping rule $n = 1000$ delays were not too far off, at least in absolute terms. However, we were somewhat lucky, since $n = 1000$ was chosen arbitrarily! In practice, the choice of a stopping rule that will give good estimates of steady-state measures is quite difficult. To illustrate this point, suppose for the $M/M/1$ queue that the arrival rate of customers were increased from 1 per minute to 1.98 per minute (the mean interarrival time is now 0.505 minute), that the mean service time is unchanged, and that we wish to estimate the steady-state measures from a run of length $n = 1000$ delays, as before. We performed this simulation run and got values for the average delay, average number in queue, and server utilization of 17.404 minutes, 34.831, and 0.997, respectively. Since the true steady-state values of these measures are 49.5 minutes, 98.01, and 0.99 (respectively), it is clear that the stopping rule cannot be chosen arbitrarily. We discuss how to specify the run length for a steady-state simulation in Chap. 9.

The reader may have wondered why we did not estimate the expected average waiting time in the system of a customer, $w(n)$, rather than the expected average delay in queue, $d(n)$, where the waiting time of a customer is defined as the time interval from the instant the customer arrives to the instant the customer completes service and departs. There were two reasons. First, for many queueing systems we believe that the customer's delay in queue while

---

--- pág. 22 del PDF --- (contiene: página impresa 62 [izquierda]; la mitad derecha de la hoja está en blanco. Numeración manuscrita al pie: **[MANUSCRITO] 20**, precedida de un garabato ilegible)

### [Página izquierda — libro pág. 62]

**62  SIMULATION MODELING AND ANALYSIS**

waiting for other customers to be served is the most troublesome part of the customer's wait in the system. Moreover, if the queue represents part of a manufacturing system where the "customers" are actually parts waiting for service at a machine (the "server"), then the delay in queue represents a loss, whereas the time spent in service is "necessary." Our second reason for focusing on the delay in queue is one of statistical efficiency. The usual estimator of $w(n)$ would be

$$\hat{w}(n) = \frac{\sum_{i=1}^{n} W_i}{n} = \frac{\sum_{i=1}^{n} D_i}{n} + \frac{\sum_{i=1}^{n} S_i}{n} = \hat{d}(n) + \bar{S}(n) \qquad (1.7)$$

where $W_i = D_i + S_i$ is the waiting time in system of the $i$th customer and $\bar{S}(n)$ is the average of the $n$ customers' service times. Since the service-time distribution would have to be known to perform a simulation in the first place, the expected or mean service time, $E(S)$, would also be known and an alternative estimator of $w(n)$ is

$$\tilde{w}(n) = \hat{d}(n) + E(S)$$

[Note that $\bar{S}(n)$ is an unbiased estimator of $E(S)$ in Eq. (1.7).] In almost all queueing simulations, $\tilde{w}(n)$ will be a more efficient (less variable) estimator of $w(n)$ than $\hat{w}(n)$ and is thus preferable (both estimators are unbiased). Therefore, if one wants an estimate of $w(n)$, estimate $d(n)$ and add the known expected service time, $E(S)$. In general, the moral is to replace estimators by their expected values whenever possible (see the discussion of indirect estimators in Sec. 11.5).

### [Página derecha]

En blanco (solo se ve el margen espiralado de la fotocopia).

---

--- pág. 23 del PDF --- (contiene: mitad izquierda en blanco; página impresa 74 [derecha, sin número visible — inicio de la Sec. 1.5]. Numeración manuscrita al pie izquierdo: **[MANUSCRITO] 21**)

### [Página izquierda]

En blanco.

### [Página derecha — libro pág. 74]

**1.5  SIMULATION OF AN INVENTORY SYSTEM**

We shall now see how simulation can be used to compare alternative ordering policies for an inventory system. Many of the elements of our model are representative of those found in actual inventory systems.

**1.5.1  Problem Statement**

A company that sells a single product would like to decide how many items it should have in inventory for each of the next $n$ months. The times between demands are IID exponential random variables with a mean of 0.1 month. The sizes of the demands, $D$, are IID random variables (independent of when the demands occur), with

$$D = \begin{cases} 1 & \text{w.p. } \tfrac{1}{6} \\ 2 & \text{w.p. } \tfrac{1}{3} \\ 3 & \text{w.p. } \tfrac{1}{3} \\ 4 & \text{w.p. } \tfrac{1}{6} \end{cases}$$

where w.p. is read "with probability."

At the beginning of each month, the company reviews the inventory level and decides how many items to order from its supplier. If the company orders $Z$ items, it incurs a cost of $K + iZ$, where $K = \$32$ is the *setup cost* and $i = \$3$ is the *incremental cost* per item ordered. (If $Z = 0$, no cost is incurred.) When an order is placed, the time required for it to arrive (called the *delivery lag* or *lead time*) is a random variable that is distributed uniformly between 0.5 and 1 month.

The company uses a stationary $(s, S)$ policy to decide how much to order, i.e.,

$$Z = \begin{cases} S - I & \text{if } I < s \\ 0 & \text{if } I \geq s \end{cases}$$

where $I$ is the inventory level at the beginning of the month.

---

--- pág. 24 del PDF --- (contiene: página impresa 76 [izquierda] y página impresa 77 [derecha]. Numeración manuscrita al pie: **[MANUSCRITO] 22**)

### [Página izquierda — libro pág. 76]

**76  SIMULATION MODELING AND ANALYSIS**

When a demand occurs, it is satisfied immediately if the inventory level is at least as large as the demand. If the demand exceeds the inventory level, the excess of demand over supply is backlogged and satisfied by future deliveries. (In this case, the new inventory level is equal to the old inventory level minus the demand size, resulting in a negative inventory level.) When an order arrives, it is first used to eliminate as much of the backlog (if any) as possible; the remainder of the order (if any) is added to the inventory.

So far we have discussed only one type of cost incurred by the inventory system, the ordering cost. However, most real inventory systems also have two additional types of costs, *holding* and *shortage* costs, which we discuss after introducing some additional notation. Let $I(t)$ be the inventory level at time $t$ [note that $I(t)$ could be positive, negative, or zero], let $I^+(t) = \max\{I(t), 0\}$ be the number of items physically on hand in the inventory at time $t$ [note that $I^+(t) \geq 0$], and let $I^-(t) = \max\{-I(t), 0\}$ be the backlog at time $t$ [$I^-(t) \geq 0$ as well]. A possible realization of $I(t)$, $I^+(t)$, and $I^-(t)$ is shown in Fig. 1.54. The time points at which $I(t)$ decreases are the ones at which demands occur.

For our model, we shall assume that the company incurs a holding cost of $h = \$1$ per item per month held in (positive) inventory. The holding cost includes such costs as warehouse rental, insurance, taxes, and maintenance, as well as the opportunity cost of having capital tied up in inventory rather than invested elsewhere. We have ignored in our formulation the fact that some holding costs are still incurred when $I^+(t) = 0$. However, since our goal is to *compare* ordering policies, ignoring this factor, which after all is independent of the policy used, will not affect our assessment of which policy is best. Now, since $I^+(t)$ is the number of items held in inventory at time $t$, the time-average (per month) number of items held in inventory for the $n$-month period is

$$\bar{I}^+ = \frac{\int_0^n I^+(t)\, dt}{n}$$

> [FIGURA pág. 76]: Figura 1.54 — "A realization of $I(t)$, $I^+(t)$, and $I^-(t)$ over time." Gráfico de escalera en el plano tiempo–nivel de inventario. Eje vertical marcado con $S$ (arriba) y $s$ (más abajo); eje horizontal $t$ con marcas en 1, 2, 3 (meses). Clave (Key) en el recuadro superior derecho: línea llena ——— $I(t)$; línea punteada ·········· $I^+(t)$; línea de puntos y rayas —·—·— $I^-(t)$. La trayectoria de $I(t)$ baja en escalones en los instantes en que ocurren las demandas, cruza el cero y toma valores negativos (zona marcada como $I^-(t)$, indicada con una flecha hacia la región bajo el eje); se señala con llave la cantidad $S - I(1)$ (el tamaño del pedido colocado en $t=1$). Al pie del gráfico, tres anotaciones sobre el eje temporal: "Place an order" (en $t \approx 1$), "Order arrives" (entre 1 y 2) y "Place an order" (en $t = 3$).

FIGURE 1.54
A realization of $I(t)$, $I^+(t)$, and $I^-(t)$ over time.

### [Página derecha — libro pág. 77]

**BASIC SIMULATION MODELING  77**

which is akin to the definition of the time-average number of customers in queue given in Sec. 1.4.1. Thus, the average holding cost per month is $h\bar{I}^+$.

Similarly, suppose that the company incurs a backlog cost of $\pi = \$5$ per item per month in backlog; this accounts for the cost of extra record keeping when a backlog exists, as well as loss of customers' goodwill. The time-average number of items in backlog is

$$\bar{I}^- = \frac{\int_0^n I^-(t)\, dt}{n}$$

so the average backlog cost per month is $\pi\bar{I}^-$.

Assume that the initial inventory level is $I(0) = 60$ and that no order is outstanding. We simulate the inventory system for $n = 120$ months and use the average total cost per month (which is the sum of the average ordering cost per month, the average holding cost per month, and the average shortage cost per month) to compare the following nine inventory policies:

| $s$ | 20 | 20 | 20 | 20 | 40 | 40 | 40 | 60 | 60 |
|---|---|---|---|---|---|---|---|---|---|
| $S$ | 40 | 60 | 80 | 100 | 60 | 80 | 100 | 80 | 100 |

We do not address here the issue of how these particular policies were chosen for consideration; statistical techniques for making such a determination are discussed in Chap. 12.

It should be noted that the state variables for a simulation model of this inventory system are the inventory level $I(t)$, the amount of an outstanding order from the company to the supplier, and the time of the last event [which is needed to compute the areas under the $I^+(t)$ and $I^-(t)$ functions].

**1.5.2  Program Organization and Logic**

Our model of the inventory system uses the following types of events:

| Event description | Event type |
|---|---|
| Arrival of an order to the company from the supplier | 1 |
| Demand for the product from a customer | 2 |
| End of the simulation after $n$ months | 3 |
| Inventory evaluation (and possible ordering) at the beginning of a month | 4 |

We have chosen to make the end of the simulation event type 3 rather than type 4, since at time 120 both "end-simulation" and "inventory-evaluation" events will eventually be scheduled and we would like to execute the former event first at this time. (Since the simulation is over at time 120, there is no sense in evaluating the inventory and possibly ordering, incurring an ordering cost for an order that will never arrive.) The execution of event type 3 before event type 4 is guaranteed because the timing routines (in all three languages) give preference to the lowest-numbered event if two or more events are

---

--- pág. 25 del PDF --- (contiene: página impresa 78 [izquierda] y página impresa 79 [derecha]. Numeración manuscrita al pie: **[MANUSCRITO] 23**)

### [Página izquierda — libro pág. 78]

**78  SIMULATION MODELING AND ANALYSIS**

scheduled to occur at the same time. In general, a simulation model should be designed to process events in an appropriate order when time ties occur. An event graph (see Sec. 1.4.9) appears in Fig. 1.55.

There are three types of random variates needed to simulate this system. The interdemand times are distributed exponentially, so the same algorithm (and code) as developed in Sec. 1.4 can be used here. The demand-size random variate $D$ must be discrete, as described above, and can be generated as follows. First divide the unit interval into the contiguous subintervals $C_1 = [0, \tfrac{1}{6})$, $C_2 = [\tfrac{1}{6}, \tfrac{1}{2})$, $C_3 = [\tfrac{1}{2}, \tfrac{5}{6})$, and $C_4 = [\tfrac{5}{6}, 1]$, and obtain a $U(0,1)$ random variate $U$ from the random-number generator. If $U$ falls in $C_1$, return $D = 1$; if $U$ falls in $C_2$, return $D = 2$; and so on. Since the width of $C_1$ is $\tfrac{1}{6} - 0 = \tfrac{1}{6}$, and since $U$ is uniformly distributed over $[0, 1]$, the probability that $U$ falls in $C_1$ (and thus that we return $D = 1$) is $\tfrac{1}{6}$; this agrees with the desired probability that $D = 1$. Similarly, we return $D = 2$ if $U$ falls in $C_2$, having probability equal to the width of $C_2$, $\tfrac{1}{2} - \tfrac{1}{6} = \tfrac{1}{3}$, as desired, and so on for the other intervals. The subprograms to generate the demand sizes all use this principle, and take as input the cutoff points defining the above subintervals, which are the *cumulative* probabilities of the distribution of $D$.

The delivery lags are uniformly distributed, but not over the unit interval $[0, 1]$. In general, we can generate a random variate distributed uniformly over any interval $[a, b]$ by generating a $U(0,1)$ random number $U$, and then returning $a + U(b - a)$. That this method is correct seems intuitively clear, but will be formally justified in Sec. 8.3.1.

Of the four events, only three actually involve state changes (the end-simulation event being the exception). Since their logic is language-independent, we will describe it here.

The order-arrival event is flowcharted in Fig. 1.56, and must make the changes necessary when an order (which was previously placed) arrives from the supplier. The inventory level is increased by the amount of the order, and

> [FIGURA pág. 78]: Figura 1.55 — "Event graph, inventory model." Grafo de eventos con cuatro nodos elípticos: "Order arrival", "Demand", "Evaluate" y "End simulation". Los nodos "Demand" y "Evaluate" tienen cada uno un arco ondulado (línea en zigzag) que vuelve sobre sí mismos (auto-programación con retardo). Un arco ondulado va de "Order arrival" a "Demand" y otro de "Demand" a "Evaluate". Una flecha curva larga sale de "Evaluate" y llega a "Order arrival". Debajo, un arco ondulado horizontal apunta al nodo "End simulation".

FIGURE 1.55
Event graph, inventory model.

### [Página derecha — libro pág. 79]

**BASIC SIMULATION MODELING  79**

> [FIGURA pág. 79]: Figura 1.56 — "Flowchart for order-arrival routine, inventory model." Diagrama de flujo vertical: óvalo "Order-arrival event" → caja "Increment the inventory level by the amount previously ordered" → caja "Eliminate order-arrival event from consideration" → óvalo "Return". [MANUSCRITO] Junto a la flecha entre la primera y la segunda caja hay un garabato/tilde manuscrito ilegible.

FIGURE 1.56
Flowchart for order-arrival routine, inventory model.

> [FIGURA pág. 79]: Figura 1.57 — "Flowchart for demand routine, inventory model." Diagrama de flujo vertical: óvalo "Demand event" → caja "Generate the size of this demand" → caja "Decrement the inventory level by this demand size" → caja "Schedule the next demand event" → óvalo "Return".

FIGURE 1.57
Flowchart for demand routine, inventory model.
