# RD — Claves de subnetting y direcciones IP

> 2do parcial práctico de Baró. **Convención de la cátedra:** subredes válidas = 2ⁿ − 2 (se descartan la primera y la última subred).

## 1. Lo básico

Valor de cada posición de un byte (de izquierda a derecha):

```
128   64   32   16   8   4   2   1
```

- IP = **32 bits** = 4 bytes. Máscara: **1 = red, 0 = host**. **/n** = cantidad de unos.
- Bits libres para host = **32 − n**.
- En cada bloque: **primera = red** · **última = broadcast** · **las del medio = hosts**.

## 2. Tabla de máscaras (último byte)

| /n | Último byte | Binario | Bits de host (h) | Bloque = salto | Hosts (2ʰ − 2) |
|---|---|---|---|---|---|
| /24 | 0 | `00000000` | 8 | 256 | 254 |
| /25 | 128 | `10000000` | 7 | 128 | 126 |
| /26 | 192 | `11000000` | 6 | 64 | 62 |
| /27 | 224 | `11100000` | 5 | 32 | 30 |
| /28 | 240 | `11110000` | 4 | 16 | 14 |
| /29 | 248 | `11111000` | 3 | 8 | 6 |
| /30 | 252 | `11111100` | 2 | 4 | 2 |

De /17 a /23 es el mismo patrón, pero en el **3.er byte**. Por ejemplo, /20 = 255.255.**240**.0, con salto 16 en el 3.er byte.

## 3. Fórmulas

```
bits de subred     n = máscara nueva − máscara original
bits de host       h = 32 − máscara
subredes válidas     = 2ⁿ − 2        (convención de Baró)
hosts por subred     = 2ʰ − 2        (menos red y broadcast)
salto (bloque)       = 256 − byte de la máscara
byte de la máscara   = 256 − bloque
red                  = múltiplo del salto ≤ IP    (= IP AND máscara)
broadcast            = red + salto − 1             (= red siguiente − 1)
hosts                = red + 1  …  broadcast − 1
cantidad en un rango = último − primero + 1
```

Para elegir n o h: siempre el **menor** valor que cumpla **≥** lo pedido.

## 4. Recetas por tipo de ejercicio

### A. Dividir una red en N subredes (E4)

1. Menor n con **2ⁿ − 2 ≥ N**.
2. Máscara nueva = original + n → byte con la tabla.
3. Salto = 256 − byte. Bloques: 0, salto, 2·salto…
4. Descartar el primer bloque (bits de subred 0…0) y el último (1…1).
5. Listar cada subred: red · hosts · broadcast.

*Ej.:* 192.168.10.0/24, N = 6 → n = 3 → /27 (224) → salto 32 → válidas .32, .64, .96, .128, .160 y .192.

### B. Subredes de H hosts cada una (E5)

1. Menor h con **2ʰ − 2 ≥ H**.
2. Máscara nueva = 32 − h → byte con la tabla.
3. n = máscara nueva − original → válidas = 2ⁿ − 2.
4. Salto, descartar y listar igual que en A.

*Ej.:* 200.10.5.0/24, H = 50 → h = 6 → /26 (192) → n = 2 → 2 válidas: .64 y .128.

### C. IP + máscara → red, broadcast y hosts (E1, E2)

1. **Byte interesante** = el primero de la máscara que no es 255.
2. Salto = 256 − ese byte.
3. **Red:** en ese byte, el múltiplo del salto ≤ el valor de la IP. Los bytes de la derecha van en **0**.
4. **Broadcast:** en ese byte, red + salto − 1. Los bytes de la derecha van en **255**.

*Ej.:* 172.16.45.200 / 255.255.240.0 → 3.er byte, salto 16 → 45 cae entre 32 y 47 → red **172.16.32.0**, broadcast **172.16.47.255**.

### D. ¿Están en la misma subred? (E3)

Calculá la red de cada IP con la misma máscara. Si dan igual, están en la misma subred.

*Ej.:* /25 (salto 128): .70 → red .0 y .130 → red .128 → **distintas**.

### E. Rango de hosts → red, broadcast y máscara (E6)

1. Red = primer host − 1 · broadcast = último host + 1.
2. Bloque = broadcast − red + 1.
3. Byte de la máscara = 256 − bloque (o buscá el bloque en la tabla).
4. Control: la red tiene que ser **múltiplo del bloque**.

*Ej.:* .65 a .94 → red .64, broadcast .95 → bloque 32 → **255.255.255.224 (/27)**.

### F. Clase y pública o privada (E7)

| Clase | 1.er byte | Máscara por defecto | Rango privado |
|---|---|---|---|
| A | 0 – 127 | 255.0.0.0 (/8) | **10**.x.x.x |
| B | 128 – 191 | 255.255.0.0 (/16) | **172.16** a **172.31**.x.x |
| C | 192 – 223 | 255.255.255.0 (/24) | **192.168**.x.x |
| D | 224 – 239 | — (multicast) | no aplica |
| E | 240 – 255 | — (reservadas) | no aplica |

1. Clase: mirá **el 1.er número**.
2. ¿Cae en uno de los tres rangos privados? Sí → **privada**. No → **pública**.

127.x.x.x es **loopback** (tu propio equipo).

## 5. Trampas

- Salto = **256** − byte, no 255. (255 − byte da la distancia de la red a su broadcast.)
- Los bloques arrancan en **0** y en múltiplos del salto. Un bloque de 32 va de .32 a **.63**, no de .33 a .65.
- **Bloque** (32 direcciones) ≠ **rango de hosts** (30). Contá con +1: de .33 a .62 hay 62 − 33 + 1 = 30.
- Hay **dos −2** distintos: en hosts (red y broadcast, vale siempre) y en subredes (primera y última, convención de Baró).
- La clase da la máscara **por defecto**. Si los datos muestran un bloque más chico, manda el bloque.
- **172:** mirá el 2.º número (16–31). **192:** solo 192.168. Las D y E no son ni públicas ni privadas.
- Escribí **máscara**, nunca "mac" (MAC es la dirección física, capa 2). "Trama" es capa 2: acá se habla de **bloques** o **subredes**.
- Revisá que los tres primeros bytes sean los del ejercicio en toda la tabla (no copies del anterior).
- Justificá siempre: la cuenta de 2ⁿ − 2, el salto y qué bloques descartás.
