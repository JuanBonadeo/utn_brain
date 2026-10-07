#!/usr/bin/env python3
"""Genera CaserHorno.alp (AnyLogic 8.9.9, Process Modeling Library) para la Etapa 1 del TPI Caser.

Uso, desde la raíz del repo:
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/construir_modelo.py

Sirve SOLO para crear la primera versión del .alp. Una vez que el modelo se abre y se guarda en el IDE
(statechart visual, ajustes de presentación), el .alp pasa a ser la fuente de verdad: volver a correr este
script lo pisa. Por eso se niega a sobrescribir salvo con --forzar.

Lee las entradas agregadas de datos-locales/_perfil/entradas_etapa1.json (gitignorado; lo genera
entradas_etapa1.py). En el .alp quedan solo agregados: 52 semanas de conteos diarios y 101 cuantiles de kg.
Formato XML tomado de TP_Colas.alp (escrito por el IDE 8.9.9) y del modelo de subte que compiló en 8.9.9.
"""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "CaserHorno.alp"
ENTRADAS = AQUI.parent / "datos-locales" / "_perfil" / "entradas_etapa1.json"
PKG = "caserhorno"
PML = "com.anylogic.libraries.processmodeling"
GEN = {"Source": "1412336242928", "Sink": "1412336242929", "Delay": "1412336242930", "Wait": "1412336243169"}

_id = [1800000000000]


def nid():
    _id[0] += 1
    return str(_id[0])


def x(s):
    return escape(str(s))


# ---------------------------------------------------------------------------------------------------------
# Parámetros de Main: (nombre, tipo, valor por defecto, descripción)
# ---------------------------------------------------------------------------------------------------------
ent = json.loads(ENTRADAS.read_text(encoding="utf-8"))
semanas = ent["llegadasSemanas"]
assert len(semanas) % 5 == 0 and len(semanas) >= 5 * 50, "se esperan ~52 semanas de 5 días hábiles"
kgq = ent["kgCuantiles"]
assert len(kgq) == 101

PARAMS = [
    ("escenario", "String", '"E0"', "Etiqueta del escenario en la fila de resultados (E0..E3, MM1, ...)."),
    ("umbralULI", "int", "75", "ULI en cola que disparan el encendido. Base 75 (relevado 70-80; cola al encender medida: mediana 77)."),
    ("esperaMaxDias", "double", "Double.POSITIVE_INFINITY", "Espera máxima de la ULI más vieja antes de forzar el encendido (E2). Infinito = sin límite."),
    ("horasEnVacio", "double", "48", "Horas que el horno sigue caliente con la cola vacía antes de enfriar. Base 48 h: el registro muestra huecos de 1-2 días dentro de campañas que solo se explican con el horno caliente."),
    ("hCalentamiento", "double", "36", "Horas de calentamiento (relevado)."),
    ("hEnfriamiento", "double", "48", "Horas de enfriamiento (relevado)."),
    ("minPorULI", "double", "1440.0 / 17", "Minutos de ciclo por ULI. Base 85 min (17 ULI/día, encargado). Medido en fines de semana: ~99 min (sensibilidad)."),
    ("modoFinCampana", "String", '"workConserving"', "workConserving: procesa mientras haya cola (lo que respaldan los datos). cupo: solo las ULI en cola al terminar de calentar (regla del 27/09)."),
    ("pPrioridad", "double", str(ent["pPrioridad"]), "Probabilidad de que una ULI sea urgente (entrega comprometida). Estimada como encendidos chicos / ULI llegadas con el horno apagado (17/1794, 2024-2026)."),
    ("soloUrgentesEnPrioridad", "boolean", "true", "Un encendido por prioridad trata solo las ULI urgentes y apaga sin tiempo en vacío (campañas chicas del registro)."),
    ("factorDemanda", "double", "1.0", "Multiplica las llegadas (0,8 / 1,0 / 1,2 en la sensibilidad)."),
    ("semilla", "long", "1", "Semilla de la réplica: la réplica j usa la semilla j en todos los escenarios (números aleatorios comunes)."),
    ("calentamientoModeloDias", "double", "90", "Período de calentamiento del modelo, descartado de las estadísticas (a fijar con Welch)."),
    ("horizonteDias", "double", "365", "Días medidos después del calentamiento."),
    ("kWhPorDiaCaliente", "double", "2445", "kWh por día con el horno a temperatura (regresión sobre 28 meses de facturas: 2.445 ± 179, ≈102 kW)."),
    ("kWhPorEncendido", "double", "1384", "kWh fijos por encendido (regresión: 1.384 ± 1.288; sensibilidad 0-5.220)."),
    ("tarifaKWh", "double", "290", "$/kWh todo incluido (factura del horno, mar/2025). El kWh se informa también aparte."),
    ("modoLlegadas", "String", '"semanas"', "semanas: bootstrap de semanas reales (lun-vie) de ULI lavadas, últimos 12 meses. poisson: solo para la verificación M/M/1."),
    ("tasaPoissonPorHora", "double", "0", "Tasa de llegadas en modo poisson (ULI/h)."),
    ("cicloExponencial", "boolean", "false", "Ciclo exponencial de media minPorULI (solo verificación M/M/1). Falso = ciclo constante."),
    ("llegadasSemanas", "int[]", "new int[] {" + ",".join(map(str, semanas)) + "}",
     f"ULI lavadas por día hábil (lun-vie), {len(semanas)//5} semanas reales consecutivas {ent['ventana'][0]} a {ent['ventana'][1]}."),
    ("kgCuantiles", "double[]", "new double[] {" + ",".join(f"{v:g}" for v in kgq) + "}",
     "Cuantiles 0..100 % de kg por ULI (mismas ULI). Se muestrea por inversa de la función de distribución empírica."),
    ("archivoSalida", "String", '""', "Si no está vacío, agrega una fila por corrida a ese CSV (en la carpeta del .alp)."),
]

# Variables de estado y acumuladores: (nombre, tipo, valor inicial)
VARS = [
    ("estado", "int", "0"),  # 0 Apagado, 1 Acumulando, 2 Calentando, 3 Procesando, 4 Enfriando
    ("ocupado", "boolean", "false"),
    ("enVacio", "boolean", "false"),
    ("campanaPrioridad", "boolean", "false"),
    ("campanaMedida", "boolean", "false"),
    ("nEnCola", "int", "0"),
    ("kgEnCola", "double", "0"),
    ("semanaActual", "int", "0"),
    ("llegadasPendientes", "java.util.ArrayList<Double>", "new java.util.ArrayList<Double>()"),
    ("rngLlegadas", "java.util.Random", "null"),
    ("rngKg", "java.util.Random", "null"),
    ("rngUrgente", "java.util.Random", "null"),
    ("rngDemanda", "java.util.Random", "null"),
    ("rngCiclo", "java.util.Random", "null"),
    ("midiendo", "boolean", "false"),
    ("tInicioMedicion", "double", "0"),
    ("tUltimo", "double", "0"),
    ("tEncendido", "double", "0"),
    ("tPrimerCiclo", "double", "-1"),
    ("tUltimoCiclo", "double", "-1"),
    ("ulisCampana", "int", "0"),
    ("kgCampana", "double", "0"),
    ("nLlegadas", "int", "0"),
    ("nTratadas", "int", "0"),
    ("kgTratados", "double", "0"),
    ("nEncendidos", "int", "0"),
    ("nEncendidosPrioridad", "int", "0"),
    ("sumaColaAlEncender", "double", "0"),
    ("sumaColaAlApagar", "double", "0"),
    ("areaCola", "double", "0"),
    ("areaColaKg", "double", "0"),
    ("areaSistema", "double", "0"),
    ("horasOcupado", "double", "0"),
    ("horasCaliente", "double", "0"),
    ("sumaSistema", "double", "0"),
    ("esperas", "java.util.ArrayList<Double>", "new java.util.ArrayList<Double>()"),
    ("ulisPorCampana", "java.util.ArrayList<Double>", "new java.util.ArrayList<Double>()"),
    ("kgPorCampana", "java.util.ArrayList<Double>", "new java.util.ArrayList<Double>()"),
    ("diasPorCampana", "java.util.ArrayList<Double>", "new java.util.ArrayList<Double>()"),
    ("prioridadPorCampana", "java.util.ArrayList<Boolean>", "new java.util.ArrayList<Boolean>()"),
    ("finalizado", "boolean", "false"),
]

# ---------------------------------------------------------------------------------------------------------
# Funciones de Main: (nombre, tipo de retorno, [(tipo, arg)], cuerpo Java). Tiempo del modelo en HORAS;
# t = 0 es un lunes 00:00. Estados: 0 Apagado, 1 Acumulando, 2 Calentando, 3 Procesando, 4 Enfriando.
# ---------------------------------------------------------------------------------------------------------
FUNCS = [
    ("inicializar", "void", [], r'''
if (umbralULI < 1) throw new IllegalArgumentException("umbralULI debe ser >= 1: " + umbralULI);
if (minPorULI <= 0 || hCalentamiento < 0 || hEnfriamiento < 0 || horasEnVacio < 0)
    throw new IllegalArgumentException("tiempos del horno invalidos");
if (!(esperaMaxDias > 0)) throw new IllegalArgumentException("esperaMaxDias debe ser > 0 (infinito = sin limite)");
if (!modoFinCampana.equals("workConserving") && !modoFinCampana.equals("cupo"))
    throw new IllegalArgumentException("modoFinCampana debe ser workConserving o cupo: " + modoFinCampana);
if (pPrioridad < 0 || pPrioridad > 1) throw new IllegalArgumentException("pPrioridad fuera de [0,1]");
if (factorDemanda < 0) throw new IllegalArgumentException("factorDemanda negativo");
if (modoLlegadas.equals("semanas")) {
    if (llegadasSemanas == null || llegadasSemanas.length < 5 || llegadasSemanas.length % 5 != 0)
        throw new IllegalArgumentException("llegadasSemanas debe tener 5 valores (lun-vie) por semana");
} else if (modoLlegadas.equals("poisson")) {
    if (tasaPoissonPorHora <= 0) throw new IllegalArgumentException("tasaPoissonPorHora debe ser > 0");
} else throw new IllegalArgumentException("modoLlegadas debe ser semanas o poisson: " + modoLlegadas);
if (kgCuantiles == null || kgCuantiles.length < 2) throw new IllegalArgumentException("kgCuantiles vacio");
// Un generador por fuente de aleatoriedad: con la misma semilla, las llegadas, los kg y las urgencias
// son identicos en todos los escenarios (numeros aleatorios comunes).
rngLlegadas = new java.util.Random(semilla * 10 + 1);
rngKg = new java.util.Random(semilla * 10 + 2);
rngUrgente = new java.util.Random(semilla * 10 + 3);
rngDemanda = new java.util.Random(semilla * 10 + 4);
rngCiclo = new java.util.Random(semilla * 10 + 5);
tUltimo = time();
midiendo = calentamientoModeloDias <= 0;
tInicioMedicion = midiendo ? time() : calentamientoModeloDias * 24;
if (!midiendo) eInicioMedicion.restart(calentamientoModeloDias * 24);
eFin.restart((Math.max(0, calentamientoModeloDias) + horizonteDias) * 24);
if (modoLlegadas.equals("semanas")) eDia.restart(0);
else eLlegada.restart(exponencial(tasaPoissonPorHora, rngLlegadas));
traceln("HORNO " + escenario + " semilla=" + semilla + " umbral=" + umbralULI + " esperaMax=" + esperaMaxDias
    + " vacio=" + horasEnVacio + "h modo=" + modoFinCampana + " pPrioridad=" + pPrioridad + " demanda=" + factorDemanda);'''),
    ("exponencial", "double", [("double", "tasa"), ("java.util.Random", "r")],
     "return -Math.log(1 - r.nextDouble()) / tasa;"),
    ("tiempoCiclo", "double", [], "return cicloExponencial ? exponencial(60.0 / minPorULI, rngCiclo) : minPorULI / 60.0;"),
    ("muestraKg", "double", [], r'''
double u = rngKg.nextDouble() * (kgCuantiles.length - 1);
int i = (int) Math.floor(u);
if (i >= kgCuantiles.length - 1) return kgCuantiles[kgCuantiles.length - 1];
return kgCuantiles[i] + (u - i) * (kgCuantiles[i + 1] - kgCuantiles[i]);'''),
    ("nuevoDia", "void", [], r'''
// Lavado de lunes a viernes. Cada lunes se sortea una semana real completa de las observadas
// (bootstrap por bloques: conserva los dias sin lavado y la autocorrelacion dentro de la semana).
int dia = (int) Math.floor(time() / 24 + 1e-9);
int dow = dia % 7;
if (dow == 0) semanaActual = rngLlegadas.nextInt(llegadasSemanas.length / 5);
if (dow >= 5) return;
int base = llegadasSemanas[semanaActual * 5 + dow];
int n = 0;
for (int i = 0; i < base; i++) {
    n += (int) Math.floor(factorDemanda);
    if (rngDemanda.nextDouble() < factorDemanda - Math.floor(factorDemanda)) n++;
}
java.util.ArrayList<Double> horas = new java.util.ArrayList<Double>();
for (int i = 0; i < n; i++) horas.add(dia * 24 + 6 + rngLlegadas.nextDouble() * 16);  // entre las 6 y las 22
java.util.Collections.sort(horas);
llegadasPendientes.addAll(horas);
if (!llegadasPendientes.isEmpty() && !eLlegada.isActive()) eLlegada.restart(Math.max(0, llegadasPendientes.get(0) - time()));'''),
    ("llegada", "void", [], r'''
if (modoLlegadas.equals("poisson")) {
    source.inject(1);
    eLlegada.restart(exponencial(tasaPoissonPorHora, rngLlegadas));
    return;
}
while (!llegadasPendientes.isEmpty() && llegadasPendientes.get(0) <= time() + 1e-9) {
    llegadasPendientes.remove(0);
    source.inject(1);
}
if (!llegadasPendientes.isEmpty()) eLlegada.restart(Math.max(0, llegadasPendientes.get(0) - time()));'''),
    ("entraCola", "void", [("ULI", "u")], r'''
acumular();
u.tLlegada = time();
u.kg = muestraKg();
u.urgente = rngUrgente.nextDouble() < pPrioridad;
u.enCupo = false;
u.despachado = false;
nEnCola++;
kgEnCola += u.kg;
if (midiendo) nLlegadas++;
evaluarEncendido();
pedirDespacho();'''),
    ("evaluarEncendido", "void", [], r'''
if (estado == 0 && nEnCola > 0) {
    acumular();
    estado = 1;
    if (!Double.isInfinite(esperaMaxDias))
        eEsperaMax.restart(Math.max(0, esperaMaxDias * 24 - (time() - llegadaMasVieja())));
}
if (estado == 1) {
    if (nEnCola >= umbralULI) encender(false);
    else if (hayUrgenteEnCola()) encender(true);
}'''),
    ("llegadaMasVieja", "double", [], r'''
double t = time();
for (Agent a : colaHorno) { ULI u = (ULI) a; if (!u.despachado && u.tLlegada < t) t = u.tLlegada; }
return t;'''),
    ("hayUrgenteEnCola", "boolean", [], r'''
for (Agent a : colaHorno) { ULI u = (ULI) a; if (!u.despachado && u.urgente) return true; }
return false;'''),
    ("encender", "void", [("boolean", "porPrioridad")], r'''
acumular();
eEsperaMax.reset();
estado = 2;
campanaPrioridad = porPrioridad;
tEncendido = time();
campanaMedida = midiendo;
if (campanaMedida) {
    nEncendidos++;
    if (porPrioridad) nEncendidosPrioridad++;
    sumaColaAlEncender += nEnCola;
}
ulisCampana = 0;
kgCampana = 0;
tPrimerCiclo = -1;
tUltimoCiclo = -1;
eCalentamiento.restart(hCalentamiento);'''),
    ("finCalentamiento", "void", [], r'''
acumular();
estado = 3;
enVacio = false;
// Modo cupo (regla del 27/09): la campana trata solo lo que estaba en cola al llegar a temperatura,
// mas las urgentes que lleguen despues. En workConserving no se marca nada.
if (modoFinCampana.equals("cupo") && !campanaPrioridad)
    for (Agent a : colaHorno) { ULI u = (ULI) a; if (!u.despachado) u.enCupo = true; }
pedirDespacho();'''),
    ("pedirDespacho", "void", [], "if (!eDespacho.isActive()) eDespacho.restart(0);"),
    ("despachar", "void", [], r'''
if (estado != 3 || ocupado) return;
ULI sig = elegirSiguiente();
if (sig == null) {
    if (!enVacio) {
        enVacio = true;
        eVacio.restart(campanaPrioridad && soloUrgentesEnPrioridad ? 0 : horasEnVacio);
    }
    return;
}
if (enVacio) { enVacio = false; eVacio.reset(); }
acumular();
sig.despachado = true;
sig.tInicio = time();
nEnCola--;
kgEnCola -= sig.kg;
ocupado = true;
if (tPrimerCiclo < 0) tPrimerCiclo = time();
if (midiendo) esperas.add(time() - sig.tLlegada);
if (!colaHorno.free(sig)) throw new IllegalStateException("colaHorno.free fallo para una ULI en cola");'''),
    ("elegirSiguiente", "ULI", [], r'''
// Urgentes primero; entre iguales, la mas vieja (FIFO).
ULI mejor = null;
for (Agent a : colaHorno) {
    ULI u = (ULI) a;
    if (u.despachado) continue;
    boolean candidata;
    if (campanaPrioridad && soloUrgentesEnPrioridad) candidata = u.urgente;
    else if (modoFinCampana.equals("cupo")) candidata = u.urgente || u.enCupo;
    else candidata = true;
    if (!candidata) continue;
    if (mejor == null || (u.urgente && !mejor.urgente) || (u.urgente == mejor.urgente && u.tLlegada < mejor.tLlegada)) mejor = u;
}
return mejor;'''),
    ("finCiclo", "void", [("ULI", "u")], r'''
acumular();
ocupado = false;
ulisCampana++;
kgCampana += u.kg;
tUltimoCiclo = u.tInicio;
if (midiendo) {
    nTratadas++;
    kgTratados += u.kg;
    sumaSistema += time() - u.tLlegada;
}
pedirDespacho();'''),
    ("finVacio", "void", [], r'''
if (estado != 3 || ocupado) return;
acumular();
enVacio = false;
cerrarCampana();
estado = 4;
eEnfriamiento.restart(hEnfriamiento);'''),
    ("cerrarCampana", "void", [], r'''
if (!campanaMedida) return;
ulisPorCampana.add((double) ulisCampana);
kgPorCampana.add(kgCampana);
prioridadPorCampana.add(campanaPrioridad);
// Igual que en el registro: dias calendario entre el primer y el ultimo cementado.
diasPorCampana.add(tPrimerCiclo < 0 ? 0.0 : Math.floor(tUltimoCiclo / 24) - Math.floor(tPrimerCiclo / 24) + 1);
sumaColaAlApagar += nEnCola;'''),
    ("finEnfriamiento", "void", [], r'''
acumular();
estado = 0;
evaluarEncendido();'''),
    ("esperaMaxCumplida", "void", [], "if (estado == 1 && nEnCola > 0) encender(false);"),
    ("acumular", "void", [], r'''
double t = time();
if (midiendo) {
    double dt = t - tUltimo;
    areaCola += nEnCola * dt;
    areaColaKg += kgEnCola * dt;
    areaSistema += (nEnCola + (ocupado ? 1 : 0)) * dt;
    if (ocupado) horasOcupado += dt;
    if (estado == 3) horasCaliente += dt;
}
tUltimo = t;'''),
    ("inicioMedicion", "void", [], r'''
acumular();
midiendo = true;
tInicioMedicion = time();
nLlegadas = 0; nTratadas = 0; kgTratados = 0; nEncendidos = 0; nEncendidosPrioridad = 0;
sumaColaAlEncender = 0; sumaColaAlApagar = 0; areaCola = 0; areaColaKg = 0; areaSistema = 0;
horasOcupado = 0; horasCaliente = 0; sumaSistema = 0;
esperas.clear(); ulisPorCampana.clear(); kgPorCampana.clear(); diasPorCampana.clear(); prioridadPorCampana.clear();'''),
    ("finCorrida", "void", [], r'''
acumular();
emitirResultado();
finalizado = true;
finishSimulation();'''),
    ("horasMedidas", "double", [], "return time() - tInicioMedicion;"),
    ("media", "double", [("java.util.ArrayList<Double>", "v")], r'''
if (v.isEmpty()) return Double.NaN;
double s = 0;
for (double d : v) s += d;
return s / v.size();'''),
    ("cuantil", "double", [("java.util.ArrayList<Double>", "v"), ("double", "p")], r'''
// Rango mas proximo: ceil(p n), igual que en el analisis de los datos reales.
if (v.isEmpty()) return Double.NaN;
java.util.ArrayList<Double> c = new java.util.ArrayList<Double>(v);
java.util.Collections.sort(c);
int k = (int) Math.ceil(p * c.size());
return c.get(Math.max(0, Math.min(c.size() - 1, k - 1)));'''),
    ("kWhTotal", "double", [], "return kWhPorEncendido * nEncendidos + kWhPorDiaCaliente / 24 * horasCaliente;"),
    ("campanasPorMes", "double", [], "return nEncendidos / (horasMedidas() / (24 * 30.4375));"),
    ("nombreEstado", "String", [], r'''
switch (estado) {
    case 0: return "Apagado";
    case 1: return "Acumulando";
    case 2: return "Calentando";
    case 3: return enVacio ? "Caliente en vacio" : "Cargando";
    case 4: return "Enfriando";
    default: return "?";
}'''),
    ("encabezado", "String", [], r'''
return "escenario;semilla;umbralULI;esperaMaxDias;horasEnVacio;modoFinCampana;pPrioridad;factorDemanda;minPorULI;"
    + "horasMedidas;nLlegadas;nTratadas;kgTratados;nEncendidos;nEncendidosPrioridad;campanasPorMes;"
    + "uliPorCampanaMedia;uliPorCampanaMediana;diasPorCampanaMedia;colaAlEncenderMedia;colaAlApagarMedia;"
    + "esperaMediaDias;esperaP90Dias;esperaMaximaDias;colaMediaULI;colaMediaKg;sistemaMedioULI;sistemaMedioHoras;"
    + "utilizacion;fraccionCaliente;kWhTotal;kWhPorKg;costoEnergiaPorKg";'''),
    ("filaResultado", "String", [], r'''
double h = horasMedidas();
java.util.ArrayList<Double> esperasDias = new java.util.ArrayList<Double>();
for (double e : esperas) esperasDias.add(e / 24);
int nc = ulisPorCampana.size();
double[] v = {
    umbralULI, esperaMaxDias, horasEnVacio, pPrioridad, factorDemanda, minPorULI,
    h, nLlegadas, nTratadas, kgTratados, nEncendidos, nEncendidosPrioridad, campanasPorMes(),
    media(ulisPorCampana), cuantil(ulisPorCampana, 0.5), media(diasPorCampana),
    nEncendidos > 0 ? sumaColaAlEncender / nEncendidos : Double.NaN, nc > 0 ? sumaColaAlApagar / nc : Double.NaN,
    media(esperasDias), cuantil(esperasDias, 0.9), esperasDias.isEmpty() ? Double.NaN : java.util.Collections.max(esperasDias),
    areaCola / h, areaColaKg / h, areaSistema / h, nTratadas > 0 ? sumaSistema / nTratadas : Double.NaN,
    horasOcupado / h, horasCaliente / h, kWhTotal(), kWhTotal() / kgTratados, kWhTotal() / kgTratados * tarifaKWh };
StringBuilder sb = new StringBuilder(escenario + ";" + semilla);
for (int i = 0; i < v.length; i++) {
    if (i == 3) sb.append(";").append(modoFinCampana);
    sb.append(";").append(String.format(java.util.Locale.US, "%.6g", v[i]));
}
return sb.toString();'''),
    ("emitirResultado", "void", [], r'''
String fila = filaResultado();
traceln("CSV_HORNO;" + fila);
traceln(String.format(java.util.Locale.US,
    "RESUMEN %s semilla=%d: encendidos=%d (prioridad %d), %.2f campanas/mes, ULI/campana media %.1f, espera media %.2f d, p90 %.2f d, kWh/kg %.3f",
    escenario, semilla, nEncendidos, nEncendidosPrioridad, campanasPorMes(), media(ulisPorCampana),
    media(esperas) / 24, cuantil(esperas, 0.9) / 24, kWhTotal() / kgTratados));
if (archivoSalida == null || archivoSalida.isEmpty()) return;
synchronized (java.io.File.class) {
    try {
        java.io.File f = new java.io.File(archivoSalida);
        boolean nuevo = !f.exists() || f.length() == 0;
        java.io.FileWriter w = new java.io.FileWriter(f, true);
        if (nuevo) w.write(encabezado() + "\n");
        w.write(fila + "\n");
        w.close();
    } catch (java.io.IOException ex) {
        throw new RuntimeException("No se pudo escribir " + archivoSalida, ex);
    }
}'''),
]

# Eventos: (nombre, acción). Todos "de control manual": se programan con restart() desde las funciones.
EVENTS = [
    ("eDia", "nuevoDia(); eDia.restart(24);"),
    ("eLlegada", "llegada();"),
    ("eDespacho", "despachar();"),
    ("eCalentamiento", "finCalentamiento();"),
    ("eVacio", "finVacio();"),
    ("eEnfriamiento", "finEnfriamiento();"),
    ("eEsperaMax", "esperaMaxCumplida();"),
    ("eInicioMedicion", "inicioMedicion();"),
    ("eFin", "finCorrida();"),
]

ULI_VARS = [("tLlegada", "double", "0"), ("kg", "double", "0"), ("tInicio", "double", "0"),
            ("urgente", "boolean", "false"), ("enCupo", "boolean", "false"), ("despachado", "boolean", "false")]

# ---------------------------------------------------------------------------------------------------------
# XML
# ---------------------------------------------------------------------------------------------------------
LABEL = "<Label><X>10</X><Y>0</Y></Label>"
FLAGS_OFF = "<PublicFlag>false</PublicFlag><PresentationFlag>false</PresentationFlag><ShowLabel>true</ShowLabel>"
FLAGS_ON = "<PublicFlag>false</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>true</ShowLabel>"
param_ids = {}


def xml_param(name, typ, default, desc, X, Y):
    pid = nid()
    param_ids[name] = pid
    return f"""<Variable Class="Parameter"><Id>{pid}</Id><Name>{x(name)}</Name><X>{X}</X><Y>{Y}</Y>{LABEL}{FLAGS_OFF}
<Properties SaveInSnapshot="true" ModificatorType="STATIC"><Type>{x(typ)}</Type><UnitType>NONE</UnitType><SdArray>false</SdArray>
<DefaultValue Class="CodeValue"><Code>{x(default)}</Code></DefaultValue>
<ParameterEditor><Id>{nid()}</Id><EditorContolType>TEXT_BOX</EditorContolType><MinSliderValue>0</MinSliderValue><MaxSliderValue>100</MaxSliderValue><DelimeterType>NO_DELIMETER</DelimeterType></ParameterEditor>
</Properties><Description>{x(desc)}</Description></Variable>"""


def xml_var(name, typ, init, X, Y, presentation=False):
    flags = FLAGS_ON if presentation else FLAGS_OFF
    return f"""<Variable Class="PlainVariable"><Id>{nid()}</Id><Name>{x(name)}</Name><X>{X}</X><Y>{Y}</Y>{LABEL}{flags}
<Properties SaveInSnapshot="true" Constant="false" AccessType="public" StaticVariable="false"><Type>{x(typ)}</Type><UnitType>NONE</UnitType><SdArray>false</SdArray>
<InitialValue Class="CodeValue"><Code>{x(init)}</Code></InitialValue></Properties></Variable>"""


def xml_func(name, ret, args, body, X, Y):
    mod = "VOID" if ret == "void" else "RETURNS_VALUE"
    a = "".join(f"<Parameter><Name>{x(n)}</Name><Type>{x(t)}</Type></Parameter>" for t, n in args)
    return f"""<Function AccessType="public" StaticFunction="false"><ReturnModificator>{mod}</ReturnModificator><ReturnType>{x(ret)}</ReturnType>
<Id>{nid()}</Id><Name>{x(name)}</Name><X>{X}</X><Y>{Y}</Y><PublicFlag>true</PublicFlag><PresentationFlag>false</PresentationFlag><ShowLabel>true</ShowLabel>{LABEL}
{a}<Body>{x(body.strip())}</Body></Function>"""


def xml_event(name, action, X, Y):
    t = '<Code>1e12</Code><Unit Class="TimeUnits">HOUR</Unit>'
    return f"""<Event><Id>{nid()}</Id><Name>{x(name)}</Name><X>{X}</X><Y>{Y}</Y>{LABEL}{FLAGS_OFF}
<Properties TriggerType="timeout" Mode="occuresOnce"><Timeout Class="CodeUnitValue">{t}</Timeout>
<Rate Class="CodeUnitValue"><Code>1</Code><Unit Class="RateUnits">PER_HOUR</Unit></Rate>
<Id>{nid()}</Id><OccurrenceAtTime>true</OccurrenceAtTime><OccurrenceDate>1783584000000</OccurrenceDate>
<OccurrenceTime Class="CodeUnitValue">{t}</OccurrenceTime><RecurrenceCode Class="CodeUnitValue">{t}</RecurrenceCode>
<Condition>false</Condition></Properties><Action>{x(action)}</Action></Event>"""


def block_param(name, code, unit=None):
    if unit:
        return f'<Parameter><Name>{name}</Name><Value Class="CodeUnitValue"><Code>{x(code)}</Code><Unit Class="TimeUnits">{unit}</Unit></Value></Parameter>'
    return f'<Parameter><Name>{name}</Name><Value Class="CodeValue"><Code>{x(code)}</Code></Value></Parameter>'


TAIL = """<ReplicationFlag>false</ReplicationFlag><Replication Class="CodeValue"><Code>100</Code></Replication>
<CollectionType>ARRAY_LIST_BASED</CollectionType><InitialLocationType>XYZ</InitialLocationType>
<ColumnCode Class="CodeValue"><Code>0</Code></ColumnCode><RowCode Class="CodeValue"><Code>0</Code></RowCode>
<LocationNameCode Class="CodeValue"><Code>""</Code></LocationNameCode><InitializationType>SPECIFIED_NUMBER</InitializationType>
<InitializationDatabaseTableQuery><Id>{qid}</Id><TableReference></TableReference></InitializationDatabaseTableQuery>
<InitializationDatabaseType>ONE_AGENT_PER_DATABASE_RECORD</InitializationDatabaseType><QuantityColumn></QuantityColumn>"""


def xml_block(name, cls, X, Y, params):
    return f"""<EmbeddedObject><Id>{nid()}</Id><Name>{name}</Name><X>{X}</X><Y>{Y}</Y><Label><X>-5</X><Y>-20</Y></Label>{FLAGS_ON}
<ActiveObjectClass><PackageName>{PML}</PackageName><ClassName>{cls}</ClassName></ActiveObjectClass>
<GenericParameterSubstitute><GenericParameterSubstituteReference><PackageName>{PML}</PackageName><ClassName>{cls}</ClassName><ItemName>{GEN[cls]}</ItemName></GenericParameterSubstituteReference></GenericParameterSubstitute>
<Parameters>{''.join(params)}</Parameters>{TAIL.format(qid=nid())}</EmbeddedObject>"""


def xml_connector(name, src, srccls, srcport, dst, dstcls, X, Y, dx):
    return f"""<Connector><Id>{nid()}</Id><Name>{name}</Name><X>{X}</X><Y>{Y}</Y>{LABEL}<PublicFlag>false</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel>
<SourceEmbeddedObjectReference><PackageName>{PKG}</PackageName><ClassName>Main</ClassName><ItemName>{src}</ItemName></SourceEmbeddedObjectReference>
<SourceConnectableItemReference><PackageName>{PML}</PackageName><ClassName>{srccls}</ClassName><ItemName>{srcport}</ItemName></SourceConnectableItemReference>
<TargetEmbeddedObjectReference><PackageName>{PKG}</PackageName><ClassName>Main</ClassName><ItemName>{dst}</ItemName></TargetEmbeddedObjectReference>
<TargetConnectableItemReference><PackageName>{PML}</PackageName><ClassName>{dstcls}</ClassName><ItemName>in</ItemName></TargetConnectableItemReference>
<Points><Point><X>0</X><Y>0</Y></Point><Point><X>{dx}</X><Y>0</Y></Point></Points></Connector>"""


def xml_text(name, X, Y, text, code=None, size=14, bold=False):
    tc = f"<TextCode>{x(code)}</TextCode>" if code else ""
    return f"""<Text><Id>{nid()}</Id><Name>{name}</Name><X>{X}</X><Y>{Y}</Y>{LABEL}<PublicFlag>true</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel>
<DrawMode>SHAPE_DRAW_2D3D</DrawMode><EmbeddedIcon>false</EmbeddedIcon><Z>0</Z><Rotation>0.0</Rotation><Color>-12490271</Color>
<Text>{x(text)}</Text>{tc}<Font><Name>SansSerif</Name><Size>{size}</Size><Style>{1 if bold else 0}</Style></Font><Alignment>LEFT</Alignment></Text>"""


AGENT_HEAD = """<Generic>false</Generic>
<GenericParameter><Id>{gid}</Id><Name>{gid}</Name><GenericParameterValue Class="CodeValue"><Code>T extends Agent</Code></GenericParameterValue><GenericParameterLabel>Generic parameter:</GenericParameterLabel></GenericParameter>
<FlowChartsUsage>ENTITY</FlowChartsUsage><SamplesToKeep>100</SamplesToKeep><LimitNumberOfArrayElements>false</LimitNumberOfArrayElements><ElementsLimitValue>100</ElementsLimitValue><MakeDefaultViewArea>true</MakeDefaultViewArea><SceneGridColor /><SceneBackgroundColor>-4144960</SceneBackgroundColor><EnvironmentResourceRef /><EnvironmentType>NONE</EnvironmentType><EnvironmentRotationX>0</EnvironmentRotationX><EnvironmentRotationY>0</EnvironmentRotationY><EnvironmentRotationZ>0</EnvironmentRotationZ><EnvironmentIntensity>1</EnvironmentIntensity>
<AgentProperties><EnvironmentDefinesInitialLocation>true</EnvironmentDefinesInitialLocation><RotateAnimationTowardsMovement>true</RotateAnimationTowardsMovement><RotateAnimationVertically>false</RotateAnimationVertically><VelocityCode Class="CodeUnitValue"><Code>10</Code><Unit Class="SpeedUnits">MPS</Unit></VelocityCode><PhysicalLength Class="CodeUnitValue"><Code>1</Code><Unit Class="LengthUnits">METER</Unit></PhysicalLength><PhysicalWidth Class="CodeUnitValue"><Code>1</Code><Unit Class="LengthUnits">METER</Unit></PhysicalWidth><PhysicalHeight Class="CodeUnitValue"><Code>1</Code><Unit Class="LengthUnits">METER</Unit></PhysicalHeight></AgentProperties>
<EnvironmentProperties><EnableSteps>false</EnableSteps><StepDurationCode Class="CodeUnitValue"><Code>1.0</Code><Unit Class="TimeUnits">HOUR</Unit></StepDurationCode><SpaceType>CONTINUOUS</SpaceType><WidthCode>500</WidthCode><HeightCode>500</HeightCode><ZHeightCode>0</ZHeightCode><ColumnsCountCode>100</ColumnsCountCode><RowsCountCode>100</RowsCountCode><NeigborhoodType>MOORE</NeigborhoodType><LayoutType>USER_DEF</LayoutType><NetworkType>USER_DEF</NetworkType><ConnectionsPerAgentCode>2</ConnectionsPerAgentCode><ConnectionsRangeCode>50</ConnectionsRangeCode><NeighborLinkFractionCode>0.95</NeighborLinkFractionCode><MCode>10</MCode></EnvironmentProperties>
<DatasetsCreationProperties><AutoCreate>false</AutoCreate><Id>{did}</Id><OccurrenceAtTime>true</OccurrenceAtTime><OccurrenceDate>1783584000000</OccurrenceDate><OccurrenceTime Class="CodeUnitValue"><Code>0</Code><Unit Class="TimeUnits">HOUR</Unit></OccurrenceTime><RecurrenceCode Class="CodeUnitValue"><Code>24</Code><Unit Class="TimeUnits">HOUR</Unit></RecurrenceCode></DatasetsCreationProperties>
<ScaleRuler><Id>{sid}</Id><Name>scale</Name><X>0</X><Y>-150</Y><PublicFlag>false</PublicFlag><PresentationFlag>false</PresentationFlag><ShowLabel>false</ShowLabel><DrawMode>SHAPE_DRAW_2D3D</DrawMode><Length>100</Length><Rotation>0</Rotation><ScaleType>BASED_ON_LENGTH</ScaleType><ModelLength>10</ModelLength><LengthUnits>METER</LengthUnits><Scale>10</Scale><InheritedFromParentAgentType>true</InheritedFromParentAgentType></ScaleRuler>
<CurrentLevel>{lid}</CurrentLevel><ConnectionsId>{cid}</ConnectionsId>"""

AGENT_LINKS = """<AgentLinks><AgentLink><Id>{cid}</Id><Name>connections</Name><X>50</X><Y>-50</Y><Label><X>15</X><Y>0</Y></Label><PublicFlag>false</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>true</ShowLabel><HandleReceiveInConnections>false</HandleReceiveInConnections><AgentLinkType>COLLECTION_OF_LINKS</AgentLinkType><AgentLinkBidirectional>true</AgentLinkBidirectional><MessageType>Object</MessageType><LineStyle>SOLID</LineStyle><LineWidth>1</LineWidth><LineColor>-16777216</LineColor><LineZOrder>UNDER_AGENTS</LineZOrder><LineArrow>NONE</LineArrow><LineArrowPosition>END</LineArrowPosition></AgentLink></AgentLinks>"""


def level(lid, inner):
    return f"""<Presentation><Level><Id>{lid}</Id><Name>level</Name><X>0</X><Y>0</Y>{LABEL}<PublicFlag>true</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel>
<DrawMode>SHAPE_DRAW_2D3D</DrawMode><Z>0</Z><LevelVisibility>DIM_NON_CURRENT</LevelVisibility><Presentation>{inner}</Presentation></Level></Presentation>"""


def construir():
    main_id, uli_id = nid(), nid()
    # --- ULI ---
    u_ids = {k: nid() for k in ("gid", "did", "sid", "lid", "cid")}
    uli_vars = "".join(xml_var(n, t, v, 40, 40 + 25 * i, presentation=True) for i, (n, t, v) in enumerate(ULI_VARS))
    rect = f"""<Rectangle><Id>{nid()}</Id><Name>cuerpoULI</Name><X>-5</X><Y>-5</Y><Label><X>0</X><Y>-10</Y></Label><PublicFlag>true</PublicFlag><PresentationFlag>true</PresentationFlag><ShowLabel>false</ShowLabel><DrawMode>SHAPE_DRAW_2D3D</DrawMode><EmbeddedIcon>false</EmbeddedIcon><Z>0</Z><ZHeight>10</ZHeight><LineWidth>1</LineWidth><LineColor>-10066330</LineColor><LineMaterial>null</LineMaterial><LineStyle>SOLID</LineStyle><Width>10</Width><Height>10</Height><Rotation>0.0</Rotation><FillColor>-23296</FillColor><FillMaterial>null</FillMaterial></Rectangle>"""
    uli = f"""<ActiveObjectClass><Id>{uli_id}</Id><Name>ULI</Name>{AGENT_HEAD.format(**u_ids)}
<Variables>{uli_vars}</Variables>{AGENT_LINKS.format(cid=u_ids['cid'])}{level(u_ids['lid'], rect)}</ActiveObjectClass>"""

    # --- Main ---
    m_ids = {k: nid() for k in ("gid", "did", "sid", "lid", "cid")}
    m_ids["gid"] = "1783514567442"
    variables = "".join(xml_param(n, t, d, desc, 1100, 40 + 22 * i) for i, (n, t, d, desc) in enumerate(PARAMS))
    variables += "".join(xml_var(n, t, v, 1400, 40 + 22 * i) for i, (n, t, v) in enumerate(VARS))
    uli_entity = (f'<Parameter><Name>newEntity</Name><Value Class="EntityCodeValue"><IsAgentEntity>true</IsAgentEntity>'
                  f'<EntityEmbeddedObject><Id>{nid()}</Id><ActiveObjectClass><PackageName>{PKG}</PackageName><ClassName>ULI</ClassName></ActiveObjectClass>'
                  f'<GenericParameterSubstitute><GenericParameterSubstituteReference><PackageName>{PKG}</PackageName><ClassName>ULI</ClassName><ItemName>{u_ids["gid"]}</ItemName></GenericParameterSubstituteReference></GenericParameterSubstitute>'
                  f'<Parameters></Parameters><ReplicationFlag>true</ReplicationFlag><Replication Class="CodeValue"><Code>100</Code></Replication><CollectionType>ARRAY_LIST_BASED</CollectionType><InitialLocationType>XYZ</InitialLocationType><ColumnCode Class="CodeValue"><Code>0</Code></ColumnCode><RowCode Class="CodeValue"><Code>0</Code></RowCode><LocationNameCode Class="CodeValue"><Code>""</Code></LocationNameCode><InitializationType>SPECIFIED_NUMBER</InitializationType><InitializationDatabaseTableQuery><Id>{nid()}</Id><TableReference></TableReference></InitializationDatabaseTableQuery><InitializationDatabaseType>ONE_AGENT_PER_DATABASE_RECORD</InitializationDatabaseType><QuantityColumn></QuantityColumn></EntityEmbeddedObject></Value></Parameter>')
    blocks = (
        xml_block("source", "Source", 80, 200, [block_param("arrivalType", "self.MANUAL"), uli_entity])
        + xml_block("colaHorno", "Wait", 230, 200, [block_param("maximumCapacity", "true"), block_param("onEnter", "entraCola((ULI) agent);"),
                                                      block_param("forceStatisticsCollection", "true")])
        + xml_block("horno", "Delay", 380, 200, [block_param("delayTime", "tiempoCiclo()", "HOUR"), block_param("capacity", "1"),
                                                 block_param("forceStatisticsCollection", "true")])
        + xml_block("sink", "Sink", 530, 200, [block_param("onEnter", "finCiclo((ULI) agent);")])
    )
    connectors = (xml_connector("c1", "source", "Source", "out", "colaHorno", "Wait", 90, 200, 130)
                  + xml_connector("c2", "colaHorno", "Wait", "out", "horno", "Delay", 240, 200, 130)
                  + xml_connector("c3", "horno", "Delay", "out", "sink", "Sink", 390, 200, 130))
    funcs = "".join(xml_func(n, r, a, b, 1700, 40 + 22 * i) for i, (n, r, a, b) in enumerate(FUNCS))
    events = "".join(xml_event(n, a, 1950, 40 + 30 * i) for i, (n, a) in enumerate(EVENTS))
    textos = (
        xml_text("titulo", 40, 30, "Caser - horno de cementacion y temple (Etapa 1: llegadas exogenas)", size=22, bold=True)
        + xml_text("txtEscenario", 40, 70, "Escenario", '"Escenario " + escenario + " | semilla " + semilla + " | umbral " + umbralULI + " ULI | vacio " + horasEnVacio + " h | " + modoFinCampana')
        + xml_text("txtEstado", 40, 100, "Estado", '"Horno: " + nombreEstado() + (campanaPrioridad && estado >= 2 && estado <= 3 ? " (prioridad)" : "") + "   |   dia " + (int) Math.floor(time() / 24)', size=18, bold=True)
        + xml_text("txtCola", 40, 130, "Cola", '"ULI en cola: " + nEnCola + "   (" + Math.round(kgEnCola) + " kg)"')
        + xml_text("txtStats", 40, 300, "Stats", '(midiendo ? "Midiendo" : "Calentamiento del modelo") + " | encendidos " + nEncendidos + " (prioridad " + nEncendidosPrioridad + ") | ULI tratadas " + nTratadas + " | kWh " + Math.round(kWhTotal())')
        + xml_text("aviso", 40, 330, "Entradas reales agregadas (12 meses). Modelo en verificacion: resultados no validados.", size=12)
    )
    main = f"""<ActiveObjectClass><Id>{main_id}</Id><Name>Main</Name>{AGENT_HEAD.format(**m_ids)}
<Variables>{variables}</Variables><Connectors>{connectors}</Connectors>{AGENT_LINKS.format(cid=m_ids['cid'])}
<EmbeddedObjects>{blocks}</EmbeddedObjects>{level(m_ids['lid'], textos)}
<StartupCode>inicializar();</StartupCode><Functions>{funcs}</Functions><Events>{events}</Events></ActiveObjectClass>"""

    # --- Experimentos ---
    def params_sim(valores):
        out = []
        for n, *_ in PARAMS:
            if n in valores:
                out.append(f'<Parameter><ParameterName>{n}</ParameterName><ParameterValue Class="CodeValue"><Code>{x(valores[n])}</Code></ParameterValue></Parameter>')
            else:
                out.append(f"<Parameter><ParameterName>{n}</ParameterName></Parameter>")
        return "<Parameters>" + "".join(out) + "</Parameters>"

    def model_time(final):
        return f"<ModelTimeProperties><StopOption>Stop at specified time</StopOption><InitialDate>1783584000000</InitialDate><InitialTime>0.0</InitialTime><FinalDate>1783584000000</FinalDate><FinalTime>{final}</FinalTime></ModelTimeProperties>"

    def sim_exp(name, titulo, valores, final, escala):
        return f"""<SimulationExperiment ActiveObjectClassId="{main_id}"><Id>{nid()}</Id><Name>{name}</Name><CommandLineArguments /><MaximumMemory>1024</MaximumMemory>
<RandomNumberGenerationType>fixedSeed</RandomNumberGenerationType><CustomGeneratorCode>new Random()</CustomGeneratorCode><SeedValue>1</SeedValue><SelectionModeForSimultaneousEvents>LIFO</SelectionModeForSimultaneousEvents><VmArgs /><LoadRootFromSnapshot>false</LoadRootFromSnapshot>
<Presentation>{xml_text('text', 50, 30, titulo, size=20)}</Presentation>{params_sim(valores)}
<PresentationProperties><EnableZoomAndPanning>true</EnableZoomAndPanning><ExecutionMode>realTimeScaled</ExecutionMode><Title>{x(titulo)}</Title><EnableDeveloperPanel>true</EnableDeveloperPanel><ShowDeveloperPanelOnStart>false</ShowDeveloperPanelOnStart><RealTimeScale>{escala}</RealTimeScale></PresentationProperties>
{model_time(final)}<BypassInitialScreen>true</BypassInitialScreen></SimulationExperiment>"""

    def pv_exp(name, titulo, runs, free, final):
        ff = "".join(f'<FreeformParamValue><Id>{param_ids[n]}</Id>' + (f'<Expression Class="CodeValue"><Code>{x(free[n])}</Code></Expression>' if n in free else "") + "</FreeformParamValue>" for n, *_ in PARAMS)
        rr = "".join(f'<RangeVariationParamValue><Id>{param_ids[n]}</Id><Type>FIXED</Type></RangeVariationParamValue>' for n, *_ in PARAMS)
        return f"""<ParamVariationExperiment ActiveObjectClassId="{main_id}"><Id>{nid()}</Id><Name>{name}</Name><CommandLineArguments /><MaximumMemory>2048</MaximumMemory>
<RandomNumberGenerationType>fixedSeed</RandomNumberGenerationType><CustomGeneratorCode>new Random()</CustomGeneratorCode><SeedValue>1</SeedValue><SelectionModeForSimultaneousEvents>LIFO</SelectionModeForSimultaneousEvents><VmArgs /><LoadRootFromSnapshot>false</LoadRootFromSnapshot>
<Presentation>{xml_text('text', 50, 30, titulo, size=20)}</Presentation>
<AllowParallelEvaluations>false</AllowParallelEvaluations><UseFreeformParameters>true</UseFreeformParameters><NumberOfRuns>{runs}</NumberOfRuns>{ff}{rr}
{model_time(final)}
<PresentationProperties><EnableZoomAndPanning>false</EnableZoomAndPanning><Title>{x(titulo)}</Title><EnableDeveloperPanel>true</EnableDeveloperPanel><ShowDeveloperPanelOnStart>false</ShowDeveloperPanelOnStart></PresentationProperties>
<ReplicationsProperties><UseReplication>false</UseReplication><FixedReplicationsNumber>true</FixedReplicationsNumber><ReplicationPerIteration>1</ReplicationPerIteration><MinimumReplication>1</MinimumReplication><MaximumReplication>1</MaximumReplication><ConfidenceLevel>LEVEL_95</ConfidenceLevel><ErrorPercent>0.5</ErrorPercent><ExpressionForConfidenceComputation>0</ExpressionForConfidenceComputation></ReplicationsProperties>
</ParamVariationExperiment>"""

    fin_base = (90 + 365) * 24 + 1
    mm1 = {"escenario": '"MM1"', "modoLlegadas": '"poisson"', "tasaPoissonPorHora": "0.7", "minPorULI": "60",
           "cicloExponencial": "true", "umbralULI": "1", "hCalentamiento": "0", "hEnfriamiento": "0",
           "horasEnVacio": "0", "pPrioridad": "0", "calentamientoModeloDias": "100", "horizonteDias": "2400"}
    e = "index / 30"
    corridas = {
        "escenario": f'"E" + ({e})',
        "semilla": "1 + index % 30",
        "umbralULI": f"{e} == 1 ? 45 : 75",
        "esperaMaxDias": f"{e} == 2 ? 15 : Double.POSITIVE_INFINITY",
        "horasEnVacio": f"{e} == 3 ? 96 : 48",
        "archivoSalida": '"corridas_horno.csv"',
    }
    experiments = (
        sim_exp("Visual", "Caser horno - E0, semilla 1 (animacion)", {"escenario": '"E0"'}, fin_base, 48.0)
        + sim_exp("VerificacionMM1", "Caser horno - caso degenerado M/M/1 (lambda 0,7/h, mu 1/h)", mm1, (100 + 2400) * 24 + 1, 1000000.0)
        + pv_exp("CorridasE0E3", "Caser horno - E0 a E3, 30 replicas con semillas comunes", 120, corridas, fin_base)
    )

    uuids = """9f7858c9-b2c8-4ead-9244-fd08833f642b 404652e6-561a-404c-aab2-ab7415f40ef5 6fd6cd57-6dfe-4fc6-be0b-c74065351957 3325dc48-3ad4-41e3-836f-dfd0e98fe1ed bb27038a-0f3a-48bb-b235-4a44066a14aa 3f69ef3d-706e-41a6-8af0-11658c5eef68 3f6fe405-e047-4304-91d6-6eee206d1106 820d2b51-5b4a-48e7-b0b6-e46418e3c0f2 630818fa-8975-4b70-976f-03180dce01db 7c7e471c-004e-495e-a4ad-d840620ab38e 3e38ff63-1f70-4ec0-b42c-e879b146785d b1eb86e4-14b3-405c-8257-56b80f1b485d d55f9fb6-86bb-45ea-9db1-79cecfa0ce91 ab77aafd-8f02-4354-b789-928d45b1f73c e4f14fd7-1c4a-42e9-b91d-db2415f475db 6d208120-6c7a-45a6-b411-402f18890d9b 1816cdd0-177c-4973-9e88-dd8b95318556 5c23f62f-06dc-46ad-8ead-688ec434e3e5 5c7d7990-3f35-41eb-ae16-d0c16098acc6 02a16c52-a834-4f30-b6af-a6aee51a294e f0988929-2718-4984-a1b6-c1f2ce152f1f 1c9d9cfe-ea2b-43f9-8f62-dc31d8ed3ae1 34cb742a-8ba4-47a7-87e6-f2685fe69e97 4fe10751-c399-4752-94b7-30113ad45070 c13fe5ac-6466-446e-886a-12df1431b1eb 714f9ca2-426e-4bff-8569-2d18f58fdcf8 045aeb5f-1087-4ac7-9702-a49404e7f7e8 840e9a0a-de98-4b7d-a172-f9bbda2d6b98 e342358b-75ed-4812-9376-6043fb6cb473 f3d5ccdc-1bb3-466f-871d-f6b92a26cbb4 59acb6fb-561c-4038-b722-a596a748b3c7 be7e6726-05c0-4228-821d-a8df91aeb5bc df4a6a60-9ce8-4c6c-91c0-ad5a5d732259 47491eb9-4606-42bd-8399-125a2b95fded 9b2d1306-5d19-439a-8f2c-b144dd7e22fa ef421152-8732-4f97-9acb-c8e9a6890d5e d48f8080-25b1-44f5-8322-7bf2712ff974 6c4de826-daad-4cd4-b703-51dfe803e822 01af22d6-6889-4e98-a3df-e6eddc40fc92 ea3b3dbe-cca2-4bde-957b-feaef7e18789 e737c8c6-b526-4f88-b89e-554e205b0614 efd24e87-d7f7-425f-9cb0-3ee17c7b2116 a62607e6-047e-4910-a1ec-5426bf9283b5 64dceb5b-de05-47c7-8e40-e9b293e80d75 8d51c652-6aee-4de8-ba03-47b289a13ec5 51d7b5ce-5664-4750-b1a0-fabcdc31e49a 6522e3af-aa9e-421c-b667-e11db73cd8ca 9ac073a0-7abf-4dff-826f-9c44d4780590 2da9c21c-adc7-405a-a36e-46fbd9dfcd42 fe4d1053-9c84-4221-bac7-cb489a7064ff 1f005f88-e6d7-4bdc-81fa-3acf4c89cf64 42dc5a7c-d7b1-4653-92b9-9359b46cc2d4 e25721a9-34f9-479c-a4c3-31f5ec9e117d 506d1de3-06df-4131-9e88-e43f1768e3d8 e6625695-25a2-43d0-9056-1e9a1a594b1e 91990287-4edf-4e38-aa6c-66d0e906807b 2216cdd0-177c-5678-9e88-dd8b95312234 1737c8c6-b526-4dd8-589e-ee4e205b06f4 6a43bef6-8b70-4253-a828-82c3ab399655 0a27038a-0f3a-48bb-b235-4a44066a1402 0a9ec2c3-5e18-4c0a-a183-fd86d9d9a08b 2216cdd0-177c-5678-9e88-dd8b95313334 2216cdd0-177c-5678-9e88-dd8b95313335 5b8ebeed-6b58-4c3a-8d5f-0958b1a90ce6""".split()

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<AnyLogicWorkspace WorkspaceVersion="1.9" AnyLogicVersion="8.9.9.202607020844" AlpVersion="8.9.9">
<Model><Id>{nid()}</Id><Name>CaserHorno</Name><EngineVersion>6</EngineVersion><JavaPackageName>{PKG}</JavaPackageName><ModelTimeUnit>Hour</ModelTimeUnit>
<Folders></Folders>
<ActiveObjectClasses>
{main}
{uli}
</ActiveObjectClasses>
<DifferentialEquationsMethod>EULER</DifferentialEquationsMethod><MixedEquationsMethod>RK45_NEWTON</MixedEquationsMethod><AlgebraicEquationsMethod>MODIFIED_NEWTON</AlgebraicEquationsMethod><AbsoluteAccuracy>1.0E-5</AbsoluteAccuracy><FixedTimeStep>0.001</FixedTimeStep><RelativeAccuracy>1.0E-5</RelativeAccuracy><TimeAccuracy>1.0E-9</TimeAccuracy>
<Frame><Id>{nid()}</Id><Width>1200</Width><Height>760</Height></Frame>
<Database><Id>{nid()}</Id><Logging>false</Logging><AutoExport>false</AutoExport><ShutdownCompact>false</ShutdownCompact><ImportSettings></ImportSettings><ExportSettings></ExportSettings></Database>
<RunConfiguration ActiveObjectClassId="{main_id}"><Id>{nid()}</Id><Name>RunConfiguration</Name><MaximumMemory>1024</MaximumMemory>
{model_time(fin_base)}
<AnimationProperties><StopNever>true</StopNever><ExecutionMode>realTimeScaled</ExecutionMode><RealTimeScale>48.0</RealTimeScale><EnableZoomAndPanning>true</EnableZoomAndPanning><EnableDeveloperPanel>false</EnableDeveloperPanel><ShowDeveloperPanelOnStart>false</ShowDeveloperPanelOnStart></AnimationProperties>
<Inputs></Inputs><Outputs></Outputs></RunConfiguration>
<Experiments>{experiments}</Experiments>
<RequiredLibraryReference><LibraryName>com.anylogic.libraries.modules.markup_descriptors</LibraryName><VersionMajor>1</VersionMajor><VersionMinor>0</VersionMinor><VersionBuild>0</VersionBuild></RequiredLibraryReference>
<RequiredLibraryReference><LibraryName>{PML}</LibraryName><VersionMajor>8</VersionMajor><VersionMinor>0</VersionMinor><VersionBuild>5</VersionBuild></RequiredLibraryReference>
</Model>
<ConvertersApplied>{''.join(f'<Uuid>{u}</Uuid>' for u in uuids)}</ConvertersApplied>
</AnyLogicWorkspace>
"""


if __name__ == "__main__":
    if SALIDA.exists() and "--forzar" not in sys.argv:
        sys.exit(f"{SALIDA.name} ya existe: el .alp es la fuente de verdad una vez abierto en el IDE. Usar --forzar para regenerarlo.")
    texto = construir()
    import xml.etree.ElementTree as ET
    ET.fromstring(texto.encode("utf-8"))  # bien formado
    SALIDA.write_text(texto, encoding="utf-8", newline="\n")
    print(f"Escrito {SALIDA} ({len(texto)//1024} KB)")
