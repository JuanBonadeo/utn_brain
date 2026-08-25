**TRABAJO PRÁCTICO DE SIMULACIÓN**

**COLA SIMPLE**

Comisión 403

29/08/2017

|  |  |  |
| --- | --- | --- |
| **ALUMNO** | **LEGAJO** | **CORREO ELECTRÓNICO** |
| **Guadagnoli, Luciano Ismael** | 27.711 | luciano.guadagnoli@gmail.com |
| **Ciancio, Damián** | 41.895 | damian.ciancio@yahoo.com.ar |
| **Castaño Landin, Alexis** | 40.308 | a.castano.landin@gmail.com |
| **Ponce Agüero, Rodrigo** | 40.293 | ponceaguero.rodrigo@yahoo.com |
| **Arnold, Joel** | 34.392 | ar.joelarnold@yahoo.com.ar |

# OBJETIVO

Desarrollar un algoritmo con el software Wolfram Mathematica que simule un sistema de colas del tipo M/M/1 y sacar conclusiones analizando los gráficos generados con el aplicativo.

# FUNDAMENTOS DEL PROBLEMA

Una cola M/M/1 es un sistema al que los clientes llegan según una distribución de Poisson, la atención se presta según una negativa exponencial y tienen un único servidor. Por tanto:

* **La tasa de arribos es:** a(t)= λe-λt
* **La tasa de servicio es:** a(t)=µe.µt

![](data:image/png;base64...)

**DONDE:**

λ = tasa de arribos (clientes / tiempo)

µ = tasa de servicio (cliente / tiempo)

**Nota**: para que el sistema sea estable debe darse que λ / µ < 1

# REPORTE Y GRÁFICOS

* Utilización promedio de los servidores: 49.7766%
* Tasa media de llegadas: 0.055368 clientes/minuto
* Tasa media de servicios: 8.99439 minutos/cliente

N° promedio en el tiempo de clientes en cola: 0.585957 clientes

Valor analítico - fórmula: 0.5 clientes

![](data:image/x-emf;base64...)

**Fig. 1 - Número promedio de clientes en cola**

Demora promedio por cliente en cola: 10.477 minutos

Valor analítico - fórmula: 9 minutos

![](data:image/x-emf;base64...)

**Fig. 2 – Demora promedio por cliente en cola**

Tiempo promedio de clientes en sistema: 19.6758 minutos

Valor analítico - fórmula: 18 clientes

![](data:image/x-emf;base64...)

**Fig. 3 – Tiempo promedio de clientes en el sistema**

Nro. promedio en el tiempo de clientes en sistema: 1.1004 clientes

Valor analítico - fórmula: 1 cliente

![](data:image/x-emf;base64...)

**Fig. 4 – Número promedio de clientes en el sistema**

Probabilidad de que haya un cliente en el sistema: 0.246612

Valor analítico - fórmula: 0.25

![](data:image/x-emf;base64...)

**Fig. 5 – Probabilidad de que haya un cliente en el sistema**

Promedio de promedios de clientes en el sistema – Método de Lotes

Media muestral: 1.10063

![](data:image/x-emf;base64...)

**Fig. 6 - Promedio de promedios de clientes en el sistema – Método de Lotes**

Nro. promedio en el tiempo de clientes en sistema: 0.980244 clientes

Valor analítico - fórmula: 1. Clientes

![](data:image/x-emf;base64...)

**Fig. 7 - Promedio de promedios de clientes en el sistema – Método de varias réplicas**

# CÓDIGO DE LA SIMULACION

Quit;

ClearAll;

**(\*\*\*\*\* DEFINICION DE FUNCIONES \*\*\*\*\*)**

**(\* Rutina de tiempos \*)**

tiempos[] := Module[{menor, eme},

menor = Position[listaDeEventos, Min[listaDeEventos]];

eme = First[First[menor]];

tiempoUltimoEvento = reloj;

reloj = listaDeEventos[[eme]];

proximoEvento = tiposEventos[[eme]];

];

**(\* Rutina de arribos \*)**

arribos[] := Module[{tarr},

tarr = RandomVariate[ExponentialDistribution[1/tmEntreArribos]];

listaDeEventos[[1]] = reloj + tarr;

If[estadoServidor == "D",

estadoServidor = "O";

tserv = RandomVariate[ExponentialDistribution[1/tmDeServicio]];

listaDeEventos = ReplacePart[listaDeEventos, 2 -> (reloj + tserv)];

tsAcumuladoUlt = tsAcumulado; (\*Corrección del % de utilización del servidor \*)

tsAcumulado = tsAcumulado + tserv;

completaronDemora = completaronDemora + 1;

,(\* Else \*)

areaQDeT =

areaQDeT + (nroDeClientesEnCola \* (reloj - tiempoUltimoEvento));

nroDeClientesEnCola = nroDeClientesEnCola + 1;

cola = Prepend[cola, reloj];

];

];

**(\* Rutina de partidas \*)**

partidas[] := Module[{tserv, tdem},

If[nroDeClientesEnCola > 0,

tserv = RandomVariate[ExponentialDistribution[1/tmDeServicio]];

listaDeEventos =

ReplacePart[listaDeEventos, 2 -> (reloj + tserv)];

tdem = reloj - cola[[1]];

demoraAcumulada = demoraAcumulada + tdem;

completaronDemora = completaronDemora + 1;

tsAcumuladoUlt = tsAcumulado;(\* Corrección del % de utilización del servidor \*)

tsAcumulado = tsAcumulado + tserv;

areaQDeT =

areaQDeT + (nroDeClientesEnCola\*(reloj - tiempoUltimoEvento));

nroDeClientesEnCola = nroDeClientesEnCola - 1;

cola = Delete[cola, 1],(\* Else \*)

estadoServidor = "D";

listaDeEventos = ReplacePart[listaDeEventos, 2 -> 999999];

];

];

**(\* Cálculo de variables de respuesta \*)**

calculaVR[] := Module[{},

nroPromCliCola = areaQDeT/reloj;

nroPromCliSis = areaSDeT/reloj;(\* Gráfico nro. promedio de clientes en el sistema \*)

demPromPorCli = demoraAcumulada/completaronDemora;

demPromPorCliSis = (demoraAcumulada + tsAcumulado)/completaronDemora; (\* Gráfico tiempo promedio de clientes en el sistema \*)

(\* utilizServ=tsAcumulado/reloj; Corrección del % de utilización del servidor \*)

utilizServ = tsAcumuladoUlt/reloj; (\* Corrección del % de utilización del servidor \*)

];

**(\* Definición e inicialización de variables \*)**

reloj = 0;

estadoServidor = "D";

proximoEvento = "null";

tiposEventos = {"Arribo", "Partida"};

listaDeEventos = {};

cola = {};

tsAcumulado = 0.0;

tsAcumuladoUlt =

0.0;(\* Corrección del % de utilización del servidor \*)

demoraAcumulada = 0.0;

nroDeClientesEnCola = 0;

areaQDeT = 0.0;

areaSDeT = 0.0;(\* Gráfico nro. promedio de clientes en el sistema \*)

nroCCUlt = 0;(\* Gráfico nro. promedio de clientes en el sistema \*)

tiempoUltimoEvento = 0.0;

completaronDemora = 0;

tmEntreArribos = 18.0;(\* 1/\[Lambda] \*)

tmDeServicio = 9.0;(\* 1/\[Mu] \*)

tmax = 2000\*60; (\* 2000 horas - 120000 minutos \*)

tasaLlegadas = 0.0;

tasaServicios = 0.0;

factorUtilizacion = 0.0;

probClientes = 0.0;

vRespuesta = {};

areaSDeTNue = {}; (\* Gráfico método de subintervalos \*)

listaDeEventos =

Append[listaDeEventos,

RandomVariate[ExponentialDistribution[1/tmEntreArribos]]];

listaDeEventos = Append[listaDeEventos, 999999];

tabla = Table[{"Reloj", "Tipo\_Ev", "t\_Arribos", "t\_Partidas",

"estado\_serv", "nro\_CC", "nro\_CCD", "area\_Qt", "ts\_acum",

"dem\_Acum", "area\_St"}, 1]; (\* Gráfico nro. promedio de clientes en el sistema \*)

tabla = Append[

tabla, {reloj, proximoEvento, listaDeEventos[[1]],

listaDeEventos[[2]], estadoServidor, nroDeClientesEnCola,

completaronDemora, areaQDeT, tsAcumulado, demoraAcumulada,

areaSDeT}];(\* Gráfico nro. promedio de clientes en el \

sistema \*)

vRespuesta =

Table[{"Reloj", "Nro\_PTCC", "Dem\_PPC", "Uti\_PS", "Nro\_PTCS",

"Dem\_PPCS"},

1]; (\* Gráficos nro. y tiempo promedio de clientes en el sistema \*)

**(\* Programa principal \*)**

While[reloj <= tmax,

a = tiempos[];

If[proximoEvento == "Arribo",

a = arribos[];

,

a = partidas[];

];

**(\*Gráfico nro. promedio de clientes en el sistema \*)**

(\* If - 1 \*)

If[(estadoServidor == "D" || nroDeClientesEnCola > 0 ||

nroCCUlt > 0) && reloj > 0,

(\* If - 2 \*)

If[nroDeClientesEnCola > 0,

(\* If - 3 \*)

If[proximoEvento == "Partida",

areaSDeT =

areaSDeT + ((reloj - tiempoUltimoEvento)\*(nroCCUlt + 1)),(\*

Else - 3 \*)

areaSDeT =

areaSDeT + ((reloj - tiempoUltimoEvento)\*nroDeClientesEnCola)];

nroCCUlt = nroDeClientesEnCola;,(\* Else - 2 \*)

areaSDeT =

areaSDeT + ((reloj - tiempoUltimoEvento)\*(nroCCUlt + 1));

nroCCUlt = 0;],(\* Else - 1 \*)

nroCCUlt = 0;

];

(\*FIN Gráfico nro. promedio de clientes en el sistema \*)

tabla =

Append[tabla, {reloj, proximoEvento, listaDeEventos[[1]],

listaDeEventos[[2]], estadoServidor, nroDeClientesEnCola,

completaronDemora, areaQDeT, tsAcumulado, demoraAcumulada,

areaSDeT}]; (\* Gráfico nro. promedio de clientes en el sistema \*)

a = calculaVR[];

vRespuesta =

Append[vRespuesta, {reloj, nroPromCliCola, demPromPorCli,

utilizServ, nroPromCliSis, demPromPorCliSis}];

(\* Gráficos nro. y tiempo promedio de clientes en el sistema \*)

];

nroPromCliCola = areaQDeT/reloj;

nroPromCliSis =

areaSDeT/reloj;

(\* Gráfico nro. promedio de clientes en el sistema \*)

demPromPorCli = demoraAcumulada/completaronDemora;

demPromPorCliSis = (demoraAcumulada + tsAcumulado)

completaronDemora;

(\*Gráfico tiempo promedio de clientes en el sistema \*)

(\*utilizServ=tsAcumulado/reloj; Corrección del % de utilización del servidor \*)

utilizServ =

tsAcumuladoUlt/

reloj;(\* Corrección del % de utilización del servidor \*)

tasaLlegadas = completaronDemora/tiempoUltimoEvento;

tasaServicios = tsAcumulado/completaronDemora;

factorUtilizacion =

tmEntreArribos^(-1)/

tmDeServicio^(-1); (\* \[Lambda]/\[Mu] \*)

probClientes = (1 - factorUtilizacion)\*(factorUtilizacion)^3;

(\* (1-(\[Lambda]/\[Mu])).(\[Lambda]/\[Mu])3 \*)

**(\* Reporte \*)**

Print["Utilización promedio de los servidores: ", utilizServ\*100, "%"]

Print["Tasa media de llegadas: ", tasaLlegadas, " clientes/minuto"]

Print["Tasa media de servicios: ", tasaServicios, " minutos/cliente"]

Grid[tabla];

Grid[vRespuesta];

**(\* Gráficos \*)**

**(\* Gráfico 1 - Nro. promedio en el tiempo de clientes en cola \*)**

(\* Creamos una tabla sólo con el nro. promedio de clientes en cola \*)

nroPCCt = vRespuesta[[All, 2]];

nroPCCt = Delete[nroPCCt, 1];

Grid[nroPCCt];

g1 = ListLinePlot[nroPCCt, AxesLabel -> {tiempo, NPCC}];

nroPCCm = (factorUtilizacion)^2\*(1 - factorUtilizacion)^(-1); (\* valor analítico - fórmula \*)

solana1 = Plot[nroPCCm, {x, 0, tiempoUltimoEvento}, PlotStyle -> Green];

Print["Nro. promedio en el tiempo de clientes en cola: ",

nroPromCliCola, " clientes"];

Print["Valor analítico - fórmula: ", nroPCCm, " clientes"];

Show[g1, solana1]

**(\* Gráfico 2 - Demora promedio por cliente en cola \*)**

(\* Creamos una tabla sólo con la demora promedio de clientes en cola \*)

demPCCt = vRespuesta[[All, 3]];

demPCCt = Delete[demPCCt, 1];

Grid[demPCCt];

g2 = ListLinePlot[demPCCt, AxesLabel -> {tiempo, DPCC}];

demPCCm = (tmEntreArribos^(-1)/

tmDeServicio^(-2))\*(1 -

factorUtilizacion)^(-1); (\* valor analítico - fórmula \*)

solana2 =

Plot[demPCCm, {x, 0, tiempoUltimoEvento}, PlotStyle -> Green];

Print["\nDemora promedio por cliente en cola: ", demPromPorCli,

" minutos"];

Print["Valor analítico - fórmula: ", demPCCm, " minutos"];

Show[g2, solana2]

**(\* Gráfico 3 - Tiempo promedio de clientes en sistema \*)**

(\* Creamos una tabla sólo con el tiempo promedio de clientes en sistema \*)

tiePCSt = vRespuesta[[All, 6]];

tiePCSt = Delete[tiePCSt, 1];

Grid[tiePCSt];

g3 = ListLinePlot[tiePCSt, AxesLabel -> {tiempo, TPCS}];

tiePCSm =

tmDeServicio\*(1 -

factorUtilizacion)^(-1); (\* valor analítico - fórmula \*)

solana3 =

Plot[tiePCSm, {x, 0, tiempoUltimoEvento}, PlotStyle -> Green];

Print["\nTiempo promedio de clientes en sistema: ", demPromPorCliSis,

" minutos"];

Print["Valor analítico - fórmula: ", tiePCSm, " clientes"];

Show[g3, solana3]

**(\* Gráfico 4 - Nro. promedio en el tiempo de clientes en sistema \*)**

(\* Creamos una tabla sólo con el nro. promedio de clientes en sistema \*)

nroPCSt = vRespuesta[[All, 5]];

nroPCSt = Delete[nroPCSt, 1];

Grid[nroPCSt];

g4 = ListLinePlot[nroPCSt, AxesLabel -> {tiempo, NPCS},

PlotRange -> All];

nroPCSm =

factorUtilizacion\*((1 -

factorUtilizacion)^(-1)); (\* valor analítico - fórmula \*)

solana4 =

Plot[nroPCSm, {x, 0, tiempoUltimoEvento}, PlotStyle -> Green];

Print["\nNro. promedio en el tiempo de clientes en sistema: ",

nroPromCliSis, " clientes"];

Print["Valor analítico - fórmula: ", nroPCSm, " clientes"];

Show[g4, solana4]

**(\* Gráfico 6 - Método de subintervalos \*)**

lonPerTra = 1500; (\* Longitud en minutos del período transitorio \*)

(\* lonPerTra = 80; Prueba \*)

lonSubInt = 3950; (\* Longitud en minutos de cada subintervalo \*)

(\* lonSubInt = 25; Prueba \*)

canSubInt =

Round[(tmax - lonPerTra)/lonSubInt];(\* cantidad de subintervalos \*)

subInt = tabla[[All, {1, 11}]];

subInt = Delete[subInt, 1];

solana5 =

ParametricPlot[{{lonPerTra, t}, {lonPerTra + lonSubInt,

t}, {lonPerTra + 2\*lonSubInt, t}, {lonPerTra + 3\*lonSubInt,

t}, {lonPerTra + 4\*lonSubInt, t}, {lonPerTra + 5\*lonSubInt,

t}, {lonPerTra + 6\*lonSubInt, t}, {lonPerTra + 7\*lonSubInt,

t}, {lonPerTra + 8\*lonSubInt, t}, {lonPerTra + 9\*lonSubInt,

t}, {lonPerTra + 10\*lonSubInt, t}}, {t, 0, tiempoUltimoEvento},

PlotStyle -> Green];

Grid[subInt];

medMue = 0.0;

tieLim = lonPerTra + lonSubInt;

(\* PPrint["1 - tieLim: ", tieLim]; \*)

i = 1;

While [subInt[[i, 1]] < lonPerTra, areaSDeTAnt = subInt[[i, 2]];

i++] (\* quitamos el período inicial \*)

(\* Print["1 - areaSDeTAnt: ", areaSDeTAnt]; \*)

For[j = 1, j <= canSubInt, j++,

tieLim = lonPerTra + (j\*lonSubInt);

While[subInt[[i, 1]] < tieLim,

areaSDeTNue = Append[areaSDeTNue, subInt[[i, 2]]]; i++] ;

medMue =

medMue + ((Last[areaSDeTNue] - areaSDeTAnt)/lonSubInt)/canSubInt;

Print["Area bajo la curva del subintervalo - ", j, ": ",

Last[areaSDeTNue] - areaSDeTAnt,

" - Media del subintervalo: ", (Last[areaSDeTNue] - areaSDeTAnt)/

lonSubInt]; (\* tabla de áreas de cada subintervalo \*)

areaSDeTAnt = Last[areaSDeTNue];

(\* Print[j, " - areaSDeTAnt: ", areaSDeTAnt]; \*)

]

Print["Media muestral: ", medMue];

Show[g4, solana5]

**(\* Gráfica 5 - Probabilidad de 1 cliente en sistema \*)**

p1Tabla = tabla[[All, {1, 5, 6}]];

p1Tabla = Delete[p1Tabla, 1];

p1CSistTabla = {};

t1CSistAcum = 0;

i = 1;

While[ i <= Length[p1Tabla],

If[ (Part[p1Tabla, i, 2 ]) == "O" ,(\* Si servidor ocupado \*)

If[ (Part[p1Tabla, i, 3 ]) == 0 , (\* Si Nro CC es cero \*)

If[ i != Length[p1Tabla], (\*

Evita error si queda 1 cliente pero nunca se atiende \*)

t1CSistAcum =

t1CSistAcum + (Part[p1Tabla, i + 1, 1]) - (Part[p1Tabla, i,

1]) ; (\* Calcula tSist de c/ Cliente mientras estuvo solo \*)

p1CSist = t1CSistAcum / (Part[p1Tabla, i, 1]); (\*

Probabilidad 1 Cliente en Sist como Acumulada/Reloj,

función en el tiempo\*)

p1CSistTabla =

Append[p1CSistTabla, {(Part[p1Tabla, i, 1]), p1CSist} ];];];];

i++;];

p1CSistTotal = t1CSistAcum / tmax;

Grid[gX];

gX = ListLinePlot[p1CSistTabla, AxesLabel -> {tiempo, p1 (t)}];

prob1CSistAna = (1/tmEntreArribos)\*

tmDeServicio \* (

1 - (1/tmEntreArribos) \*

tmDeServicio);(\* [\[Lambda]/\[Mu] \* (1 - \[Lambda]/\[Mu])] \

Valor Analítico \*)

solanaX =

Plot[prob1CSistAna, {x, 0, tiempoUltimoEvento}, PlotStyle -> Green];

Print["Probabilidad de que haya un cliente en Sistema ", p1CSistTotal];

Print["Valor analítico - fórmula: ", prob1CSistAna];

Show[gX, solanaX]