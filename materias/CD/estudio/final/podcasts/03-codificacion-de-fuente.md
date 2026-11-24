# Podcast CD 3 de 8 — Codificación de fuente: Kraft, longitud media y Huffman

Fuente para un episodio de podcast de estudio. Materia: Comunicación de Datos (UTN Facultad
Regional Rosario, Ingeniería en Sistemas, 3.er año). Sirve para rendir el final: tres problemas
de práctica y tres preguntas de teoría para desarrollar. Las respuestas de las preguntas son
respuestas modelo armadas por nosotros a partir de los apuntes de la cátedra, no la corrección
oficial.

## Indicaciones para el episodio

La jerarquía de códigos (no singular, unívoco, instantáneo, compacto) con ejemplos, la inecuación de Kraft, la cota inferior de la longitud media y el método de Huffman. Es la pregunta de teoría que salió en todos los finales: armá la respuesta modelo en voz alta.

## Contenido principal

### 4. Codificación de fuente

*Fuentes: apunte 2 (Codificación), Ejercitación Codificación y "Fórmulas y pasos". Kraft y la cota inferior salieron en los 6 finales de teoría.*

#### 4.1 La jerarquía de códigos

**Codificar** es poner en correspondencia las secuencias del **alfabeto fuente** $S = \{s_1, \dots, s_q\}$ con secuencias del **alfabeto código** $Z = \{z_1, \dots, z_r\}$ ($r = 2$: binario).

- **Código bloque**: asigna a **cada símbolo del alfabeto fuente una secuencia fija de símbolos del alfabeto código**.
- **Palabra código**: cada una de esas **secuencias fijas de símbolos código**.

Las clases se van anidando, cada una más exigente que la anterior:

| Clase | Definición del apunte | Ejemplo | Por qué |
|---|---|---|---|
| **No singular** | **todas sus palabras son distintas** | 1, 11, 00, 10 | no es unívoco: `1100` puede ser $s_2 s_3$ o $s_1 s_1 s_3$ |
| **Unívoco** | **a cualquier secuencia de palabras código le corresponde una y sólo una secuencia de símbolos fuente** | 0, 01, 011, 0111 | no es instantáneo: al recibir `01` hay que esperar el dígito siguiente |
| **Instantáneo** | cada palabra se decodifica **sin esperar la llegada de la próxima palabra código** | 1, 01, 001, 0001 | ninguna palabra es prefijo de otra |
| **Compacto** | instantáneo de longitud media mínima (§4.4) | 0, 10, 110, 111 para 1/2, 1/4, 1/8, 1/8 | $L = H$ |

- **Condición necesaria y suficiente de instantáneo**: **ninguna palabra es prefijo de otra**.
- Todo código no singular de **longitud constante** es unívoco (y también instantáneo: 00, 01, 10, 11).

> **Ojo:** "a cualquier **palabra** código le corresponde un único símbolo" define un código **no singular**; el unívoco habla de **secuencias**. La condición de instantáneo es "prefijo", no "terminación". En el examen, poné un ejemplo distinto para cada clase.

#### 4.2 Inecuación de Kraft (y McMillan)

**Teorema de Kraft.** La inecuación

$$\sum_{i=1}^{q} r^{-l_i} \le 1$$

es condición **necesaria y suficiente** para que **exista al menos un** código instantáneo $r$-ario con palabras de longitudes $l_1, \dots, l_q$.

Para entenderla, pensá el código binario como un árbol. Cada palabra es un camino desde la raíz, y una palabra de longitud $l$ "ocupa" la fracción $2^{-l}$ del árbol. En un código instantáneo ninguna palabra cuelga de otra: son todas hojas. Kraft dice que **las hojas no pueden ocupar más que el árbol entero**. Con 0, 10 y 110 la suma da $1/2 + 1/4 + 1/8 = 7/8$: sobra la hoja 111.

**El matiz que se toma: el teorema habla de longitudes, no de un código concreto.**

- `0, 00, 11` (longitudes 1, 2, 2): $2^{-1} + 2^{-2} + 2^{-2} = 1$. **Cumple Kraft y no es instantáneo**, porque `0` es prefijo de `00`.
- `0, 10, 11` tiene **las mismas longitudes** y sí es instantáneo. Kraft garantiza que existe uno, no que el que te dieron lo sea.
- Si las longitudes **no** cumplen Kraft, no hay ningún instantáneo con ellas. Ejemplo: 1, 2, 2, 3 da $9/8 > 1$.

**McMillan.** La misma inecuación es condición necesaria y suficiente para que exista un código **unívoco**. Consecuencia: pasar de instantáneo a unívoco no permite acortar las palabras.

> **Ojo:** en el *multiple choice*, "un código que cumple Kraft **puede ser** instantáneo". No "es instantáneo", ni "es unívoco", ni "es compacto". Un resumen de alumnos la llama "condición necesaria" a secas: el apunte dice **necesaria y suficiente** para la existencia.

#### 4.3 Longitud media y su cota inferior

La **longitud media** es el promedio de dígitos por símbolo:

$$L = \sum_i P_i\, l_i \quad [\text{dígitos } r\text{-arios por símbolo}]$$

Para achicarla, **a mayor probabilidad, menor longitud**.

**Teorema de la cota inferior.** Para todo código instantáneo (y, por McMillan, todo unívoco) de una fuente de memoria nula:

$$L \;\ge\; H_r(S) = \frac{H(S)}{\log_2 r} \qquad (r = 2:\ L \ge H(S))$$

$H_r(S)$ es la entropía medida en dígitos $r$-arios. **Ningún código usa menos dígitos por símbolo que la información que trae cada símbolo.**

- **Igualdad** sólo si las probabilidades son potencias de $1/r$: $P_i = r^{-l_i}$. Ejemplo del apunte: 1/2, 1/8, 1/8, 1/8, 1/8 con 0, 100, 101, 110, 111 da $L = H = 2$.
- **Si no son potencias**, se codifica la **extensión de orden $n$** (los símbolos de a $n$). Es el **primer teorema de Shannon**: $H_r(S) \le L_n/n < H_r(S) + 1/n$. El costo es la complejidad. Ejemplo: fuente 0,7 / 0,3 ($H = 0{,}881$); de a uno, $L = 1$; de a dos, $L_2/2 = 0{,}905$.

**Idea de la demostración**: con $\ln z \le z - 1$ se llega a $H(S) \le L \log_2 r + \log_2 \sum_j r^{-l_j}$, y por Kraft el último término es $\le 0$. El desarrollo completo está en la wiki.

> **Ojo:** en el *multiple choice*, la cota "expresa el límite **inferior** de la longitud media, que es igual o mayor a la entropía **$r$-aria** de la fuente". "Límite superior" es falso.

#### 4.4 Código compacto y método de Huffman

**Código compacto** (definición del apunte): un código **instantáneo** cuya longitud media es **igual o menor que la de todos los códigos instantáneos que puedan aplicarse a la misma fuente y al mismo alfabeto**. Su ventaja: transmite la menor cantidad de dígitos por símbolo, y eso ahorra tiempo, ancho de banda y costo.

**Método de Huffman** (construye un compacto):

1. Ordená los símbolos de mayor a menor probabilidad.
2. Fundí los dos menos probables en uno, con la suma de sus probabilidades, y reordená. Repetí hasta que queden dos.
3. Asigná 0 y 1 a esos dos.
4. Volvé hacia atrás: cada símbolo que venía de una fusión le pasa su palabra a sus dos componentes, que agregan un 0 y un 1.

**Ejemplo de la cátedra:** 0,4 / 0,3 / 0,1 / 0,1 / 0,06 / 0,04.

| Paso | Probabilidades (entre paréntesis, lo fundido) |
|---|---|
| Fuente | 0,4 · 0,3 · 0,1 · 0,1 · 0,06 · 0,04 |
| Reducción 1 | 0,4 · 0,3 · 0,1 · 0,1 · (0,1 = $s_5 + s_6$) |
| Reducción 2 | 0,4 · 0,3 · (0,2 = $s_3 + s_4$) · 0,1 |
| Reducción 3 | 0,4 · 0,3 · (0,3 = 0,2 + 0,1) |
| Reducción 4 | (0,6 = 0,3 + 0,3) → **0** · 0,4 → **1** |

Hacia atrás, el 0,6 se abre en $s_2$ = 00 y 0,3 = 01; ese 01 se abre en 0,2 = 010 y 0,1 = 011; y así:

| $s_i$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ | $s_6$ |
|---|---|---|---|---|---|---|
| $P_i$ | 0,4 | 0,3 | 0,1 | 0,1 | 0,06 | 0,04 |
| Palabra | 1 | 00 | 0100 | 0101 | 0110 | 0111 |

$$L = 0{,}4 \cdot 1 + 0{,}3 \cdot 2 + (0{,}1 + 0{,}1 + 0{,}06 + 0{,}04) \cdot 4 = 2{,}2 \text{ binit/símbolo}$$

Con $H = 2{,}1435$ bit, el rendimiento es $\eta = 0{,}974$. El apunte demuestra por inducción que Huffman es compacto: si una reducción es compacta, la anterior también, y la última (0 y 1) lo es trivialmente.

**Huffman $r$-ario.** Se funden los $r$ menos probables en cada paso, así que cada reducción tiene $r - 1$ símbolos menos. Para terminar con exactamente $r$, la cantidad de símbolos $\omega$ tiene que cumplir $\omega = r + \alpha (r - 1)$ con $\alpha$ entero. Si no, se agregan **símbolos falsos de probabilidad 0** y al final se descartan. Ejemplo: 6 símbolos en ternario dan $\alpha = 1{,}5$; con un falso son 7 y $\alpha = 2$. En binario no hacen falta nunca.

**Rendimiento y redundancia:**

$$\eta = \frac{H_r(S)}{L} \le 1 \qquad \text{redundancia} = 1 - \eta$$

> **Ojo:** "¿puede haber otro instantáneo con menor longitud media?": **no**, Huffman es compacto; puede haber otro distinto con la **misma** $L$ si hay empates. En $r$-ario, $\eta$ se calcula con $H_r$, no con $H$ en bits. Y el apunte tiene una errata en la reducción 1: imprime "0,1 − 001" donde va **011**.

**Ejercicio tipo** (final 09/03/2012, código dado). Para A = 0 (27/64); B, C, D = 100, 101, 110 (9/64); E, F, G = 11100, 11101, 11110 (3/64); H = 11111 (1/64): es **instantáneo** (ninguna palabra es prefijo de otra); $L = 158/64 = 2{,}469$; Kraft da exactamente **1** (árbol completo); $H = 2{,}434$, así que $\eta = 0{,}986$; y es **compacto**, porque Huffman da las mismas longitudes.

#### 4.5 Cómo contestar "propiedades de los códigos" (final 2025)

1. Definí código bloque y palabra código.
2. Recorré la jerarquía (Figura 5) con un ejemplo por clase y la condición de prefijo.
3. Kraft: enunciado, el matiz de "existe" con `0, 00, 11` contra `0, 10, 11`, y McMillan en una línea.
4. Longitud media y cota inferior: $L \ge H_r(S)$, cuándo vale la igualdad y la extensión de orden $n$.
5. Compacto: definición textual, ventaja, y que Huffman lo construye.

## Preguntas reales de teoría de los finales, con su respuesta

### 3. Codificación de fuente

> Bloque más preguntado. En el MC las opciones difieren en una palabra: hay que saber la definición textual del apunte.

#### 3.1 Código bloque y palabra código
**Salió:** código bloque en 18/12/2020; palabra código en 28/08/2020, 10/09/2021, 19/11/2021 y 17/12/2021 (MC).

**Respuesta.** Codificar es poner en correspondencia las secuencias del **alfabeto fuente** $S=\{s_1,\dots,s_q\}$ con secuencias de un **alfabeto código** $Z=\{z_1,\dots,z_r\}$.
- **Código bloque:** asigna a **cada símbolo del alfabeto fuente una secuencia fija de símbolos del alfabeto código**.
- **Palabra código:** cada una de esas **secuencias fijas de símbolos del alfabeto código**.

Ejemplo: $s_1\to 00,\ s_2\to 01,\ s_3\to 10,\ s_4\to 11$. Cada $s_i$ tiene asignada siempre la misma palabra.

**En el MC:** código bloque = "asigna a cada uno de los símbolos del alfabeto fuente una secuencia fija de símbolos del alfabeto código" (las otras invierten fuente y código). Palabra código = "una secuencia **fija** de símbolos **códigos**": "una secuencia fija de símbolos" no dice de qué alfabeto, y "una secuencia de símbolos códigos" omite *fija*.

(teoria/2 - Codificación.md)

#### 3.2 Código no singular, unívoco e instantáneo (definiciones y ejemplos)
**Salió:** no singular en 18/12/2020; unívoco en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 y **04/04/2025** (desarrollo); instantáneo en 18/12/2020 y **04/04/2025**; condición necesaria y suficiente de instantáneo en 28/08/2020, 18/12/2020 y 10/09/2021; FAQ ("Definir código no singular, unívoco e instantáneo. Dar ejemplos", "Concepto de código unívoco, instantáneo y compacto. Condiciones necesarias").

**Respuesta.** Son clases anidadas: instantáneos ⊂ unívocos ⊂ no singulares ⊂ bloque.

- **No singular:** **todas sus palabras código son distintas**.
- **Unívoco (unívocamente decodificable):** **a cualquier secuencia de palabras código le corresponde una y solo una secuencia de símbolos de la fuente**. Equivalente: un código bloque es unívoco si y solo si **su extensión de orden $n$ es no singular para todo $n$ finito**. Todo código no singular de longitud constante es unívoco.
- **Instantáneo:** cada palabra se puede decodificar **sin esperar la llegada de la próxima palabra código**, sin conocer los símbolos que siguen. **Condición necesaria y suficiente:** **ninguna palabra del código es prefijo de otra**. El prefijo de $z_{i1}z_{i2}\dots z_{im}$ es cualquier $z_{i1}\dots z_{ij}$ con $j\le m$.

Ejemplos del apunte, uno por clase:

```
            No singular,      Unívoco,             Instantáneo
            NO unívoco        NO instantáneo       (código "coma")
 s1           1                 0                    1
 s2          11                01                   01
 s3          00               011                  001
 s4          10              0111                 0001
```
- 1.ª columna: si llega `1100`, puede ser $s_2s_3$ o $s_1s_1s_3$. Las palabras son distintas, pero una secuencia es ambigua.
- 2.ª columna: es unívoco (cada palabra empieza con 0, que marca el comienzo), pero al recibir `01` hay que esperar el siguiente símbolo para saber si es $s_2$ o el inicio de $s_3$: `0` es prefijo de `01`.
- 3.ª columna: ninguna palabra es prefijo de otra → se decodifica al terminar cada palabra.

**En el MC:** unívoco = "si a cualquier **secuencia de palabras** código le corresponde una y solo una **secuencia de símbolos** de la fuente". "Si a cualquier palabra código le corresponde un único símbolo" describe un código no singular, no uno unívoco. Instantáneo = "puede decodificarse sin esperar la llegada de la próxima palabra código" y su condición = "ninguna palabra código sea **prefijo** de otra" (no "terminación"/"subfijo", y la longitud variable no tiene nada que ver).

(teoria/2 - Codificación.md; resumenes/El Santo Resumen/el-santo-resumen.md, sección Final)

#### 3.3 Inecuación de Kraft (y McMillan)
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC "Un código que cumple la inecuación de Kraft es…") y **04/04/2025** ("Explicar la inecuación de Kraft").

**Respuesta.** **Teorema de Kraft:** si los enteros $l_1,\dots,l_q$ satisfacen
$$\sum_{i=1}^{q} r^{-l_i}\le 1$$
esa es condición **necesaria y suficiente para que exista al menos un** código instantáneo de $r$ símbolos en su alfabeto con palabras de esas longitudes.

**Matiz que se toma:** el teorema **no** dice que todo código cuyas longitudes cumplan Kraft sea instantáneo. Dice que **existe** uno con esas longitudes. Si un código no cumple Kraft, seguro **no** es instantáneo.

Ejemplo del apunte ($r=2$, longitudes 1, 2, 2): $2^{-1}+2^{-2}+2^{-2}=1\le 1$ ✓.
- `0, 00, 11` cumple Kraft y **no** es instantáneo (`0` es prefijo de `00`).
- `0, 10, 11` tiene las mismas longitudes y **sí** es instantáneo.

**McMillan:** la misma desigualdad es condición necesaria y suficiente para que exista un código **unívoco** con esas longitudes. Como los instantáneos son subclase de los unívocos, la suficiencia sale de Kraft, y McMillan demostró la necesidad. Consecuencia: pasar de instantáneo a unívoco no permite acortar las palabras.

**En el MC:** "**puede ser** instantáneo". No "es instantáneo", "es unívoco" ni "es compacto".

(teoria/2 - Codificación.md)

#### 3.4 Código compacto, longitud media y Huffman
**Salió:** compacto en 28/08/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC) y **04/04/2025**; FAQ ("Concepto de código compacto y ventajas de su aplicación", "¿Para qué sirve el método de Huffman? ¿Qué puede suceder si el alfabeto código tiene r=2?").

**Respuesta.**
- **Longitud media:** $L=\sum_{i} P_i\, l_i$ [dígitos/símbolo].
- **Código compacto** (definición del apunte): dada la fuente $S$, un código **instantáneo** aplicado a $S$ es compacto si su longitud media es **igual o menor que la de todos los códigos instantáneos que puedan aplicarse a la misma fuente y al mismo alfabeto**.
- **Cómo se logra:** "a mayor probabilidad, menor longitud de palabra". Si la fuente es equiprobable, las longitudes no dependen de las probabilidades.
- **Ventaja:** es el código de **menor longitud media posible**. Se transmiten menos dígitos por símbolo, lo que reduce tiempo, ancho de banda y costo de transmisión.
- **Método de Huffman** (construye un código compacto):
  1. Ordenar los símbolos por probabilidad decreciente.
  2. **Reducir** la fuente juntando los $r$ símbolos menos probables en uno, cuya probabilidad es la suma. Reordenar y repetir hasta que queden $r$ símbolos.
  3. Asignar a la última fuente reducida los $r$ dígitos y **volver hacia atrás**, desdoblando cada símbolo compuesto: a su palabra se le agrega un dígito distinto por cada componente.
- **Binario ($r=2$):** se agrupa de a 2, cada fuente reducida tiene **un símbolo menos** que la anterior y **siempre** se llega a 2 símbolos, sin ninguna condición.
- **r-ario:** se agrupa de a $r$ y cada reducción quita $r-1$ símbolos. Se llega exactamente a $r$ símbolos solo si $q=r+\alpha(r-1)$ con $\alpha$ entero. Si no, se agregan **símbolos falsos de probabilidad nula** hasta cumplirlo, y después se descartan.

**Ejemplo binario:** $P=(0{,}5;\ 0{,}25;\ 0{,}125;\ 0{,}125)$ → Huffman da `0, 10, 110, 111`, $L=0{,}5\cdot1+0{,}25\cdot2+0{,}125\cdot3\cdot2=1{,}75$ = $H(S)$: compacto y con rendimiento 100 %.
**Ejemplo ternario** (FAQ, $q=7=3+2\cdot2$ ✓): `1, 2, 01, 02, 000, 001, 002`.

**En el MC:** "Aquel código instantáneo que tiene la menor longitud promedio de todos los códigos **instantáneos** que se pueden aplicar a esa fuente **con ese código**" (= con ese alfabeto código). La opción que termina en "…a esa fuente." omite el alfabeto. La que agrega "y de valor igual a la entropía r-aria" es falsa: $L=H_r$ solo en casos particulares (3.5).

(teoria/2 - Codificación.md)

#### 3.5 Cota inferior de la longitud media
**Salió:** 28/08/2020, 18/12/2020, 10/09/2021, 19/11/2021, 17/12/2021 (MC) y **04/04/2025** ("Dar la cota inferior de la long. media"); FAQ.

**Respuesta.** Para un código instantáneo (y, por McMillan, para uno unívoco) aplicado a una fuente de memoria nula, la longitud media no puede bajar de la **entropía r-aria** de la fuente:
$$L \;\ge\; H_r(S)=\frac{H(S)}{\lg r}=\sum_i P_i\log_r\frac{1}{P_i}$$
Expresa el **límite inferior** de la longitud media: ningún código puede representar la fuente con menos dígitos r-arios por símbolo que su entropía r-aria. Para $r=2$, $L\ge H(S)$.

- **Igualdad** ($L=H_r$) si y solo si se pueden elegir $l_i=\log_r(1/P_i)$ enteros, o sea, si las probabilidades son de la forma $P_i=(1/r)^{l_i}$.
- Si no, codificando la **extensión de orden $n$** se puede acercar $L_n/n$ a $H_r(S)$ tanto como se quiera, a costa de complejidad (primer teorema de Shannon): $H_r(S)\le L_n/n< H_r(S)+1/n$.
- Rendimiento $\eta = H_r(S)/L\le 1$; redundancia $=1-\eta$.

**Ejemplo:** la fuente de 3.4 tiene $H=1{,}75$ bit y el código Huffman da $L=1{,}75$ → alcanza la cota porque las probabilidades son potencias de 1/2.

**En el MC:** "Expresa el límite **inferior** de la longitud media, que es igual o mayor a la entropía **r-aria** de la fuente". Con "la entropía de la fuente" (binaria) solo vale para $r=2$; "límite superior" es falso.

(teoria/2 - Codificación.md)
