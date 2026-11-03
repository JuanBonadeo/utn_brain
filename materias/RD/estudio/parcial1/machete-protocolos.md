# 🃏 Machete — Protocolos de Control (Capa de Red)

> Repaso rápido para el MC de Medin. Al final están las **trampas frecuentes**, que es donde se pierden los puntos.

---

## 🧠 La memotecnia madre: **I-A-D**

Los tres "asistentes" de la capa de red, en orden alfabético, y la primera letra dice qué hacen:

| | Protocolo | Verbo | Qué hace |
|---|---|---|---|
| **I** | **I**CMP | **I**nforma | errores y diagnóstico |
| **A** | **A**RP | **A**verigua | la MAC de una IP |
| **D** | **D**HCP | **D**a | la IP (+ gateway + DNS) |

**"ICMP Informa, ARP Averigua, DHCP Da."** Si te acordás de esta línea, no cruzás nunca los tres.

---

## 📖 Qué significan las siglas

| Sigla | Significado | Qué te adelanta el nombre |
|---|---|---|
| **ICMP** | *Internet **Control Message** Protocol* | Protocolo de **mensajes de control** → avisa cosas, no transporta datos |
| **ARP** | ***Address Resolution** Protocol* | **Resuelve una dirección** (la IP) en otra (la MAC) |
| **DHCP** | ***Dynamic Host Configuration** Protocol* | **Configura** al host **dinámicamente** → le da IP, gateway, DNS |
| **MPLS** | ***Multiprotocol Label Switching*** | **Conmuta por etiqueta** (*label*) y sirve para **varios protocolos** |
| **OSPF** | *Open **Shortest Path First*** | Va por el **camino más corto primero** → es Dijkstra / estado de enlaces |
| **IS-IS** | ***Intermediate System** to **Intermediate System*** | De **router a router** (en jerga ISO, "sistema intermedio" = router) |
| **BGP** | ***Border** Gateway Protocol* | **Border = frontera** → va **ENTRE** dominios (interdominio) |
| **RIP** | ***Routing Information** Protocol* | Es de **ruteo** (no de traducir direcciones) |

**Siglas menores que aparecen:** **LSR** = *Label Switched Router* (el router de MPLS) · **ECMP** = *Equal Cost Multi Path* (balanceo de OSPF) · **SA** = Sistema Autónomo · **BOOTP/RARP** = los viejos que reemplazó DHCP.

---

## 📋 Tabla maestra

| Protocolo | Función | Datos clave |
|---|---|---|
| **ICMP** *(Internet Control Message Protocol)* | Informa **errores** y diagnostica | Mensajes: destino inalcanzable · tiempo excedido (TTL=0) · problema en parámetro · bajar tráfico de fuente (*source quench*, **en desuso**) · ruta alternativa · **eco**. Viaja **encapsulado en IP** |
| **ARP** *(Address Resolution Protocol)* | **IP → MAC** dentro de la LAN | Pregunta por **broadcast**: "¿quién tiene tal IP?". Si el destino está en **otra red** → resuelve la MAC del **default gateway** (la **IP más baja**). RFC 826 |
| **DHCP** *(Dynamic Host Configuration Protocol)* | Asigna **IP dinámica** | Por **broadcast** (el host aún no tiene IP). Entrega también **gateway y DNS**. Tiene **tiempo de arriendo** (expira/renueva). **Reemplazó a BOOTP y RARP** |
| **MPLS** *(Multiprotocol Label Switching)* | Rutea por **etiqueta**, no por IP | **Capa 2,5** · routers **LSR** · header **32 bits** (= **20 de label** + QoS + 1 bit stack + TTL) |
| **OSPF** *(Open Shortest Path First)* | Ruteo **INTRA**dominio | **Estado de enlaces** · **solo IP** · áreas → **backbone = área 0** · *designated router* + backup · mensajes **Hello** y *Link State Update* · **ECMP** |
| **IS-IS** *(Intermediate System to Intermediate System)* | Ruteo **INTRA**dominio | **Estado de enlaces** · **MULTIPROTOCOLO** (IP, IPX, AppleTalk) · vino **primero** (DECnet → ISO); OSPF se basó en él |
| **BGP** *(Border Gateway Protocol)* | Ruteo **INTER**dominio | **Path vector** · corre sobre **TCP** · maneja **políticas** · *multihoming* · *peering* · detecta bucles |
| *(RIP)* *(Routing Information Protocol)* | Ruteo **obsoleto** | **Vector distancia** → sufre la **cuenta a infinito**. Lo reemplazaron OSPF/IS-IS |

---

## 🎯 Memotecnias por protocolo

**BGP = *Border* Gateway Protocol** → *border* = **frontera** = **ENTRE** dominios (inter).
👉 El nombre te lo dice. Si es "border", está en el borde entre Sistemas Autónomos.

```
     SA 1                      SA 2
┌──────────────┐          ┌──────────────┐
│  OSPF/IS-IS  │◄── BGP ──►│  OSPF/IS-IS  │
│   (adentro)  │  (entre)  │   (adentro)  │
└──────────────┘          └──────────────┘
   INTRA                      INTRA
```

**ping hace ECO · traceroute mata el TTL**
- `ping` → mensaje **Eco** ("¿estás vivo?" → *echo reply*)
- `traceroute` → **Tiempo excedido** (manda TTL=1, 2, 3… y cada router que lo descarta se identifica)

**IS-IS habla varios idiomas** (IP, IPX, AppleTalk) · **OSPF solo habla IP**.
👉 IS-IS es el **viejo y ancho**; OSPF el **nuevo y acotado**.

**MPLS es el entrepiso** → capa **2,5**, entre la 2 y la 3.
👉 Y es "el ticket de guardarropa": te dan un **número (label)** y ya no miran tu nombre (la IP).

**El backbone arranca de CERO** → OSPF: backbone = **área 0**.

**El gateway se lleva la más baja** → default gateway = **IP más baja** de la red.

**ICMP es el mensajero de malas noticias** → solo **avisa** el problema, no lo arregla.

---

## ⚠️ Trampas frecuentes (acá se pierden los puntos)

| Trampa | La posta |
|---|---|
| "**RIP** traduce IP a MAC" | ❌ Eso es **ARP**. RIP es **ruteo** por vector distancia (obsoleto) |
| "**BGP** es intradominio" | ❌ Es **INTER**dominio. Intra = OSPF, IS-IS |
| "Header MPLS = **20 bits**" | ❌ 20 es **solo la etiqueta**; el header entero son **32 bits** |
| "MPLS es capa **3,5**" | ❌ Es **2,5** (entre la 2 y la 3) |
| "Backbone de OSPF = área **1**" | ❌ Es el **área 0** |
| "**OSPF** es multiprotocolo" | ❌ Al revés: **IS-IS** es multiprotocolo, OSPF **solo IP** |
| "**OSPF** usa vector distancia" | ❌ Usa **estado de enlaces** (vector distancia = RIP) |
| "DHCP pide la IP por **unicast**" | ❌ Por **broadcast** — todavía no tiene IP ni sabe dónde está el servidor |
| "DHCP **fue reemplazado por** BOOTP/RARP" | ❌ Al revés: DHCP **los reemplazó a ellos** |
| "El gateway y el DNS los resuelve **ARP**" | ❌ Los entrega **DHCP**. ARP **solo** hace IP→MAC |
| "ARP resuelve la MAC **del host destino** aunque esté en otra red" | ❌ Resuelve la del **próximo salto** (el gateway). La **IP es fija** todo el camino, la **MAC cambia** en cada tramo |
| "**ping** usa 'destino inalcanzable' / 'tiempo excedido'" | ❌ ping usa **Eco**; 'tiempo excedido' es de **traceroute** |

---

## ⚡ Repaso de 30 segundos

1. **I**CMP **I**nforma · **A**RP **A**verigua · **D**HCP **D**a.
2. **B**GP = **B**order = **entre** dominios. OSPF/IS-IS = adentro.
3. **IS-IS** multiprotocolo · **OSPF** solo IP · ambos **estado de enlaces**.
4. **MPLS**: capa **2,5**, **LSR**, **32 bits** (20 de label).
5. **ping → eco** · **traceroute → tiempo excedido**.
6. **Backbone = área 0** · **gateway = IP más baja**.
7. **RIP** es ruteo viejo (vector distancia), **no** traduce direcciones.
