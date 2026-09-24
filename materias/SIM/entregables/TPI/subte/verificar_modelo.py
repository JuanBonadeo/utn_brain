#!/usr/bin/env python3
"""Verifica estructura y lógica del prototipo; no sustituye Build/Run en AnyLogic.
Requiere AnyLogic 8 PLE instalado en /Applications (macOS).
"""
from pathlib import Path
import xml.etree.ElementTree as E
import subprocess
p=Path(__file__).with_name('SubteConstitucion.alp')
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
  eq(n.capacidadMolinetes(),e==1?28:20);eq(n.servicioSeg(),e==3?2.5:3);
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
ped_check='''public class SubtePedLogicCheck {
static class Pasajero {
 double tEntradaColaPed, tIngresoSistemaPed, tInicioServicioPed, servicioAsignadoPed, y;
 double getY(){return y;}
 boolean enColaPed, enPicoPed, desdeRocaPed=true;
 String nombreMolinetePed="";
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
EventStub proximaTandaPed=new EventStub(), cierreMetricasPed=new EventStub(), proximaLiberacionPed=new EventStub(), proximaLlegadaCallePed=new EventStub();
java.util.ArrayList<String> eventos=new java.util.ArrayList<String>();
// Bucle de eventos minimo para la demanda de la franja (liberaciones del Roca y llegadas de calle).
void correrDemanda(){ while(proximaLiberacionPed.at>=0||proximaLlegadaCallePed.at>=0){ boolean roca=proximaLlegadaCallePed.at<0||(proximaLiberacionPed.at>=0&&proximaLiberacionPed.at<=proximaLlegadaCallePed.at); EventStub e=roca?proximaLiberacionPed:proximaLlegadaCallePed; clock=e.at; e.at=-1; int r0=pedSource.injected,c0=pedSourceCalle.injected; if(roca)liberarPendientesPed(); else llegadaCallePed(); eventos.add(String.format(java.util.Locale.US,"%.6f;%d;%d",clock,pedSource.injected-r0,pedSourceCalle.injected-c0)); } }
static SubtePedLogicCheck franja(int molinetes,double factor){ SubtePedLogicCheck f=new SubtePedLogicCheck(); f.modoFranjaPed=true; f.molinetesOperativosPed=molinetes; f.proporcionRocaPed=0.8; f.demoraAccesoRocaSeg=60; f.duracionDescargaSeg=120; f.servicioPedSeg=3; f.servicioMinPedSeg=2; f.servicioMaxPedSeg=5; f.factorDemandaPed=factor; f.inicializarPed(); f.programarDemandaFranjaPed(); f.correrDemanda(); return f; }
ServiceStub molinetesPeatonales=new ServiceStub(); EngineStub engine=new EngineStub(); RandomStub rng=new RandomStub();
Object molinetePed21=new Object(), molinetePed22=new Object(), molinetePed23=new Object(), molinetePed24=new Object();
Object molinetePed25=new Object(), molinetePed26=new Object(), molinetePed27=new Object(), molinetePed28=new Object();
java.util.ArrayList<String> trazas=new java.util.ArrayList<String>();
double clock; double time(){return clock;} void traceln(String s){trazas.add(s);}
EngineStub getEngine(){return engine;} java.util.Random getDefaultRandomGenerator(){return rng;}
'''+ '\n'.join(ped_fields+ped_functions) + '''
static void ok(boolean c,String m){if(!c)throw new AssertionError(m);}
static void eq(double a,double b,String m){ok(Math.abs(a-b)<1e-9,m+": "+a+" != "+b);}
public static void main(String[] args) throws Exception {
 SubtePedLogicCheck m=new SubtePedLogicCheck();
 m.configurarMolinetesPed();
 ok(m.molinetesPeatonales.calls==8 && m.molinetesPeatonales.suspended==8,"E0 suspende 8");
 SubtePedLogicCheck e1=new SubtePedLogicCheck();e1.molinetesOperativosPed=28;e1.configurarMolinetesPed();
 ok(e1.molinetesPeatonales.calls==8 && e1.molinetesPeatonales.suspended==0,"E1 habilita 28");
 // Eleccion de cola: nunca un molinete suspendido; equilibra desvio lateral y personas en cola.
 for(int k=0;k<28;k++){m.molinetesPeatonales.colas.add(new QueuePath(225+10*k+(k>=14?20:0),0));e1.molinetesPeatonales.colas.add(m.molinetesPeatonales.colas.get(k));}
 Pasajero sur=new Pasajero();sur.y=515;sur.servicioAsignadoPed=3;
 ok(m.elegirColaPed(sur)==m.molinetesPeatonales.colas.get(19),"E0 elige el habilitado mas cercano (20)");
 ok(e1.elegirColaPed(sur)==e1.molinetesPeatonales.colas.get(27),"E1 puede usar el 28");
 m.molinetesPeatonales.colas.get(19).size=3;
 ok(m.elegirColaPed(sur)==m.molinetesPeatonales.colas.get(18),"una cola ocupada desvia al molinete vecino");
 m.molinetesPeatonales.colas.get(19).size=0;
 // Demo: corte de metricas en horizonteMetricasPedSeg y semilla efectiva semillaPed.
 m.inicioPicoPedSeg=0;m.finPicoPedSeg=10;m.inicializarPed();
 eq(m.horizonteCortePed,600,"corte demo");ok(m.rng.seed==20260923L,"semilla efectiva");
 Pasajero p=new Pasajero();m.clock=2;m.registraIngresoPed(p);p.tEntradaColaPed=m.time();m.entraColaPed(p);
 eq(p.servicioAsignadoPed,3,"servicio demo asignado");
 m.clock=5;p.nombreMolinetePed="molinetePed01";m.comienzaServicioPed(p);
 m.clock=8;m.terminaServicioPed(p);
 ok(m.nEsperandoPed==0 && m.nEsperasPed==1 && Math.abs(m.esperaMediaPed()-3)<1e-9,"espera");
 ok(m.percentil90Ped()==3 && m.proporcionMas30Ped()==0 && m.esperasPicoPed.size()==1 && m.p90PicoPed()==3,"P90 y cohorte");
 eq(m.utilizacionMediaPed(),3.0/(600*20),"utilizacion");
 ok(m.utilizacionPorMolinetePed().contains("molinetePed01=0.005"),"utilizacion por puesto");
 m.nProcesadosHorizontePed=1;
 ok(m.filaResultadoPed().startsWith("E0;20260923;1;0;1;"),"fila");
 ok(m.filaResultadoPed().split(";").length==17,"17 campos");
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
 ok(f.nDesdeRocaPed>0.97*0.8*total && f.nDesdeRocaPed<=0.8*total+trenes,"Roca ~80% del perfil SBASE: "+f.nDesdeRocaPed);
 ok(Math.abs(f.nDesdeCallePed-0.2*total)<5*Math.sqrt(0.2*total),"calle ~20% del perfil SBASE: "+f.nDesdeCallePed);
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
 ok(f.caudalPorVentanaPed().contains("08:15 sim=0 obs=2054"),"control de caudal por ventana: "+f.caudalPorVentanaPed());
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
 SubtePedLogicCheck h=new SubtePedLogicCheck();h.inicializarPed();h.nInyectadosPed=2;h.nGeneradosPed=1;h.nProcesadosPed=2;
 try{h.emitirResultadoPed();throw new AssertionError("Conservacion violada aceptada");}catch(IllegalStateException expected){}
 h.emitirIncompletoPed();ok(h.trazas.get(h.trazas.size()-1).startsWith("CSV_PEATONAL_INCOMPLETO;E0;"),"fila incompleta");
 salida.delete();
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
ids=[x.text for x in r.iter('Id') if id(x) not in references];assert len(ids)==len(set(ids)), 'Duplicate IDs'
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
for agent, min_x in ((a,1100),(ped,1000)):
 for section in ('Variables','Functions','Events'):
  technical=agent.findall(f'{section}/*')
  assert all(x.findtext('PresentationFlag')=='false' for x in technical)
  assert all(int(x.findtext('X'))>=min_x for x in technical)
ped_defaults_early={v.findtext('Name'):v.findtext('Properties/DefaultValue/Code') for v in ped.findall("Variables/Variable[@Class='Parameter']")}
ped_blocks={x.findtext('Name'):x.findtext('ActiveObjectClass/ClassName') for x in ped.findall('EmbeddedObjects/EmbeddedObject')}
assert ped_blocks=={'pedSource':'PedSource','pedSourceCalle':'PedSource','pedMolinetes':'PedService','pedSalida':'PedGoTo','pedSink':'PedSink'}
sources={x.findtext('Name'):{p.findtext('Name'):p.findtext('Value/Code') for p in x.findall('Parameters/Parameter')} for x in ped.findall('EmbeddedObjects/EmbeddedObject') if x.findtext('Name').startswith('pedSource')}
assert sources['pedSource']['locationLine']=='entradaPeatonal' and sources['pedSourceCalle']['locationLine']=='entradaCalle'
assert sources['pedSource']['onExit']=='ped.desdeRocaPed = true; registraIngresoPed(ped);'
assert sources['pedSourceCalle']['onExit']=='ped.desdeRocaPed = false; registraIngresoPed(ped);'
conns={(c.findtext('SourceEmbeddedObjectReference/ItemName'),c.findtext('TargetEmbeddedObjectReference/ItemName')) for c in ped.findall('Connectors/Connector')}
assert {('pedSource','pedMolinetes'),('pedSourceCalle','pedMolinetes'),('pedMolinetes','pedSalida'),('pedSalida','pedSink')}<=conns
# El horario embebido es exactamente el extraído de los PDFs oficiales del Roca.
import csv as _csv
horario=[r['segundos_desde_07'] for r in _csv.DictReader(open(p.parent/'datos'/'arribos_roca_constitucion_habiles.csv',encoding='utf-8'),delimiter=';')]
assert ped_defaults_early['llegadasRocaSeg']=='new double[] {'+','.join(horario)+'}', 'llegadasRocaSeg no coincide con datos/arribos_roca_constitucion_habiles.csv'
assert ped_defaults_early['factorDemandaPed']=='1.0'
assert agents['Pasajero'] is not None
assert any(e.findtext('Name')=='PeatonalDemo' and e.get('ActiveObjectClassId')==ped.findtext('Id') for e in experiments)
ped_experiments={e.findtext('Name'):e for e in experiments if e.findtext('Name') in {'PeatonalE0','PeatonalE1'}}
assert set(ped_experiments)=={'PeatonalE0','PeatonalE1'}
for name, expected in {'PeatonalE0':'20','PeatonalE1':'28'}.items():
 ps={p.findtext('ParameterName'):p.findtext('ParameterValue/Code') for p in ped_experiments[name].findall('Parameters/Parameter')}
 assert ps['molinetesOperativosPed']==expected
 assert ps['semillaPed']=='20260923L'
 assert ped_experiments[name].findtext('SeedValue')=='20260923'
 assert ped_experiments[name].findtext('ModelTimeProperties/FinalTime')=='900'
callbacks_delay=next(x for x in ped.findall('EmbeddedObjects/EmbeddedObject') if x.findtext('Name')=='pedMolinetes').find("Parameters/Parameter[Name='delayTime']").findtext('Value/Code')
# Plano hipotético: 28 molinetes lineales orientados hacia la zona paga, una cola por molinete.
svc=ped.find(".//ServiceWithLine[Name='molinetesPeatonales']")
assert svc.findtext('Type')=='LINEAR'
gates=svc.findall('Presentation/ServiceLine'); queues=svc.findall('Presentation/QueueLine')
assert [g.findtext('Name') for g in gates]==[f'molinetePed{i:02d}' for i in range(1,29)]
assert [q.findtext('Name') for q in queues]==[f'colaMolinete{i:02d}' for i in range(1,29)]
assert not ped.findall('.//ServicePoint')
entry_x=float(ped.find(".//TargetLine[Name='entradaPeatonal']").findtext('X'))
exit_x=float(ped.find(".//TargetLine[Name='salidaPeatonal']").findtext('X'))
for g,q in zip(gates,queues):
 gx,gy=float(g.findtext('X')),float(g.findtext('Y'))
 assert float(g.findtext('Dx'))>0 and float(g.findtext('Dy'))==0 and g.findtext('Bidirectional')=='false', 'el paso va del hall a la zona paga'
 pts=[(float(x.findtext('X')),float(x.findtext('Y'))) for x in q.find('Points')][::3]
 qx,qy=float(q.findtext('X')),float(q.findtext('Y'))
 head=(qx+pts[-1][0],qy+pts[-1][1])
 assert entry_x < qx < head[0] < gx < gx+float(g.findtext('Dx')) < exit_x and abs(head[1]-gy)<1e-9, g.findtext('Name')
assert len(ped.findall('.//Wall'))>=40
aviso=ped.find(".//Text[Name='avisoPeatonal']")
assert 'PLANO HIPOTÉTICO' in aviso.findtext('Text') and 'NO ES EL PLANO OFICIAL' in aviso.findtext('TextCode')
assert ped.find(".//TargetLine[Name='salidaPeatonal']") is not None
assert 'configurarMolinetesPed()' in ped.findtext('StartupCode')
startup=ped.findtext('StartupCode')
assert startup.index('inicializarPed()') < startup.index('configurarMolinetesPed()')
assert 'cierreMetricasPed.restart(horizonteCortePed)' in startup
assert 'if (modoFranjaPed) programarDemandaFranjaPed(); else proximaTandaPed.restart(0);' in startup
assert ped.findtext('DestroyCode')=='emitirIncompletoPed();'
assert callbacks_delay=='ped.servicioAsignadoPed'
assert ped.find(".//Text[Name='etiquetaMolinetes']").findtext('TextCode')=='"Molinetes activos: " + molinetesOperativosPed + "/28"'
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
assert demo.findtext('ModelTimeProperties/FinalTime')=='900'
ped_param_ids={v.findtext('Id'):v.findtext('Name') for v in ped.findall("Variables/Variable[@Class='Parameter']")}
for e in [x for x in experiments if x.get('ActiveObjectClassId')==ped.findtext('Id')]:
 assert {p.findtext('ParameterName') for p in e.findall('Parameters/Parameter')}==set(ped_param_ids.values()), e.findtext('Name')
pvs={e.findtext('Name'):e for e in r.findall('Model/Experiments/ParamVariationExperiment')}
assert set(pvs)=={'PeatonalCorridasApareadas','PeatonalCorridasDemo','PeatonalFranjaPrueba'}
prueba={ped_param_ids[x.findtext('Id')]:x.findtext('Expression/Code') for x in pvs['PeatonalFranjaPrueba'].findall('FreeformParamValue')}
assert prueba['modoFranjaPed']=='true' and prueba['pruebaSinteticaPed']=='true' and prueba['archivoSalidaPed']=='"corridas_peatonales_demo.csv"'
assert pvs['PeatonalFranjaPrueba'].findtext('NumberOfRuns')=='2' and float(pvs['PeatonalFranjaPrueba'].findtext('ModelTimeProperties/FinalTime'))<=18000
assert ped_defaults_early['pruebaSinteticaPed']=='false'
pvs={k:v for k,v in pvs.items() if k!='PeatonalFranjaPrueba'}
for name,(runs,modo,archivo,final) in {'PeatonalCorridasApareadas':('60','true','"corridas_peatonales.csv"','18000'),
                                       'PeatonalCorridasDemo':('6','false','"corridas_peatonales_demo.csv"','900')}.items():
 e=pvs[name]
 assert e.get('ActiveObjectClassId')==ped.findtext('Id')
 assert e.findtext('UseFreeformParameters')=='true' and e.findtext('NumberOfRuns')==runs
 assert e.findtext('AllowParallelEvaluations')=='false'
 assert float(e.findtext('ModelTimeProperties/FinalTime'))<=18000, 'PLE limita la Pedestrian Library a 5 h de modelo'
 free={ped_param_ids[x.findtext('Id')]:x.findtext('Expression/Code') for x in e.findall('FreeformParamValue')}
 assert set(free)==set(ped_param_ids.values())
 assert free['semillaPed']=='20260923L + index / 2' and free['molinetesOperativosPed']=='index % 2 == 0 ? 20 : 28'
 assert free['modoFranjaPed']==modo and free['archivoSalidaPed']==archivo
 assert all(free[k] is None for k in ('proporcionRocaPed','demoraAccesoRocaSeg','duracionDescargaSeg','servicioPedSeg'))
# Par i -> semilla 20260923+i, E0 en índice par y E1 en el siguiente.
assert [(20260923+i//2, 20 if i%2==0 else 28) for i in range(4)]==[(20260923,20),(20260923,28),(20260924,20),(20260924,28)]
pasajero_variable_names={x.findtext('Name') for x in agents['Pasajero'].findall('Variables/Variable')}
assert {'tIngresoSistemaPed','enPicoPed','tInicioServicioPed','nombreMolinetePed','servicioAsignadoPed'} <= pasajero_variable_names
libs={x.findtext('LibraryName') for x in r.findall('Model/RequiredLibraryReference')}
assert 'com.anylogic.libraries.pedestrian' in libs
print('OK: XML, unique IDs, clean presentations, pedestrian KPIs, hypothetical plan with 28 linear gates and 20/28 experiments')
# The CSV schema, the workbook and the loader share one field order.
import sys, shutil
sys.path.insert(0, str(p.parent))
import cargar_corridas as cc
import openpyxl
book=openpyxl.load_workbook(cc.PLANILLA_OFICIAL)
cc.verificar_encabezados(book[cc.HOJA])
assert [book[cc.HOJA].cell(row,2).value for row in range(8,38)]==list(range(20260923,20260953))
fila_ped=next(f for f in ped.findall('Functions/Function') if f.findtext('Name')=='filaResultadoPed').findtext('Body')
assert fila_ped.count('Integer.toString')+fila_ped.count('String.format')+fila_ped.count('Long.toString')+2==2+len(cc.CAMPOS), 'escenario + "0" desviados + 15 conversiones'
import contextlib, io
with tempfile.TemporaryDirectory(prefix='subte-carga-') as tmp, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
 tmp=Path(tmp); log=tmp/'consola.txt'; copia=tmp/'copia.xlsx'
 rows=[]
 for i in range(30):
  for esc,esp in (('E0',40+i),('E1',20+i)):
   rows.append(f'CSV_PEATONAL_DEMO;{esc};{20260923+i};480;0;470;480;{esp}.5;{esp+10};0.25;3.5;60;120.0;0.4;0.05;0;0;0')
 log.write_text('ruido de consola\n'+'\n'.join(rows)+'\n')
 assert cc.main([str(log),'--demo'])==0
 assert cc.main([str(log),'--demo','--escribir'])==1, 'demo no puede escribir la planilla oficial'
 assert cc.main([str(log)])==1, 'demo no puede cargarse como producción'
 assert cc.main([str(log),'--demo','--escribir','--salida',str(copia)])==0
 hoja=openpyxl.load_workbook(copia)[cc.HOJA]
 assert hoja['C8'].value==480 and hoja['O8'].value==40.5 and hoja['P8'].value==20.5 and hoja['Q8'].value=='=IF(OR(O8="",P8=""),"",P8-O8)'
 assert hoja['AS37'].value==0 and hoja['AG37'].value==0.4
 (tmp/'incompleta.txt').write_text(rows[0]+'\nCSV_PEATONAL_INCOMPLETO;E1;20260923;480;0;470;479\n')
 assert cc.main([str(tmp/'incompleta.txt'),'--demo'])==1
 (tmp/'impar.txt').write_text(rows[0]+'\n')
 assert cc.main([str(tmp/'impar.txt'),'--demo'])==1
 (tmp/'desbalance.txt').write_text(rows[0]+'\n'+rows[1].replace(';480;0;470;480;',';481;0;470;481;')+'\n')
 assert cc.main([str(tmp/'desbalance.txt'),'--demo'])==1
assert openpyxl.load_workbook(cc.PLANILLA_OFICIAL)[cc.HOJA]['C8'].value is None, 'la planilla oficial debe seguir vacía'
print('OK: CSV_PEATONAL order matches 04-resultados-corridas.xlsx and the loader rejects demo, incomplete or unpaired runs')
