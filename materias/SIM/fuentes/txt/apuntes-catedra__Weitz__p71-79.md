# Apunte cátedra Weitz — transcripción páginas 71 a 79 del PDF

> Fuente: `materias/SIM/fuentes/apuntes-catedra/Apunte Weitz con hojas rotadas y acotado.pdf`
> Contenido: fotocopias de *Simulation Modeling and Analysis* (Law & Kelton), páginas impresas 536–544 y 582–589.
> Cada página del PDF contiene dos páginas impresas del libro (izquierda y derecha), salvo la pág. 75 del PDF que contiene una sola.
> Los números manuscritos que aparecen abajo a la derecha de cada hoja son la numeración propia del apunte de cátedra.

---

--- pág. 71 --- *(contiene las páginas impresas 536 y 537)*

**536 SIMULATION MODELING AND ANALYSIS**

TABLE 9.3
Fixed-sample-size results for $E(G|\text{all components new}) = 0.78$ based on 500 experiments, reliability model

| $n$ | Estimated coverage | Average of (confidence interval half-length)/$\bar{X}(n)$ |
|---|---|---|
| 5 | $0.708 \pm 0.033$ | 1.16 |
| 10 | $0.750 \pm 0.032$ | 0.82 |
| 20 | $0.800 \pm 0.029$ | 0.60 |
| 40 | $0.840 \pm 0.027$ | 0.44 |

worked better for the $M/M/1$ queue than it did for the reliability model. Two possible reasons come to mind. First, an $X_j$ for the queueing system is actually an average of 25 individual delays, while an $X_j$ for the reliability model is computed from the three individual times to failure by a formula involving a minimum and a maximum. There are central limit theorems for certain types of correlated data which state that averages of these data become approximately normally distributed as the number of points in the average gets large. (See Sec. 9.5.3 for further discussion.) We therefore expect that if $X_j$ is the average of a large number of individual points (even though correlated), the degradation in coverage of the confidence interval may not be severe. Our experience indicates that many real-world simulations produce $X_j$'s of this type. A second reason is that the delays for the queueing system are themselves more normal-like than are the times to failure for the reliability model. In fact, recall that the distribution of the times to failure of the individual components was purposely chosen to be extremely nonnormal.

**Obtaining a Specified Precision.** One disadvantage of the fixed-sample-size procedure based on $n$ replications is that the analyst has no control over the confidence-interval half-length [or the precision of $\bar{X}(n)$]; for fixed $n$, the half-length will depend on Var($X$), the population variance of the $X_j$'s. In what follows we discuss procedures for determining the number of replications required to estimate the mean $\mu = E(X)$ with a specified error or precision.

We begin by defining two ways of measuring the error in the estimate $\bar{X}$. (The dependence on $n$ is suppressed, since the number of replications may be a random variable.) If the estimate $\bar{X}$ is such that $|\bar{X} - \mu| = \beta$, then we say that $\bar{X}$ has an *absolute error* of $\beta$. If we make replications of a simulation until the half-length of the $100(1-\alpha)$ percent confidence interval given by (9.1) is less than or equal to $\beta$ (where $\beta > 0$), then

$$1 - \alpha = P(\bar{X} - \text{half-length} \le \mu \le \bar{X} + \text{half-length})$$
$$= P(|\bar{X} - \mu| \le \text{half-length})$$
$$\le P(|\bar{X} - \mu| \le \beta)$$

[If $A$ and $B$ are events with $A$ being a subset of $B$, then $P(A) \le P(B)$.] Thus, $\bar{X}$ has an absolute error of at most $\beta$ with a probability of approximately $1-\alpha$. In

**OUTPUT DATA ANALYSIS FOR A SINGLE SYSTEM 537**

other words, if we construct 100 independent 90 percent confidence intervals using the above stopping rule, we would expect $\bar{X}$ to have an absolute error of at most $\beta$ in about 90 out of the 100 cases; in about 10 cases the absolute error would be greater than $\beta$.

Suppose that we have constructed a confidence interval for $\mu$ based on a fixed number of replications $n$. If we assume that our estimate $S^2(n)$ of the population variance will not change (appreciably) as the number of replications increases, an *approximate* expression for the total number of replications, $n_a^*(\beta)$, required to obtain an absolute error of $\beta$ is given by

$$n_a^*(\beta) = \min\left\{ i \ge n : t_{i-1,1-\alpha/2}\sqrt{\frac{S^2(n)}{i}} \le \beta \right\} \qquad (9.2)$$

(The colon ":" is read "such that.") We can determine $n_a^*(\beta)$ by iteratively increasing $i$ by 1 until a value of $i$ is obtained for which $t_{i-1,1-\alpha/2}\sqrt{S^2(n)/i} \le \beta$. [Alternatively, $n_a^*(\beta)$ can be approximated as the smallest integer $i$ satisfying $i \ge S^2(n)(z_{1-\alpha/2}/\beta)^2$.] If $n_a^*(\beta) > n$ and if we make $n_a^*(\beta) - n$ additional replications of the simulation, then the estimate $\bar{X}$ based on all $n_a^*(\beta)$ replications should have an absolute error of approximately $\beta$. The accuracy of Eq. (9.2) depends on how close the variance estimate $S^2(n)$ is to Var($X$).

> **Example 9.17.** For the bank of Example 9.14, suppose that we would like to estimate the expected average delay with an absolute error of 0.25 minute and a confidence level of 90 percent. From the 10 available replications, we get
>
> $$n_a^*(0.25) = \min\left\{ i \ge 10: t_{i-1,0.95}\sqrt{\frac{0.31}{i}} \le 0.25 \right\} = 16$$

We now discuss another way of measuring the error in $\bar{X}$. If the estimate $\bar{X}$ is such that $|\bar{X} - \mu|/|\mu| = \gamma$, then we say that $\bar{X}$ has a *relative error* of $\gamma$, or that the *percentage error* in $\bar{X}$ is $100\gamma$ percent. Suppose that we make replications of a simulation until the half-length of the confidence interval given by (9.1), divided by $|\bar{X}|$, is less than or equal to $\gamma$ ($0 < \gamma < 1$). This ratio is an estimate of the actual relative error. Then

$$1 - \alpha \approx P(|\bar{X} - \mu|/|\bar{X}| \le \text{half-length}/|\bar{X}|)$$
$$\le P(|\bar{X} - \mu| \le \gamma|\bar{X}|) \qquad \text{[(half-length/}|\bar{X}|) \le \gamma\text{]}$$
$$= P(|\bar{X} - \mu| \le \gamma|\bar{X} - \mu + \mu|) \qquad \text{(add, subtract } \mu)$$
$$\le P(|\bar{X} - \mu| \le \gamma(|\bar{X} - \mu| + |\mu|)) \qquad \text{(triangle inequality)}$$
$$= P((1-\gamma)|\bar{X} - \mu| \le \gamma|\mu|) \qquad \text{(algebra)}$$
$$= P(|\bar{X} - \mu|/|\mu| \le \gamma/(1-\gamma)) \qquad \text{(algebra)}$$

Thus, $\bar{X}$ has a relative error of at most $\gamma/(1-\gamma)$ with a probability of approximately $1-\alpha$. In other words, if we construct 100 independent 90 percent confidence intervals using the above stopping rule, we would expect $\bar{X}$ to have a relative error of at most $\gamma/(1-\gamma)$ in about 90 of the 100 cases; in

[MANUSCRITO] Número de página del apunte abajo a la derecha: **76**

---

--- pág. 72 --- *(contiene las páginas impresas 538 y 539)*

**538 SIMULATION MODELING AND ANALYSIS**

about 10 cases the relative error would be greater than $\gamma/(1-\gamma)$. Note that we get a relative error of $\gamma/(1-\gamma)$ rather than the desired $\gamma$, since we *estimate* $|\mu|$ by $|\bar{X}|$.

Suppose once again that we have constructed a confidence interval for $\mu$ based on a fixed number of replications $n$. If we assume that our estimates of both the population mean and population variance will not change (appreciably) as the number of replications increases, an approximate expression for the number of replications, $n_r^*(\gamma)$, required to obtain a relative error of $\gamma$ is given by

$$n_r^*(\gamma) = \min\left\{ i \ge n : \frac{t_{i-1,1-\alpha/2}\sqrt{S^2(n)/i}}{|\bar{X}(n)|} \le \gamma' \right\} \qquad (9.3)$$

where $\gamma' = \gamma/(1+\gamma)$ is the "adjusted" relative error needed to get an *actual* relative error of $\gamma$. [Again, $n_r^*(\gamma)$ is approximated as the smallest integer $i$ satisfying $i \ge S^2(n)[z_{1-\alpha/2}/\gamma'\bar{X}(n)]^2$.] If $n_r^*(\gamma) > n$ and if we make $n_r^*(\gamma) - n$ additional replications of the simulation, then the estimate $\bar{X}$ based on all $n_r^*(\gamma)$ replications should have a relative error of approximately $\gamma$.

> **Example 9.18.** For the bank of Example 9.14, suppose that we would like to estimate the expected average delay with a relative error of 0.10 and a confidence level of 90 percent. From the 10 available replications, we get
>
> $$n_r^*(0.10) = \min\left\{ i \ge 10: \frac{t_{i-1,0.95}\sqrt{0.31/i}}{2.03} \le 0.09 \right\} = 27$$
>
> where $\gamma' = 0.1/(1+0.1) = 0.09$.

The difficulty with using Eq. (9.3) directly to obtain an estimate $\bar{X}$ with a relative error of $\gamma$ is that $\bar{X}(n)$ and $S^2(n)$ may not be precise estimates of their corresponding population parameters. If $n_r^*(\gamma)$ is greater than the number of replications actually required, then a significant number of unnecessary replications may be made, resulting in a waste of computer resources. Conversely, if $n_r^*(\gamma)$ is too small, then an estimate $\bar{X}$ based on $n_r^*(\gamma)$ replications may not be as precise as we think. We now present a *sequential* procedure (new replications are added one at a time) for obtaining an estimate of $\mu$ with a specified relative error that takes only as many replications as are actually needed. The procedure assumes that $X_1, X_2, \ldots$ is a sequence of IID random variables that need not be normal.

The specific objective of the procedure is to obtain an estimate of $\mu$ with a relative error of $\gamma$ ($0 < \gamma < 1$) and a confidence level of $100(1-\alpha)$ percent. Choose an initial number of replications $n_0 \ge 2$ and let

$$\delta(n, \alpha) = t_{n-1,1-\alpha/2}\sqrt{\frac{S^2(n)}{n}}$$

be the usual confidence-interval half-length. Then the sequential procedure is as follows:

**OUTPUT DATA ANALYSIS FOR A SINGLE SYSTEM 539**

0. Make $n_0$ replications of the simulation and set $n = n_0$.
1. Compute $\bar{X}(n)$ and $\delta(n,\alpha)$ from $X_1, X_2, \ldots, X_n$.
2. If $\delta(n,\alpha)/|\bar{X}(n)| \le \gamma'$, use $\bar{X}(n)$ as the point estimate for $\mu$ and stop. Equivalently,

$$I(\alpha,\gamma) = [\bar{X}(n) - \delta(n,\alpha),\ \bar{X}(n) + \delta(n,\alpha)] \qquad (9.4)$$

is an approximate $100(1-\alpha)$ percent confidence interval for $\mu$ with the desired precision. Otherwise, replace $n$ by $n+1$, make an additional replication of the simulation, and go to step 1.

Note that the procedure computes a new estimate of Var($X$) after *each* replication is obtained, and that the total number of replications required by the procedure is a random variable.

> **Example 9.19.** For the bank of Example 9.14, suppose that we would like to obtain an estimate of the expected average delay with a relative error of $\gamma = 0.1$ and a confidence level of 90 percent. Using the previous $n_0 = 10$ replications as a starting point, we obtained
>
> number of replications at termination = 74
> $\bar{X}(74) = 1.76$, $S^2(74) = 0.67$
> 90 percent confidence interval: [1.60, 1.92]
>
> Note that the number of replications actually required, 74, is considerably larger than the 27 predicted in Example 9.18, due mostly to the imprecise variance estimate based on 10 replications.

Although the sequential procedure described above is intuitively appealing, the question naturally arises as to how well it performs in terms of producing a confidence interval with coverage close to the desired $1-\alpha$. In Law, Kelton, and Koenig (1981), it is shown that if $\mu \ne 0$ [and $0 < \text{Var}(X) < \infty$], then the coverage of the confidence interval given by Eq. (9.4) will be arbitrarily close to $1-\alpha$, provided the desired relative error is sufficiently close to 0. Based on sampling from a large number of stochastic models and probability distributions (including the $M/M/1$ queue and the above reliability model) for which the true values of $\mu$ are known, our recommendation is to use the sequential procedure with $n_0 \ge 10$ and $\gamma \le 0.15$. It was found that if these recommendations are followed, the estimated coverage (based on 500 independent experiments for each model) for a desired 90 percent confidence interval was never less than 0.864.

Analogous to the sequential procedure described above is a sequential procedure due to Chow and Robbins (1965) for constructing a $100(1-\alpha)$ percent confidence interval for $\mu$ with a small absolute error $\beta$. Furthermore, it can be shown that the coverage actually produced by the procedure will be arbitrarily close to $1-\alpha$ provided the desired absolute error $\beta$ is sufficiently close to 0. However, since the meaning of "*absolute error* sufficiently small" is

[MANUSCRITO] Número de página del apunte abajo a la derecha: **77**

---

--- pág. 73 --- *(contiene las páginas impresas 540 y 541)*

**540 SIMULATION MODELING AND ANALYSIS**

extremely model-dependent, and since the coverage results in Law (1980) indicate that the procedure is very sensitive to the choice of $\beta$, we do not recommend the use of the Chow and Robbins procedure in general.

**Recommended Use of the Procedures.** We now make our recommendations on the use of the fixed-sample-size and sequential procedures for terminating simulations. If one is performing an exploratory experiment where the precision of the confidence interval may not be overwhelmingly important, we recommend using the fixed-sample-size procedure. However, if the $X_j$'s are highly nonnormal and the number of replications $n$ is too small, the actual coverage of the constructed confidence interval may be somewhat lower than desired.

From an exploratory experiment consisting of $n$ replications, one can estimate the cost per replication and the population variance of the $X_j$'s, and then obtain from Eq. (9.2) a *rough estimate* of the number of replications, $n_a^*(\beta)$, required to estimate $\mu$ with a desired absolute error $\beta$. Alternatively, one can obtain from Eq. (9.3) a *rough estimate* of the number of replications, $n_r^*(\gamma)$, required to estimate $\mu$ with a desired relative error $\gamma$. Sometimes the choice of $\beta$ or $\gamma$ may have to be tempered by the cost associated with the required number of replications. If it is finally decided to construct a confidence interval with a small relative error $\gamma$, we recommend use of the sequential procedure with $\gamma \le 0.15$ and $n_0 \ge 10$. If one wants a confidence interval with a relative error $\gamma$ greater than 0.15, we recommend several successive applications of the fixed-sample-size procedure. In particular, one might estimate $n_r^*(\gamma)$, collect, say $[n_r^*(\gamma) - n]/2$ more replications, and then use (9.1) to construct a confidence interval based on the existing $[n + n_r^*(\gamma)]/2$ replications. If the estimated relative error of the resulting confidence interval is still greater than $\gamma'$, then $n_r^*(\gamma)$ can be reestimated based on a new variance estimate, and some portion of the necessary additional replications may be collected, etc. To construct a confidence interval with a small absolute error $\beta$, we once again recommend several successive applications of the fixed-sample-size approach. It should be mentioned that all of the statistical analyses [except the calculation of $n_a^*(\beta)$] for terminating simulations thus far discussed can be performed in SIMSCRIPT II.5 using an optional library routine called STAT.R [see Law (1979)].

Regardless of the cost per replication, we recommend always making at least three to five replications of a stochastic simulation to assess the variability of the $X_j$'s. If this is not possible due to time or cost considerations, then the simulation study should probably not be done at all.

**9.4.2 Estimating Other Measures of Performance**

In this section we discuss estimating measures of performance other than means. As the following example shows, comparing two or more systems by some sort of mean system response may result in misleading conclusions.

**OUTPUT DATA ANALYSIS FOR A SINGLE SYSTEM 541**

> **Example 9.20.** Consider the bank of Example 9.14, where the utilization factor $\rho = \lambda/(5\omega) = 0.8$. We compare the policy of having one queue for each teller (and jockeying) with the policy of having one queue feed all tellers on the basis of *expected average delay in queue* (see Example 9.14) and *expected time-average number of customers in queue*, which is defined by
>
> $$E\left[\frac{\int_0^T Q(t)\,dt}{T}\right]$$
>
> where $Q(t)$ is the number of customers in queue at time $t$ and $T$ is the bank's operating time ($T \ge 8$ hours). Table 9.4 gives the results of making one simulation run of each policy. [These simulation runs were performed so that the time of arrival of the $i$th customer ($i = 1, 2, \ldots, N$) was identical for both policies and so that the service time of the $i$th customer to begin service ($i = 1, 2, \ldots, N$) was the same for both policies.] Thus, on the basis of "average system response," it would appear that the two policies are equivalent. However, this is clearly not the case. Since customers need not be served in the order of their arrival with the multiqueue policy, we would expect this policy to result in greater variability of a customer's delay. Table 9.5 gives estimates, computed from the same two simulation runs used above, of the expected proportion of customers with a delay in the interval [0,5) (in minutes), the expected proportion of customers with a delay in [5,10), ..., the expected proportion of customers with a delay in [40,45) for both policies. (We did not estimate variances from these runs since, as pointed out in Sec. 4.4, variance estimates computed from correlated simulation output data are highly biased.) Observe from Table 9.5 that a customer is more likely to have a large delay with the multiqueue policy than with the single-queue policy. In particular, if 480 customers arrive in a day, then 33 and 6 of them would be expected to have delays greater than or equal to 20 minutes for the five-queue and one-queue policies, respectively. (For larger values of $\rho$, the differences between the two policies would be even greater.) This observation together with the greater equitability of the single-queue policy has probably led many organizations, e.g., banks and airlines, to adopt this policy.

We conclude from the above example that comparing alternative systems or policies on the basis of average system behavior alone can sometimes result in misleading conclusions and, furthermore, that proportions can be a useful measure of system performance. In Example 9.16 we showed how to obtain a point estimate and a confidence interval for an expected proportion. In this

TABLE 9.4
Simulation results for the two bank policies: averages

| | Estimates | |
|---|---|---|
| Measure of performance | Five queues | One queue |
| Expected operating time, hours | 8.14 | 8.14 |
| Expected average delay, minutes | 5.57 | 5.57 |
| Expected average number in queue | 5.52 | 5.52 |

[MANUSCRITO] Número de página del apunte abajo a la derecha: **78**

---

--- pág. 74 --- *(contiene las páginas impresas 542 y 543)*

**542 SIMULATION MODELING AND ANALYSIS**

TABLE 9.5
Simulation results for the two bank policies: proportions

| | Estimates of expected proportions of delays in interval | |
|---|---|---|
| Interval (minutes) | Five queues | One queue |
| [0,5) | 0.626 | 0.597 |
| [5,10) | 0.182 | 0.188 |
| [10,15) | 0.076 | 0.107 |
| [15,20) | 0.047 | 0.095 |
| [20,25) | 0.031 | 0.013 |
| [25,30) | 0.020 | 0 |
| [30,35) | 0.015 | 0 |
| [35,40) | 0.003 | 0 |
| [40,45) | 0 | 0 |

section we show how to perform similar analyses for probabilities and quantiles in the context of terminating simulations.

Let $X$ be a random variable defined on a replication as described in Sec. 9.4.1. Suppose that we would like to estimate the probability $p = P(X \in B)$, where $B$ is a set of real numbers. (For example, $B$ could be the interval $[20,\infty)$ in Example 9.20.) Make $n$ independent replications and let $X_1, X_2, \ldots, X_n$ be the resulting IID random variables. Let $S$ be the number of $X_j$'s that fall in the set $B$. Then $S$ has a binomial distribution (see Sec. 6.2.3) with parameters $n$ and $p$, and an unbiased point estimator for $p$ is given by

$$\hat{p} = \frac{S}{n}$$

Furthermore, a confidence interval for $p$ may be constructed using procedures described in Welch (1983, pp. 285–287) and Conover (1980, pp. 99–104) (see also Prob. 9.9).

> **Example 9.21.** For the bank of Example 9.14, suppose that we would like to get a point estimate for
>
> $$p = P(X \le 15) \qquad \text{where } X = \max_{0 \le t \le T} Q(t)$$
>
> In this case $B = [0,15]$. We made 100 independent replications of the bank simulation and obtained $\hat{p} = 0.77$. Thus, for approximately 77 out of every 100 days, we expect the maximum queue length during a day to be less than or equal to 15 customers.

Suppose now that we would like to estimate the $q$-quantile ($100q$th percentile) $x_q$ of the distribution of the random variable $X$ (see Sec. 6.4.3 for the definition). For example, the 0.5-quantile is the median. If $X_{(1)}, X_{(2)}, \ldots, X_{(n)}$ are the order statistics corresponding to the $X_j$'s from $n$

**OUTPUT DATA ANALYSIS FOR A SINGLE SYSTEM 543**

independent replications, then a point estimator for $x_q$ is the sample $q$-quantile $\hat{x}_q$, which is given by

$$\hat{x}_q = \begin{cases} X_{(nq)} & \text{if } nq \text{ is an integer} \\ X_{(\lfloor nq \rfloor + 1)} & \text{otherwise} \end{cases}$$

A confidence interval for $x_q$ can also be obtained; see Welch [1983, pp. 287–288) and Conover (1980, pp. 111–116).

> **Example 9.22.** For the bank of Example 9.14, suppose that we would like to decide how large a lobby is needed to accommodate customers waiting in the queue. If we let $X$ be the maximum queue length as defined in Example 9.21, then we might want to build a lobby large enough to hold $x_{0.95}$ customers, the 0.95-quantile of $X$. From the 100 replications in the previous example, we obtained $\hat{x}_{0.95} = X_{(95)} = 20$. Thus, if the lobby has room for 20 customers, this will be sufficient for approximately 95 out of every 100 days. Note also that $\hat{x}_{0.99} = X_{(99)} = 23$.

The interested reader may also want to consult Conover (1980, pp. 117–121) for a discussion of *tolerance limits*, which is an interval that contains a specified proportion of the *values* of the random variable $X$ (and does so with a certain prescribed confidence level).

**9.4.3 Choosing Initial Conditions**

As stated in Sec. 9.3, the measures of performance for a terminating simulation depend explicitly on the state of the system at time 0; thus, care must be taken in choosing appropriate initial conditions. Let us illustrate this potential problem by means of an example. Suppose that we would like to estimate the expected average delay of all customers who arrive and complete their delays between 12 noon and 1 P.M. (the busiest period) in a bank. Since the bank will probably be quite congested at noon, starting the simulation then with no customers present (the usual initial conditions for a queueing simulation) will cause our estimate of expected average delay to be biased low. We now discuss two heuristic approaches to this problem, the first of which appears to be used widely (see Sec. 9.5.1).

For the first approach, let us assume that the bank opens at 9 A.M. with no customers present. Then we can start the simulation at 9 A.M. with no customers present and run it for 4 simulated hours. In estimating the desired expected average delay, we use only the delays of those customers who arrive and complete their delays between noon and 1 P.M. The evolution of the simulation between 9 A.M. and noon (the "warmup period") determines the appropriate conditions for the simulation at noon. A disadvantage of this approach is that 3 hours of simulated time are not used directly in the estimate. As a result, one might compromise and start the simulation at some other time, say 11 A.M., with no customers present. However, there is no guarantee that the conditions in the simulation at noon will be representative of the actual

[MANUSCRITO] Número de página del apunte abajo a la derecha: **79**

**Errata del libro (transcripta tal cual arriba):** en la pág. 543, la referencia "Welch [1983, pp. 287–288)" abre con corchete y cierra con paréntesis.

---

--- pág. 75 --- *(contiene UNA sola página impresa: 544; la mitad derecha de la hoja está en blanco)*

**544 SIMULATION MODELING AND ANALYSIS**

conditions in the bank at noon. This approach can be carried out in SIMLIB (see Chap. 2) by reinitializing the statistical counters for subroutines SAMPST, TIMEST, and FILEST (see Prob. 2.7) at noon.

An alternative approach is to collect data on the number of customers present in the bank at noon for several different days. Let $\hat{p}_i$ be the proportion of these days that $i$ customers ($i = 0, 1, \ldots$) are present at noon. Then we simulate the bank from noon to 1 P.M. with the number of customers present at noon being randomly chosen from the distribution $\{\hat{p}_i\}$. (All customers who are being served at noon might be assumed to be just beginning their services. Starting all services fresh at noon results in an approximation to the actual situation in the bank, since the customers who are in the process of being served at noon would have partially completed their services. However, the effect of this approximation should be negligible for a simulation of length 1 hour.)

If more than one simulation run from noon to 1 P.M. is desired, then a different sample from $\{\hat{p}_i\}$ is drawn for each run. The $X_j$'s that result from these runs are still IID, since the initial conditions for each run are chosen independently from the same distribution.

*(La mitad derecha de la hoja está en blanco — sólo se ve la marca de la costura/encuadernación del fotocopiado.)*

[MANUSCRITO] Número de página del apunte abajo a la derecha: **80**

> **Nota de la transcripción:** entre esta hoja y la siguiente hay un salto en el original impreso (de la pág. 544 a la 582) y también en la numeración manuscrita (de 80 a 84).

---

--- pág. 76 --- *(contiene las páginas impresas 582 y 583)*

**CHAPTER 10 — COMPARING ALTERNATIVE SYSTEM CONFIGURATIONS**

> Recommended sections for a first reading: 10.1 through 10.3, 10.4.1

**10.1 INTRODUCTION**

In Chap. 9 we saw the importance of applying appropriate statistical analyses to the output from a simulation model of a *single* system. In this chapter we discuss statistical analyses of the output from several *different* simulation models that might represent competing system designs or alternative operating policies. This is a very important subject, since the real utility of simulation lies in comparing such alternatives before implementation. As the following example illustrates, appropriate statistical methods are essential if we are to avoid making serious errors leading to fallacious conclusions and, ultimately, poor decisions. We hope that this example will demonstrate the danger inherent in making decisions based on the output from a *single* run (or replication) of each alternative system.

**582**

**COMPARING ALTERNATIVE SYSTEM CONFIGURATIONS 583**

> **Example 10.1.** A bank planning to install an automated teller station must choose between buying one Zippytel machine or two Klunkytel machines. Although one Zippy costs twice as much to purchase, install, and operate as one Klunky, the Zippy works twice as fast. Since the total cost to the bank is thus the same regardless of its decision, the managers would like to install the system that will provide the best service.
>
> From available data, it appears that during a certain rush period, customers arrive one at a time according to a Poisson process with rate 1 per minute. The Zippy could provide service times that are IID exponential random variables with mean 0.9 minute. Alternatively, if two Klunkies are installed, each will yield service times that are IID exponential random variables with mean 1.8 minutes; in this case a single FIFO queue will be formed instead of two separate lines. Thus, we are comparing an $M/M/1$ queue with an $M/M/2$ queue, each with utilization factor $\rho = 0.9$, as shown in Fig. 10.1. The performance measure of interest is the expected average delay in queue of the first 100 customers, assuming that the first customer arrives to an empty and idle system; we denote these (expected) quantities by $d_Z(100)$ and $d_K(100)$ for the one-Zippy and two-Klunky cases, respectively. (The bank decided to ignore customer service times, since waiting in line is the most irritating part of the experience and customers are reasonably pacified as long as they are being served; see Prob. 10.1 for further consideration of this issue.) The bank's intrepid systems analyst decided to make a simulation run of length 100 customer delays for each system (using independent random numbers) and to use the average of the 100 delays in each case to infer whether $d_Z(100)$ or $d_K(100)$ is smaller, and thus make a recommendation.
>
> How likely is it that the analyst will make the right recommendation? To find out, we performed 100 independent experiments of the analyst's entire scheme and noted how many times the best system would have been recommended. The best system is actually the two-Klunky installation, since $d_Z(100) = 4.13$ and $d_K(100) = 3.70$. [These values were determined from the queueing-theoretic results in Kelton and Law (1985).] Our experiment was, thus, to

> [FIGURA pág. 583]: FIGURE 10.1 — "One Zippy or two Klunkies?" Diagrama esquemático de dos sistemas de colas. A la izquierda: un rectángulo rotulado "Zippy" (el servidor) con una única fila vertical de círculos (clientes) debajo, y una flecha hacia arriba indicando la llegada por el extremo inferior: es el $M/M/1$. A la derecha: dos rectángulos rotulados "Klunky" y "Klunky" (dos servidores), con un círculo bajo cada uno, unidos por una llave que converge hacia una única fila vertical de círculos, y una flecha hacia arriba en el extremo inferior indicando la llegada: es el $M/M/2$ con cola FIFO única.

[MANUSCRITO] Número de página del apunte abajo a la derecha: **84**

---

--- pág. 77 --- *(contiene las páginas impresas 584 y 585)*

**584 SIMULATION MODELING AND ANALYSIS**

perform 100 independent pairs of independent simulations of the two systems, and average the delays in each simulation to obtain $\hat{d}_Z(100)$ and $\hat{d}_K(100)$, say, and then recommend the Zippy or Klunky system according as $\hat{d}_Z(100)$ or $\hat{d}_K(100)$ was smaller; some of the results are in Table 10.1. In only 48 of our 100 experiments was $\hat{d}_K(100) < \hat{d}_Z(100)$, so the analyst would not really appear to have any better chance of making the right decision than making the wrong one.

We have an uneasy feeling that many simulation studies are carried out in a manner similar to that described in Example 10.1. The difficulty is that the simulation output data are stochastic, so comparing the two systems on the basis of only a single run of each is a very unreliable approach.

The following example indicates how the comparison in Example 10.1 could be improved.

> **Example 10.2.** To illuminate the problem with the one-run-of-each approach in Example 10.1, we plotted all 100 $\hat{d}_Z(100)$'s and $\hat{d}_K(100)$'s in the "$n=1$" pair of horizontal dot plots in Fig. 10.2; each circle (solid or hollow) represents the average of the 100 delays in a single simulation, positioned according to the scale at the bottom. Even though the *expected* average delay for the two-Klunky system is smaller than that for the one-Zippy system, the distributions of the *observed* average delays overlap substantially. This accounts for the distressingly large probability of making the wrong choice noted at the end of Example 10.1.

Instead, we could make some number, $n$, of complete independent replications of each alternative system, and compare the systems on the basis of their averages across replications. Specifically, let $X_{1j}$ be the average of the 100 delays in the one-Zippy system on the $j$th independent replication of this system, and let $X_{2j}$ be the average of the 100 delays in the two-Klunky system on its $j$th replication, for $j = 1, 2, \ldots, n$. (We also made the simulations so that the $X_{1j}$'s and the $X_{2j}$'s are independent.) Then if $\bar{X}_1(n)$ and $\bar{X}_2(n)$ are the sample means of the $X_{1j}$'s and $X_{2j}$'s, respectively, we would recommend the system with the smaller $\bar{X}_i(n)$. (The method of Example 10.1 is thus a special case, taking $n = 1$.)

TABLE 10.1
Testing the analyst's decision rule

| Experiment | $\hat{d}_Z(100)$ | $\hat{d}_K(100)$ | Recommendation | |
|---|---|---|---|---|
| 1 | 3.80 | 4.60 | Zippy | (wrong) |
| 2 | 3.17 | 8.37 | Zippy | (wrong) |
| 3 | 3.96 | 4.18 | Zippy | (wrong) |
| 4 | 1.91 | 5.77 | Zippy | (wrong) |
| 5 | 1.71 | 2.23 | Zippy | (wrong) |
| 6 | 6.16 | 4.72 | Klunky | (right) |
| 7 | 5.67 | 1.39 | Klunky | (right) |
| ⋮ | ⋮ | ⋮ | ⋮ | |
| 98 | 8.40 | 9.39 | Zippy | (wrong) |
| 99 | 7.70 | 1.54 | Klunky | (right) |
| 100 | 4.64 | 1.17 | Klunky | (right) |

**COMPARING ALTERNATIVE SYSTEM CONFIGURATIONS 585**

> [FIGURA pág. 585]: FIGURE 10.2 — "One Zippy vs. two Klunkies, as described in Examples 10.1 and 10.2." Cuatro pares de dot plots horizontales apilados verticalmente, rotulados a la derecha con llaves: $n=20$ (arriba), $n=10$, $n=5$ y $n=1$ (abajo). Eje horizontal: "Average delay in queue", con marcas en 0, 5, 10 y 15. Cada círculo representa el promedio de una réplica (o de $n$ réplicas). Recuadro de referencias arriba a la derecha con dos columnas, "Simulated" y "Expected": fila "2 Klunkies" (círculos huecos, línea de trazos para el valor esperado) y fila "1 Zippy" (círculos llenos, línea continua para el valor esperado). Dos líneas verticales cerca del centro-izquierda marcan los valores esperados $d_K(100) = 3.70$ (trazos) y $d_Z(100) = 4.13$ (continua). A medida que $n$ crece de 1 a 20, las nubes de puntos se concentran alrededor de sus esperanzas, pero siguen solapándose.

Table 10.2 shows the proportion of 100 independent pairs of $n$-replication averages in which the one-Zippy system appeared better, i.e., would result in the wrong recommendation, for $n = 1, 5, 10$, and 20. The chance of making an error falls as $n$ increases, but at a correspondingly higher cost of simulating. The four pairs of plots in Fig. 10.2 also indicate that as $n$ rises, the distributions of the $n$-replication averages (each circle represents such an average) tighten up around their expectations, but there is still considerable overlap even for $n = 20$, where the proportion of incorrect recommendations is still 0.34.

Examples 10.1 and 10.2 illustrate the need for careful design and analysis of comparative simulations. Indeed, even with $n = 20$ replications of each system design, Example 10.2 indicates that there is substantial room for error. One way of sharpening the comparison will be discussed in Sec. 11.2, and the above examples will be reworked in that context; see Example 11.2 in Sec. 11.2.4.

TABLE 10.2
Proportion of wrong recommendations in the $n$-replication method of Example 10.2

| $n$ | Proportion of experiments favoring the one-Zippy system |
|---|---|
| 1 | 0.52 |
| 5 | 0.43 |
| 10 | 0.38 |
| 20 | 0.34 |

[MANUSCRITO] Número de página del apunte abajo a la derecha: **85**

---

--- pág. 78 --- *(contiene las páginas impresas 586 y 587)*

**586 SIMULATION MODELING AND ANALYSIS**

Note that both Examples 10.1 and 10.2 dealt with terminating simulations (see Secs. 9.3 and 9.4). As we shall see in this chapter, a basic requirement for using many statistical methods for comparing alternative configurations is the ability to collect IID observations with expectation equal to the desired measure of performance. For terminating simulations, this is easily accomplished by simply making independent replications; e.g., a basic unit of observation in Examples 10.1 and 10.2 was the average of the 100 delays in a single *entire* replication of the model. If we want to compare alternative systems on the basis of steady-state behavior (see Secs. 9.3 and 9.5), however, the situation becomes more complicated, since we cannot easily obtain IID observations having expectation (approximately) equal to the desired steady-state measure of performance. There are different ways of dealing with steady-state comparisons, which will be discussed throughout the chapter, specifically in Secs. 10.2.4 and 10.4.4.

Our purpose in this chapter is to present several different types of comparison and selection problems that have been found useful in simulation, together with appropriate statistical procedures for their solution, and numerical examples. It will be assumed throughout this chapter that the various alternative systems are simply *given*. In many situations care should be taken in choosing *which* particular system variants to simulate; see Chap. 12 for discussion of how to choose appropriate alternative systems for comparison.

In Sec. 10.2 we treat the special but important case of comparing just two systems by constructing a confidence interval for the difference between their performance measures. These ideas are extended in Sec. 10.3 to confidence-interval comparisons of more than two systems. Section 10.4 introduces some procedures for selecting the "best" of several alternative systems, as well as other goals involving choice of certain "good" subsets from among the set of all alternatives. Appendixes 10A and 10B treat certain technical issues related to the selection procedures of Sec. 10.4.

**10.2 CONFIDENCE INTERVALS FOR THE DIFFERENCE BETWEEN PERFORMANCE MEASURES OF TWO SYSTEMS**

Here we consider the special case of comparing two systems on the basis of some performance measure, or expected *response*. We effect this comparison by forming a confidence interval for the *difference* in their expectations, rather than by doing a hypothesis test to see whether the observed difference is significantly different from zero. Whereas a test results in only a "reject" or "fail-to-reject" conclusion, a confidence interval gives us this information (according as the interval misses or contains zero, respectively) as well as quantifies how much the measures differ, if at all. Also, we shall take a parametric, i.e., normal-theory, approach here, even though nonparametric analogues could be used instead [see, for example, Conover (1980, pp. 223–225)]. The parametric approach is simple and familiar, and moreover

**COMPARING ALTERNATIVE SYSTEM CONFIGURATIONS 587**

should be quite robust in this context, since troublesome skewness (see Sec. 9.4.1) in the underlying distributions of the output random variables should be ameliorated upon subtraction (assuming the two output distributions are skewed in the same direction).

For $i = 1, 2$, let $X_{i1}, X_{i2}, \ldots, X_{in_i}$ be a sample of $n_i$ IID observations from system $i$, and let $\mu_i = E(X_{ij})$ be the expected response of interest; we want to construct a confidence interval for $\zeta = \mu_1 - \mu_2$. Whether or not $X_{1j}$ and $X_{2j}$ are independent depends on how the simulations are executed, and could determine which of the two confidence-interval approaches discussed in Secs. 10.2.1 and 10.2.2 are used.

**10.2.1 A Paired-$t$ Confidence Interval**

If $n_1 = n_2$ ($=n$, say), or we are willing to discard some observations from the system on which we actually have more data, we can pair $X_{1j}$ with $X_{2j}$ to define $Z_j = X_{1j} - X_{2j}$, for $j = 1, 2, \ldots, n$. Then the $Z_j$'s are IID random variables and $E(Z_j) = \zeta$, the quantity for which we want to construct a confidence interval. Thus, we can let

$$\bar{Z}(n) = \frac{\sum_{j=1}^{n} Z_j}{n}$$

and

$$\widehat{\text{Var}}[\bar{Z}(n)] = \frac{\sum_{j=1}^{n} [Z_j - \bar{Z}(n)]^2}{n(n-1)}$$

and form the (approximate) $100(1-\alpha)$ percent confidence interval

$$\bar{Z}(n) \pm t_{n-1,1-\alpha/2}\sqrt{\widehat{\text{Var}}[\bar{Z}(n)]} \qquad (10.1)$$

If the $Z_j$'s are normally distributed, this confidence interval is *exact*, i.e., it covers $\zeta$ with probability $1-\alpha$; otherwise, we rely on the central limit theorem (see Sec. 4.5), which implies that this coverage probability will be *near* $1-\alpha$ for large $n$. An important point here is that we did *not* have to assume that $X_{1j}$ and $X_{2j}$ are independent; nor did we have to assume that $\text{Var}(X_{1j}) = \text{Var}(X_{2j})$. Allowing positive correlation between $X_{1j}$ and $X_{2j}$ can be of great importance, since this leads to a reduction in $\text{Var}(Z_j)$ (see Prob. 4.13) and thus to a smaller confidence interval. Section 11.2 discusses a method (*common random numbers*) that can often induce this positive correlation between the observations on the different systems. The confidence interval in (10.1) will be called the *paired-$t$ confidence interval*, and in its derivation we essentially reduced the two-system problem to one involving a single sample, namely, the $Z_j$'s. In this sense, the paired-$t$ approach is the same as the method discussed in Sec. 9.4.1 for analysis of a single system. (Thus, the sequential confidence-interval

[MANUSCRITO] Número de página del apunte abajo a la derecha: **86**

---

--- pág. 79 --- *(contiene las páginas impresas 588 y 589)*

**588 SIMULATION MODELING AND ANALYSIS**

procedures of Sec. 9.4.1 could be applied here.) It is important to note that the $X_{ij}$'s are random variables defined over an entire *replication*; for example, $X_{1j}$ might be the average of the 100 delays on the $j$th replication of the Zippytel system of Example 10.2; it is *not* the delay of some individual customer.

> **Example 10.3.** For the inventory model of Sec. 1.5, suppose we want to compare two different $(s,S)$ policies in terms of their effect on the expected average total cost per month for the first 120 months of operation, where we assume that the initial inventory level is 60. For the first policy $(s,S) = (20,40)$, and the second policy sets $(s,S) = (20,80)$. Here, $X_{ij}$ is the average total cost per month of policy $i$ on the $j$th independent replication. We made the runs for policy 1 and policy 2 independently of each other and made $n = n_1 = n_2 = 5$ independent replications of the model under each policy; Table 10.3 contains the results. Using the paired-$t$ approach, we obtained $\bar{Z}(5) = 4.98$ and $\widehat{\text{Var}}[\bar{Z}(5)] = 2.44$, leading to the (approximate) 90 percent confidence interval [1.65, 8.31] for $\zeta = \mu_1 - \mu_2$. Thus, with approximately 90 percent confidence, we can say that $\mu_1$ differs from $\mu_2$; and it furthermore appears that policy 2 is superior, since it leads to a lower average operating cost (between 1.65 and 8.31 lower, which would *not* have been evident from a hypothesis test). We must use the word "approximate" to describe the confidence level, since $n_1 = n_2 = 5$ may or may not be "large" enough for this model for the central limit theorem to have taken effect.

**10.2.2 A Modified Two-Sample-$t$ Confidence Interval**

A second approach to forming a confidence interval for $\zeta$ does not pair up the observations from the two systems, but *does* require that the $X_{1j}$'s be independent of the $X_{2j}$'s. However, $n_1$ and $n_2$ can now be different.

To apply the classical two-sample-$t$ approach [see, for example, Devore (1982, pp. 287–291)], we *must* have $\text{Var}(X_{1j}) = \text{Var}(X_{2j})$; if these variances are not equal, the two-sample-$t$ confidence interval can exhibit serious coverage degradation. [If, however, $n_1 = n_2$, the two-sample-$t$ approach is fairly safe even if the variances differ; see Scheffé (1970) for further discussion.] Since equality of variances is probably not a safe assumption when simulating real systems, we would recommend against using the two-sample-$t$ approach.

TABLE 10.3
Average total cost per month for five independent replications of two inventory policies, and the differences

| $j$ | $X_{1j}$ | $X_{2j}$ | $Z_j$ |
|---|---|---|---|
| 1 | 126.97 | 118.21 | 8.76 |
| 2 | 124.31 | 120.22 | 4.09 |
| 3 | 126.68 | 122.45 | 4.23 |
| 4 | 122.66 | 122.68 | −0.02 |
| 5 | 127.23 | 119.40 | 7.83 |

**COMPARING ALTERNATIVE SYSTEM CONFIGURATIONS 589**

Instead, we shall give an old but reliable approximate solution, due to Welch (1938), to this problem of comparing two systems with unequal and unknown variances, called the *Behrens-Fisher problem* when the $X_{ij}$'s are normally distributed [see also Scheffé (1970)]. As usual, let

$$\bar{X}_i(n_i) = \frac{\sum_{j=1}^{n_i} X_{ij}}{n_i}$$

and

$$S_i^2(n_i) = \frac{\sum_{j=1}^{n_i} [X_{ij} - \bar{X}_i(n_i)]^2}{n_i - 1}$$

for $i = 1, 2$. Then compute the *estimated* degrees of freedom

$$\hat{f} = \frac{[S_1^2(n_1)/n_1 + S_2^2(n_2)/n_2]^2}{[S_1^2(n_1)/n_1]^2/(n_1 - 1) + [S_2^2(n_2)/n_2]^2/(n_2 - 1)}$$

and use

$$\bar{X}_1(n_1) - \bar{X}_2(n_2) \pm t_{\hat{f},1-\alpha/2}\sqrt{\frac{S_1^2(n_1)}{n_1} + \frac{S_2^2(n_2)}{n_2}} \qquad (10.2)$$

as an approximate $100(1-\alpha)$ percent confidence interval for $\zeta$. Since $\hat{f}$ will not, in general, be an integer, interpolation in the $t$ tables will probably be necessary. The confidence interval given by (10.2), which we will call the *Welch confidence interval*, can also be used to validate a simulation model of an existing system (see Sec. 5.6.2). If "system 1" is the real-world system on which we have physically collected data and "system 2" is the corresponding simulation model from which we have simulation output data, it is likely that $n_1$ will be far less than $n_2$. Finally, if we are comparing two simulated systems and want a "small" confidence interval, a sequential procedure due to Robbins, Simons, and Starr (1967) can be used, which is efficient in the sense of minimizing the final value of $n_1 + n_2$. It is also asymptotically correct in the sense that the confidence interval will have approximately the correct coverage probability as the prespecified confidence-interval width becomes small.

> **Example 10.4.** Since the runs for the two different inventory policies of Example 10.3 were done independently, we can apply the Welch approach to form an approximate 90 percent confidence interval for $\zeta$; we use the same $X_{ij}$ data as given in Table 10.3. We get $\bar{X}_1(5) = 125.57$, $\bar{X}_2(5) = 120.59$, $S_1^2(5) = 4.00$, $S_2^2(5) = 3.76$, and $\hat{f} = 7.99$. Interpolating in the $t$ tables leads to $t_{7.99,0.95} = 1.860$. Thus, the Welch confidence interval is [2.66, 7.30].

**10.2.3 Contrasting the Two Methods**

Since the inventory data of Table 10.3 were collected so that $n_1 = n_2$ and the $X_{1j}$'s were independent of the $X_{2j}$'s, we could apply either the paired-$t$ or Welch approach to construct a confidence interval for $\zeta$. It happened that the

[MANUSCRITO] Número de página del apunte abajo a la derecha: **87**

---

## Notas de la transcripción

- **Erratas del libro** (transcriptas tal cual en el cuerpo):
  - Pág. 543: `Welch [1983, pp. 287–288)` — abre corchete, cierra paréntesis.
- Todas las páginas del PDF son fotocopias con la sombra oscura de la costura del libro en el centro; en varias hojas el borde derecho muestra la espiral de la carpeta. Ninguna página resultó ilegible.
- La mitad derecha de la pág. 75 del PDF (impresa 544) está en blanco.
- Las anotaciones manuscritas se limitan a la numeración correlativa del apunte (76 a 80 y 84 a 87) en el ángulo inferior derecho de cada hoja; no hay notas manuscritas en el margen ni sobre el texto.
- Salto de contenido: entre la pág. 75 (impresa 544, fin del Cap. 9) y la pág. 76 (impresa 582, inicio del Cap. 10) faltan las páginas impresas 545–581 y los números manuscritos 81–83.
