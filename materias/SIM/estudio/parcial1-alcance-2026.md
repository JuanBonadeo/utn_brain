# SIM — Parcial 1 2026: alcance y clase del 14/10

> Fuente: transcripción de la clase de teoría del 2026-10-14 (Ross, cap. 2).
> Lo que dice el profe pesa más que el "Mapa del parcial 1" de la wiki, que sale de años anteriores.

## Fecha y cronograma

| Fecha | Qué hay |
|---|---|
| Mié 21/10 | Probablemente clase con Juan (puede que el profe la tome para cerrar teoría) |
| Mié 28/10 | El profe cierra la teoría que entra en el parcial |
| Mié 4/11 | Empieza análisis de resultados (no entra) |
| **Sáb 7/11** | **Parcial 1** |
| Mié 11/11 | Última clase: análisis de resultados para el TP integrador |

Si hay paro, el cronograma se mueve.

## Qué entra

- **Ross, cap. 2, §2.1 a §2.9 inclusive.**
- **Lo visto antes en el apunte de Weitz.**

## Qué NO entra

- Ross cap. 1. Hay que leerlo (3 páginas), pero no se toma.
- Los ejercicios del libro.
- §2.10 completa.
- **Variables gamma**: segunda mitad de la pág. 28 y su continuación en la 29.
- En la pág. 29, **sí** entra el proceso de Poisson **no homogéneo**, hasta la proposición. La última proposición de la 29 y la pág. 30 no entran.
- **Análisis de resultados.** Se evalúa en la entrega final del TP integrador, no en el parcial.

> Las páginas son de la edición que mostró en pantalla. Verificalas contra tu copia.

## Demostraciones

Criterio del profe: *"lo que no explico no lo quiero pedir"*. Se pueden tomar las demostraciones que están en el libro **y** que él desarrolló en clase. Las propiedades sin desarrollo se piden solo enunciadas.

**Pueden tomarse:**

- Propiedades de §2.6: $E[aX+b]=aE[X]+b$, $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$, $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\,\mathrm{Cov}(X,Y)$. Lo confirmó cuando le preguntaron.
- Cadena Markov → Chebyshev → ley débil de los grandes números, incluido el paso del límite que el libro omite.
- $E$ y $\mathrm{Var}$ de Bernoulli y de binomial (la binomial como suma de Bernoulli).

**No se piden (solo saber el resultado):**

- Fórmulas de recurrencia de la binomial y de la Poisson. Hay que saber que existen y para qué sirven: la fórmula directa es cara de calcular, y la recurrencia es lo que usa AnyLogic internamente.
- Poisson como límite de la binomial.
- $E$ y $\mathrm{Var}$ de la geométrica, porque usan series: $E=1/p$, $\mathrm{Var}=(1-p)/p^2$.

## Lo que remarcó como importante

- **Proceso de Poisson y Poisson no homogéneo.** Es lo que más quiere explicar bien.
- **Teorema central del límite**: "muy importante", no lo va a saltear.
- **Normal**: importa sobre todo para el análisis de resultados.
- **Independencia** como hipótesis clave, por ejemplo en los tiempos entre arribos.
- Las variables vistas en Probabilidad y Estadística las va a pasar rápido. Las tenés que repasar vos.

## Resumen de lo dado

**§2.7: Markov, Chebyshev y leyes de los grandes números**

- **Markov**: si $X\ge 0$ y $a>0$, entonces $P\{X\ge a\}\le E[X]/a$.
- **Chebyshev**: $P\{|X-\mu|\ge k\sigma\}\le 1/k^2$.
  Se demuestra aplicando Markov a $(X-\mu)^2/\sigma^2$, que tiene esperanza 1, con $a=k^2$, y después sacando raíz en los dos miembros.
- **Ley débil**: si las $X_i$ son i.i.d. con media $\mu$, para todo $\varepsilon>0$ vale $P\{|\bar X-\mu|>\varepsilon\}\to 0$ cuando $n\to\infty$.
  - Se usa $E[\bar X]=\mu$ y $\mathrm{Var}(\bar X)=\sigma^2/n$. Esto último necesita independencia.
  - Se aplica Chebyshev con $k=\varepsilon\sqrt n/\sigma$, y queda $P\le\sigma^2/(n\varepsilon^2)$.
  - Se toma límite: la cota tiende a 0, y como $P\ge 0$, la probabilidad tiende a 0.
- **Ley fuerte**: con probabilidad 1, $\lim \bar X=\mu$. Lo que tiende a infinito es $n$, la cantidad de variables, no el tiempo.

**§2.8: VA discretas (hasta la geométrica)**

| Variable | $P\{X=i\}$ | $E$ | $\mathrm{Var}$ |
|---|---|---|---|
| Bernoulli | $p$ si $i=1$; $1-p$ si $i=0$ | $p$ | $p(1-p)$ |
| Binomial | $\binom{n}{i}p^i(1-p)^{n-i}$ | $np$ | $np(1-p)$ |
| Poisson | $e^{-\lambda}\lambda^i/i!$ | $\lambda$ | $\lambda$ |
| Geométrica (nº del ensayo con el primer éxito) | $(1-p)^{n-1}p$ | $1/p$ | $(1-p)/p^2$ |

**Errata del libro:** en la Poisson dice $\lambda<0$. Lo correcto es $\lambda>0$.

**Falta dar** (clase del 28/10):

- Binomial negativa e hipergeométrica.
- Toda la §2.9: uniforme, normal, TCL, exponencial, proceso de Poisson y Poisson no homogéneo.

## Choques con la wiki

1. El Mapa del parcial 1 pone las Unidades 9 y 10 (análisis de salida, comparación de sistemas) como temas del parcial. **Este año no entran.**
2. **Generación de números aleatorios** (Unidad 7) no se mencionó en el alcance. **Preguntar el 28/10** si entra vía Weitz. De eso dependen las preguntas "fijas" 9 y 10 de 2022–2023.
