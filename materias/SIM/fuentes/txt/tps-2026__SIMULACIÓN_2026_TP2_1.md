TP 2.1 - GENERADORES PSEUDOALEATORIOS
JuanI.Torres
UniversidadTecnológicaNacional-FRRO
Zeballos1341,S2000,Argentina
orkuan@gmail.com
29demayo,2026
ABSTRACT
El siguiente documento tiene por objetivo detallar el trabajo de clase que debe realizarse para
introducirnosenunodeloselementosfundamentalesparagranpartedelassimulaciones,estoson
losgeneradoresdenúmerospseudoaleatorios.
Keywords Simulación·generadorespseudoaleatorios
1 Introducción
Unnúmeropseudoaleatorioesunnúmerogeneradoenunprocesoquepareceproducirnúmerosalazar,peronolo
hacerealmente. Lassecuenciasdenúmerospseudoaleatoriosnomuestranningúnpatrónoregularidadaparentedesde
unpuntodevistaestadístico,apesardehabersidogeneradasporunalgoritmocompletamentedeterminista,antelas
mismascondicionesinicialesproducensiempreelmismoresultado.
2 Descripcióndeltrabajo
EltrabajodeinvestigaciónconsisteenconstruirprogramasenlenguajePython3.xquegenerennúmerospseudoaleatorios
yqueestossecomportencomoseespera. Paraestosedebetenerencuentalosiguientestemasainvestigar:
• Generadoresdenúmerosaleatoriosreales.
• Generadoresdenúmerospseudoaleatorios(Métododeloscuadrados,GCLs,otros).
• Testparadeterminarelcomportamientodelosgeneradores.
SepideprogramaralmenosdosgeneradoresdenúmerospseudoaleatoriosenparticularelgeneradorGCLdelcual
sedebetestearconalmenoscuatropruebasparadeterminarlacalidaddegeneración. Tambiénsepidecompararlos
generadoresprogramadosconotros(incluyendoelqueposeeellenguajePython).
AmododeintroducciónyejemplosdecódigosedejaunlinkenlaseccióndeRecursosonlineobligatorios.
2.1 Exposicióndelosresultadosyanálisisdelosmismos
Losresultadossedebenanalizaryluegoconcluirsobresucomportamientoobtenidoyesperado.
Seaconsejaelusodetablasparamostrarlosdatosdelosdistintosgeneradoresypruebas. Enotroscasospuedesermás
convenienteselusodeimágenes. Verlossiguientesejemplos:
2.2 Presentacióndeltrabajoyentrega
EstetrabajodeinvestigaciónyaligualquelosanterioressedebepresentarobligatoriamenteenformatoLATEX.
Elcontenidomínimoaentregares:

| Generador | TipodeGenerador                 | TestX TestY | ... |
| --------- | ------------------------------- | ----------- | --- |
| GCL       | Pseudoaletorio                  | 0.4 OK      | ... |
| ERNIE     | Aleatorio                       | 0.2 ERROR   | ... |
| ...       | ...                             | ... ...     | ... |
| Tabla1:   | Ejemplodeexposiciónderesultados |             |     |
Figura1: Comparaciónentrevaloresdedosgeneradoresdistintos. Imagentomadadehttp://www.random.org/analysis/.
• CódigocompletoenPython3.x. conlosgeneradoresytests.
• InformeenformatoLatexconintroducción,gráficas,fórmulasempleadas,conclusiones,referencias(hayun
apartadoparaesto)ycualquierotrainformaciónquesequieraagregar.
3 Recursosonlineobligatorios
VolveremosausareltemplateLATEXdelaCornellUniversityporsusencillez:
https://es.overleaf.com/latex/templates/style-and-template-for-preprints-arxiv-bio-arxiv/
pkzcrhzcdxmc
Unresumenquevaaayudaraencontrarmuchaotrainformación:
https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html
Acáencontraráninformacióndevariostipostestsquepuedenrealizarse:
https://www.random.org/analysis/
Serecomiendaleercondetenimientoelsiguienteinforme:
https://www.random.org/analysis/Analysis2005.pdf
4 Recursosonlinesugeridos
https://www.youtube.com/watch?v=FtEe0IlK6Hc
2