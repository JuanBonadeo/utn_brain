#!/usr/bin/env python3
"""Verifica CaserHorno.alp sin abrir el IDE. No reemplaza Build/Run en AnyLogic.

Uso, desde la raíz del repo (Windows):
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/verificar_modelo.py [archivo.alp] [--largo]

1. Estructura del XML: bien formado, Ids únicos, bloques y conexiones, experimentos que referencian parámetros.
2. Compila los parámetros, variables y funciones de Main contra la API instalada de AnyLogic 8.9 PLE
   (bloques Source/Wait/Delay/Sink, EventTimeout, Agent).
3. Ejecuta las MISMAS funciones (extraídas del .alp) dentro de un motor de eventos discretos mínimo que
   imita el cableado del modelo: Source.inject -> colaHorno.onEnter; colaHorno.free -> horno (Delay,
   capacidad 1, delayTime del .alp) -> sink.onEnter. Pruebas: trazas exactas de campaña, modo cupo,
   prioridad, espera máxima, conservación, números aleatorios comunes, desempate FIFO/LIFO y el caso
   degenerado M/M/1 (L, Lq, W, Wq, rho contra la teoría).
Requiere AnyLogic 8.9 PLE en D:\\AnyLogic 8.9 Personal Learning Edition (o la variable ANYLOGIC_HOME).
"""
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
LARGO = "--largo" in sys.argv
ALP = Path(args[0]).resolve() if args else AQUI / "CaserHorno.alp"
AL = Path(os.environ.get("ANYLOGIC_HOME", r"D:\AnyLogic 8.9 Personal Learning Edition"))
JAVAC, JAVA = AL / "jre" / "bin" / "javac.exe", AL / "jre" / "bin" / "java.exe"
if not JAVAC.exists():
    sys.exit(f"No encuentro javac en {JAVAC}. Definir ANYLOGIC_HOME.")


def code(e):
    return (e.text or "").strip() if e is not None else ""


# ------------------------------------------------------------------ 1. estructura
root = ET.parse(ALP).getroot()
model = root.find("Model")
clases = {c.findtext("Name"): c for c in model.findall("ActiveObjectClasses/ActiveObjectClass")}
assert set(clases) == {"Main", "ULI"}, clases.keys()
main, uli = clases["Main"], clases["ULI"]
assert model.findtext("ModelTimeUnit") == "Hour"
refs = {id(i) for tag in ("FreeformParamValue", "RangeVariationParamValue") for v in root.iter(tag) for i in v.findall("Id")}
ids = [(i.text or "").strip() for i in root.iter("Id") if id(i) not in refs]
dup = {i for i in ids if ids.count(i) > 1}
assert not dup, f"Ids duplicados: {dup}"
assert main.findtext("CurrentLevel") == main.find("Presentation/Level").findtext("Id"), "Main necesita un Level con el Id de CurrentLevel"
bloques = {b.findtext("Name"): b for b in main.findall("EmbeddedObjects/EmbeddedObject")}
assert {n: b.findtext("ActiveObjectClass/ClassName") for n, b in bloques.items()} == \
    {"source": "Source", "colaHorno": "Wait", "horno": "Delay", "sink": "Sink"}
bp = {n: {p.findtext("Name"): p for p in b.findall("Parameters/Parameter")} for n, b in bloques.items()}
assert code(bp["horno"]["capacity"].find("Value/Code")) == "1"
assert bp["horno"]["delayTime"].findtext("Value/Unit") == "HOUR"
assert bp["source"]["newEntity"].findtext("Value/EntityEmbeddedObject/ActiveObjectClass/ClassName") == "ULI"
conns = {(c.findtext("SourceEmbeddedObjectReference/ItemName"), c.findtext("TargetEmbeddedObjectReference/ItemName"))
         for c in main.findall("Connectors/Connector")}
assert conns == {("source", "colaHorno"), ("colaHorno", "horno"), ("horno", "sink")}, conns
params = {v.findtext("Name"): v for v in main.findall("Variables/Variable[@Class='Parameter']")}
pid = {v.findtext("Id"): n for n, v in params.items()}
for e in model.findall("Experiments/*"):
    if e.tag == "SimulationExperiment":
        assert {p.findtext("ParameterName") for p in e.findall("Parameters/Parameter")} == set(params), e.findtext("Name")
    else:
        assert {pid[f.findtext("Id")] for f in e.findall("FreeformParamValue")} == set(params), e.findtext("Name")
exps = {e.findtext("Name"): e for e in model.findall("Experiments/*")}
assert set(exps) == {"Visual", "VerificacionMM1", "CorridasE0E3"}
cor = {pid[f.findtext("Id")]: f.findtext("Expression/Code") for f in exps["CorridasE0E3"].findall("FreeformParamValue")}
assert exps["CorridasE0E3"].findtext("NumberOfRuns") == "120" and cor["semilla"] == "1 + index % 30"
assert all(r.findtext("ReturnModificator") in ("VOID", "RETURNS_VALUE") for r in main.findall("Functions/Function"))
# Los eventos se programan solo con restart(): tienen que ser "User control". Con "occuresOnce" el motor los
# agenda al arrancar el agente y pisa el restart(0) de inicializar() (07/10/2026: sin llegadas en el IDE).
modos = {e.findtext("Name"): e.find("Properties").get("Mode") for e in main.findall("Events/Event")}
assert all(m == "userControls" for m in modos.values()), f"eventos que no son userControls: {modos}"
print("OK 1/3: XML bien formado, Ids unicos, Source->Wait->Delay(1)->Sink, experimentos completos")

# ------------------------------------------------------------------ extracción de Java
campos = []
for v in main.findall("Variables/Variable"):
    pr = v.find("Properties")
    val = code(pr.find("DefaultValue/Code")) if v.get("Class") == "Parameter" else code(pr.find("InitialValue/Code"))
    campos.append(f"{pr.findtext('Type')} {v.findtext('Name')} = {val};")
funcs = []
for f in main.findall("Functions/Function"):
    a = ", ".join(p.findtext("Type") + " " + p.findtext("Name") for p in f.findall("Parameter"))
    funcs.append(f"public {f.findtext('ReturnType')} {f.findtext('Name')}({a}) {{\n{code(f.find('Body'))}\n}}")
eventos = [(e.findtext("Name"), code(e.find("Action"))) for e in main.findall("Events/Event")]
uli_campos = [f"{v.findtext('Properties/Type')} {v.findtext('Name')} = {code(v.find('Properties/InitialValue/Code'))};"
              for v in uli.findall("Variables/Variable")]
on_cola = code(bp["colaHorno"]["onEnter"].find("Value/Code"))
on_sink = code(bp["sink"]["onEnter"].find("Value/Code"))
delay_expr = code(bp["horno"]["delayTime"].find("Value/Code"))
startup = code(main.find("StartupCode"))
# Expresiones de la presentación, el statechart y los gráficos: se compilan contra la API (no se ejecutan).
expr_pres = []
for el in main.find("Presentation").iter():
    if el.tag in ("XCode", "YCode", "VisibleCode", "FillColorCode", "LineColorCode", "TextCode", "ColorCode", "WidthCode", "HeightCode"):
        expr_pres.append(code(el))
    elif el.tag == "ReplicationCode":
        expr_pres.append("(int) (" + code(el.find("Code")) + ")")
    elif el.tag == "Expression2":
        expr_pres.append("(double) (" + code(el) + ")")
for t in main.findall("StatechartElements/StatechartElement[@Class='Transition']"):
    expr_pres.append("(boolean) (" + code(t.find("Properties/Condition")) + ")")
presentacion = "void presentacion(int index) {" + " ".join(f"Object p{i} = {e};" for i, e in enumerate(expr_pres)) + "}"
cuerpo = "\n".join(campos + funcs)

tmp = tempfile.TemporaryDirectory(prefix="caser-check-")
d = Path(tmp.name)
jars = [str(j) for j in (AL / "plugins").rglob("*.jar") if "anylogic" in str(j).lower()]
cp = ";".join(jars)

# ------------------------------------------------------------------ 2. compilación contra la API
api = """import com.anylogic.engine.*;
import com.anylogic.libraries.processmodeling.*;
public class CaserApiCheck extends Agent {
static class ULI extends Agent { %ULI% }
Source<Agent> source; Wait<Agent> colaHorno; Delay<Agent> horno; Sink<Agent> sink;
EventTimeout %EVENTOS%;
%CUERPO%
void callbacks(Agent agent) { %ONCOLA% %ONSINK% double dt = %DELAY%; %STARTUP% %ACCIONES% }
%PRESENTACION%
}""".replace("%ULI%", " ".join(uli_campos)).replace("%EVENTOS%", ", ".join(n for n, _ in eventos)) \
   .replace("%CUERPO%", cuerpo).replace("%ONCOLA%", on_cola).replace("%ONSINK%", on_sink) \
   .replace("%DELAY%", delay_expr).replace("%STARTUP%", startup).replace("%ACCIONES%", " ".join(a for _, a in eventos))    .replace("%PRESENTACION%", presentacion)
(d / "CaserApiCheck.java").write_text(api, encoding="utf-8")
# El classpath completo supera el largo máximo de una línea de comando en Windows: va en un @argfile.
(d / "javac.args").write_text('-cp "' + cp.replace("\\", "/") + '"', encoding="utf-8")
r = subprocess.run([str(JAVAC), "-encoding", "UTF-8", "-nowarn", "@" + str(d / "javac.args"), "-d", str(d), str(d / "CaserApiCheck.java")],
                   capture_output=True, text=True)
if r.returncode:
    print(r.stdout, r.stderr)
    sys.exit("FALLA 2/3: las funciones no compilan contra la API de AnyLogic")
print(f"OK 2/3: funciones, eventos, callbacks y {len(expr_pres)} expresiones de presentacion/statechart compilan contra la API de AnyLogic 8.9")

# ------------------------------------------------------------------ 3. motor mínimo + pruebas
harness = r"""import java.util.*;
public class CaserLogicCheck {
static class Agent {}
static class ULI extends Agent { %ULI% }
// ---------- motor de eventos discretos mínimo ----------
static boolean LIFO = false;
double clock = 0; long seq = 0; boolean terminado = false;
static class Ev { double t; long s; Runnable r; boolean cancelado; }
PriorityQueue<Ev> fel = new PriorityQueue<Ev>((a, b) -> a.t != b.t ? Double.compare(a.t, b.t) : (LIFO ? Long.compare(b.s, a.s) : Long.compare(a.s, b.s)));
Ev agendar(double t, Runnable r) { if (t < clock - 1e-9) throw new AssertionError("evento en el pasado"); Ev e = new Ev(); e.t = t; e.s = seq++; e.r = r; fel.add(e); return e; }
void correr(double hasta) { while (!terminado && !fel.isEmpty() && fel.peek().t <= hasta) { Ev e = fel.poll(); if (e.cancelado) continue; clock = e.t; e.r.run(); } if (!terminado) clock = Math.max(clock, Math.min(hasta, 1e15)); }
class EventTimeout { Ev p; Runnable accion;
  void restart(double dt) { reset(); if (dt < 0) throw new AssertionError("timeout negativo"); p = agendar(clock + dt, () -> { p = null; accion.run(); }); }
  void reset() { if (p != null) { p.cancelado = true; p = null; } }
  boolean isActive() { return p != null; }
  double getRest() { return p == null ? 0 : p.t - clock; } }
class Wait implements Iterable<Agent> { ArrayList<Agent> l = new ArrayList<Agent>();
  boolean free(Agent a) { if (!l.remove(a)) return false; entraHorno(a); return true; }
  public Iterator<Agent> iterator() { return new ArrayList<Agent>(l).iterator(); }
  int size() { return l.size(); } }
class Source { int creadas = 0; void inject(int n) { for (int i = 0; i < n; i++) { ULI u = new ULI(); creadas++; colaHorno.l.add(u); creadasLista.add(u); onEnterCola(u); } } }
ArrayList<ULI> creadasLista = new ArrayList<ULI>();
Source source = new Source(); Wait colaHorno = new Wait(); Agent enHorno = null; int salidas = 0;
void entraHorno(Agent agent) { if (enHorno != null) throw new AssertionError("Delay de capacidad 1 con dos ULI"); enHorno = agent; double dt = %DELAY%; agendar(clock + dt, () -> { enHorno = null; salidas++; onEnterSink(agent); }); }
void onEnterCola(Agent agent) { %ONCOLA% }
void onEnterSink(Agent agent) { %ONSINK% }
EventTimeout %EVENTOS_DECL%;
CaserLogicCheck() { %EVENTOS_INIT% }
ArrayList<String> trazas = new ArrayList<String>();
double time() { return clock; }
void traceln(String s) { trazas.add(s); }
void finishSimulation() { terminado = true; }
void startup() { %STARTUP% }
// ---------- funciones de Main, tal cual están en el .alp ----------
%CUERPO%
// ---------- pruebas ----------
static void ok(boolean c, String m) { if (!c) throw new AssertionError(m); }
static void eq(double a, double b, String m) { ok(Math.abs(a - b) < 1e-9, m + ": " + a + " != " + b); }
static void cerca(double a, double b, double rel, String m) { ok(Math.abs(a - b) <= rel * Math.abs(b), m + String.format(": %.4f vs %.4f (tol %.0f%%)", a, b, 100 * rel)); System.out.println(String.format("   %-28s modelo %.4f  teoria %.4f  (%+.2f%%)", m, a, b, 100 * (a - b) / b)); }
// Modelo de traza: sin llegadas propias (semanas en cero), tiempos chicos, se inyecta a mano.
static CaserLogicCheck traza(int umbral, String modo) {
  CaserLogicCheck m = new CaserLogicCheck();
  m.llegadasSemanas = new int[] {0, 0, 0, 0, 0}; m.umbralULI = umbral; m.modoFinCampana = modo;
  m.hCalentamiento = 1; m.hEnfriamiento = 2; m.horasEnVacio = 0.5; m.minPorULI = 60; m.pPrioridad = 0;
  m.calentamientoModeloDias = 0; m.horizonteDias = 100; m.kgCuantiles = new double[] {100, 100};
  m.startup(); return m; }
void llegaEn(double t) { agendar(t, () -> source.inject(1)); }
void llegaUrgenteEn(double t) { agendar(t, () -> { double p = pPrioridad; pPrioridad = 1; source.inject(1); pPrioridad = p; }); }
int balance() { return creadasLista.size() - nEnCola - (ocupado ? 1 : 0) - salidas; }
public static void main(String[] a) {
  // Validaciones de entrada
  for (String malo : new String[] {"cupoo", ""}) { CaserLogicCheck m = new CaserLogicCheck(); m.modoFinCampana = malo; try { m.startup(); throw new AssertionError("modo invalido aceptado"); } catch (IllegalArgumentException e) {} }
  { CaserLogicCheck m = new CaserLogicCheck(); m.umbralULI = 0; try { m.startup(); throw new AssertionError("umbral 0 aceptado"); } catch (IllegalArgumentException e) {} }
  // A. Campaña work-conserving: 3 ULI disparan el umbral, una cuarta llega en vacío y se carga.
  { CaserLogicCheck m = traza(3, "workConserving");
    m.llegaEn(0); m.llegaEn(1); m.llegaEn(2); m.llegaEn(6.2);
    m.correr(2.0); ok(m.estado == 2, "a t=2 el umbral enciende: estado " + m.estado);
    m.correr(6.1); ok(m.estado == 3 && m.enVacio, "a t=6.1 caliente en vacio");
    m.correr(7.5); ok(m.estado == 3 && m.enVacio, "la ULI de 6.2 cancela el vacio y se trata");
    m.correr(7.8); ok(m.estado == 4, "vacio de 0.5 h tras la ultima ULI (7.2) -> enfria a 7.7");
    m.correr(9.8); ok(m.estado == 0, "enfriamiento de 2 h -> apagado a 9.7");
    ok(m.esperas.equals(Arrays.asList(3.0, 3.0, 3.0, 0.0)), "esperas " + m.esperas);
    ok(m.nEncendidos == 1 && m.ulisPorCampana.equals(Arrays.asList(4.0)), "una campana de 4 ULI");
    eq(m.horasCaliente, 4.7, "horas a temperatura (3 a 7.7)");
    eq(m.kWhTotal(), 1384 + 2445.0 / 24 * 4.7, "kWh");
    eq(m.diasPorCampana.get(0), 1, "dias calendario de la campana");
    ok(m.balance() == 0 && m.nTratadas == 4, "conservacion"); }
  // B. Modo cupo: la ULI que llega durante la campaña espera a la próxima.
  { CaserLogicCheck m = traza(3, "cupo");
    m.llegaEn(0); m.llegaEn(1); m.llegaEn(2); m.llegaEn(4.5);
    m.correr(20); ok(m.ulisPorCampana.equals(Arrays.asList(3.0)), "cupo: la campana trata 3 " + m.ulisPorCampana);
    ok(m.estado == 1 && m.nEnCola == 1, "la cuarta queda acumulando para la proxima");
    eq(m.sumaColaAlApagar, 1, "cola al apagar");
    CaserLogicCheck w = traza(3, "workConserving"); w.llegaEn(0); w.llegaEn(1); w.llegaEn(2); w.llegaEn(4.5); w.correr(20);
    ok(w.ulisPorCampana.equals(Arrays.asList(4.0)), "workConserving trata las 4"); }
  // C. Prioridad: una urgente con 2 normales en cola enciende antes del umbral y trata solo la urgente.
  { CaserLogicCheck m = traza(5, "workConserving");
    m.llegaEn(0); m.llegaEn(1); m.llegaUrgenteEn(2);
    m.correr(2.0); ok(m.estado == 2 && m.campanaPrioridad, "la urgente enciende por prioridad");
    m.correr(4.0); ok(m.estado == 4, "trata solo la urgente (3-4) y enfria sin vacio");
    m.correr(6.5); ok(m.estado == 1 && m.nEnCola == 2, "las 2 normales siguen acumulando");
    ok(m.nEncendidosPrioridad == 1 && m.ulisPorCampana.equals(Arrays.asList(1.0)) && m.prioridadPorCampana.get(0), "campana de prioridad de 1 ULI");
    eq(m.esperas.get(0), 1, "espera de la urgente");
    // Con soloUrgentesEnPrioridad = false la misma campaña trata todo.
    CaserLogicCheck t = traza(5, "workConserving"); t.soloUrgentesEnPrioridad = false; t.llegaEn(0); t.llegaEn(1); t.llegaUrgenteEn(2); t.correr(20);
    ok(t.ulisPorCampana.equals(Arrays.asList(3.0)), "sin soloUrgentes trata las 3: " + t.ulisPorCampana);
    ok(t.esperas.get(0) == 1.0, "y la urgente va primero"); }
  // D. Espera máxima: con umbral 10 y 5 h de espera máxima, enciende a las 5 h de la primera ULI.
  { CaserLogicCheck m = traza(10, "workConserving"); m.esperaMaxDias = 5.0 / 24; m.startup();
    m.llegaEn(0); m.llegaEn(3);
    m.correr(4.9); ok(m.estado == 1, "antes de 5 h sigue acumulando");
    m.correr(5.0); ok(m.estado == 2 && !m.campanaPrioridad, "a las 5 h enciende por espera maxima");
    // La espera se mide desde la ULI más vieja aunque haya llegado durante el enfriamiento.
    m.llegaEn(9.0); m.correr(10.0); ok(m.estado == 4 && m.nEnCola == 1, "campana de 2 ULI (6-8), vacio 0.5, enfria 8.5-10.5; llega una a las 9");
    m.correr(10.6); ok(m.estado == 1, "apagado con 1 en cola -> acumulando");
    m.correr(14.0); ok(m.estado == 2 && m.tEncendido == 14.0, "enciende a 14 = llegada 9 + 5 h: " + m.tEncendido); }
  // E. Corrida larga con entradas reales: conservación, CRN entre escenarios y desempate FIFO/LIFO.
  String[] filas = new String[4]; double[][] llegadas = new double[4][];
  for (int e = 0; e < 4; e++) {
    CaserLogicCheck m = new CaserLogicCheck(); m.escenario = "E" + e; m.semilla = 7;
    if (e == 1) m.umbralULI = 45; if (e == 2) m.esperaMaxDias = 15; if (e == 3) m.horasEnVacio = 96;
    m.startup(); m.correr(1e9);
    ok(m.terminado && m.finalizado, "la corrida termina sola");
    ok(m.balance() == 0, "conservacion E" + e);
    ok(m.creadasLista.size() < 50000, "limite PLE de 50.000 agentes: " + m.creadasLista.size());
    double[] ll = new double[3 * m.creadasLista.size()]; int k = 0;
    for (ULI u : m.creadasLista) { ll[k++] = u.tLlegada; ll[k++] = u.kg; ll[k++] = u.urgente ? 1 : 0; }
    llegadas[e] = ll; filas[e] = m.filaResultado();
    System.out.println("   " + m.trazas.get(m.trazas.size() - 1));
  }
  for (int e = 1; e < 4; e++) ok(Arrays.equals(llegadas[0], llegadas[e]), "E" + e + " recibe exactamente las mismas ULI que E0 (CRN)");
  LIFO = true;
  { CaserLogicCheck m = new CaserLogicCheck(); m.escenario = "E0"; m.semilla = 7; m.startup(); m.correr(1e9);
    ok(m.filaResultado().equals(filas[0]), "el resultado no depende del orden de eventos simultaneos (LIFO = FIFO)"); }
  LIFO = false;
  // F. Caso degenerado M/M/1 (05- §4.1): umbral 1, sin calentamiento ni enfriamiento, vacío 0.
  double lam = 0.7, mu = 1.0, rho = lam / mu;
  double[] teo = {rho * rho / (1 - rho), rho / (1 - rho), 1 / (mu - lam), rho / (mu - lam), rho};
  String[] nom = {"Lq (colaMediaULI)", "L (sistemaMedioULI)", "W horas (sistemaMedio)", "Wq horas (espera media)", "rho (utilizacion)"};
  for (int config = 0; config < 2; config++) {
    double dias = config == 0 ? 2400 : %DIAS_LARGO%; int sem = config == 0 ? 1 : 5;
    double[] acc = new double[5];
    for (int s = 1; s <= sem; s++) {
      CaserLogicCheck m = new CaserLogicCheck(); m.escenario = "MM1"; m.semilla = s; m.modoLlegadas = "poisson"; m.tasaPoissonPorHora = lam;
      m.minPorULI = 60 / mu; m.cicloExponencial = true; m.umbralULI = 1; m.hCalentamiento = 0; m.hEnfriamiento = 0; m.horasEnVacio = 0;
      m.pPrioridad = 0; m.calentamientoModeloDias = 100; m.horizonteDias = dias; m.startup(); m.correr(1e12);
      double h = m.horasMedidas();
      double[] v = {m.areaCola / h, m.areaSistema / h, m.sumaSistema / m.nTratadas, m.media(m.esperas), m.horasOcupado / h};
      for (int i = 0; i < 5; i++) acc[i] += v[i] / sem;
      ok(m.balance() == 0, "conservacion MM1");
      if (config == 0) ok(m.creadasLista.size() < 50000, "MM1 del IDE entra en el limite PLE: " + m.creadasLista.size());
    }
    System.out.println(config == 0 ? "   M/M/1 configuracion del IDE (2.400 dias, semilla 1):" : "   M/M/1 largo (" + (int) dias + " dias x 5 semillas):");
    double tol = config == 0 ? 0.10 : 0.03;
    for (int i = 0; i < 5; i++) cerca(acc[i], teo[i], tol, nom[i]);
  }
  System.out.println("OK 3/3: trazas exactas (umbral, vacio, enfriamiento, kWh), cupo, prioridad, espera maxima, conservacion, CRN, FIFO=LIFO y M/M/1");
  // G. Mismo diseño que el experimento CorridasE0E3 (expresiones idénticas), para probar el analizador y
  //    para comparar fila por fila con el CSV que escriba AnyLogic.
  if (a.length > 0) {
    new java.io.File(a[0]).delete();
    for (int index = 0; index < 120; index++) {
      CaserLogicCheck m = new CaserLogicCheck(); m.archivoSalida = a[0];
      %CORRIDAS%
      m.startup(); m.correr(1e12); ok(m.finalizado, "corrida " + index);
    }
  }
}
}"""
acciones_decl = ", ".join(n for n, _ in eventos)
acciones_init = " ".join(f"{n} = new EventTimeout(); {n}.accion = () -> {{ {a} }};" for n, a in eventos)
harness = (harness.replace("%ULI%", " ".join(uli_campos)).replace("%DELAY%", delay_expr).replace("%ONCOLA%", on_cola)
           .replace("%ONSINK%", on_sink).replace("%EVENTOS_DECL%", acciones_decl).replace("%EVENTOS_INIT%", acciones_init)
           .replace("%STARTUP%", startup).replace("%CUERPO%", cuerpo).replace("%DIAS_LARGO%", "40000" if LARGO else "12000")
           .replace("%CORRIDAS%", " ".join(f"m.{k} = {v};" for k, v in cor.items() if v and k != "archivoSalida")))
(d / "CaserLogicCheck.java").write_text(harness, encoding="utf-8")
r = subprocess.run([str(JAVAC), "-encoding", "UTF-8", "-nowarn", "-d", str(d), str(d / "CaserLogicCheck.java")], capture_output=True, text=True)
if r.returncode:
    print(r.stdout, r.stderr)
    sys.exit("FALLA: el harness no compila")
CSV_H = AQUI / "corridas_horno_harness.csv"
r = subprocess.run([str(JAVA), "-Xss8m", "-cp", str(d), "CaserLogicCheck", str(CSV_H)], capture_output=True, text=True)
print(r.stdout, end="")
if r.returncode:
    print(r.stderr)
    sys.exit("FALLA 3/3: pruebas de logica")
r = subprocess.run([sys.executable, "-I", str(AQUI / "analizar_corridas.py"), str(CSV_H)], capture_output=True, text=True, encoding="utf-8")
if r.returncode:
    print(r.stdout, r.stderr)
    sys.exit("FALLA: el analizador no procesa el CSV del harness")
print(f"OK: {CSV_H.name} (120 corridas del harness con las expresiones de CorridasE0E3) y analizar_corridas.py lo procesa.")
print("    Ese CSV es la referencia para comparar fila por fila con el de AnyLogic; no es un resultado del TPI.")
