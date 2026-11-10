#!/usr/bin/env python3
"""Verifica estructura y lógica del prototipo; no sustituye Build/Run en AnyLogic.
Requiere AnyLogic 8 PLE instalado en /Applications (macOS).
"""
import collections
from pathlib import Path
import xml.etree.ElementTree as E
import subprocess, sys
# Uso: verificar_modelo.py [archivo.alp]. Sin argumento verifica SubteConstitucion.alp. Admite el formato
# que escribe AnyLogic 8.9.9 y el que escribe 8.9.10 al guardar desde el IDE (CDATA, Id=0 en datasets, "900.0").
p=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).with_name('SubteConstitucion.alp')
r=E.parse(p).getroot();a=r.find('Model/ActiveObjectClasses/ActiveObjectClass')
fields=[]
for v in a.findall('Variables/Variable'):
 prop=v.find('Properties'); val=prop.findtext('DefaultValue/Code') if v.get('Class')=='Parameter' else prop.findtext('InitialValue/Code')
 fields.append(f'{prop.findtext("Type")} {v.findtext("Name")} = {val};')
functions=[]
for f in a.findall('Functions/Function'):
 args=', '.join(x.findtext('Type')+' '+x.findtext('Name') for x in f.findall('Parameter'))
 functions.append(f'public {f.findtext("ReturnType")} {f.findtext("Name")}({args}) {{\n{f.findtext("Body")}\n}}')
common='\n'.join(fields+functions)
# Compile actual signatures against the installed AnyLogic libraries.
real='''import com.anylogic.engine.*;
import com.anylogic.libraries.processmodeling.*;
public class SubteApiCheck extends Agent {
Source<Agent> source;
EventTimeout proximaTanda, cierreFranja, observarCola;
'''+common+'\n}'
import tempfile
workspace=tempfile.TemporaryDirectory(prefix='subte-check-')
d=Path(workspace.name)
(d/'SubteApiCheck.java').write_text(real)
plugins=Path('/Applications/AnyLogic 8 PLE.app/Contents/Resources/Java/plugins')
jars=list(plugins.glob('com.anylogic*/**/*.jar'))
javac='/Applications/AnyLogic 8 PLE.app/Contents/jre/bin/javac'
subprocess.run([javac,'-cp',':'.join(map(str,jars)),str(d/'SubteApiCheck.java')],check=True)
print('OK: Java functions compile against the installed AnyLogic API')
# Exercise the model functions with explicit event traces, not a second queue model.
harness='''public class SubteLogicCheck {
static class Agent {}
static class Event { void restart(double t) {} }
static class Source { int injected; void inject(int n) {injected+=n;} }
static class Engine { void finish() {} }
Source source=new Source();
Event proximaTanda=new Event(), cierreFranja=new Event(), observarCola=new Event();
double clock;
double time() {return clock;}
Engine getEngine(){return new Engine();}
void traceln(String s){}
'''+common+'''
static void eq(double a,double b){if(Math.abs(a-b)>1e-8)throw new AssertionError(a+" != "+b);}
public static void main(String[] args){
 SubteLogicCheck m=new SubteLogicCheck();m.modoDemo=false;
 try{m.inicializar();throw new AssertionError("Missing field data accepted");}catch(IllegalArgumentException expected){}
 m.modoDemo=true;m.molinetesBase=2;m.usarPerfilSBASE=false;m.inicializar();
 Agent[] p={new Agent(),new Agent(),new Agent(),new Agent(),new Agent()};
 Agent u=new Agent(),v=new Agent();
 m.nPrincipal=5;m.nGenerados=5;m.tandasAbiertas.add(0.0);
 // A single batch: two immediately served, three wait.
 for(Agent x:p)m.entraCola(x);
 m.iniciaServicio(p[0],u);m.iniciaServicio(p[1],v);eq(m.qMax,3);
 m.clock=3;m.liberaMolinete(u);m.salePasajero();m.iniciaServicio(p[2],u);
 m.liberaMolinete(v);m.salePasajero();m.iniciaServicio(p[3],v);
 m.clock=6;m.liberaMolinete(u);m.salePasajero();m.iniciaServicio(p[4],u);
 m.liberaMolinete(v);m.salePasajero();m.observar();
 eq(m.sumaEspera/5,2.4);eq(m.percentil90(),6);eq(m.disipaciones.get(0),6);
 m.clock=9;m.liberaMolinete(u);m.salePasajero();m.observar();
 m.clock=9000;m.cerrarFranja();m.observar();eq(m.areaCola,12);eq(m.areaOcupados,15);
 eq(m.nEsperando,0);eq(m.nOcupados,0);eq(m.pendientesAlCierre,0);
 if(!m.finalizado)throw new AssertionError("Not finished");
 // E2 zero/full diversion, E1 capacity, E3 service and batch cut-off.
 for(int e=0;e<4;e++){
  SubteLogicCheck n=new SubteLogicCheck();n.escenario=e;n.fraccionDesvioE2=1;n.inicializar();n.generarTanda();
  eq(n.nGenerados,n.nPrincipal+n.nDesviados);
  eq(n.source.injected,n.nPrincipal);
  if(e==2)eq(n.nPrincipal,0);
  eq(n.capacidadMolinetes(),e==1?22:20);eq(n.servicioSeg(),e==3?2.5:3);
  int total=n.nGenerados;n.clock=9000;n.generarTanda();eq(n.nGenerados,total);
 }
 // A passenger still in service at 09:30 is counted only in drained throughput.
 SubteLogicCheck z=new SubteLogicCheck();z.inicializar();z.nPrincipal=1;z.nGenerados=1;
 z.clock=8999;Agent late=new Agent();z.entraCola(late);z.iniciaServicio(late,u);
 z.clock=9000;z.cerrarFranja();eq(z.pendientesAlCierre,1);
 z.clock=9002;z.liberaMolinete(u);z.salePasajero();z.observar();
 eq(z.nProcesadosFranja,0);eq(z.nProcesados,1);eq(z.areaOcupados,1);
 System.out.println("OK: missing data, exact batch waits/P90/Lq/occupation, E0-E3, balance and 09:30 drain");
}
}'''
(d/'SubteLogicCheck.java').write_text(harness)
subprocess.run([javac,str(d/'SubteLogicCheck.java')],check=True)
subprocess.run(['/Applications/AnyLogic 8 PLE.app/Contents/jre/bin/java','-cp',str(d),'SubteLogicCheck'],check=True)
# Compile the Java bodies of the incremental pedestrian root with small API stubs.
ped_agent=next(x for x in r.findall('Model/ActiveObjectClasses/ActiveObjectClass') if x.findtext('Name')=='MainPeatonal')
ped_fields=[]
for v in ped_agent.findall('Variables/Variable'):
 prop=v.find('Properties'); val=prop.findtext('DefaultValue/Code') if v.get('Class')=='Parameter' else prop.findtext('InitialValue/Code')
 ped_fields.append(f'{prop.findtext("Type")} {v.findtext("Name")} = {val};')
ped_functions=[]
for f in ped_agent.findall('Functions/Function'):
 args=', '.join(x.findtext('Type')+' '+x.findtext('Name') for x in f.findall('Parameter'))
 ped_functions.append(f'public {f.findtext("ReturnType")} {f.findtext("Name")}({args}) {{\n{f.findtext("Body")}\n}}')
# Textos dinámicos de la vista (panel en vivo y KPI): se compilan como métodos para detectar errores antes del IDE.
ped_textos=[f'String _texto{i}() {{ return String.valueOf({c}); }}' for i,c in enumerate([t.findtext('TextCode') for t in ped_agent.iter('Text') if t.findtext('TextCode')])]
assert len(ped_textos)>=10, 'panel en vivo y KPI'
ped_check='''public class SubtePedLogicCheck {
static class Pasajero {
 double tEntradaColaPed, tIngresoSistemaPed, tInicioServicioPed, servicioAsignadoPed, y, x=200;
 double getY(){return y;} double getX(){return x;}
 boolean enColaPed, enPicoPed, desdeRocaPed=true;
 String nombreMolinetePed=""; int colaElegidaPed=-1;
}
static class PedSourceStub { int injected, calls; java.util.ArrayList<Integer> sizes=new java.util.ArrayList<Integer>(); void inject(int n) {injected+=n;calls++;sizes.add(n);} }
class EventStub { double at=-1; void restart(double t) {at=clock+t;} }
static class Point { double x, y; Point(double x,double y){this.x=x;this.y=y;} }
static class QueuePath { Point end; int size; QueuePath(double y,int size){end=new Point(496,y);this.size=size;} Point getEndPoint(){return end;} }
static class ServiceStub { int calls, suspended; java.util.List<QueuePath> colas=new java.util.ArrayList<QueuePath>();
 void setServiceSuspended(Object p, boolean value) { calls++; if(value)suspended++; }
 java.util.List<QueuePath> getQueues(){return colas;} int queueSize(QueuePath q){return q.size;} }
static class EngineStub { boolean finished; void finish(){finished=true;} }
static class RandomStub extends java.util.Random { long seed=-1; public synchronized void setSeed(long s){seed=s;super.setSeed(s);} }
PedSourceStub pedSource=new PedSourceStub(), pedSourceCalle=new PedSourceStub();
static class TrainSourceStub { int injected; void inject(){injected++;} }
TrainSourceStub trenesRocaFuente=new TrainSourceStub();
EventStub proximoTrenRocaPed=new EventStub(), proximaTandaPed=new EventStub(), cierreMetricasPed=new EventStub(), proximaLiberacionPed=new EventStub(), proximaLlegadaCallePed=new EventStub(), progresoPed=new EventStub();
java.util.ArrayList<String> eventos=new java.util.ArrayList<String>();
// Bucle de eventos minimo para la demanda de la franja (liberaciones del Roca y llegadas de calle).
void correrDemanda(){ while(proximaLiberacionPed.at>=0||proximaLlegadaCallePed.at>=0){ boolean roca=proximaLlegadaCallePed.at<0||(proximaLiberacionPed.at>=0&&proximaLiberacionPed.at<=proximaLlegadaCallePed.at); EventStub e=roca?proximaLiberacionPed:proximaLlegadaCallePed; clock=e.at; e.at=-1; int r0=pedSource.injected,c0=pedSourceCalle.injected; if(roca)liberarPendientesPed(); else llegadaCallePed(); eventos.add(String.format(java.util.Locale.US,"%.6f;%d;%d",clock,pedSource.injected-r0,pedSourceCalle.injected-c0)); } }
static SubtePedLogicCheck franja(int molinetes,double factor){ SubtePedLogicCheck f=new SubtePedLogicCheck(); f.modoFranjaPed=true; f.molinetesOperativosPed=molinetes; f.proporcionRocaPed=0.8; f.demoraAccesoRocaSeg=60; f.duracionDescargaSeg=120; f.servicioPedSeg=3; f.servicioMinPedSeg=2; f.servicioMaxPedSeg=5; f.factorDemandaPed=factor; f.inicializarPed(); f.programarDemandaFranjaPed(); f.correrDemanda(); return f; }
static SubtePedLogicCheck franjaReal(int molinetes,double moda,double min,double max,int dia){ SubtePedLogicCheck f=new SubtePedLogicCheck(); f.modoFranjaPed=true; f.molinetesOperativosPed=molinetes; f.proporcionRocaPed=0.8; f.demoraAccesoRocaSeg=10; f.duracionDescargaSeg=30; f.servicioPedSeg=moda; f.servicioMinPedSeg=min; f.servicioMaxPedSeg=max; f.diaSbasePed=dia; f.llegadasRealesPed=true; f.cargaTrenPoissonPed=true; f.inicializarPed(); f.programarDemandaFranjaPed(); f.correrDemanda(); return f; }
static SubtePedLogicCheck franjaVar(int molinetes,double moda,double min,double max){ SubtePedLogicCheck f=new SubtePedLogicCheck(); f.modoFranjaPed=true; f.molinetesOperativosPed=molinetes; f.proporcionRocaPed=0.8; f.demoraAccesoRocaSeg=10; f.duracionDescargaSeg=30; f.servicioPedSeg=moda; f.servicioMinPedSeg=min; f.servicioMaxPedSeg=max; f.diaSbasePed=-2; f.atrasoMaxRocaSeg=120; f.cargaTrenPoissonPed=true; f.inicializarPed(); f.programarDemandaFranjaPed(); f.correrDemanda(); return f; }
ServiceStub molinetesPeatonales=new ServiceStub(); EngineStub engine=new EngineStub(); RandomStub rng=new RandomStub();
Object molinetePed21=new Object(), molinetePed22=new Object(), molinetePed23=new Object(), molinetePed24=new Object();
Object molinetePed25=new Object(), molinetePed26=new Object(), molinetePed27=new Object(), molinetePed28=new Object();
java.util.ArrayList<String> trazas=new java.util.ArrayList<String>();
double clock; double time(){return clock;} void traceln(String s){trazas.add(s);}
EngineStub getEngine(){return engine;} java.util.Random getDefaultRandomGenerator(){return rng;}
'''+ '\n'.join(ped_fields+ped_functions+ped_textos) + '''
static void ok(boolean c,String m){if(!c)throw new AssertionError(m);}
static void eq(double a,double b,String m){ok(Math.abs(a-b)<1e-9,m+": "+a+" != "+b);}
public static void main(String[] args) throws Exception {
 SubtePedLogicCheck m=new SubtePedLogicCheck();
 m.configurarMolinetesPed();
 ok(m.molinetesPeatonales.calls==8 && m.molinetesPeatonales.suspended==8,"E0 suspende 8");
 SubtePedLogicCheck e1=new SubtePedLogicCheck();e1.molinetesOperativosPed=22;e1.configurarMolinetesPed();
 ok(e1.molinetesPeatonales.calls==8 && e1.molinetesPeatonales.suspended==6,"E1 habilita los 22 del vestibulo Principal");
 SubtePedLogicCheck e1b=new SubtePedLogicCheck();e1b.molinetesOperativosPed=28;e1b.configurarMolinetesPed();
 ok(e1b.molinetesPeatonales.calls==8 && e1b.molinetesPeatonales.suspended==0,"ampliacion hipotetica habilita 28");
 for(int mal:new int[]{19,29}){SubtePedLogicCheck x=new SubtePedLogicCheck();x.molinetesOperativosPed=mal;try{x.configurarMolinetesPed();throw new AssertionError("acepta "+mal+" molinetes");}catch(IllegalArgumentException expected){}}
 // Eleccion de cola: nunca un molinete suspendido; equilibra desvio lateral y personas en cola.
 for(int k=0;k<28;k++){m.molinetesPeatonales.colas.add(new QueuePath(225+10*k+(k>=14?20:0),0));e1.molinetesPeatonales.colas.add(m.molinetesPeatonales.colas.get(k));e1b.molinetesPeatonales.colas.add(m.molinetesPeatonales.colas.get(k));}
 Pasajero sur=new Pasajero();sur.y=515;sur.servicioAsignadoPed=3;
 ok(m.elegirColaPed(sur)==m.molinetesPeatonales.colas.get(19),"E0 elige el habilitado mas cercano (20)");
 sur.colaElegidaPed=-1;ok(e1.elegirColaPed(sur)==e1.molinetesPeatonales.colas.get(21),"E1 usa hasta el 22");
 sur.colaElegidaPed=-1;ok(e1b.elegirColaPed(sur)==e1b.molinetesPeatonales.colas.get(27),"la ampliacion puede usar el 28");
 m.asignadosPed=new int[28];m.asignadosPed[19]=3;
 sur.colaElegidaPed=-1;ok(m.elegirColaPed(sur)==m.molinetesPeatonales.colas.get(18),"una cola ocupada desvia al molinete vecino");
 m.asignadosPed=new int[28];
 // Efecto manada: con colas vacias, cinco pasajeros del mismo tren no eligen todos la misma cola,
 // porque cada eleccion cuenta a los asignados que todavia no empezaron a validar (caminando o en fila).
 {SubtePedLogicCheck h=new SubtePedLogicCheck();h.molinetesOperativosPed=22;for(QueuePath q:m.molinetesPeatonales.colas)h.molinetesPeatonales.colas.add(q);
  java.util.HashSet<QueuePath> elegidas=new java.util.HashSet<QueuePath>();Pasajero[] tanda=new Pasajero[5];
  for(int i=0;i<5;i++){tanda[i]=new Pasajero();tanda[i].y=360;tanda[i].servicioAsignadoPed=2.4;elegidas.add(h.elegirColaPed(tanda[i]));}
  ok(elegidas.size()==5,"la tanda se reparte entre colas: "+elegidas.size());
  // Aunque el servicio propio todavia no este sorteado (eleccion antes del On exit de la fuente), la fila pesa.
  {SubtePedLogicCheck z=new SubtePedLogicCheck();z.molinetesOperativosPed=22;for(QueuePath q:m.molinetesPeatonales.colas)z.molinetesPeatonales.colas.add(q);
   java.util.HashSet<QueuePath> el=new java.util.HashSet<QueuePath>();for(int i=0;i<5;i++){Pasajero x=new Pasajero();x.y=360;x.servicioAsignadoPed=0;el.add(z.elegirColaPed(x));}
   ok(el.size()==5 && z.eleccionesSinServicioPed==5,"sin servicio sorteado igual se reparte: "+el.size());}
  int total=0;for(int c:h.asignadosPed)total+=c;ok(total==5,"cinco asignados");
  h.elegirColaPed(tanda[0]);total=0;for(int c:h.asignadosPed)total+=c;ok(total==5,"re-elegir no duplica el conteo");
  h.clock=1;tanda[1].tEntradaColaPed=1;h.entraColaPed(tanda[1]);total=0;for(int c:h.asignadosPed)total+=c;ok(total==5,"en la fila sigue contando");
  // Con 40 asignados en el molinete mas cercano, el siguiente va a otro aunque quede a 10 m.
  for(int i=0;i<40;i++){Pasajero x=new Pasajero();x.y=360;x.servicioAsignadoPed=2.4;h.asignadosPed[13]++;}
  Pasajero otro=new Pasajero();otro.y=360;otro.servicioAsignadoPed=2.4;ok(h.elegirColaPed(otro)!=h.molinetesPeatonales.colas.get(13),"no se suma a una fila de 40");
  h.liberaAsignacionPed(tanda[0]);h.liberaAsignacionPed(tanda[0]);ok(tanda[0].colaElegidaPed==-1,"liberar dos veces es inocuo");
  h.clock=5;tanda[1].nombreMolinetePed="molinetePed10";int antes=0;for(int c:h.asignadosPed)antes+=c;h.comienzaServicioPed(tanda[1]);int despues=0;for(int c:h.asignadosPed)despues+=c;ok(despues==antes-1,"al empezar a validar se libera");}
 // Demo: corte de metricas en horizonteMetricasPedSeg y semilla efectiva semillaPed.
 m.inicioPicoPedSeg=0;m.finPicoPedSeg=10;m.inicializarPed();
 eq(m.horizonteCortePed,600,"corte demo");ok(m.rng.seed==20260923L,"semilla efectiva");
 Pasajero p=new Pasajero();m.clock=2;m.registraIngresoPed(p);p.tEntradaColaPed=m.time();m.entraColaPed(p);
 eq(p.servicioAsignadoPed,3,"servicio demo asignado");
 ok(m.hallPed()==0 && m.hallMaxPed==1,"transito: al entrar a la cola deja el hall");
 m.clock=5;p.nombreMolinetePed="molinetePed01";m.comienzaServicioPed(p);
 ok(m.pagaPed()==1 && m.pagaMaxPed==1,"transito: validando cuenta en zona paga");
 SubtePedLogicCheck dir=new SubtePedLogicCheck();dir.inicializarPed();Pasajero sinCola=new Pasajero();dir.registraIngresoPed(sinCola);
 ok(dir.hallPed()==1,"transito: recien ingresado esta en el hall");sinCola.nombreMolinetePed="molinetePed02";dir.comienzaServicioPed(sinCola);
 ok(dir.hallPed()==0 && dir.pagaPed()==1 && dir.nEsperandoPed==0,"transito: servicio inmediato sin cola");
 // Quien pasa directo sin hacer cola espera 0, aunque haya tardado en caminar desde el acceso.
 {SubtePedLogicCheck w=new SubtePedLogicCheck();w.inicializarPed();Pasajero directo=new Pasajero();w.clock=10;w.registraIngresoPed(directo);directo.tEntradaColaPed=10;
  w.clock=42;directo.nombreMolinetePed="molinetePed03";w.comienzaServicioPed(directo);
  ok(w.nEsperasPed==1 && w.esperaMaxPed==0 && w.nMas30Ped==0,"sin cola la espera es 0, no la caminata: "+w.esperaMaxPed);}dir.salePed();ok(dir.pagaPed()==0,"transito: sale de la zona paga");
 ok(dir.segundosRealesPed()>=0 && dir.inicioRealMsPed>0,"tiempo real medido desde la inicializacion");
 ok(dir.intervaloProgresoPed()==300 && franja(20,0.001).intervaloProgresoPed()==900,"progreso cada 5 min (demo) o 15 min (franja)");
 m.clock=8;m.terminaServicioPed(p);
 ok(m.nEsperandoPed==0 && m.nEsperasPed==1 && Math.abs(m.esperaMediaPed()-3)<1e-9,"espera");
 ok(m.percentil90Ped()==3 && m.proporcionMas30Ped()==0 && m.esperasPicoPed.size()==1 && m.p90PicoPed()==3,"P90 y cohorte");
 eq(m.utilizacionMediaPed(),3.0/(600*20),"utilizacion");
 ok(m.utilizacionPorMolinetePed().contains("molinetePed01=0.005"),"utilizacion por puesto");
 m.nProcesadosHorizontePed=1;
 ok(m.filaResultadoPed().startsWith("E0;20260923;1;0;1;"),"fila");
 ok(m.filaResultadoPed().split(";").length==20,"20 campos (17 + dia SBASE, P90 de transito del Roca y CV entre molinetes)");
 {String[] c=m.filaResultadoPed().split(";");ok(c[17].equals("-1") && c[18].equals("0.000000") && Math.abs(Double.parseDouble(c[19])-Math.sqrt(19))<1e-5,"demo: dia -1, transito 0, CV de 1 validacion en 20 molinetes = raiz(19): "+m.filaResultadoPed());}
 Pasajero tarde=new Pasajero();tarde.nombreMolinetePed="molinetePed01";tarde.tInicioServicioPed=599;
 m.clock=605;m.terminaServicioPed(tarde);
 eq(m.ocupacionPorMolinetePed.get("molinetePed01"),4,"ocupacion recortada al corte");
 // Demo completa: seis tandas, cierre de arribos, drenaje y prefijo DEMO sin finalizar el motor.
 SubtePedLogicCheck d=new SubtePedLogicCheck();d.inicializarPed();
 for(int k=0;k<6;k++){d.clock=30*k;d.generarTandaPed();}
 ok(d.arribosCerradosPed && d.nTandasPed==6 && d.nInyectadosPed==480 && d.pedSource.injected==480 && d.nDesdeRocaPed==480,"demo 6x80");
 d.clock=700;d.generarTandaPed();ok(d.nInyectadosPed==480,"sin arribos despues del cierre");
 for(int k=0;k<480;k++){Pasajero x=new Pasajero();d.registraIngresoPed(x);}
 for(int k=0;k<479;k++)d.salePed();
 ok(!d.resultadoEmitidoPed,"no emite antes de drenar");
 d.salePed();ok(d.resultadoEmitidoPed && !d.engine.finished,"demo emite al drenar");
 ok(d.trazas.get(d.trazas.size()-1).startsWith("CSV_PEATONAL_DEMO;E0;20260923;480;0;"),"prefijo demo");
 d.emitirIncompletoPed();ok(!d.trazas.get(d.trazas.size()-1).startsWith("CSV_PEATONAL_INCOMPLETO"),"sin fila incompleta tras emitir");
 // Franja: sin datos calibrados se bloquea.
 SubtePedLogicCheck sd=new SubtePedLogicCheck();sd.modoFranjaPed=true;
 try{sd.inicializarPed();throw new AssertionError("Franja sin calibrar aceptada");}catch(IllegalArgumentException expected){}
 sd.emitirIncompletoPed();ok(sd.trazas.isEmpty() && !sd.resultadoEmitidoPed,"sin fila incompleta si la inicializacion fallo");
 // Franja con entradas de prueba: horario oficial del Roca, descarga pareja, calle Poisson y servicio triangular.
 SubtePedLogicCheck f=franja(20,1.0), f1=franja(28,1.0);
 eq(f.horizonteCortePed,9000,"corte franja");
 int trenes=0;for(double t:f.llegadasRocaSeg)if(t+60>=0&&t+60<9000)trenes++;
 ok(f.nTrenesPed==trenes && trenes>=45,"trenes del horario dentro de la franja: "+f.nTrenesPed);
 ok(f.arribosCerradosPed && f.rocaCerradoPed && f.calleCerradaPed,"arribos cerrados al agotar horario y calle");
 ok(f.nInyectadosPed==f.nDesdeRocaPed+f.nDesdeCallePed && f.pedSource.injected==f.nDesdeRocaPed && f.pedSourceCalle.injected==f.nDesdeCallePed,"origenes");
 double total=0;for(double v:f.perfilPed15min)total+=v;
 ok(Math.abs(f.nDesdeRocaPed-0.8*total)<=1,"Roca = 80% del perfil SBASE (acumulacion por ramal reescalada al total): "+f.nDesdeRocaPed);
 ok(Math.abs(f.nDesdeCallePed-0.2*total)<5*Math.sqrt(0.2*total),"calle ~20% del perfil SBASE: "+f.nDesdeCallePed);
 // Puertas: 21 por tren, todas sobre el andén (X -2420 a -830) y distintas; Y a 0,8 m del borde de cada andén.
 java.util.HashSet<Double> xs=new java.util.HashSet<Double>();for(int k=0;k<21;k++){double x=f.xPuertaPed(k);ok(x<-830&&x>-2420,"puerta en el anden: "+x);xs.add(x);}
 ok(xs.size()==21 && Math.abs(f.xPuertaPed(0)+868.33)<0.01 && Math.abs(f.xPuertaPed(20)+2401.67)<0.01,"21 puertas de -868 a -2402");
 ok(f.yPuertaPed(0)==354 && f.yPuertaPed(6)==1316,"descenso junto al borde del anden");
 double ultimo=0;for(String e:f.eventos){String[] x=e.split(";");ultimo=Math.max(ultimo,Double.parseDouble(x[0])+(Integer.parseInt(x[1])+Integer.parseInt(x[2])>0?0:-1e9));}
 ok(ultimo<9000,"ningun ingreso a partir de las 09:30: "+ultimo);
 ok(f.eventos.equals(f1.eventos),"E0 y E1 reciben exactamente los mismos ingresos (numeros aleatorios comunes)");
 double suma=0;int n=4000;java.util.ArrayList<Double> s0=new java.util.ArrayList<Double>(),s1=new java.util.ArrayList<Double>();
 for(int k=0;k<n;k++){Pasajero x=new Pasajero(),y=new Pasajero();f.registraIngresoPed(x);f1.registraIngresoPed(y);s0.add(x.servicioAsignadoPed);s1.add(y.servicioAsignadoPed);suma+=x.servicioAsignadoPed;ok(x.servicioAsignadoPed>=2&&x.servicioAsignadoPed<=5,"servicio en [2,5]");}
 ok(s0.equals(s1),"E0 y E1 sortean los mismos tiempos de servicio");
 ok(Math.abs(suma/n-10.0/3)<0.05,"media triangular (2+3+5)/3: "+suma/n);
 SubtePedLogicCheck cte=new SubtePedLogicCheck();cte.modoFranjaPed=true;cte.proporcionRocaPed=1;cte.demoraAccesoRocaSeg=0;cte.duracionDescargaSeg=60;cte.servicioPedSeg=3;cte.inicializarPed();
 ok(cte.tiempoServicioPed()==3,"servicio constante sin minimo ni maximo");
 cte.servicioMinPedSeg=4;cte.servicioMaxPedSeg=5;
 try{cte.inicializarPed();throw new AssertionError("Triangular invalido aceptado");}catch(IllegalArgumentException expected){}
 SubtePedLogicCheck soloRoca=franja(20,1.0);ok(soloRoca.eventos.equals(f.eventos),"la demanda es reproducible con la misma semilla");
 ok(f.caudalPorVentanaPed().contains("08:15 sim=0 obs=2214"),"control de caudal por ventana: "+f.caudalPorVentanaPed());
 // Corrida chica de punta a punta: drenaje, cohorte pico, archivo de salida y fin del motor.
 SubtePedLogicCheck g=franja(20,0.01);
 java.io.File salida=java.io.File.createTempFile("corridas",".csv");salida.delete();g.archivoSalidaPed=salida.getPath();
 int ng=g.nInyectadosPed;ok(ng>100,"corrida chica: "+ng);
 Pasajero[] q=new Pasajero[ng];for(int k=0;k<ng;k++){q[k]=new Pasajero();g.clock=4600;g.registraIngresoPed(q[k]);}
 ok(q[0].enPicoPed,"cohorte pico por instante de ingreso");
 for(int k=0;k<ng-1;k++)g.salePed();
 g.clock=9000;g.actualizarAreaColaPed();g.nProcesadosHorizontePed=g.nProcesadosPed;ok(!g.drenadoPed(),"pendiente al cierre");
 g.clock=9050;g.salePed();
 ok(g.resultadoEmitidoPed && g.engine.finished,"franja emite y finaliza al drenar");
 g.pruebaSinteticaPed=true;ok(g.prefijoResultadoPed().equals("CSV_PEATONAL_DEMO"),"prueba sintetica de franja sale como demo");g.pruebaSinteticaPed=false;
 java.util.List<String> lineas=java.nio.file.Files.readAllLines(salida.toPath());
 ok(lineas.size()==1 && lineas.get(0).startsWith("CSV_PEATONAL;E0;20260923;"+ng+";0;"+(ng-1)+";"+ng+";"),"archivo de salida: "+lineas);
 eq(g.ultimaDisipacionPed,9050-g.tiempoUltimaTandaPed,"disipacion desde el ultimo ingreso");
 // Conservacion y corrida incompleta.
 ok(g.trazas.stream().anyMatch(t->t.contains("enTransitoHallMax=") && t.contains("segundosReales=")),"el resumen informa transito y tiempo real");
 SubtePedLogicCheck h=new SubtePedLogicCheck();h.inicializarPed();h.nInyectadosPed=2;h.nGeneradosPed=1;h.nProcesadosPed=2;
 try{h.emitirResultadoPed();throw new AssertionError("Conservacion violada aceptada");}catch(IllegalStateException expected){}
 h.emitirIncompletoPed();ok(h.trazas.get(h.trazas.size()-1).startsWith("CSV_PEATONAL_INCOMPLETO;E0;"),"fila incompleta");
 ok(h.trazas.get(h.trazas.size()-2).contains("enTransitoHallMax="),"la corrida incompleta tambien imprime el resumen");
 // Cierre por atasco: 15 min sin salidas pasada la franja, con pocos trabados, emite la fila normal y los excluye.
 SubtePedLogicCheck at=new SubtePedLogicCheck();at.inicializarPed();at.modoFranjaPed=true;at.pruebaSinteticaPed=false;at.arribosCerradosPed=true;
 at.horizonteCortePed=9000;at.nInyectadosPed=1000;at.nGeneradosPed=1000;at.nProcesadosPed=990;at.tiempoUltimaTandaPed=8900;at.nProcesadosPed=980;
 at.clock=8100;at.controlAtascoPed();at.nProcesadosPed=990;at.clock=9000;at.controlAtascoPed();ok(!at.resultadoEmitidoPed,"no cierra en el primer control");
 at.nProcesadosPed=995;at.clock=9900;at.controlAtascoPed();ok(!at.resultadoEmitidoPed,"no cierra si hubo salidas");
 at.clock=10800;at.controlAtascoPed();ok(at.resultadoEmitidoPed && at.nAtascadosPed==5 && at.engine.finished,"cierra con 5 atascados");
 ok(at.trazas.stream().anyMatch(t->t.startsWith("CSV_PEATONAL;")) && at.trazas.stream().anyMatch(t->t.startsWith("ATASCADOS: 5")),"fila normal y aviso");
 ok(at.filaVentanasPed().endsWith(";5"),"ventanas informan los atascados");
 SubtePedLogicCheck mu=new SubtePedLogicCheck();mu.inicializarPed();mu.modoFranjaPed=true;mu.arribosCerradosPed=true;mu.horizonteCortePed=9000;
 mu.nInyectadosPed=1000;mu.nGeneradosPed=1000;mu.nProcesadosPed=900;mu.clock=9000;mu.controlAtascoPed();mu.clock=9900;mu.controlAtascoPed();
 ok(!mu.resultadoEmitidoPed,"con muchos trabados no se cierra: queda incompleta");
 SubtePedLogicCheck lbl=new SubtePedLogicCheck();lbl.molinetesOperativosPed=22;ok(lbl.filaResultadoPed().startsWith("E1;"),"22 molinetes = E1");
 lbl.molinetesOperativosPed=28;ok(lbl.filaResultadoPed().startsWith("E1B;"),"28 molinetes = ampliacion E1B");
 salida.delete();new java.io.File(salida.getPath().replaceFirst("(\\\\.csv)?$","_ventanas.csv")).delete();
 // --- 2026-11-04: dia SBASE (bootstrap), trenes con atraso y carga Poisson, escenarios E3/E13 y metricas nuevas ---
 {SubtePedLogicCheck base=franja(20,1.0);ok(base.perfilEfectivoPed==base.perfilPed15min && base.diaEfectivoPed==-1,"diaSbasePed=-1 usa el perfil medio");}
 ok(new SubtePedLogicCheck().perfilesDiasPed.length>=60,"perfilesDiasPed embebido (datos/embeber_dias_sbase.py)");
 SubtePedLogicCheck b0=franjaVar(20,2.4,1.8,3.5), b1=franjaVar(22,2.4,1.8,3.5), b3=franjaVar(20,1.8,1.5,2.5), b13=franjaVar(22,1.8,1.5,2.5);
 ok(b0.diaEfectivoPed>=0 && b0.diaEfectivoPed<b0.perfilesDiasPed.length && b0.perfilEfectivoPed==b0.perfilesDiasPed[b0.diaEfectivoPed],"dia sorteado en rango");
 ok(b0.diaEfectivoPed==b1.diaEfectivoPed && b0.diaEfectivoPed==b3.diaEfectivoPed && b0.diaEfectivoPed==b13.diaEfectivoPed,"los 4 escenarios del par usan el mismo dia");
 ok(b0.eventos.equals(b1.eventos) && b0.eventos.equals(b3.eventos) && b0.eventos.equals(b13.eventos),"E0, E1, E3 y E13 reciben los mismos ingresos con atraso y Poisson (numeros aleatorios comunes)");
 ok(!b0.eventos.equals(franja(20,1.0).eventos),"el dia sorteado, el atraso y la Poisson cambian la demanda");
 ok(b0.escenarioPed().equals("E0") && b1.escenarioPed().equals("E1") && b3.escenarioPed().equals("E3") && b13.escenarioPed().equals("E13"),"etiquetas E0, E1, E3, E13");
 {java.util.HashSet<Integer> dias=new java.util.HashSet<Integer>();for(int k=0;k<30;k++){SubtePedLogicCheck x=new SubtePedLogicCheck();x.modoFranjaPed=true;x.proporcionRocaPed=0.8;x.demoraAccesoRocaSeg=10;x.duracionDescargaSeg=30;x.servicioPedSeg=2.4;x.diaSbasePed=-2;x.semillaPed=20260923L+k;x.inicializarPed();dias.add(x.diaEfectivoPed);}
  ok(dias.size()>=18,"30 semillas sortean dias distintos (con reposicion): "+dias.size());}
 {SubtePedLogicCheck x=new SubtePedLogicCheck();x.modoFranjaPed=true;x.proporcionRocaPed=0.8;x.demoraAccesoRocaSeg=10;x.duracionDescargaSeg=30;x.servicioPedSeg=2.4;x.diaSbasePed=3;x.inicializarPed();
  ok(x.diaEfectivoPed==3 && x.perfilEfectivoPed==x.perfilesDiasPed[3],"dia fijo");
  x.diaSbasePed=x.perfilesDiasPed.length;try{x.inicializarPed();throw new AssertionError("dia fuera de rango aceptado");}catch(IllegalArgumentException expected){}
  x.diaSbasePed=-3;try{x.inicializarPed();throw new AssertionError("diaSbasePed=-3 aceptado");}catch(IllegalArgumentException expected){}
  x.diaSbasePed=-1;x.atrasoMaxRocaSeg=-1;try{x.inicializarPed();throw new AssertionError("atraso negativo aceptado");}catch(IllegalArgumentException expected){}}
 // La demanda total del Roca sigue al perfil del dia (80 %): la Poisson y el atraso no la sesgan.
 {double totDia=0;for(double v:b0.perfilEfectivoPed)totDia+=v;ok(Math.abs(b0.nDesdeRocaPed-0.8*totDia)<0.05*0.8*totDia,"Roca ~80% del dia sorteado: "+b0.nDesdeRocaPed+" vs "+0.8*totDia);}
 {SubtePedLogicCheck x=new SubtePedLogicCheck();x.rngTrenesPed.setSeed(7);int N=20000;double su=0,s2=0;for(int k=0;k<N;k++){int v=x.poissonTrenPed(40.0);su+=v;s2+=v*(double)v;}
  double med=su/N,var=s2/N-med*med;ok(Math.abs(med-40)<0.3 && Math.abs(var-40)<4,"Poisson(40): media "+med+" varianza "+var);
  ok(x.poissonTrenPed(0)==0 && x.poissonTrenPed(-1)==0,"Poisson con media <= 0 es 0");
  int grande=x.poissonTrenPed(900);ok(grande>780 && grande<1020,"Poisson(900) sin desborde: "+grande);}
 // Atraso: ningun tren antes de su horario, ninguno con mas de atrasoMaxRocaSeg.
 {SubtePedLogicCheck x=franjaVar(20,2.4,1.8,3.5);java.util.ArrayList<double[]> t=new java.util.ArrayList<double[]>(x.trenesRocaPed);
  ok(t.size()==x.nTrenesPed && t.size()>=45,"un tren animado por tren del horario: "+t.size());}
 // Transito del Roca y CV entre molinetes.
 {SubtePedLogicCheck x=new SubtePedLogicCheck();x.inicializarPed();Pasajero pr=new Pasajero();x.clock=0;x.registraIngresoPed(pr);x.clock=100;pr.tEntradaColaPed=100;x.entraColaPed(pr);
  x.clock=130;pr.nombreMolinetePed="molinetePed01";x.comienzaServicioPed(pr);eq(x.p90TransitoRocaPed(),100,"transito del Roca hasta la cola");
  Pasajero calle=new Pasajero();calle.desdeRocaPed=false;x.clock=140;x.registraIngresoPed(calle);x.clock=150;calle.nombreMolinetePed="molinetePed02";x.comienzaServicioPed(calle);
  ok(x.transitosRocaPed.size()==1,"la calle no cuenta en el transito del Roca");
  x.molinetesOperativosPed=2;eq(x.cvValidacionesMolinetePed(),0,"dos molinetes con una validacion cada uno: CV 0");
  x.molinetesOperativosPed=4;eq(x.cvValidacionesMolinetePed(),1,"1,1,0,0: CV 1");}

 // Llegadas reales del dia (Trenes Argentinos): los trenes son los de ese dia, iguales en los 4 escenarios, y nunca
 // dos trenes en la misma via a la vez (en ninguno de los dias embebidos).
 {SubtePedLogicCheck r0=franjaReal(20,2.4,1.8,3.5,-2), r13=franjaReal(22,1.8,1.5,2.5,-2);
  int esperados=0;for(double t:r0.llegadasDiasPed[r0.diaEfectivoPed])if(t+10>=0&&t+10<9000)esperados++;
  ok(r0.nTrenesPed==esperados && esperados>=40,"trenes reales del dia "+r0.diaEfectivoPed+": "+r0.nTrenesPed+" de "+esperados);
  ok(r0.eventos.equals(r13.eventos),"E0 y E13 reciben los mismos ingresos con llegadas reales");
  ok(r0.llegadasDiasPed.length==r0.perfilesDiasPed.length && r0.ramalesDiasPed.length==r0.perfilesDiasPed.length,"llegadas alineadas con los dias");
  double totDia=0;for(double v:r0.perfilEfectivoPed)totDia+=v;ok(Math.abs(r0.nDesdeRocaPed-0.8*totDia)<0.05*0.8*totDia,"Roca ~80% del dia con llegadas reales: "+r0.nDesdeRocaPed);}
 for(int dd=0;dd<new SubtePedLogicCheck().perfilesDiasPed.length;dd++){SubtePedLogicCheck r=franjaReal(20,2.4,1.8,3.5,dd);
  ok(r.trazas.stream().noneMatch(t->t.startsWith("ADVERTENCIA: tren")),"dia "+dd+": un tren en una via ocupada");
  double tot=0;for(double v:r.perfilEfectivoPed)tot+=v;
  // Poisson: el total del dia es Poisson(0,8 x total) salvo el redondeo: dentro de 4 desvios.
  ok(Math.abs(r.nDesdeRocaPed-0.8*tot)<4*Math.sqrt(0.8*tot)+1,"dia "+dd+": Roca "+r.nDesdeRocaPed+" vs 80% = "+0.8*tot);}
 // Sin Poisson, el total del Roca coincide con el dato en todos los dias (a menos del redondeo por ramal).
 for(int dd=0;dd<new SubtePedLogicCheck().perfilesDiasPed.length;dd++){SubtePedLogicCheck r=new SubtePedLogicCheck();r.modoFranjaPed=true;r.proporcionRocaPed=0.8;r.demoraAccesoRocaSeg=10;r.duracionDescargaSeg=30;r.servicioPedSeg=2.4;r.diaSbasePed=dd;r.llegadasRealesPed=true;r.inicializarPed();r.programarDemandaFranjaPed();r.correrDemanda();
  double tot=0;for(double v:r.perfilEfectivoPed)tot+=v;ok(Math.abs(r.nDesdeRocaPed-0.8*tot)<=6,"dia "+dd+" sin Poisson: Roca "+r.nDesdeRocaPed+" vs "+0.8*tot);}
 // Numeros comunes en la validacion: el mismo uniforme por pasajero en los 4 escenarios (inversa triangular monotona):
 // E0 = E1 y E3 = E13 valor a valor, y E0 y E3 con el mismo orden entre pasajeros.
 {double[][] sv=new double[4][3000];SubtePedLogicCheck[] es={b0,b1,b3,b13};
  for(int e=0;e<4;e++)for(int k=0;k<3000;k++){Pasajero x=new Pasajero();es[e].registraIngresoPed(x);sv[e][k]=x.servicioAsignadoPed;}
  ok(java.util.Arrays.equals(sv[0],sv[1]) && java.util.Arrays.equals(sv[2],sv[3]),"E0=E1 y E3=E13 en el servicio pasajero a pasajero");
  boolean mismoOrden=true;for(int k=1;k<3000;k++)if(Double.compare(sv[0][k],sv[0][k-1])!=Double.compare(sv[2][k],sv[2][k-1]))mismoOrden=false;
  ok(mismoOrden,"E0 y E3 reciben el mismo uniforme por pasajero (mismo orden de servicios)");
  double m3=0;for(double v:sv[2])m3+=v;ok(Math.abs(m3/3000-(1.5+1.8+2.5)/3)<0.03,"media triangular E3 (1,5+1,8+2,5)/3: "+m3/3000);}
 ok(franja(20,1.0).trazas.stream().noneMatch(t->t.startsWith("ADVERTENCIA: tren")),"horario oficial: via j % 7 siempre libre");
 ok(b3.filaVentanasPed().split(";").length==24 && b3.filaVentanasPed().endsWith(";0") && b3.filaVentanasPed().startsWith("E3;20260923;"+b3.diaEfectivoPed+";"),"fila de ventanas: "+b3.filaVentanasPed());

 {SubtePedLogicCheck tv=franjaReal(20,2.4,1.8,3.5,-2);tv.clock=4500;for(java.lang.reflect.Method mt:SubtePedLogicCheck.class.getDeclaredMethods())if(mt.getName().startsWith("_texto")){Object v=mt.invoke(tv);ok(v!=null&&!v.toString().isEmpty(),mt.getName());}}
 System.out.println("OK: pedestrian demo, Roca timetable + street demand, triangular service, common random numbers, 09:30 cut, drain and CSV output");
}
}'''
(d/'SubtePedLogicCheck.java').write_text(ped_check)
subprocess.run([javac,str(d/'SubtePedLogicCheck.java')],check=True)
subprocess.run(['/Applications/AnyLogic 8 PLE.app/Contents/jre/bin/java','-cp',str(d),'SubtePedLogicCheck'],check=True)
# Compile the real AnyLogic API call used to suspend the last eight physical service points.
ped_api='''import com.anylogic.engine.*;
import com.anylogic.engine.markup.*;
public class SubtePedApiCheck extends Agent {
 ServiceWLine<ServiceLine> services;
 ServiceLine point;
 void configure(){ services.setServiceSuspended(point, true); point.getName(); }
 double choose(){ QueuePath q=services.getQueues().get(0); return q.getEndPoint().y + services.queueSize(q); }
 void seedAndFinish(long semilla){ getDefaultRandomGenerator().setSeed(semilla); getEngine().finish(); }
}'''
(d/'SubtePedApiCheck.java').write_text(ped_api)
subprocess.run([javac,'-cp',':'.join(map(str,jars)),str(d/'SubtePedApiCheck.java')],check=True)
# Parameter-variation entries reference parameter Ids; every other Id must be unique.
references={id(x) for tag in ('FreeformParamValue','RangeVariationParamValue') for v in r.iter(tag) for x in v.findall('Id')}
# AnyLogic 8.9.10 escribe <Id>0</Id> en cada DatasetExpression de un gráfico: no es un identificador de elemento.
references|={id(x) for v in r.iter('DatasetExpression') for x in v.findall('Id') if (x.text or '').strip()=='0'}
ids=[(x.text or '').strip() for x in r.iter('Id') if id(x) not in references];assert len(ids)==len(set(ids)), 'Duplicate IDs'
return_modifiers={x.text for x in r.iter('ReturnModificator')}
assert return_modifiers <= {'VOID','RETURNS_VALUE'}, f'Invalid function return modifier: {return_modifiers}'
assert len(a.findall('EmbeddedObjects/EmbeddedObject'))==7
experiments=r.findall('Model/Experiments/SimulationExperiment')
for e in [x for x in experiments if x.findtext('Name') in {'E0','E1','E2','E3'}]:
 ps={p.findtext('ParameterName'):p.findtext('ParameterValue/Code') for p in e.findall('Parameters/Parameter')}
 assert ps['escenario']==e.findtext('Name')[1:]
agents={x.findtext('Name'):x for x in r.findall('Model/ActiveObjectClasses/ActiveObjectClass')}
ped=agents['MainPeatonal']
main=agents['Main']
assert main.findtext('CurrentLevel')=='1783514567443'
main_level=main.find('Presentation/Level')
assert main_level is not None and main_level.findtext('Id')=='1783514567443'
assert main_level.find("Presentation/Rectangle[Name='panelTablero']") is not None
for section in ('Variables','Functions','Events'):
 technical=a.findall(f'{section}/*')
 assert all(x.findtext('PresentationFlag')=='false' for x in technical)
 assert all(int(x.findtext('X'))>=1100 for x in technical)
# MainPeatonal en 4 bloques (consigna del docente, 2026-11-04): arriba 1 Variables, 2 Medidas, 3 Lógica; abajo
# 4 Modelo espacial. Ningún elemento técnico invisible en la corrida queda sobre la animación (Y < -120) y cada uno
# cae dentro del recuadro de su bloque.
_lvv=next(l for l in ped.find('Presentation') if l.findtext('Name')=='nivelVestibulo')
_bl={x.findtext('Name'):tuple(float(x.findtext(k)) for k in ('X','Y','Width','Height')) for x in _lvv.findall('Presentation/Rectangle') if (x.findtext('Name') or '') in ('bloque1','bloque2','bloque3','bloque4')}
assert set(_bl)=={'bloque1','bloque2','bloque3','bloque4'}
_dentro=lambda b,x,y: b[0]<=x<=b[0]+b[2] and b[1]<=y<=b[1]+b[3]
for section in ('Variables','Functions','Events','EmbeddedObjects'):
 for x in ped.findall(f'{section}/*'):
  if section!='EmbeddedObjects': assert x.findtext('PresentationFlag')=='false', x.findtext('Name')
  xx,yy=float(x.findtext('X')),float(x.findtext('Y'))
  assert yy<-120 and any(_dentro(_bl[b],xx,yy) for b in ('bloque1','bloque2','bloque3')), (x.findtext('Name'),xx,yy)
for n in ('molinetesOperativosPed','servicioPedSeg','diaSbasePed','proporcionRocaPed'):
 v=ped.find(f"Variables/Variable[Name='{n}']"); assert _dentro(_bl['bloque1'],float(v.findtext('X')),float(v.findtext('Y'))), n
for n in ('percentil90Ped','proporcionMas30Ped','p90PicoPed'):
 v=ped.find(f"Functions/Function[Name='{n}']"); assert _dentro(_bl['bloque2'],float(v.findtext('X')),float(v.findtext('Y'))), n
for n in ('pedSource','bajadaHall','pedMolinetes','trenesRocaFuente'):
 v=ped.find(f"EmbeddedObjects/EmbeddedObject[Name='{n}']"); assert _dentro(_bl['bloque3'],float(v.findtext('X')),float(v.findtext('Y'))), n
assert _bl['bloque4'][1]<0 and _bl['bloque4'][1]+_bl['bloque4'][3]>=1700, 'el bloque 4 enmarca la animación'
ped_defaults_early={v.findtext('Name'):v.findtext('Properties/DefaultValue/Code') for v in ped.findall("Variables/Variable[@Class='Parameter']")}
ped_blocks={x.findtext('Name'):x.findtext('ActiveObjectClass/ClassName') for x in ped.findall('EmbeddedObjects/EmbeddedObject')}
assert ped_blocks=={'pedSettings':'PedSettings','pedSource':'PedSource','bajadaHall':'PedChangeLevel','pedSourceCalle':'PedSource','pedMolinetes':'PedService','pedSalida':'PedGoTo','pedSink':'PedSink',
 # Trenes del Roca (sólo animación, Rail Library): fuente, avance al andén, descarga y fin.
 'trenesRocaFuente':'TrainSource','trenesRocaAlAnden':'TrainMoveTo','trenesRocaDescarga':'Delay','trenesRocaFin':'TrainDispose'}
assert all(ped.find(f".//RailTrack[Name='viaRoca{k}']") is not None and ped.find(f".//RailStopline[Name='paradaRoca{k}']") is not None for k in range(7))
assert {('trenesRocaFuente','trenesRocaAlAnden'),('trenesRocaAlAnden','trenesRocaDescarga'),('trenesRocaDescarga','trenesRocaFin')} <= {(c.findtext('SourceEmbeddedObjectReference/ItemName'),c.findtext('TargetEmbeddedObjectReference/ItemName')) for c in ped.findall('Connectors/Connector')}
# Permanencia del tren en el andén (sólo animación): 10 min como mínimo, menos que los 17 min entre dos trenes de la misma
# vía (j % 7 sobre el horario). Con 50 s, a 30x el tren se veía 2 s.
_dw=[e for e in ped.findall('.//EmbeddedObject') if e.findtext('Name')=='trenesRocaDescarga'][0]
assert [q.findtext('Value/Code') for q in _dw.findall('Parameters/Parameter') if q.findtext('Name')=='delayTime']==['Math.max(demoraAccesoRocaSeg + duracionDescargaSeg + 10, 600)']
import csv as _c
_t=[float(x['segundos_desde_07']) for x in _c.DictReader(open(p.parent/'datos'/'arribos_roca_constitucion_habiles.csv',encoding='utf-8'),delimiter=';')]
assert min(b-a for a,b in zip(_t,_t[7:])) > 600+120+20, 'un tren llegaría a una vía todavía ocupada (10 min detenido + atraso de hasta 120 s)'
assert {x.findtext('Name') for x in r.findall('Model/ActiveObjectClasses/ActiveObjectClass')} >= {'TrenRoca','CocheRoca'}
# Plano en 3D (datos/plano_3d.py): grupo plano3D de MainPeatonal, sólo 3D, rectángulos sin rotación; vías hundidas 1,1 m.
plano3d=ped.find(".//Group[Name='plano3D']")
assert plano3d is not None and plano3d.findtext('DrawMode')=='SHAPE_DRAW_3D'
figs3d=list(plano3d.find('Presentation'))
assert 500<=len(figs3d)<=1500 and all(f.tag=='Rectangle' and f.findtext('DrawMode')=='SHAPE_DRAW_3D' and f.findtext('Rotation')=='0.0' for f in figs3d)
assert all(ped.find(f".//RailTrack[Name='viaRoca{k}']").findtext('Z')=='-11' for k in range(7))
ids_3d=[plano3d.findtext('Id')]+[f.findtext('Id') for f in figs3d]
ids_resto=collections.Counter(x.text for x in r.iter('Id'))
assert len(set(ids_3d))==len(ids_3d) and all(ids_resto[i]==1 for i in ids_3d), 'Id del plano 3D repetido'
def _caja(f): return tuple(float(f.findtext(k)) for k in ('X','Y','Width','Height'))
def _pisa(c, x0, y0, x1, y1): return c[0] < x1 and c[0]+c[2] > x0 and c[1] < y1 and c[1]+c[3] > y0
muros3d=[_caja(f) for f in figs3d if f.findtext('Name').startswith(('muro3D','bajo3D','escalera3D'))]
# Ningún muro del plano dentro del pasillo, del vestíbulo ni de la circulación libre del hall (frente a la boca B2).
for zona in ((-150,952,-22,996),(-18,340,28,996),(80,190,580,530),(-205,880,-160,1010),(-540,300,-420,1350)):
 assert not any(_pisa(c,*zona) for c in muros3d), zona
sources={x.findtext('Name'):{p.findtext('Name'):p.findtext('Value/Code') for p in x.findall('Parameters/Parameter')} for x in ped.findall('EmbeddedObjects/EmbeddedObject') if x.findtext('Name').startswith('pedSource')}
# Roca: cada pasajero aparece en la cabecera del andén de su tren (andenActualPed, asignado por turno).
# Roca (2026-11-02): cada pasajero baja por una de las 21 puertas de su tren (7 coches x 3 puertas por lado, CSR) y
# camina el andén; la puerta va por turno (sin números aleatorios) y el andén lo fija andenActualPed.
assert (sources['pedSource']['locationType'],sources['pedSource']['level'],sources['pedSource']['locationX'],sources['pedSource']['locationY'])==('self.LOCATION_POINT','nivelHall','xPuertaPed((nDesdeRocaPed - 1) % 21)','yPuertaPed(andenActualPed)')
# Calle: una boca, la escalera B3 de la calle Brasil (OSM), que aterriza en X ~ 194 desde el lado este.
assert sources['pedSourceCalle']['locationLine']=='entradaCalle'
# Accesos (2026-11-04): los andenes al norte del centro del bloque central (Y < 840) bajan por la escalera norte.
assert sources['pedSource']['onExit']=='ped.desdeRocaPed = true; ped.accesoNortePed = ped.getY() < 840; registraIngresoPed(ped);'
assert sources['pedSourceCalle']['onExit']=='ped.desdeRocaPed = false; registraIngresoPed(ped);'
# Velocidad con generador propio (numeros aleatorios comunes E0/E1); el generador por defecto lo consume la libreria.
assert all(sources[k]['comfortableSpeed']=='uniform(1.1, 1.5, rngVelocidadPed)' for k in ('pedSource','pedSourceCalle'))
conns={(c.findtext('SourceEmbeddedObjectReference/ItemName'),c.findtext('TargetEmbeddedObjectReference/ItemName')) for c in ped.findall('Connectors/Connector')}
assert {('pedSource','bajadaHall'),('bajadaHall','pedMolinetes'),('pedSourceCalle','pedMolinetes'),('pedMolinetes','pedSalida'),('pedSalida','pedSink')}<=conns and ('pedSource','pedMolinetes') not in conns
# Subsuelo (2026-11-02): hall del Roca a nivel de calle (nivelHall, Z 0) y pasillo + vestíbulo a -4,60 m (nivelVestibulo;
# plaza de transbordo a -4,60 m, GCBA 2015).
# Accesos reales (2026-11-04, reemplazan a la boca B2 inventada; 2026-11-09, sobre las escaleras mecánicas del plano):
# escaleras mecánicas norte y sur del bloque central del hall (capa ESCALERA del plano de Trenes Argentinos, X -386 a
# -278), cada una un área en pendiente de 10,5 m x 2,8 m con el tope al oeste (muesca del bloque central) y 4,6 m de
# desnivel a 0,30 m/s vertical, que desembocan en la plaza de transbordo del subsuelo (supuesta) y de ahí al pasillo.
niveles={lv.findtext('Name'):lv for lv in ped.iter('Level')}
# Mapa de calor (2026-11-09): un DensityMap por nivel (molde del ejemplo Subway Entrance Hall), máximo de la corrida.
for _nv,_dm in (('nivelHall','mapaCalorHall'),('nivelVestibulo','mapaCalorSubsuelo')):
 _m=next(l for l in ped.iter('Level') if l.findtext('Name')==_nv).find(f"Presentation/DensityMap[Name='{_dm}']")
 assert _m is not None and (_m.findtext('Type'),_m.findtext('TimePeriod'),_m.findtext('DisplayedValue'),_m.findtext('CriticalDensity'))==('PEDESTRIAN','COMPLETE','MAX','1.5'), _dm
assert set(niveles)=={'nivelHall','nivelVestibulo'} and niveles['nivelHall'].findtext('Z')=='0' and niveles['nivelVestibulo'].findtext('Z')=='-46'
en_nivel=lambda n: {c.findtext('Name') for c in niveles[n].find('Presentation')}
assert {f'bordeAndenRoca{k}' for k in range(7)}|{f'hallCabecera{k}' for k in range(6)}|{'bocaNorteHall','bocaSurHall','hallEstructuraCentral','hallVestuarioSOFSE','hallBoleteriasSOFSE','plano3D','viasRoca','planoConstitucion'} <= en_nivel('nivelHall')
assert {'escaleraNorte','escaleraSur','bocaNortePlaza','bocaSurPlaza','plazaTransbordo','pasilloRocaNorte','pasilloRocaSur','molinetesPeatonales','entradaCalle','salidaPeatonal'} <= en_nivel('nivelVestibulo')
# Equipamiento 3D del vestíbulo (datos/vestibulo_3d.py): molinetes en los 30 divisores, boletería, cabina, máquinas y
# coches de la Línea C; recursos registrados y listados en copiar_figuras_3d.py.
vest3d=niveles['nivelVestibulo'].find("Presentation/Group[Name='vestibulo3D']")
figs_v=list(vest3d.find('Presentation'))
assert vest3d.findtext('DrawMode')=='SHAPE_DRAW_3D' and all(f.tag=='Figure3D' and f.findtext('DrawMode')=='SHAPE_DRAW_3D' for f in figs_v)
usa={f.findtext('ResourceReference/ClassName') for f in figs_v}
assert sum(f.findtext('ResourceReference/ClassName')=='3d/turnstile_open.dae' for f in figs_v)==30
recursos={x.findtext('Path') for x in r.findall('Model/ModelResources/Resource')} if r.find('Model/ModelResources') is not None else {x.findtext('Path') for x in r.iter('Resource')}
assert usa <= recursos, usa-recursos
copia=open(Path(__file__).resolve().parent/'datos'/'copiar_figuras_3d.py',encoding='utf-8').read()
assert all(u.split('/')[-1] in copia for u in usa)
bajada={p.findtext('Name'):p.findtext('Value/Code') for p in ped.find("EmbeddedObjects/EmbeddedObject[Name='bajadaHall']").findall('Parameters/Parameter')}
assert bajada['exitLine']=='ped.accesoNortePed ? bocaNorteHall : bocaSurHall' and bajada['entryLine']=='ped.accesoNortePed ? bocaNortePlaza : bocaSurPlaza'
assert 'accesoNortePed' in {x.findtext('Name') for x in agents['Pasajero'].findall('Variables/Variable')}
def _linea(nivel, n):
 t=niveles[nivel].find(f"Presentation/TargetLine[Name='{n}']"); x,y=float(t.findtext('X')),float(t.findtext('Y'))
 return [(x+float(q.findtext('X')),y+float(q.findtext('Y'))) for q in t.findall('Points/Point')]
for nombre,y,boca_hall,boca_plaza in (('escaleraNorte','740','bocaNorteHall','bocaNortePlaza'),('escaleraSur','916','bocaSurHall','bocaSurPlaza')):
 esc=niveles['nivelVestibulo'].find(f"Presentation/RectangleNode[Name='{nombre}']")
 esc_p={q.findtext('Name'):q.findtext('Value/Code') for q in esc.findall('EmbeddedObject/Parameters/Parameter')}
 assert esc_p['speedRestricted']=='true' and abs(float(esc_p['maxSpeed'])-10.5/(4.6/0.30))<0.01 and esc.findtext('Sloped')=='true', nombre
 assert (esc.findtext('X'),esc.findtext('Y'),esc.findtext('Width'),esc.findtext('Height'),esc.findtext('Slope/Dx'),esc.findtext('Slope/Dy'),esc.findtext('Slope/Dz'))==('-385',y,'105','28','-105','0','46') and esc.findtext('Slope/X')=='105', nombre
 # La línea del subsuelo queda dentro de la escalera, a menos de 1 m de su tope (X -385, donde aparece quien baja).
 lp=_linea('nivelVestibulo',boca_plaza); assert abs(lp[1][1]-lp[0][1])>=25 and all(-385<x<=-375 and int(y)<yy<int(y)+28 for x,yy in lp), (boca_plaza,lp)
 # La línea del hall queda fuera del bloque central (muesca oeste en X -385) y a menos de 3 m del tope.
 lh=_linea('nivelHall',boca_hall); assert abs(lh[1][1]-lh[0][1])>=25 and all(-415<=x<=-390 and int(y)<yy<int(y)+28 for x,yy in lh), (boca_hall,lh)
# El horario embebido es exactamente el extraído de los PDFs oficiales del Roca.
import csv as _csv
horario=[r['segundos_desde_07'] for r in _csv.DictReader(open(p.parent/'datos'/'arribos_roca_constitucion_habiles.csv',encoding='utf-8'),delimiter=';')]
assert ped_defaults_early['llegadasRocaSeg']=='new double[] {'+','.join(horario)+'}', 'llegadasRocaSeg no coincide con datos/arribos_roca_constitucion_habiles.csv'
# Ramal de cada tren (mismo orden): la carga de cada tren es la demanda acumulada desde el tren anterior de su ramal.
_RAMALES=['La Plata','Bosques (vía Quilmes)','Bosques (vía Temperley)','Glew / A. Korn','Ezeiza / Cañuelas']
_ramales=[str(_RAMALES.index(r['ramal'])) for r in _csv.DictReader(open(p.parent/'datos'/'arribos_roca_constitucion_habiles.csv',encoding='utf-8'),delimiter=';')]
_ramal_var=next(v for v in ped.findall('Variables/Variable') if v.findtext('Name')=='ramalRocaPed')
assert _ramal_var.findtext('Properties/InitialValue/Code')=='new int[] {'+','.join(_ramales)+'}', 'ramalRocaPed no coincide con el ramal del horario oficial'
assert ped_defaults_early['factorDemandaPed']=='1.0'
assert agents['Pasajero'] is not None
assert any(e.findtext('Name')=='PeatonalDemo' and e.get('ActiveObjectClassId')==ped.findtext('Id') for e in experiments)
ped_experiments={e.findtext('Name'):e for e in experiments if e.findtext('Name') in {'PeatonalE0','PeatonalE1'}}
assert set(ped_experiments)=={'PeatonalE0','PeatonalE1'}
for name, expected in {'PeatonalE0':'20','PeatonalE1':'22'}.items():
 ps={p.findtext('ParameterName'):p.findtext('ParameterValue/Code') for p in ped_experiments[name].findall('Parameters/Parameter')}
 assert ps['molinetesOperativosPed']==expected
 assert ps['semillaPed']=='20260923L'
 assert ped_experiments[name].findtext('SeedValue')=='20260923'
 assert float(ped_experiments[name].findtext('ModelTimeProperties/FinalTime'))==900
callbacks_delay=next(x for x in ped.findall('EmbeddedObjects/EmbeddedObject') if x.findtext('Name')=='pedMolinetes').find("Parameters/Parameter[Name='delayTime']").findtext('Value/Code')
# Plano hipotético: 28 molinetes lineales orientados hacia la zona paga, una cola por molinete.
svc=ped.find(".//ServiceWithLine[Name='molinetesPeatonales']")
assert svc.findtext('Type')=='LINEAR'
gates=svc.findall('Presentation/ServiceLine'); queues=svc.findall('Presentation/QueueLine')
assert [g.findtext('Name') for g in gates]==[f'molinetePed{i:02d}' for i in range(1,29)]
assert [q.findtext('Name') for q in queues]==[f'colaMolinete{i:02d}' for i in range(1,29)]
assert not ped.findall('.//ServicePoint')
entry_x=-868   # puerta más adelantada del tren (xPuertaPed(0))
exit_x=float(ped.find(".//TargetLine[Name='salidaPeatonal']").findtext('X'))
for g,q in zip(gates,queues):
 gx,gy=float(g.findtext('X')),float(g.findtext('Y'))
 assert float(g.findtext('Dx'))>0 and float(g.findtext('Dy'))==0 and g.findtext('Bidirectional')=='false', 'el paso va del hall a la zona paga'
 pts=[(float(x.findtext('X')),float(x.findtext('Y'))) for x in q.find('Points')][::3]
 qx,qy=float(q.findtext('X')),float(q.findtext('Y'))
 # Convención del ejemplo oficial "Subway Entrance Hall" (fareGates y ticketMachines): el punto inicial
 # (0,0) es la cola y el último punto es la cabeza, con la flecha hacia el servicio y a 2 m de él.
 # La inversión del 2026-09-24 (cabeza en el punto inicial) era incorrecta.
 head=(qx+pts[-1][0],qy+pts[-1][1])
 assert entry_x < qx < head[0] < gx < gx+float(g.findtext('Dx')) < exit_x and abs(qy-gy)<1e-9 and 10 <= gx-head[0] <= 30, g.findtext('Name')
assert len(ped.findall('.//Wall'))>=40
# Pasillo del Roca (2026-11-02): L de 75 m x 5 m sobre el pasillo subterráneo de OSM, cerrado en el fondo, que
# desemboca en la boca oeste angostada a 5 m (Y 335-385). La llegada es el pie de la escalera de la boca del hall.
def _abs(nombre, paso=3):
 el=ped.find(f".//*[Name='{nombre}']"); X,Y=float(el.findtext('X')),float(el.findtext('Y'))
 pts=[(float(q.findtext('X')),float(q.findtext('Y'))) for q in el.iter('Point')][::paso]
 return [(X+x,Y+y) for x,y in pts]
assert _abs('pasilloRocaNorte')==[(-152,949),(-20,949),(-20,335),(80,335)]
# Plaza: el lado oeste (X -280) se abre en el pie de cada escalera mecánica y la encierra en un bolsillo.
assert _abs('plazaTransbordo')==[(-152,949),(-152,660),(-280,660),(-280,739),(-386,739),(-386,769),(-280,769),(-280,915),(-386,915),(-386,945),(-280,945),(-280,1010),(-152,1010),(-152,999)], _abs('plazaTransbordo')
assert _abs('pasilloRocaSur')==[(-152,999),(30,999),(30,385),(80,385)]
assert ped.find(".//*[Name='pasilloRocaFondo']") is None and ped.find(".//*[Name='entradaPeatonal']") is None
# El pasillo arranca en la plaza de transbordo (X = -152); el vestíbulo queda cerrado del lado de los andenes de la C.
assert _abs('paredDerechaCentro')==[(580,290),(580,430)]
# Descenso en las cabeceras de los 7 andenes (islas 2-3 ... 12-13 y 14) y obstáculos del hall medidos en el plano.
assert ped.find(".//TargetLine[Name='andenRoca0']") is None
assert [_abs(f'bordeAndenRoca{k}') for k in range(7)]==[[(-830,a),(-2420,a),(-2420,b),(-830,b)] for a,b in ((267,362),(441,536),(613,708),(789,885),(957,1060),(1128,1235),(1308,1366))]
assert all(ped.find(f".//Wall[Name='bordeAndenRoca{k}']").findtext('DrawMode')=='SHAPE_DRAW_2D' for k in range(7))
assert all(ped.find(f".//*[Name='{n}']") is not None for n in ('hallEstructuraCentral','hallVestuarioSOFSE','hallBoleteriasSOFSE'))
assert _abs('paredIzquierdaNorte')==[(80,190),(80,335)] and _abs('paredIzquierdaSur')==[(80,385),(80,530)]
# Disposición coherente con el plano georreferenciado (2026-11-02): pasillo del Roca en X = 80, escalera B3 en
# X ~ 194, molinetes en X 300-316 (la zona paga empieza en la conexión real con el andén de la C, X ~ 316) y
# escaleras al andén en X 520-580, sobre los andenes de la Línea C.
assert _abs('paredNorteOeste')==[(80,190),(580,190)] and _abs('paredInferior')==[(80,530),(580,530)]
assert ped.find(".//*[Name='paredNorteCentro']") is None and ped.find(".//*[Name='paredNorteEste']") is None
assert _abs('escaleraB3')==[(181,395),(181,455),(207,455),(207,395)] and _abs('entradaCalle',1)==[(183,399),(205,399)]
assert ped.find(".//*[Name='entradaCalle2']") is None
assert all(float(g.findtext('X'))==300 for g in gates) and all(float(q.findtext('X'))==220 for q in queues)
assert _abs('salidaPeatonal',1)==[(568,295),(568,425)] and _abs('paredDerechaNorte')==[(580,190),(580,290)]
_eleccion=next(f for f in ped.findall('Functions/Function') if f.findtext('Name')=='elegirColaPed').findtext('Body')
assert 'double yReferencia = ped.getX() < 80 ? 335 + (((ped.getY() % 50) + 50) % 50) : ped.getY();' in _eleccion
aviso=ped.find(".//Text[Name='avisoPeatonal']")
assert 'PLANO HIPOTÉTICO' in aviso.findtext('Text') and 'NO ES EL PLANO OFICIAL' in aviso.findtext('TextCode')
assert ped.find(".//TargetLine[Name='salidaPeatonal']") is not None
assert 'configurarMolinetesPed()' in ped.findtext('StartupCode')
startup=ped.findtext('StartupCode')
assert startup.index('inicializarPed()') < startup.index('configurarMolinetesPed()')
assert 'cierreMetricasPed.restart(horizonteCortePed)' in startup
_ps=[e for e in ped.findall('EmbeddedObjects/EmbeddedObject') if e.findtext('ActiveObjectClass/ClassName')=='PedSettings']
assert len(_ps)==1 and {x.findtext('Name'):x.findtext('Value/Code') for x in _ps[0].findall('Parameters/Parameter')}.get('aStarDensityModifier')=='0', 'ruteo sin peso de densidad'
assert 'aStarDensityModifier' not in startup
assert 'if (modoFranjaPed) programarDemandaFranjaPed(); else proximaTandaPed.restart(0);' in startup
assert ped.findtext('DestroyCode')=='emitirIncompletoPed();'
assert callbacks_delay=='ped.servicioAsignadoPed'
assert ped.find(".//Text[Name='etiquetaMolinetes']").findtext('TextCode')=='"Molinetes activos: " + molinetesOperativosPed + " (1-22 Principal; 23-28 hipotéticos)"'
ped_service=next(x for x in ped.findall('EmbeddedObjects/EmbeddedObject') if x.findtext('Name')=='pedMolinetes')
callbacks={x.findtext('Name'):x.findtext('Value/Code') for x in ped_service.findall('Parameters/Parameter')}
assert callbacks['onBeginService']=='ped.nombreMolinetePed = service.getName(); comienzaServicioPed(ped);'
assert callbacks['onEndService']=='terminaServicioPed(ped);'
assert callbacks['onEnterQueue']=='ped.tEntradaColaPed = time(); entraColaPed(ped);'
assert callbacks['queueChoicePolicy']=='self.CHOICE_CUSTOM' and callbacks['chooseQueue']=='elegirColaPed(ped)'
ped_variable_names={x.findtext('Name') for x in ped.findall('Variables/Variable')}
assert {'esperasPed','esperasPicoPed','ocupacionPorMolinetePed','nProcesadosHorizontePed','semillaPed','resultadoEmitidoPed'} <= ped_variable_names
ped_events={x.findtext('Name'):x for x in ped.findall('Events/Event')}
assert 'cierreMetricasPed' in ped_events
assert 'nProcesadosHorizontePed = nProcesadosPed' in ped_events['cierreMetricasPed'].findtext('Action')
assert 'if (drenadoPed()) emitirResultadoPed();' in ped_events['cierreMetricasPed'].findtext('Action')
# Franja parametrizada: los datos de campo siguen sin valor y la demo no cambia.
ped_defaults={v.findtext('Name'):v.findtext('Properties/DefaultValue/Code') for v in ped.findall("Variables/Variable[@Class='Parameter']")}
for name in ('proporcionRocaPed','demoraAccesoRocaSeg','duracionDescargaSeg','servicioPedSeg','servicioMinPedSeg','servicioMaxPedSeg'):
 assert ped_defaults[name]=='-1', f'{name} debe quedar pendiente de calibración'
assert ped_defaults['modoFranjaPed']=='false' and ped_defaults['horizonteArribosPedSeg']=='9000'
main_defaults={v.findtext('Name'):v.findtext('Properties/DefaultValue/Code') for v in a.findall("Variables/Variable[@Class='Parameter']")}
assert ped_defaults['perfilPed15min']==main_defaults['perfil15min']
assert ped_defaults['archivoSalidaPed']=='""'
demo=next(e for e in experiments if e.findtext('Name')=='PeatonalDemo')
assert float(demo.findtext('ModelTimeProperties/FinalTime'))==900
# Franja completa con animación (diagnóstico T2.6 / exhibición T6.2): desde el 2026-10-09 (142b949) usa el
# escenario intermedio de PeatonalCorridasApareadas, sin archivo de salida.
visuales={e.findtext('Name'):e for e in experiments if (e.findtext('Name') or '').startswith('PeatonalFranjaVisual')}
assert set(visuales)=={'PeatonalFranjaVisualE0','PeatonalFranjaVisualE1'}
intermedio={'proporcionRocaPed':'0.8','demoraAccesoRocaSeg':'10','duracionDescargaSeg':'30','servicioPedSeg':'2.4','servicioMinPedSeg':'1.8','servicioMaxPedSeg':'3.5'}
for name,mol in (('PeatonalFranjaVisualE0','20'),('PeatonalFranjaVisualE1','22')):
 ps={x.findtext('ParameterName'):x.findtext('ParameterValue/Code') for x in visuales[name].findall('Parameters/Parameter')}
 assert ps['molinetesOperativosPed']==mol and ps['modoFranjaPed']=='true' and ps['pruebaSinteticaPed']=='false' and ps['archivoSalidaPed'] is None, name
 assert all(ps[k]==v for k,v in intermedio.items()), f'{name}: escenario intermedio {[(k,ps[k]) for k in intermedio]}'
 assert float(visuales[name].findtext('ModelTimeProperties/FinalTime'))==17900  # margen bajo el tope de 5 h de PLE
# Memoria de la JVM de cada experimento peatonal (T2.3): la franja no entra en 512-1024 MB.
for e in r.iter():
 if e.tag in ('SimulationExperiment','ParamVariationExperiment') and e.get('ActiveObjectClassId')==ped.findtext('Id'):
  assert int(e.findtext('MaximumMemory'))>=4096, e.findtext('Name')
# Diagnóstico del atasco (T2.2): progreso periódico y foto del hall a las 09:30.
assert 'progresoPed.restart(intervaloProgresoPed());' in ped.findtext('StartupCode')
assert 'hallAlCortePed = hallPed();' in ped_events['cierreMetricasPed'].findtext('Action')
assert 'progresoPed.restart(intervaloProgresoPed());' in ped_events['progresoPed'].findtext('Action')
ped_param_ids={v.findtext('Id'):v.findtext('Name') for v in ped.findall("Variables/Variable[@Class='Parameter']")}
for e in [x for x in experiments if x.get('ActiveObjectClassId')==ped.findtext('Id')]:
 assert {p.findtext('ParameterName') for p in e.findall('Parameters/Parameter')}==set(ped_param_ids.values()), e.findtext('Name')
pvs={e.findtext('Name'):e for e in r.findall('Model/Experiments/ParamVariationExperiment')}
assert set(pvs)=={'PeatonalCorridasApareadas','PeatonalCorridasDemo','PeatonalFranjaPrueba'}
prueba={ped_param_ids[x.findtext('Id')]:x.findtext('Expression/Code') for x in pvs['PeatonalFranjaPrueba'].findall('FreeformParamValue')}
assert prueba['modoFranjaPed']=='true' and prueba['pruebaSinteticaPed']=='true' and prueba['archivoSalidaPed']=='"corridas_peatonales_prueba.csv"'
assert pvs['PeatonalFranjaPrueba'].findtext('NumberOfRuns')=='2' and float(pvs['PeatonalFranjaPrueba'].findtext('ModelTimeProperties/FinalTime'))<=18000
assert prueba['horizonteArribosPedSeg']=='1800'
assert ped_defaults_early['pruebaSinteticaPed']=='false'
pvs={k:v for k,v in pvs.items() if k!='PeatonalFranjaPrueba'}
for name,(runs,modo,archivo,final) in {'PeatonalCorridasApareadas':('40','true','"corridas_peatonales.csv"','17900'),
                                       'PeatonalCorridasDemo':('6','false','"corridas_peatonales_demo.csv"','900')}.items():
 e=pvs[name]
 assert e.get('ActiveObjectClassId')==ped.findtext('Id')
 assert e.findtext('UseFreeformParameters')=='true' and e.findtext('NumberOfRuns')==runs
 # Apareadas en paralelo (2026-11-09): 10 días x 4 escenarios = n0 del procedimiento secuencial. Es seguro porque cada
 # fuente de azar tiene su generador (lo único static es la constante posesPed del pasajero) y la escritura de los CSV
 # está sincronizada.
 assert e.findtext('AllowParallelEvaluations')==('true' if name=='PeatonalCorridasApareadas' else 'false')
 assert float(e.findtext('ModelTimeProperties/FinalTime'))<18000, 'PLE limita la Pedestrian Library a 5 h de modelo'
 free={ped_param_ids[x.findtext('Id')]:x.findtext('Expression/Code') for x in e.findall('FreeformParamValue')}
 assert set(free)==set(ped_param_ids.values())
 # Apareadas (2026-11-04): 4 escenarios por día (index % 4 = E0, E1, E3, E13) con el mismo día SBASE y la misma semilla.
 assert free['semillaPed']==('20260923L + index / 4' if name=='PeatonalCorridasApareadas' else '20260923L + index / 2')
 assert free['molinetesOperativosPed']=='index % 2 == 0 ? 20 : 22'
 # Día hábil real (perfil SBASE y llegadas reales del Roca de ese día, Trenes Argentinos) y carga Poisson; el atraso
 # uniforme queda en 0 (sólo para sensibilidad, con el horario oficial).
 nuevos={k:free[k] for k in ('diaSbasePed','atrasoMaxRocaSeg','cargaTrenPoissonPed','llegadasRealesPed')}
 assert nuevos==({'diaSbasePed':'-2','atrasoMaxRocaSeg':'0','cargaTrenPoissonPed':'true','llegadasRealesPed':'true'} if name=='PeatonalCorridasApareadas'
                 else {'diaSbasePed':None,'atrasoMaxRocaSeg':None,'cargaTrenPoissonPed':None,'llegadasRealesPed':None}), (name,nuevos)
 assert free['modoFranjaPed']==modo and free['archivoSalidaPed']==archivo
 calib={k:free[k] for k in ('proporcionRocaPed','demoraAccesoRocaSeg','duracionDescargaSeg','servicioPedSeg','servicioMinPedSeg','servicioMaxPedSeg')}
 if name=='PeatonalCorridasApareadas':
  # Escenario intermedio (T3.4, 2026-10-05): rangos de la §5 del plan; demora con D = 85 m (OpenStreetMap) y h = 5 m.
  # E3 y E13 (validación EMV/QR, [SUP]): triangular 1,5 / 1,8 / 2,5 s en lugar de 1,8 / 2,4 / 3,5 s.
  assert calib=={'proporcionRocaPed':'0.8','demoraAccesoRocaSeg':'10','duracionDescargaSeg':'30','servicioPedSeg':'index % 4 >= 2 ? 1.8 : 2.4',
                 'servicioMinPedSeg':'index % 4 >= 2 ? 1.5 : 1.8','servicioMaxPedSeg':'index % 4 >= 2 ? 2.5 : 3.5'}, calib
  rng={ped_param_ids[x.findtext('Id')]:x.findtext('Expression/Code') for x in e.findall('RangeVariationParamValue')}
  assert all(rng[k]==calib[k] for k in ('proporcionRocaPed','demoraAccesoRocaSeg','duracionDescargaSeg')), 'freeform y range deben coincidir'
  assert all(rng[k]==v for k,v in nuevos.items()), 'freeform y range deben coincidir (día, atraso, Poisson)'
 else:
  assert all(calib[k] is None for k in ('proporcionRocaPed','demoraAccesoRocaSeg','duracionDescargaSeg','servicioPedSeg'))
# Índice i -> semilla 20260923 + i // 4; i % 4 = 0 E0 (20; 2,4 s), 1 E1 (22; 2,4 s), 2 E3 (20; 1,8 s), 3 E13 (22; 1,8 s).
assert [(20260923+i//4, 20 if i%2==0 else 22, 1.8 if i%4>=2 else 2.4) for i in range(5)]==[(20260923,20,2.4),(20260923,22,2.4),(20260923,20,1.8),(20260923,22,1.8),(20260924,20,2.4)]
pasajero_variable_names={x.findtext('Name') for x in agents['Pasajero'].findall('Variables/Variable')}
assert {'tIngresoSistemaPed','enPicoPed','tInicioServicioPed','nombreMolinetePed','servicioAsignadoPed'} <= pasajero_variable_names
libs={x.findtext('LibraryName') for x in r.findall('Model/RequiredLibraryReference')}
# Muros: AnyLogic guarda 3 puntos por vértice (vértice, manija de entrada, manija de salida). Con 1 punto por vértice
# los lee de a tres y arma tramos sin sentido o ninguno ("Wall: The length is zero" al crear el modelo).
for w in r.iter('Wall'):
 pts=[(float(p.findtext('X')),float(p.findtext('Y'))) for p in w.findall('Points/Point')]
 nom=w.findtext('Name')
 assert len(pts)>=6 and len(pts)%3==0, f"muro {nom}: {len(pts)} puntos, se esperan 3 por vértice"
 v=pts[0::3]
 assert all(a!=b for a,b in zip(v,v[1:])), f"muro {nom} con tramo de largo cero"
 # Muros generados a mano: manija de salida sobre el tramo siguiente (tramo recto, sin arcos).
 if nom.startswith(('hall','bordeAndenRoca')):
  for k in range(len(v)-1):
   (x0,y0),(x1,y1)=v[k],v[k+1]; hx,hy=pts[3*k+2]
   assert abs((x1-x0)*(hy-y0)-(y1-y0)*(hx-x0))<1e-3*max(1,abs(x1-x0)+abs(y1-y0))*25, f"muro {nom}: manija fuera del tramo {k}"
assert 'com.anylogic.libraries.pedestrian' in libs
print('OK: XML, unique IDs, clean presentations, pedestrian KPIs, hypothetical plan with 28 linear gates, E0=20/E1=22 experiments, 4 GB, franja visual')
# The CSV schema, the workbook and the loader share one field order.
# T1.5: n de pares variable (planilla generada por construir_planilla.py) y primarias D4.
import sys, shutil
sys.path.insert(0, str(p.parent))
import cargar_corridas as cc
import openpyxl
book=openpyxl.load_workbook(cc.PLANILLA_OFICIAL)
for _alt in cc.ALTERNATIVAS:
 cc.verificar_encabezados(book[cc.hojas(_alt)[0]], _alt)
capacidad=cc.leer_capacidad(book[cc.HOJA])
assert list(capacidad)==list(range(cc.SEMILLA_INICIAL, cc.SEMILLA_INICIAL+len(capacidad))), \
    'las semillas de la planilla deben ser contiguas desde SEMILLA_INICIAL'
assert len(capacidad)>=cc.MIN_PARES, f'la planilla oficial debe admitir al menos {cc.MIN_PARES} pares (D4/T1.5)'
fila_ped=next(f for f in ped.findall('Functions/Function') if f.findtext('Name')=='filaResultadoPed').findtext('Body')
assert fila_ped.count('Integer.toString')+fila_ped.count('String.format')+fila_ped.count('Long.toString')+2==2+len(cc.CAMPOS), 'escenario + "0" desviados + 15 conversiones'
import contextlib, io
import hashlib
_hash_planilla=hashlib.sha256(Path(cc.PLANILLA_OFICIAL).read_bytes()).hexdigest()
with tempfile.TemporaryDirectory(prefix='subte-carga-') as tmp, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
 tmp=Path(tmp); log=tmp/'consola.txt'; copia=tmp/'copia.xlsx'
 rows=[]
 for i in range(30):
  for esc,esp in (('E0',40+i),('E1',20+i)):
   rows.append(f'CSV_PEATONAL_DEMO;{esc};{cc.SEMILLA_INICIAL+i};480;0;470;480;{esp}.5;{esp+10};0.25;3.5;60;120.0;0.4;0.05;0;0;0;-1;150.0;0.5')
 log.write_text('ruido de consola\n'+'\n'.join(rows)+'\n')
 assert cc.main([str(log),'--demo'])==0
 assert cc.main([str(log),'--demo','--escribir'])==1, 'demo no puede escribir la planilla oficial'
 assert cc.main([str(log)])==1, 'demo no puede cargarse como producción'
 # La planilla oficial ya tiene la producción: la prueba de escritura parte de una planilla vacía regenerada.
 vacia=tmp/'vacia.xlsx'
 subprocess.run([sys.executable,str(p.parent/'construir_planilla.py'),'--salida',str(vacia)],check=True,capture_output=True)
 assert cc.main([str(log),'--demo','--escribir','--planilla',str(vacia),'--salida',str(copia)])==0
 hoja=openpyxl.load_workbook(copia)[cc.HOJA]
 assert hoja['C8'].value==480 and hoja['O8'].value==40.5 and hoja['P8'].value==20.5 and hoja['Q8'].value=='=IF(OR(O8="",P8=""),"",P8-O8)'
 assert hoja['AS37'].value==0 and hoja['AG37'].value==0.4
 (tmp/'incompleta.txt').write_text(rows[0]+f'\nCSV_PEATONAL_INCOMPLETO;E1;{cc.SEMILLA_INICIAL};480;0;470;479\n')
 assert cc.main([str(tmp/'incompleta.txt'),'--demo'])==1
 (tmp/'impar.txt').write_text(rows[0]+'\n')
 assert cc.main([str(tmp/'impar.txt'),'--demo'])==1
 (tmp/'desbalance.txt').write_text(rows[0]+'\n'+rows[1].replace(';480;0;470;480;',';481;0;470;481;')+'\n')
 assert cc.main([str(tmp/'desbalance.txt'),'--demo'])==1
 # El modelo en main etiqueta 20->E0, 22->E1, 28->E1B (D1): la planilla solo carga E0/E1.
 (tmp/'e1b.txt').write_text(f'CSV_PEATONAL_DEMO;E1B;{cc.SEMILLA_INICIAL};480;0;470;480;40.5;50;0.25;3.5;60;120.0;0.4;0.05;0;0;0;-1;150.0;0.5\n')
 salida_e1b=io.StringIO()
 with contextlib.redirect_stderr(salida_e1b):
  assert cc.main([str(tmp/'e1b.txt'),'--demo'])==1, 'E1B no debe cargarse en la planilla'
 assert 'E1B' in salida_e1b.getvalue(), 'el rechazo de E1B debe explicar el motivo'
 # 2026-11-04: E3 y E13 se cargan en sus hojas; el día SBASE debe coincidir en el par; producción exige día.
 fila_e=lambda esc,sem,dia,p90: f'CSV_PEATONAL_DEMO;{esc};{sem};480;0;470;480;5.0;{p90};0.25;3.5;60;120.0;0.4;0.05;100;20.0;30.0;{dia};150.0;0.5'
 (tmp/'cuatro.txt').write_text('\n'.join(fila_e(e,cc.SEMILLA_INICIAL,7,p) for e,p in (('E0',40),('E1',38),('E3',30),('E13',28)))+'\n')
 copia4=tmp/'copia4.xlsx'
 assert cc.main([str(tmp/'cuatro.txt'),'--demo','--escribir','--planilla',str(vacia),'--salida',str(copia4)])==0
 libro4=openpyxl.load_workbook(copia4)
 assert libro4['Corridas']['S8'].value==38 and libro4['Corridas E3']['R8'].value==40 and libro4['Corridas E3']['S8'].value==30 and libro4['Corridas E13']['S8'].value==28, 'P90 en R (E0) y S (alternativa)'
 assert libro4['Corridas E13']['AV8'].value==7, 'día SBASE cargado'
 (tmp/'otro_dia.txt').write_text(fila_e('E0',cc.SEMILLA_INICIAL,7,40)+'\n'+fila_e('E3',cc.SEMILLA_INICIAL,8,30)+'\n')
 assert cc.main([str(tmp/'otro_dia.txt'),'--demo'])==1, 'E0 y E3 con días distintos no son un par'
 (tmp/'sin_dia.txt').write_text('\n'.join(fila_e(e,cc.SEMILLA_INICIAL,-1,40).replace('CSV_PEATONAL_DEMO','CSV_PEATONAL') for e in ('E0','E1'))+'\n')
 assert cc.main([str(tmp/'sin_dia.txt')])==1, 'producción sin día SBASE'
# Las pruebas del cargador no tocan la planilla oficial (que desde 2026-10-05 tiene los 30 pares de producción).
assert hashlib.sha256(Path(cc.PLANILLA_OFICIAL).read_bytes()).hexdigest()==_hash_planilla, 'las pruebas modificaron la planilla oficial'

# Autoprueba (T1.5, aceptación observable 2): el IC paired-t que calcula la hoja Resumen
# (T.INV.2T sobre n y k reales) coincide a 1e-6 con el mismo cálculo hecho a mano en Python,
# para n = 12 y n = 30. Requiere LibreOffice (soffice) para forzar el recálculo de fórmulas;
# si no está instalado, se avisa y se omite sin marcar el verificador como roto (sigue siendo
# la 5ta y última línea OK, para no correr un verificador parcial silenciosamente).
if shutil.which('soffice') is None:
 autoprueba_ic = 'omitida (soffice no está instalado)'
else:
 import math, random, statistics, csv as _csv

 def _betacf(aa, bb, x):
  MAXIT, EPS, FPMIN = 200, 3e-16, 1e-300
  qab, qap, qam = aa+bb, aa+1.0, aa-1.0
  c=1.0; d=1.0-qab*x/qap
  if abs(d)<FPMIN: d=FPMIN
  d=1.0/d; h=d
  for m in range(1, MAXIT+1):
   m2=2*m
   delta=m*(bb-m)*x/((qam+m2)*(aa+m2))
   d=1.0+delta*d
   if abs(d)<FPMIN: d=FPMIN
   c=1.0+delta/c
   if abs(c)<FPMIN: c=FPMIN
   d=1.0/d; h*=d*c
   delta=-(aa+m)*(qab+m)*x/((aa+m2)*(qap+m2))
   d=1.0+delta*d
   if abs(d)<FPMIN: d=FPMIN
   c=1.0+delta/c
   if abs(c)<FPMIN: c=FPMIN
   d=1.0/d; paso=d*c; h*=paso
   if abs(paso-1.0)<EPS: break
  return h

 def _betainc(aa, bb, x):
  if x<=0: return 0.0
  if x>=1: return 1.0
  lbeta=math.lgamma(aa)+math.lgamma(bb)-math.lgamma(aa+bb)
  front=math.exp(math.log(x)*aa+math.log1p(-x)*bb-lbeta)
  if x<(aa+1)/(aa+bb+2): return front*_betacf(aa,bb,x)/aa
  return 1.0-front*_betacf(bb,aa,1-x)/bb

 def t_inv_2t(prob, df):
  # Inversión por bisección de la función de distribución t de dos colas (verificada contra
  # LibreOffice TINV/_xlfn.T.INV.2T y tablas estándar: t(29,0.05)=2.0452296..., t(29,0.05/3)=2.5409081...).
  lo, hi = 0.0, 1000.0
  for _ in range(200):
   mid=(lo+hi)/2
   x=df/(df+mid*mid)
   if _betainc(df/2.0, 0.5, x) > prob:
    lo=mid
   else:
    hi=mid
  return (lo+hi)/2

 assert abs(t_inv_2t(0.05,29)-2.0452296421327016)<1e-9
 assert abs(t_inv_2t(0.05/3,29)-2.540908149498901)<1e-9

 def generar_pares_sinteticos(n, semilla=2026):
  rnd=random.Random(semilla)
  filas=[]; z={5:[], 6:[], 14:[]}
  for j in range(n):
   e0_p90=30+rnd.uniform(-5,5); e1_p90=e0_p90+rnd.uniform(-8,3)
   e0_prop=rnd.uniform(0.05,0.25); e1_prop=min(max(e0_prop+rnd.uniform(-0.1,0.05),0),1)
   e0_pico=32+rnd.uniform(-5,5); e1_pico=e0_pico+rnd.uniform(-9,3)
   z[5].append(e1_p90-e0_p90); z[6].append(e1_prop-e0_prop); z[14].append(e1_pico-e0_pico)
   for esc,p90,prop,pico in (('E0',e0_p90,e0_prop,e0_pico), ('E1',e1_p90,e1_prop,e1_pico)):
    campos=[480,0,470,480,5.0,p90,prop,3.5,60,120.0,0.4,0.05,100,20.0,pico,-1,150.0,0.5]
    filas.append(f'CSV_PEATONAL_DEMO;{esc};{cc.SEMILLA_INICIAL+j};'+';'.join(str(x) for x in campos))
  return filas, z

 def ic_esperado(zvals, primaria=True):
  n=len(zvals); media=statistics.fmean(zvals); sd=statistics.stdev(zvals); se=sd/math.sqrt(n)
  alfa=(0.05/9) if primaria else 0.05   # 3 primarias x 3 comparaciones contra E0 (E1, E3, E13)
  t=t_inv_2t(alfa, n-1)
  return n, media, sd, se, t, media-t*se, media+t*se

 def num(texto):
  texto=texto.strip()
  return float(texto[:-1])/100.0 if texto.endswith('%') else float(texto)

 for n_prueba in (12, 30):
  filas, z = generar_pares_sinteticos(n_prueba)
  with tempfile.TemporaryDirectory(prefix='subte-autoprueba-') as tmp2, \
       contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
   tmp2=Path(tmp2); log2=tmp2/'consola.txt'; copia2=tmp2/'copia.xlsx'; salida_csv=tmp2/'csv'
   log2.write_text('\n'.join(filas)+'\n')
   vacia2=tmp2/'vacia.xlsx'
   subprocess.run([sys.executable,str(p.parent/'construir_planilla.py'),'--salida',str(vacia2)],check=True,capture_output=True)
   assert cc.main([str(log2),'--demo','--escribir','--planilla',str(vacia2),'--salida',str(copia2)])==0
   resultado=subprocess.run(['soffice','--headless','--convert-to','csv',str(copia2),'--outdir',str(salida_csv)],
                             capture_output=True, text=True, timeout=120)
   assert resultado.returncode==0, resultado.stderr
   csvs=list(salida_csv.glob('*.csv')); assert len(csvs)==1, csvs
   with open(csvs[0], encoding='utf-8') as fh:
    filas_csv=list(_csv.reader(fh))
   for idx, fila_hoja in ((5,16), (6,17), (14,25)):
    fc=filas_csv[fila_hoja-1]
    n_c,h_c,i_c,j_c,k_c,l_c,m_c=(num(fc[col]) for col in (4,7,8,9,10,11,12))
    n_e,h_e,i_e,j_e,k_e,l_e,m_e=ic_esperado(z[idx])
    assert n_c==n_e==n_prueba
    for calc, esp in ((h_c,h_e),(i_c,i_e),(j_c,j_e),(k_c,k_e),(l_c,l_e),(m_c,m_e)):
     assert abs(calc-esp)<1e-6, (fila_hoja, calc, esp)
 autoprueba_ic = 'coincide a 1e-6 con Python (T.INV.2T, n y k = 9 reales) para n=12 y n=30 en las tres primarias D4'
print(f'OK: CSV_PEATONAL order matches 04-resultados-corridas.xlsx, the loader rejects demo, incomplete, '
      f'unpaired, E1B or mismatched-day runs, loads E1/E3/E13 sheets, and the Resumen IC {autoprueba_ic}')
