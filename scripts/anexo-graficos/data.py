# -*- coding: utf-8 -*-
# Datos tomados literalmente de materias/ASI/entregables/etapa3.md
# (tabla de red del punto 10 + EDT del punto 4.3 + corrimientos del aplanamiento)

# id: (pred, dur, ES, EF, LS, LF, HT, perfiles, nombre)
ACT = [
 ("1.1", [],            3, 0,3,     0,3,     0,  ["JP"],            "Elaborar el Acta de Proyecto"),
 ("1.2", ["1.1"],       2, 3,5,     3,5,     0,  ["JP"],            "Conformar el equipo y asignar dedicaciones"),
 ("1.3", ["1.2"],       1, 5,6,     5,6,     0,  ["JP"],            "Realizar la reunion de arranque"),
 ("2.1", ["1.3"],       8, 6,14,    6,14,    0,  ["AF","RO"],       "Relevar el proceso actual"),
 ("2.2", ["2.1"],      10, 14,24,   14,24,   0,  ["AF"],            "Especificar requerimientos funcionales"),
 ("2.3", ["2.1"],       6, 14,20,   18,24,   4,  ["EI"],            "Especificar requerimientos de integracion"),
 ("2.4", ["2.1"],      15, 14,29,   98,113, 84,  ["AF","RO"],       "Medir las lineas base O1 a O4"),
 ("2.5", ["2.1"],       5, 14,19,   19,24,   5,  ["ES"],            "Especificar requerimientos de seguridad"),
 ("2.6", ["2.2","2.3","2.5"], 3, 24,27, 24,27, 0, ["AF","RO"],      "Validar requerimientos con usuarios clave"),
 ("3.1", ["2.6"],       5, 27,32,   27,32,   0,  ["JP","AF"],       "Elaborar y emitir el RFI"),
 ("3.2", ["3.1"],       5, 32,37,   32,37,   0,  ["JP","AF"],       "Analizar respuestas y lista corta"),
 ("3.3", ["3.2"],       7, 37,44,   37,44,   0,  ["JP","AF","ES"],  "Elaborar y emitir el RFP"),
 ("3.4", ["3.3"],       8, 44,52,   44,52,   0,  ["JP","AF","EI","ES"], "Evaluar propuestas tecnicas y economicas"),
 ("3.5", ["3.4"],       6, 52,58,   52,58,   0,  ["JP"],            "Negociar y firmar el contrato"),
 ("4.1", ["3.5"],      10, 58,68,   58,68,   0,  ["CP","AF"],       "Configurar flujos, estados y roles"),
 ("4.2", ["4.1"],       6, 68,74,   77,83,   9,  ["CP","AF"],       "Parametrizar matriz impacto/urgencia y SLA"),
 ("4.3", ["4.2"],       8, 74,82,   83,91,   9,  ["CP","AF"],       "Configurar el motor de asignacion"),
 ("4.4", ["3.5"],       7, 58,65,  107,114, 49,  ["RO"],            "Relevar y cargar la matriz de competencias"),
 ("4.5", ["3.5"],       8, 58,66,   83,91,  25,  ["UX"],            "Disenar y validar la experiencia de uso"),
 ("4.6", ["4.3","4.5"], 8, 82,90,   91,99,   9,  ["CP","UX"],       "Configurar la aplicacion de campo"),
 ("4.7", ["4.2"],       4, 74,78,   95,99,  21,  ["CP"],            "Configurar los tableros de indicadores"),
 ("5.1", ["4.1"],      10, 68,78,   68,78,   0,  ["EI"],            "Integrar con el SGOT"),
 ("5.2", ["5.1"],       8, 78,86,   78,86,   0,  ["EI"],            "Integrar con el CRM"),
 ("5.3", ["5.2"],       6, 86,92,   86,92,   0,  ["EI"],            "Integrar con la base de datos"),
 ("5.4", ["5.3"],       5, 92,97,   92,97,   0,  ["EI"],            "Integrar con el sistema de monitoreo (NMS)"),
 ("5.5", ["3.5"],       6, 58,64,   88,94,  30,  ["ES"],            "Implementar SSO y doble factor"),
 ("5.6", ["5.5"],       8, 64,72,   94,102, 30,  ["ES","EI"],       "Implementar minimo privilegio y baja automatica"),
 ("6.1", ["5.3"],       4, 92,96,   93,97,   1,  ["EI"],            "Migrar las ordenes de trabajo abiertas"),
 ("6.2", ["4.4"],       3, 65,68,  114,117, 49,  ["RO"],            "Cargar padron de tecnicos y datos maestros"),
 ("7.1", ["2.6"],       6, 27,33,   91,97,  64,  ["QA"],            "Disenar el plan y los casos de prueba"),
 ("7.2", ["4.6","4.7","7.1"], 8, 90,98, 99,107, 9, ["QA","AF"],     "Ejecutar las pruebas funcionales"),
 ("7.3", ["5.4","6.1","7.1"], 6, 97,103, 97,103, 0, ["QA","EI"],    "Ejecutar las pruebas de integracion"),
 ("7.4", ["7.3"],       4, 103,107, 103,107, 0,  ["QA"],            "Ejecutar las pruebas de carga"),
 ("7.5", ["5.6","7.1"], 5, 72,77,  102,107, 30,  ["ES","QA"],       "Ejecutar las pruebas de seguridad"),
 ("7.6", ["7.2","7.4","7.5"], 6, 107,113, 107,113, 0, ["CP","EI"],  "Corregir observaciones y volver a probar"),
 ("8.1", ["7.6","2.4"], 4, 113,117, 113,117, 0,  ["JP","RO"],       "Preparar el piloto"),
 ("8.2", ["8.1","6.2"],15, 117,132, 117,132, 0,  ["RO","CP"],       "Ejecutar el piloto en zona acotada"),
 ("8.3", ["8.2"],       8, 132,140, 132,140, 0,  ["CP","UX"],       "Ajustar reglas y experiencia de uso"),
 ("8.4", ["8.3"],       2, 140,142, 140,142, 0,  ["JP"],            "Informe de piloto y decision de avance"),
 ("9.1", ["7.2"],       8, 98,106,  134,142,36,  ["CA","AF"],       "Elaborar el material de capacitacion"),
 ("9.2", ["8.4","9.1"], 4, 142,146, 142,146, 0,  ["CA"],            "Capacitar a supervisores, despacho y NOC"),
 ("9.3", ["9.2"],      10, 146,156, 166,176,20,  ["CA"],            "Capacitar a los tecnicos de campo por olas"),
 ("9.4", ["9.3"],       3, 156,159, 176,179,20,  ["CA"],            "Evaluar la capacitacion"),
 ("10.1",["9.2"],       6, 146,152, 146,152, 0,  ["CP","RO"],       "Desplegar la ola 1"),
 ("10.2",["10.1"],      6, 152,158, 152,158, 0,  ["CP","RO"],       "Desplegar la ola 2"),
 ("10.3",["10.2"],      6, 158,164, 158,164, 0,  ["CP","RO"],       "Desplegar la ola 3"),
 ("11.1",["10.3"],     15, 164,179, 164,179, 0,  ["CP","RO"],       "Acompanar la operacion en estabilizacion"),
 ("11.2",["10.3"],      3, 164,167, 181,184,17,  ["EI"],            "Alta del CI en la CMDB y cierre ante el CAB"),
 ("11.3",["11.1","9.4"],5, 179,184, 179,184, 0,  ["JP","AF"],       "Transferir a operacion y documentar"),
 ("11.4",["11.2","11.3"],3,184,187, 184,187, 0,  ["JP"],            "Acta de cierre y lecciones aprendidas"),
]

# Corrimientos del aplanamiento adoptado (punto 10). id -> inicio nivelado
NIVEL = {
 "2.4":82, "4.7":90, "5.6":96, "4.4":97, "7.2":97, "7.5":104, "7.4":105,
 "9.1":105, "7.6":109, "8.1":115, "6.2":119, "8.2":122, "8.3":137, "8.4":145,
 "9.2":147, "9.3":151, "10.1":151, "10.2":157, "9.4":161, "10.3":163,
 "11.1":169, "11.2":169, "11.3":184, "11.4":189,
}

FASES = [
 ("1","Inicio"), ("2","Relevamiento y analisis"), ("3","Seleccion de proveedor"),
 ("4","Diseno y configuracion"), ("5","Integracion y seguridad"), ("6","Migracion de datos"),
 ("7","Pruebas"), ("8","Piloto"), ("9","Capacitacion"), ("10","Despliegue por olas"),
 ("11","Estabilizacion y cierre"),
]
