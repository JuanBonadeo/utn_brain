# Podcast CD 4 de 8 — Detección y corrección de errores: Hamming y códigos lineales

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

Distancia y redundancia, Hamming por zonas, las matrices G y H, el síndrome y la familia de errores de cada síndrome. Explicá por qué el mismo síndrome lo producen también errores de orden mayor y por qué igual se corrige el más probable.

## Contenido principal

### 5. Detección y corrección de errores

*Fuentes: apuntes 3 (Detección y Corrección de errores), 4 (Ejemplos de Códigos Lineales) y 2 (Hamming posicional).*

**Notación de esta sección**: $m$ dígitos de información, $k$ de control y $n = m + k$ en total. Los apuntes cambian de letras según el tema; acá va siempre igual.

#### 5.1 Distancia y redundancia

La **distancia** (de Hamming) es la **cantidad de dígitos en que difiere una palabra código de otra palabra del mismo código**: $d(100, 101) = 1$, $d(011, 100) = 3$. La **distancia mínima** $d_{min}$ es la menor entre todos los pares.

**El inconveniente de $d_{min} = 1$.** Un código de 3 dígitos que usa las 8 combinaciones tiene $d_{min} = 1$. Si mandás `100` y llega `101`, el receptor no se entera: `101` también es válida. **Ante un error simple, una palabra se convierte en otra del mismo código.** Ese código es compacto pero no detecta nada.

**La solución es la redundancia**: usar menos palabras que combinaciones, para que las sobrantes "absorban" los errores. El precio es rendimiento.

| $d_{min}$ | Detecta | Corrige | Ejemplo |
|---|---|---|---|
| 1 | nada | nada | las $2^n$ palabras |
| 2 | error simple | nada | **bit de paridad**: detecta todo error impar, no sabe dónde; $\eta = 3/4$ con 3 + 1 |
| 3 | hasta 2 errores | error simple | **Hamming (7,4)** |

Regla general *(conocimiento general)*: se detectan $d_{min} - 1$ errores y se corrigen $\lfloor (d_{min} - 1)/2 \rfloor$.

#### 5.2 Hamming

Hamming reparte la paridad **por zonas**, de modo que cada error simple altera una combinación distinta de controles. Con $k$ controles hay $2^k$ combinaciones, que tienen que alcanzar para cada uno de los $n$ dígitos más el caso "sin error":

$$2^k \ge m + k + 1$$

Con $m = 4$, $k = 3$ ($8 \ge 8$): palabra de 7 dígitos y $\eta = 4/7 = 0{,}571$. Para 9 a 16 mensajes siempre sale así.

**Versión de zonas (diagrama de Venn, apunte 3).** Cada control es la paridad par de los dígitos de información de su zona, y cada dígito de información está en una intersección distinta:

$$C_1 = I_0 \oplus I_1 \oplus I_2 \qquad C_2 = I_1 \oplus I_2 \oplus I_3 \qquad C_3 = I_0 \oplus I_2 \oplus I_3$$

**Ejemplo del apunte.** Se transmite $I_3 I_2 I_1 I_0\, C_3 C_2 C_1$ = `1000 110` y llega `1010 110`. Con la información recibida, 1010, los controles recalculados dan $C_3 C_2 C_1 = 101$; los recibidos eran 110. Fallan $C_1$ y $C_2$: el error está en $I_1$, y la información correcta es 1000. Si falla **un solo** control, el error está en ese control y la información está bien. Si no falla ninguno, la palabra es correcta.

**Versión posicional (apunte 2).** Los controles van en las posiciones 1, 2 y 4; cada uno mira las posiciones que tienen un 1 en su bit ($C_1$: {1, 3, 5, 7}; $C_2$: {2, 3, 6, 7}; $C_3$: {4, 5, 6, 7}). La ventaja es que **$C_3 C_2 C_1$, con 1 en cada zona alterada, da en binario la posición del error.** Ejemplo: se manda `1100110`, se invierte la posición 5 y llega `1100010`; fallan $C_1$ y $C_3$, y $101 = 5$.

| Posición | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Dígito | $C_1$ | $C_2$ | $i_0$ | $C_3$ | $i_1$ | $i_2$ | $i_3$ |

> **Ojo:** en la posicional se lee $C_3 C_2 C_1$, con $C_3$ como bit más significativo. Las dos versiones son de la cátedra y los finales piden "aplicando Hamming" sin decir cuál: decí cuál usás. Además, el apunte llama $n$ a los controles en Hamming y a la longitud total en códigos lineales: fijá la notación al empezar.

#### 5.3 Códigos lineales: G y H

Las $2^n$ palabras de $n$ dígitos forman un espacio vectorial con la suma sin acarreo ($1 + 1 = 0$). Un **código lineal** o **de grupo** $V$ es un **subespacio** de $2^m$ palabras. A diferencia de Hamming, no hay un campo de control separado: todos los dígitos viajan juntos.

| Objeto | Qué es | Tamaño |
|---|---|---|
| $V$ | código de grupo | $2^m$ palabras de $n$ dígitos |
| $G$ | **matriz generadora**: base de $V$ | $m \times n$ |
| $H$ | **matriz de control de paridad**: base del espacio ortogonal a $V$ | $k \times n$ |
| $S$ | síndrome | $1 \times k$ |

- Para que $G$ sea generadora, sus filas deben ser **linealmente independientes** y **generar $V$**. Toda palabra es una combinación $c_1 g_1 + \dots + c_m g_m$, con $c_j \in \{0, 1\}$. **La base no es única.**
- **Ortogonalidad**: $v \cdot H^T = 0$ para toda $v \in V$; equivale a $G\,H^T = 0$.

> **Ojo:** en el *multiple choice*, "linealmente independientes y generar **el** espacio vectorial". "Generar **todos** los espacios" es falso.

#### 5.4 El síndrome

El **síndrome** es el **resultado de multiplicar la palabra recibida, posiblemente con error, por la matriz de control de paridad transpuesta**: $S = v' \cdot H^T$. Si $S = 0$, la palabra está en el código: es correcta o tiene un error no detectable. Si $S \ne 0$, hubo error.

**Por qué el síndrome depende sólo del error.** Modelá el error como un vector $e$ con unos donde se invirtieron dígitos. Llega $v' = v \oplus e$:

$$S = (v \oplus e)\,H^T = \underbrace{v\,H^T}_{=\,0} \oplus\; e\,H^T = e\,H^T$$

No importa qué palabra se mandó: **el mismo error da siempre el mismo síndrome**. Por eso se arma una tabla síndrome → error y se corrige sumando el error.

**Condición para corregir error simple en los $n$ dígitos.** El error en el dígito $i$ da como síndrome la **columna $i$ de $H$**. Cada uno necesita un síndrome propio:

- hacen falta al menos $n$ síndromes no nulos: $2^k - 1 \ge n$;
- o sea, **las columnas de $H$ tienen que ser distintas y no nulas**.

Dos columnas iguales: ese síndrome **detecta pero no corrige**. Una columna nula: el error en ese dígito **no se detecta**.

#### 5.5 Familia de errores y errores no detectables

**Errores no detectables**: los que **coinciden con palabras del código**. Si $e \in V$, entonces $v \oplus e$ también está en $V$, el síndrome da 0 y el receptor acepta una palabra equivocada.

**Familia de un síndrome**: **todos los patrones de error que lo producen**, de cualquier orden. Son $2^m$ por síndrome, y se obtienen resolviendo $x \cdot H^T = S$. El decodificador elige el de **menor peso**, porque un error simple es mucho más probable que uno doble. Si en la familia hay un único vector de peso 1, se corrige; si hay varios de peso 2 y ninguno de peso 1, sólo se detecta.

**Ejemplo del apunte.** $G$ con filas 100011, 101101 y 111000 ($n = 6$, $m = 3$). Se calcula $V$, después el espacio ortogonal, y se elige $H$ con filas 011100, 011011 y 110110:

| Síndrome | 001 | 111 | 110 | 101 | 011 | 010 | 100 |
|---|---|---|---|---|---|---|---|
| Menor peso en la familia | 100000 | 010000 | 001000 | 000100 | 000010 | 000001 | 100100, 010010, 001001 |
| Qué hace | corrige $x_1$ | corrige $x_2$ | corrige $x_3$ | corrige $x_4$ | corrige $x_5$ | corrige $x_6$ | **sólo detecta** error doble |

Si llega `111011`, el síndrome es 001: el error está en $x_1$ y la palabra correcta es `011011`. La familia de 001 tiene 8 vectores: el simple en $x_1$, dobles, triples, cuádruples y un quíntuple.

> **Ojo:** en el *multiple choice*, la familia tiene "**todos** los errores de las palabras código asociadas a ese síndrome". Dos resúmenes de alumnos dicen "sólo simples y dobles": está mal. Y el apunte 4 rotula mal cuatro síndromes de este ejemplo (dice que 100 corrige $x_4$ y que 101 sólo detecta). La tabla de arriba está verificada enumerando los 64 vectores.

## Preguntas reales de teoría de los finales, con su respuesta

### 4. Detección y corrección de errores (códigos lineales)

#### 4.1 Distancia de un código e inconveniente de la distancia mínima 1
**Salió:** distancia en 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021; $d_{min}=1$ en las mismas cinco fechas (MC).

**Respuesta.**
- **Distancia** (de Hamming) entre dos palabras: **cantidad de dígitos que difieren entre una palabra código y otra palabra del mismo código**. Ejemplo: $d(100,101)=1$, $d(000,011)=2$, $d(011,100)=3$.
- **Distancia mínima** $d_{min}$: la menor distancia entre dos palabras distintas del código.
- **Inconveniente de $d_{min}=1$:** ante un **error simple** (cambia un bit), una palabra código **se convierte en otra palabra del mismo código**, así que el receptor no puede detectar el error. Es lo que pasa con el código "completo" de $n$ dígitos y $2^n$ palabras: es compacto (rendimiento 100 % si son equiprobables), pero no detecta nada. Por ejemplo, si se envía `100` y se recibe `101`, la palabra recibida también es válida.
- **Solución:** aumentar $d_{min}$ agregando redundancia (bit de paridad → $d_{min}=2$, que detecta error simple; Hamming → $d_{min}=3$, que corrige error simple). La redundancia baja el rendimiento: confiabilidad y economía tiran para lados opuestos.
- Regla general: detectar $e$ errores exige $d_{min}\ge e+1$; corregir $t$ errores exige $d_{min}\ge 2t+1$ (conocimiento general).

**En el MC:** distancia = "cantidad de dígitos que difieren entre una palabra código y otra palabra del mismo código" (no "consecutivas" ni "de dos códigos"). $d_{min}=1$ = "ante un error simple (el cambio de un bit) una palabra código se convierte en otra palabra **del mismo** código".

(teoria/3 - Detección y Corrección de errores.md)

#### 4.2 Matriz generadora y matriz de control de paridad
**Salió:** 28/08/2020, 10/09/2021 (MC "Para que una matriz sea generadora de un espacio vectorial debe…"); FAQ ("Cuál es la condición para obtener una base generadora de un código de grupo").

**Respuesta.** El conjunto de las $2^n$ palabras binarias de $n$ dígitos es un espacio vectorial (EV). Para tener $d_{min}>1$ se toma un **subespacio** $V$ de $2^m$ palabras ($m<n$): el **código de grupo** (código lineal binario).
- **Matriz generadora $G$** ($m\times n$): base de $V$. **Condición:** sus $m$ vectores deben ser **linealmente independientes** (ninguno es combinación lineal de los demás) y **generar el subespacio $V$**: toda palabra es $v=k_1g_1+\dots+k_mg_m$, con $k_j\in\{0,1\}$ y suma sin acarreo. **La base no es única.**
- **Matriz de control de paridad $H$** ($(n-m)\times n$): base del **espacio ortogonal** $V'$, con $n-m$ vectores linealmente independientes. Cumple $v\cdot H^T=0$ para toda $v\in V$ (y $v'\cdot G^T=0$).

**En el MC:** "Sus vectores deben ser linealmente independientes y generar el EV" (el subespacio del código). La opción "…y generar **todos** los EV (ortogonales)" es falsa: una base genera un único espacio.

(teoria/3 - Detección y Corrección de errores.md)

#### 4.3 Síndrome: concepto, aplicación y condición para corregir errores simples
**Salió:** concepto en 18/12/2020, 19/11/2021, 17/12/2021 (MC); FAQ ("Concepto de síndrome y aplicaciones. Ejemplo. Condiciones necesarias para corregir errores simples en cada uno de los dígitos de la palabra código", "¿Por qué el síndrome de una palabra con error coincide con el síndrome de la palabra que modela el error?").

**Respuesta.**
- **Síndrome:** resultado de multiplicar la **palabra recibida (posiblemente con error) por la matriz de control de paridad transpuesta**: $S = v^{*}\cdot H^T$. Dimensiones: $(1\times n)(n\times(n-m)) = 1\times(n-m)$.
- **Aplicación:** si $S=0$, la palabra pertenece al código de grupo (es correcta, o tiene un error no detectable). Si $S\ne 0$ hubo error, y el síndrome **identifica qué error fue** → se corrige sumándolo. Si hay ambigüedad, se usa máxima verosimilitud: la palabra del código a menor distancia de Hamming.
- **¿Por qué $S(v^{*})=S(e)$?** Modelando el error como una palabra $e$ con unos en las posiciones alteradas, $v^{*}=v\oplus e$:
$$S(v^{*})=(v\oplus e)\,H^T = \underbrace{v\,H^T}_{=0\ (v\in V)} \oplus\; e\,H^T = S(e)$$
El síndrome depende solo del error, no de la palabra transmitida. Por eso el mismo error en dos palabras distintas da el mismo síndrome.
- **Condición para corregir error simple en cada uno de los $n$ dígitos:** cada error simple $e_i$ debe dar un síndrome **distinto y no nulo**. Hacen falta al menos $n$ síndromes no nulos: $2^{n-m}-1\ge n$. Como $e_i H^T$ es la columna $i$ de $H$, eso equivale a que **las columnas de $H$ sean todas distintas y no nulas** (esto último es derivación propia). Si dos errores simples $e_a$ y $e_b$ dan el mismo síndrome, se **detecta** el error pero **no se corrige**.

**Ejemplo** (apunte): $v_1=101110$ y $v_2=111001$ con el error $e=000100$ → $v_1\oplus e=101010$ y $v_2\oplus e=111101$. Las dos dan el mismo $S=e\,H^T\neq0$ → error en el 4.º dígito; se corrige y se recupera $v_1$ y $v_2$.

**En el MC:** "El resultado de multiplicar una palabra **con error** por la matriz de **control de paridad transpuesta**". No es una palabra correcta (daría 0) ni la matriz generadora.

(teoria/3 - Detección y Corrección de errores.md)

#### 4.4 Familia de errores de cada síndrome; errores no detectables
**Salió:** familia en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC); FAQ ("En qué condiciones no se detecta y corrige un error").

**Respuesta.**
- **Errores no detectables:** los que **coinciden con palabras del código de grupo** (distintas de la nula). Como $e\in V$, $v\oplus e\in V$ y el síndrome sigue siendo 0: el receptor lo toma como palabra correcta. En el ejemplo del apunte (código de 8 palabras de 6 dígitos), no se detectan los errores triples y cuádruples cuyo patrón es una palabra del código (`101010`, `011011`, …).
- **Familia de un síndrome:** todos los patrones de error que producen ese mismo síndrome. Según el apunte, **todos los demás errores caen en alguna de las familias asociadas a cada síndrome**. En cada familia hay errores simples, dobles, múltiples, etc., y son $2^m$ patrones por síndrome: el error "representante" sumado a cada palabra del código (conocimiento general, *coclase*). Por eso el decodificador asume el de **menor peso** (el más probable).

**En el MC:** "**Todos** los errores de las palabras código asociadas a ese síndrome". No "solo simples" ni "solo simples y dobles".

(teoria/3 - Detección y Corrección de errores.md)
