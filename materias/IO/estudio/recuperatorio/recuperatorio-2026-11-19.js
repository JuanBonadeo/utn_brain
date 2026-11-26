/* Réplica de la parte práctica del recuperatorio de IO del 2026-11-19, con lo que marcó el alumno.
   La usa la pestaña Práctica de simulacro-teoria.html. */
window.RECUP_REAL = function(L){
  const N = L.NONE;
  const s = x => x.replace(/X(\d)/g,"X<sub>$1</sub>").replace(/y(\d)/g,"y<sub>$1</sub>").replace(/c(\d)/g,"c<sub>$1</sub>");

  /* ---- Ejercicio 1: gráfico ---- */
  const fig1 = (() => {
    const W=460,H=340,m={l:40,r:16,t:14,b:36}, X=16, Y=13;
    const sx=x=>m.l+x/X*(W-m.l-m.r), sy=y=>H-m.b-y/Y*(H-m.t-m.b);
    let g="";
    for(let x=0;x<=X;x++) g+=`<line class="gr" x1="${sx(x)}" y1="${sy(0)}" x2="${sx(x)}" y2="${sy(Y)}"/><text class="tk" x="${sx(x)}" y="${sy(0)+15}" text-anchor="middle">${x}</text>`;
    for(let y=1;y<=Y;y++) g+=`<line class="gr" x1="${sx(0)}" y1="${sy(y)}" x2="${sx(X)}" y2="${sy(y)}"/><text class="tk" x="${sx(0)-7}" y="${sy(y)+4}" text-anchor="end">${y}</text>`;
    g+=`<polygon class="rg" points="${[[2,0],[8,0],[6,3],[0,5],[0,4]].map(p=>sx(p[0])+","+sy(p[1])).join(" ")}"/>`;
    const ln=(a,b,c,d,lab,lx,ly)=>{ g+=`<line class="ln" x1="${sx(a)}" y1="${sy(b)}" x2="${sx(c)}" y2="${sy(d)}"/><text class="lb" x="${sx(lx)}" y="${sy(ly)}">${lab}</text>`; };
    ln(0,12,8,0,"R1",0.9,11); ln(0,5,15,0,"R2",1.9,4.6); ln(0,4,2,0,"R3",0.6,3.7); ln(8,0,8,13,"R4",8.5,12.2);
    g+=`<line class="ax" x1="${sx(0)}" y1="${sy(0)}" x2="${sx(X)}" y2="${sy(0)}"/><line class="ax" x1="${sx(0)}" y1="${sy(0)}" x2="${sx(0)}" y2="${sy(Y)}"/>`;
    g+=`<text class="tk" x="${(sx(0)+sx(X))/2}" y="${H-4}" text-anchor="middle">X₁</text><text class="tk" x="10" y="${(sy(0)+sy(Y))/2}" text-anchor="middle">X₂</text>`;
    return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Región factible limitada por R1, R2, R3 y R4">${g}</svg>`;
  })();
  const tbl = (head, rows, zr) => `<div class="tblwrap"><table class="spx"><tr>${head.map(h=>`<th>${h}</th>`).join("")}</tr>${rows.map(r=>`<tr>${r.map(c=>`<td>${c}</td>`).join("")}</tr>`).join("")}${zr?`<tr class="zr">${zr.map(c=>`<td>${c}</td>`).join("")}</tr>`:""}</table></div>`;

  const sol1 = `<div class="stack"><p>${s("Rectas leídas del gráfico: R1: 3X1 + 2X2 ≤ 24 · R2: X1 + 3X2 ≤ 15 · R3: 2X1 + X2 ≥ 4 · R4: X1 ≤ 8.")}</p>
    ${tbl(["Vértice","Se cortan","Z"],[["(2, 0)","R3 y eje","10"],["(8, 0)","R1, R4 y eje","40"],["<b>(6, 3)</b>","R1 y R2","<b>42</b>"],["(0, 5)","R2 y eje","20"],["(0, 4)","R3 y eje","16"]])}
    <p>${s("Rango de c1: el óptimo se mantiene mientras la pendiente de Z quede entre la de R2 (1/3) y la de R1 (3/2): 1/3 ≤ c1/4 ≤ 3/2, o sea 4/3 ≤ c1 ≤ 6.")}</p></div>`;

  /* ---- Ejercicio 2: simplex ---- */
  const VH = ["X1","X2","X3","X4","X5","X6","X7"].map(s);
  const head2 = ["C<sub>B</sub>","Base",...VH,"X<sub>i</sub>"];
  const intro2 = `<p>${s("Una cervecería artesanal de Rosario elabora la cerveza Rubia (X1), la cerveza Negra (X2) y la cerveza IPA (X3), medidas en hectolitros (hl). Las contribuciones unitarias están en $/hl y se busca maximizar la contribución total:")}</p>
    <p class="code">${s("Max Z = 30X1 + 40X2 + 15X3")}<br>${s("X1 + 2X2 + 4X3 ≤ 180")} &nbsp;(Lúpulo disponible, kg)<br>${s("X1 ≥ 70")} &nbsp;(Contrato mínimo de Rubia)<br>${s("X1 + X3 ≤ 140")} &nbsp;(Capacidad de envasado en lata, hl)<br>${s("X1, X2, X3 ≥ 0")}</p>
    <p>Una de las tablas de su resolución con Simplex es (C<sub>j</sub> = 30, 40, 15, 0, 0, 0, −M):</p>
    ${tbl(head2,[["40",VH[1],"0","1","2","1/2","1/2","0","−1/2","55"],["30",VH[0],"1","0","0","0","−1","0","1","70"],["0",VH[5],"0","0","1","0","1","1","−1","70"]])}`;
  const sol2 = `<div class="stack"><p>${s("X4 es la holgura del lúpulo, X5 el excedente del contrato, X7 su ficticia y X6 la holgura del envasado.")}</p>
    <p>Fila c<sub>j</sub> − z<sub>j</sub> de la tabla dada: ${s("X3: −65 · X4: −20 · X5: +10 · X7: −M − 10. Entra X5. Cocientes: 55/(1/2) = 110 y 70/1 = 70: sale X6.")}</p>
    <p>Tabla óptima:</p>
    ${tbl(head2.slice(0,8).concat(["X<sub>i</sub>"]),[["40",VH[1],"0","1","3/2","1/2","0","−1/2","20"],["30",VH[0],"1","0","1","0","0","1","140"],["0",VH[4],"0","0","1","0","1","1","70"]],["","c<sub>j</sub>−z<sub>j</sub>","0","0","−75","−20","0","−10","Z = 5000"])}
    <p>${s("Precios sombra: y1 = 20 (lúpulo), y2 = 0 (contrato), y3 = 10 (envasado).")}</p></div>`;

  /* ---- Ejercicio 3: stock ---- */
  const mini = (kind) => {
    const W=150,H=84, ax=`<path d="M14 6V70H146" fill="none" stroke="currentColor" stroke-width="1.2"/>`;
    const dash = x=>`<line x1="${x}" y1="8" x2="${x}" y2="70" stroke="currentColor" stroke-width=".8" stroke-dasharray="3 3" opacity=".6"/>`;
    const lab = (x,t)=>`<text x="${x}" y="81" font-size="9" text-anchor="middle" fill="currentColor">${t}</text>`;
    const st = `fill="none" stroke="currentColor" stroke-width="1.8"`;
    let p="";
    if(kind==="a") p=dash(46)+lab(46,"1000")+`<path d="M14 22L46 12C60 44 82 62 108 62C122 62 134 58 144 54" ${st}/>`;
    if(kind==="b") p=dash(80)+lab(80,"2500")+`<path d="M14 40L80 12C98 34 118 56 144 62" ${st}/>`;
    if(kind==="c") p=dash(46)+lab(46,"1000")+`<path d="M14 18L46 12" ${st}/><path d="M46 66L144 44" ${st}/>`;
    if(kind==="d") p=dash(46)+lab(46,"1000")+`<path d="M14 18L46 12" ${st}/><path d="M48 24C58 48 80 62 106 62C122 62 134 58 144 54" ${st}/>`;
    return `<svg viewBox="0 0 ${W} ${H}" width="150" height="84" role="img" aria-label="Gráfico ${kind} de CT(Q)" style="vertical-align:middle">${ax}${p}</svg>`;
  };
  const sol3 = `<div class="stack"><p>Descuento sobre el <b>excedente</b>, con costo de pedido nulo. El precio medio es C(Q) = 10 + 2000/Q: las primeras 1000 unidades funcionan como un costo fijo de $2000 por pedido.</p>
    <p class="code">Q ≤ 1000: CT = 120000 + 1,5·Q<br>Q &gt; 1000: CT = 100000 + 20.000.000/Q + 1,25·Q + 250</p>
    <p>En Q = 1000 las dos ramas valen 121500: la curva es continua. Q* = √(20.000.000 / 1,25) = 4000 y CT(4000) = 100000 + 5000 + 5000 + 250 = 110250.</p></div>`;

  return { id:"real-2026-11-19", title:"Recuperatorio 2026-11-19", ejs:[
  { intro:`<p>${s("La región sombreada de la figura es la región factible de un problema de programación lineal con X1, X2 ≥ 0 y función objetivo Max Z = 5X1 + 4X2.")}</p>`, fig:fig1, sol:sol1,
    lead:"Resuelva gráficamente (método de la recta de isobeneficio) y responda (una sola opción):", qs:[
    {q:"¿Cuál es la solución óptima?",
     opts:[s("X1 = 0, X2 = 5; Z = 20"),s("X1 = 8, X2 = 0; Z = 40"),s("X1 = 6, X2 = 3; Z = 42"),s("X1 = 15, X2 = 0; Z = 75"),N], a:2, prev:2,
     x:"Vértices: (8, 0) → 40; (6, 3) → 42; (0, 5) → 20. El mayor está en (6, 3), donde se cortan R1 y R2. (15, 0) queda fuera de la región: no cumple R1 ni R4."},
    {q:"¿Cuál es el valor de la variable de holgura/excedente de R3 en el óptimo?",
     opts:["15","−11","0","4",N], a:4, prev:1,
     x:s("R3 es 2X1 + X2 ≥ 4, de mayor o igual: tiene excedente, y vale 2·6 + 3 − 4 = 11. No figura. Marcaste b) −11: es el mismo número con el signo al revés, y una variable de excedente nunca es negativa en un punto factible.")},
    {q:s("Manteniendo c2 = 4, ¿en qué rango puede variar c1 sin que cambie la solución óptima?"),
     opts:["[8/3, 12]","[4/3, 6]","[4/3, +∞)","[0, 6]",N], a:1, prev:3,
     x:s("La pendiente de Z tiene que quedar entre la de R2 (1/3) y la de R1 (3/2): 1/3 ≤ c1/4 ≤ 3/2, o sea [4/3, 6]. Marcaste d) [0, 6]: el límite superior está bien, pero con c1 menor que 4/3 el óptimo se muda a (0, 5).")}
  ]},
  { intro:intro2, fig:"", sol:sol2, lead:"Resuelva y responda (una sola opción):", qs:[
    {q:"¿Qué tipo de solución representa la tabla presentada?",
     opts:[s("Óptima, porque todas las variables de decisión tienen C<sub>j</sub> − Z<sub>j</sub> ≤ 0."),s("No factible, porque la columna de la artificial X7 tiene coeficientes no nulos."),"Factible para el problema original, pero no óptima.","Degenerada, porque una variable básica vale cero.",N], a:2, prev:3,
     x:s("X7 no está en la base: la solución es factible para el problema original. No es óptima porque el cj − zj de X5 es +10. Marcaste d): ninguna básica vale cero (55, 70 y 70). La a) es la trampa: mira sólo las variables de decisión y se olvida de X5.")},
    {q:"¿Qué cambio en el plan de producción introduce la siguiente iteración del Simplex?",
     opts:[s("Ingresa X2 y sale X7: se incrementa la elaboración de la cerveza Negra y se elimina la artificial."),s("Ingresa X5 y sale X2: la cerveza Rubia supera el contrato mínimo y se deja de elaborar la cerveza Negra."),s("Ingresa X3 y sale X6: se comienza a elaborar la cerveza IPA y se agota la capacidad de envasado en lata."),s("Ingresa X5 y sale X6: la cerveza Rubia supera el contrato mínimo y se agota la capacidad de envasado en lata."),N], a:3, prev:3,
     x:s("Entra X5, el único cj − zj positivo. Cocientes: 55/(1/2) = 110 y 70/1 = 70; la fila de X1 tiene −1 y no participa. Sale X6.")},
    {q:"Si la contribución de la cerveza Negra bajara a $25/hl, ¿qué ocurre con la solución óptima?",
     opts:["Cambia la base: deja de convenir elaborar la cerveza Negra.","Se mantiene la solución y Z = 4700.","Se mantiene la solución y Z no cambia.","Cambia la base: conviene comenzar a elaborar la cerveza IPA.",N], a:1, prev:1,
     x:s("X2 es básica en la óptima. Con c2 genérico los cj − zj quedan X3: −15 − (3/2)c2 · X4: −c2/2 · X6: c2/2 − 30. Todos ≤ 0 si 0 ≤ c2 ≤ 60. Con 25 la solución se mantiene y Z = 30·140 + 25·20 = 4700.")},
    {q:"Se evalúa elaborar una cerveza de Trigo, con una contribución de $80/hl, que consume 3 kg de lúpulo por hl y se envasa en lata. ¿Conviene?",
     opts:["No: consume más lúpulo por hl que la cerveza Rubia.","No: su costo reducido es −10.","Es indiferente: su costo reducido es 0.","Sí: su costo reducido es +10.",N], a:3, prev:1,
     x:s("zj = 3·y1 + 0·y2 + 1·y3 = 3·20 + 10 = 70. cj − zj = 80 − 70 = +10: conviene. Marcaste b) −10: es zj − cj, la resta al revés.")},
    {q:"En la solución óptima del problema dual, ¿qué variable dual es nula y por qué?",
     opts:[s("y1, porque la holgura X4 no es básica."),"Ninguna: todas las restricciones del primal están activas.",s("y3, porque la holgura X6 no es básica."),s("y2, porque la restricción del contrato mínimo no está activa en el óptimo."),N], a:3, prev:4,
     x:s("En el óptimo X1 = 140 > 70: el contrato no está activo, su excedente X5 es básico y por holguras complementarias y2 = 0. Las otras dos restricciones están activas, con y1 = 20 e y3 = 10.")}
  ]},
  { intro:`<p>Un distribuidor mayorista de yerba mate vende 10000 paquetes por año. Los pedidos de abastecimiento los realiza a una molinera a través de un portal electrónico y sin cargo de envío. En cada pedido, las primeras 1000 unidades cuestan $12 cada una y el resto, $10 cada una. El costo de mantener inventario es del 25 % anual.</p>`, fig:"", sol:sol3,
    lead:"Resuelva y responda (una sola opción):", qs:[
    {q:"¿Qué gráfico representa CT(Q)?",
     opts:[mini("a"),mini("b"),mini("c"),mini("d"),N], a:0, prev:3,
     x:"Hasta 1000 no hay costo de pedido y sólo crece el de mantener: una recta creciente. Después el costo sigue sin salto y forma una curva con mínimo. Marcaste d): el salto en 1000 es propio del descuento sobre todo el lote; acá el descuento es sólo sobre el excedente y el costo es continuo."},
    {q:"¿Cuál es el lote óptimo de pedido?",
     opts:["4000 unidades","3651 unidades","2828 unidades","1000 unidades",N], a:0, prev:1,
     x:"Para Q > 1000: CT = 100000 + 20.000.000/Q + 1,25·Q + 250, y Q* = √(20.000.000/1,25) = 4000. Marcaste b) 3651: sale de valuar el stock a $12 en vez de $10."},
    {q:"¿Cuánto se ahorra por año con el lote óptimo respecto de pedir exactamente 1000 unidades cada vez?",
     opts:["$11250","$9750","$21500","$5250",N], a:0, prev:4,
     x:"CT(1000) = 120000 + 1500 = 121500. CT(4000) = 100000 + 5000 + 5000 + 250 = 110250. Ahorro: 11250."},
    {q:"Considerando 365 días por año, ¿cada cuántos días se emite un pedido?",
     opts:["37 días","146 días","183 días","91 días",N], a:1, prev:3,
     x:"10000/4000 = 2,5 pedidos por año → 365/2,5 = 146 días. 37 días es el período de pedir de a 1000."}
  ]}
  ]};
};
