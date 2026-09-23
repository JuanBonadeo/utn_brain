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
print('OK: Java functions compile against installed AnyLogic 8.9.9 API')
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
static class Pasajero { double tEntradaColaPed; boolean enColaPed; }
static class PedSourceStub { void inject(int n) {} }
static class EventStub { void restart(double t) {} }
PedSourceStub pedSource=new PedSourceStub(); EventStub proximaTandaPed=new EventStub();
double clock; double time(){return clock;} void traceln(String s){}
'''+ '\n'.join(ped_fields+ped_functions) + '''
public static void main(String[] args){
 SubtePedLogicCheck m=new SubtePedLogicCheck();
 Pasajero p=new Pasajero();m.clock=2;p.tEntradaColaPed=m.time();m.entraColaPed(p);m.clock=5;m.comienzaServicioPed(p);
 if(m.nEsperandoPed!=0 || m.nEsperasPed!=1 || Math.abs(m.esperaMediaPed()-3)>1e-9)throw new AssertionError();
 m.generarTandaPed();m.nGeneradosPed=1;m.nProcesadosPed=0;m.salePed();
 if(m.nProcesadosPed!=1)throw new AssertionError();
 System.out.println("OK: pedestrian callbacks and metrics compile");
}
}'''
(d/'SubtePedLogicCheck.java').write_text(ped_check)
subprocess.run([javac,str(d/'SubtePedLogicCheck.java')],check=True)
subprocess.run(['/Applications/AnyLogic 8 PLE.app/Contents/jre/bin/java','-cp',str(d),'SubtePedLogicCheck'],check=True)
ids=[x.text for x in r.iter('Id')];assert len(ids)==len(set(ids)), 'Duplicate IDs'
assert len(a.findall('EmbeddedObjects/EmbeddedObject'))==7
experiments=r.findall('Model/Experiments/SimulationExperiment')
for e in [x for x in experiments if x.findtext('Name') in {'E0','E1','E2','E3'}]:
 ps={p.findtext('ParameterName'):p.findtext('ParameterValue/Code') for p in e.findall('Parameters/Parameter')}
 assert ps['escenario']==e.findtext('Name')[1:]
agents={x.findtext('Name'):x for x in r.findall('Model/ActiveObjectClasses/ActiveObjectClass')}
ped=agents['MainPeatonal']
ped_blocks={x.findtext('Name'):x.findtext('ActiveObjectClass/ClassName') for x in ped.findall('EmbeddedObjects/EmbeddedObject')}
assert ped_blocks=={'pedSource':'PedSource','pedMolinetes':'PedService','pedSink':'PedSink'}
assert agents['Pasajero'] is not None
assert any(e.findtext('Name')=='PeatonalDemo' and e.get('ActiveObjectClassId')==ped.findtext('Id') for e in experiments)
libs={x.findtext('LibraryName') for x in r.findall('Model/RequiredLibraryReference')}
assert 'com.anylogic.libraries.pedestrian' in libs
print('OK: XML, unique IDs, seven process blocks, four scenario overrides and pedestrian skeleton')
