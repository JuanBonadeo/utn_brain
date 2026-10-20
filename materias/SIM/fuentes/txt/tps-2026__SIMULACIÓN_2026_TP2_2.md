TP 2.2 - GENERADORES DE NÚMEROS PSEUDOALEATORIOS DE
DISTINTAS DISTRIBUCIONES DE PROBABILIDAD
JuanI.Torres
UniversidadTecnológicaNacional-FRRO
Zeballos1341,S2000,Argentina
orkuan@gmail.com
12demayo,2026
ABSTRACT
Elsiguientedocumentotieneporobjetivodetallareltrabajoquedeberealizarseparafinalizarcon
nuestro estudio sobre los números pseudoaleatorios del cual van a depender nuestros próximos
experimentos.
Keywords Simulación·generadorespseudoaleatorios·distribucionesdeprobabilidad
1 Introducción
Elestudioanterioraeste,demostróquelageneracióndenúmerospseudoaleatoriosnoesunatareasencilla. Porsuerte
paranosotrosesuntemafelizmenteresueltoparanuestrasnecesidades. Ahoraquetenemosungeneradortesteado,
eshoradeempezarautilizarlo. Elproblemasurgecomohacerlo. Siloempleamostalycomoestá,estesologenera
valoresuniformescontinuosentre0y1.
ComonosotroshemosaprendidoenlamateriaProbabilidadyEstadística,hayotrasdistribucionesdeprobabilidadtanto
continuascomodiscretas. Lapreguntaquedebemosresponderes: ¿cómohacemosparagenerarvaloresdedistintas
distribuciones?. Labuenanoticiaesquelasoluciónyahasidoinventadayesnuestratareacomoingenierosredescubrir
elmecanismoparaimplementarloennuestrosexperimentos.
Porlotantoelobjetivodeestetrabajoesconstruirgeneradoresdenúmerospseudoaleatoriosdedistintasprobabilidades
pormediodeunmaterialantiguoperosumamenteprácticoqueeselelaboradoporelautorThomasNaylor[1].
2 Descripcióndeltrabajo
Eltrabajoconsisteenhacerunestudiodelasdistintasdistribucionesdeprobabilidad,queaunquenosontodaslasque
existen,lasmismasabarcanunagrancantidaddelosfenómenosdeinterésparalasimulación. Decadaunasedeben
realizardistintastareascomosedetallaacontinuación:
• Introducir la distribución de probabilidad en forma teórica; se deben incluir su/s parámetro/s de entrada,
funcióndeprobabilidad,gráficas,etc.
• Describirmatemáticamenteelpasoapasoparalaobtencióndesufunciónacumuladaeinversa.
• ElaborarunprogramaporcadadistribucióndeprobabilidadenlenguajePython3.x.
• Testearlageneracióndevaloresdelaformamásconvenienteparacadacaso(quedaacriteriodelgrupoel
comotestear).
Enestetrabajoesnecesariomostrarelcódigoenelinforme,porlotantosebrindaelsiguienteejemplodeformatopara
presentarloenLatex(haymuchainformacióndisponibledecomorealizaresto):

| 1 from math | import | *   |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- |
2
| 3 # define | function |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
4 def analytic_fibonacci(n):
| 5 sqrt_5 | = sqrt(5);   |         |          |         |     |     |
| -------- | ------------ | ------- | -------- | ------- | --- | --- |
| 6 p =    | (1 + sqrt_5) | / 2;    |          |         |     |     |
| 7 q =    | 1/p;         |         |          |         |     |     |
| 8 return | int( (p**n   | + q**n) | / sqrt_5 | + 0.5 ) |     |     |
9
| 10 # define | range                 |     |     |     |     |     |
| ----------- | --------------------- | --- | --- | --- | --- | --- |
| 11 for i    | in range(1,31):       |     |     |     |     |     |
| 12 print    | analytic_fibonacci(i) |     |     |     |     |     |
Código1: SecuenciadeFibonaccicalculadaanalíticamentecomoejemplodeinsercióndecódigoPythonenelinforme.
Finalmentepararesumiryteniendoencuentaelordendetemasenlabibliografíaseleccionada,sesugiererepasarla
siguientetablaparaincorporarelcontenidoquedebeestarenelinforme:
DistribucióndeProbabilidad Tipo T.Inversa M.Rechazo Código Testeo
|     | UNIFORME         |         | continua | si  | si  | si si |
| --- | ---------------- | ------- | -------- | --- | --- | ----- |
|     | EXPONENCIAL      |         | continua | si  | si  | no si |
|     |                  | GAMMA   | continua | si  | no  | no no |
|     |                  | NORMAL  | continua | si  | si  | si si |
|     |                  | PASCAL  | discreta | si  | no  | no no |
|     | BINOMIAL         |         | discreta | si  | no  | no si |
|     | HIPERGEOMÉTRICA  |         | discreta | si  | no  | no no |
|     |                  | POISSON | discreta | si  | no  | no si |
|     | EMPÍRICADISCRETA |         | discreta | si  | no  | no si |
Tabla1: Listadodedistribucionesytareasarealizarconcadauna.
2.1 Presentacióndeltrabajoyentrega
EstetrabajodeinvestigaciónyaligualquelosanterioressedebepresentarobligatoriamenteenformatoLATEX.
Elcontenidoaentregares:
• InformeenformatoLatexconintroducción,gráficas,fórmulasempleadas,conclusiones,referencias(hayun
apartadoparaesto)ycualquierotrainformaciónquesequieraagregarrelevantealainvestigación.
3 Recursosonlineobligatorios
VolveremosausareltemplateLATEXdelaCornellUniversity,peroseadjuntaundocumentocomoejemplodeinserción
decódigoPythonenelinformeyelcapítulo4deellibroTécnicasdeSimulaciónenComputadoras[1]:
https://es.overleaf.com/latex/templates/style-and-template-for-preprints-arxiv-bio-arxiv/
pkzcrhzcdxmc
References
| [1] Naylor,T.H. | Técnicasdesimulaciónencomputadoras,1982. |     |     |     |     |     |
| --------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
2