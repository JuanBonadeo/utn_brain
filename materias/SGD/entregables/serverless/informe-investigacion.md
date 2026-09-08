# Serverless — Informe de investigación

> **Materia:** SGD — Soporte a la Gestión de Datos con P. Visual
> **Propósito:** base documental para la presentación a la clase. No es el guion
> de la exposición: es el material crudo, verificado y con fuentes, del que
> después se recorta el deck.
> **Fecha de relevamiento:** 2026-09-08
> **Criterio de fuentes:** se priorizó documentación de proveedor, papers
> académicos y reportes con datos propios. Cuando un dato viene de fuente
> secundaria (blog, análisis de terceros) está marcado como tal.

---

## 0. Cómo leer este informe

Cada sección está pensada como un bloque de la presentación. El nivel de
profundidad es intencionalmente "técnico pero explicable": alcanza para
responder preguntas de la clase sin entrar en internals del hipervisor.

Las secciones **5** (cómo funciona por dentro) y **6** (economía) son el
corazón técnico: si hay que recortar, se recorta de otro lado.

---

## 1. Resumen ejecutivo — 10 datos para abrir

1. **Serverless no significa "sin servidores".** Significa que el desarrollador
   no los provisiona, no los parchea y no los escala. Los servidores existen y
   son del proveedor. (CNCF)
2. Es un **paraguas con dos mitades**: *FaaS* (funciones event-driven que escalan
   a cero) y *BaaS* (servicios de backend consumidos como API gestionada). (CNCF, Fowler)
3. **Adopción real, no hype:** 65% de los clientes de AWS usan Lambda, 70% de los
   de Google Cloud usan Cloud Run, 56% de los de Azure usan App Service. (Datadog, 2025)
4. **Escala de operación:** Lambda ejecuta más de **15 billones (10^12) de
   invocaciones por mes**. (AWS, 2026)
5. **Facturación por milisegundo**: se paga por request + GB-segundo consumido.
   Sin uso, el costo de cómputo es cero. (AWS Pricing)
6. **El cold start es el precio del "escalar a cero"**: 200–400 ms en Python,
   sub-100 ms en Go/Rust, 90–140 ms en Java con SnapStart. (fuentes secundarias, 2026)
7. **Por dentro son microVMs**: AWS aísla cada entorno con *Firecracker*, un
   monitor de máquinas virtuales escrito en Rust que bootea Linux en **menos de
   125 ms** con ~5 MiB de overhead. (Firecracker / AWS)
8. **No siempre conviene.** Prime Video migró un sistema de monitoreo de
   serverless+microservicios a un monolito en ECS y **redujo el costo 90%**. (Amazon, 2023)
9. **El propio AWS lo admitió:** en 2026 lanzó *Lambda Managed Instances*, que
   corre funciones Lambda sobre EC2 "para cargas estables o predecibles que
   buscan optimizar costos". El modelo puro tiene un límite económico. (AWS, 2026)
10. **Mercado:** ~USD 26–32 mil millones en 2026, con CAGR proyectado entre 14% y
    23% según la consultora. (varias consultoras — tomar con pinzas)

---

## 2. Qué es serverless

### Definición canónica (CNCF)

> "Serverless computing refiere al concepto de construir y correr aplicaciones
> que no requieren gestión de servidores. Describe un modelo donde las
> aplicaciones, empaquetadas como una o más funciones, se suben a una
> plataforma y luego se ejecutan, escalan y facturan en respuesta a la demanda
> exacta del momento."

Las tres propiedades que definen el modelo, y que conviene machacar en la
presentación porque son el criterio para decir "esto es serverless / esto no":

| Propiedad | Qué significa |
|---|---|
| **Sin gestión de infraestructura** | No provisionás, no parcheás, no dimensionás capacidad. |
| **Escalado automático hasta cero** | De 0 a N instancias por demanda, y de vuelta a 0 si no hay tráfico. |
| **Facturación por uso real** | Se paga por ejecución, no por tiempo de servidor encendido. |

Si falta cualquiera de las tres, no es serverless. Un contenedor en un
Kubernetes gestionado cumple la primera a medias y no cumple la tercera:
el pod sigue costando aunque nadie lo llame.

### El malentendido del nombre

El nombre es marketing y es malo. Una analogía que funciona bien con la clase:
*wireless* tampoco significa que no haya cables — significa que el cable no es
tu problema. Igual acá: los servidores son problema del proveedor.

### Qué NO es serverless

- **No es "sin operaciones".** Seguís teniendo que pensar seguridad, permisos,
  observabilidad, versionado y despliegue. Fowler es explícito en esto.
- **No es lo mismo que PaaS.** La diferencia es la **granularidad del escalado**.
  Cita de Adrian Cockcroft que sirve de bala en el deck: *"Si tu PaaS puede
  arrancar instancias en 20 ms que corren medio segundo, llamalo serverless."*
- **No es lo mismo que microservicios.** Son ortogonales: podés tener un
  monolito desplegado como una sola función, o 200 microservicios en VMs.

---

## 3. Cómo llegamos acá — la escalera de abstracción

Este es el mejor gancho narrativo para abrir la presentación: serverless no
apareció de la nada, es el último escalón de una escalera de 25 años donde en
cada paso el desarrollador se desentiende de una capa más.

```
                        ¿Quién administra qué?
                        (■ vos   □ el proveedor)

                 Bare metal   IaaS      PaaS    Contenedores  FaaS
                 (on-prem)    (EC2)   (Heroku)   (K8s/ECS)  (Lambda)
Código fuente        ■          ■         ■          ■          ■
Dependencias         ■          ■         ■          ■          ■
Runtime              ■          ■         □          ■          □
Contenedor/imagen    –          –         –          ■          □
Sistema operativo    ■          ■         □          □          □
Virtualización       ■          □         □          □          □
Servidor físico      ■          □         □          □          □
Escalado             ■          ■         ■(config)  ■(config)  □
Capacity planning    ■          ■         ■          ■          □
Facturación        CAPEX     por hora  por dyno   por nodo   por ms
```

**Unidad de despliegue por escalón:** servidor → máquina virtual → aplicación →
contenedor → **función**.

**Unidad de facturación:** año → hora → hora → hora → **milisegundo**.

Ese salto de la última fila es el que cambia todo: es la primera vez que el
costo de cómputo puede ser literalmente cero cuando nadie usa el sistema.

**Analogía para la clase:** IaaS es alquilar un auto por día (lo pagás aunque
esté estacionado). Serverless es Uber: pagás el viaje. Si no viajás, no pagás —
pero el km sale más caro, y si viajás 8 horas por día conviene comprarse el auto.
Esta analogía se retoma en la sección 6 con los números reales.

---

## 4. Las dos mitades: FaaS y BaaS

La CNCF define serverless como un paraguas sobre dos modelos distintos. Es
importante separarlos porque en la industria "serverless" se usa como sinónimo
de FaaS, y no lo es.

### FaaS — Function as a Service

Cómputo event-driven: se despliegan unidades chicas de código que se ejecutan
como acciones discretas, disparadas por eventos o HTTP, y escalan sin gestionar
infraestructura.

- Ejemplos: AWS Lambda, Azure Functions, Google Cloud Functions / Cloud Run
  Functions, Cloudflare Workers.
- Vos escribís el código.

### BaaS — Backend as a Service

Servicios de terceros basados en API que **reemplazan un subconjunto de la
funcionalidad** que antes escribías vos. Como escalan y operan de forma
transparente, al desarrollador le parecen serverless.

- Ejemplos: Firebase / Firestore (base de datos + auth), Auth0 y Clerk
  (identidad), Supabase, Stripe (pagos), Algolia (búsqueda), S3 (almacenamiento).
- Vos **no** escribís ese código: lo consumís.

### Cómo se combinan

Una arquitectura serverless típica de una SPA o app móvil:

```
   Cliente (browser / app)
        │
        ├──► Auth0 / Firebase Auth ............ BaaS  (login, tokens)
        │
        ├──► API Gateway ──► Lambda ──┐ ....... FaaS  (lógica de negocio)
        │                             │
        │                             ├──► DynamoDB ......... BaaS
        │                             ├──► S3 ............... BaaS
        │                             └──► SQS / EventBridge  BaaS
        │
        └──► CDN / Static hosting ............. BaaS  (assets)
```

Observación fuerte para la presentación: **en una arquitectura serverless madura,
la mayor parte del sistema es BaaS, y la lógica propia (FaaS) es el pegamento.**
El desarrollador escribe menos código, pero **compone más servicios**. Eso mueve
la complejidad del código a la integración y a la configuración — y ahí está
buena parte de las críticas (sección 10).

---

## 5. Cómo funciona por dentro

Esta es la sección donde se gana credibilidad técnica. La idea: mostrar que
"magia" no hay, hay ingeniería.

### 5.1 El disparador: modelo de eventos

Una función no "corre": **es invocada**. Las fuentes de eventos típicas:

| Tipo de invocación | Ejemplo | Comportamiento |
|---|---|---|
| **Síncrona** | HTTP vía API Gateway, invoke directo | el cliente espera la respuesta |
| **Asíncrona** | subida a S3, evento de EventBridge | la plataforma encola y reintenta |
| **Stream / poll** | Kinesis, Kafka, SQS, DynamoDB Streams | la plataforma lee lotes y llama |
| **Programada** | cron / scheduler | invocación por tiempo |

La relación evento↔función es **n:m**: un mismo evento puede disparar varias
funciones, y una función puede escuchar varias fuentes.

Cada invocación recibe dos cosas: el **event** (los datos del disparador) y el
**context** (metadatos: request id, tiempo restante, memoria, credenciales).

### 5.2 El ciclo de vida del entorno de ejecución

Este diagrama es el que hay que dibujar en el pizarrón/slide, porque explica
el cold start, el estado, y por qué las funciones "recuerdan" cosas a veces.

```
  INVOCACIÓN 1 (cold start)                    INVOCACIÓN 2..N (warm)
  ─────────────────────────                    ──────────────────────
  ┌─ INIT ────────────────────┐
  │ 1. crear microVM          │  ~ms
  │ 2. descargar el código    │  ~ms-s        (el entorno ya existe:
  │ 3. arrancar el runtime    │  ~ms-s          se saltea todo INIT)
  │ 4. correr código de init  │  ← tu código
  │    (imports, conexión DB) │
  └───────────────────────────┘
  ┌─ INVOKE ──────────────────┐               ┌─ INVOKE ─────────────┐
  │ ejecutar el handler       │               │ ejecutar el handler  │
  └───────────────────────────┘               └──────────────────────┘
  ┌─ FREEZE ──────────────────┐               ┌─ FREEZE ─────────────┐
  │ el entorno queda congelado│               │ ...                  │
  │ (memoria y /tmp intactos) │               └──────────────────────┘
  └───────────────────────────┘
              │                                          │
              └──── si no llegan más eventos ────────────┘
                    en ~5-15 min → SHUTDOWN
```

**Consecuencias prácticas (esto respondelo bien y quedás):**

- El código **fuera** del handler corre una sola vez por entorno. Ahí van los
  `import`, el pool de conexiones, la carga de config. Es la optimización #1
  de cold start.
- El código **dentro** del handler corre en cada invocación.
- El disco `/tmp` y las variables globales **sobreviven** entre invocaciones del
  mismo entorno → sirve para caché, pero **nunca** para estado de negocio: no
  hay garantía de que dos requests caigan en el mismo entorno.
- Cloudflare lo dice explícitamente para Workers: no guardes estado global
  mutable, no hay garantía de ruteo a la misma instancia.
- Por eso **serverless es stateless por contrato**, no por casualidad.

> **Dato de facturación:** según fuentes secundarias, desde agosto de 2025 AWS
> factura también la fase INIT. En funciones con inicialización pesada eso puede
> subir el gasto entre 10% y 50%. Verificar contra la doc oficial antes de
> afirmarlo en la presentación.

### 5.3 Cold start: qué es y cuánto duele

**Cold start** = latencia adicional de la primera invocación en un entorno nuevo,
porque hay que crear el sandbox, bajar el código y arrancar el runtime.

Números reportados para 2026 (fuentes secundarias, tomarlos como orden de
magnitud, no como medición):

| Runtime | Cold start típico |
|---|---|
| Go / Rust | < 100 ms |
| Python | 200–400 ms |
| Java con SnapStart | 90–140 ms |
| Java sin SnapStart | segundos |
| **Penalidad extra si la función está en VPC** | +200–500 ms |

**Mitigaciones reales:**

- **Provisioned Concurrency** (AWS): mantenés N entornos pre-inicializados y
  calientes. Elimina el cold start pero **se paga por hora**, o sea que
  resignás parte del "pagás solo lo que usás".
- **SnapStart** (AWS, para Java/Python/.NET): en vez de bootear, **restaura un
  snapshot de memoria y disco ya inicializado**, usando la capacidad de
  snapshotting de Firecracker.
- **Elegir runtime**: compilado (Go, Rust) arranca mucho más rápido que JVM.
- **Adelgazar el paquete**: menos dependencias, menos que descargar y linkear.
- **Modelo de isolates** (Cloudflare): elimina el problema de raíz, ver 5.5.

### 5.4 El sandbox: Firecracker microVMs

Acá está el detalle técnico que casi nadie de la clase va a conocer y que
diferencia la presentación.

El problema de fondo del proveedor: correr código arbitrario de miles de
clientes distintos, en la misma máquina física, con aislamiento de nivel
hardware, y arrancando en milisegundos. Contenedores solos no alcanzan
(comparten kernel); VMs tradicionales son demasiado lentas y pesadas.

**Firecracker** es la respuesta de AWS: un *Virtual Machine Monitor* escrito en
Rust, open source, que usa KVM del kernel de Linux.

- Bootea una microVM Linux en **menos de 125 ms**.
- Usa **~5 MiB de memoria** de overhead por microVM.
- Es "una PC de 1998 con todo borrado": sin BIOS, sin bus PCI, sin VGA, sin
  USB, sin ACPI. Solo `virtio` para red, disco y vsock.
- **Capas de aislamiento**: el código corre en el guest → el guest está aislado
  por virtualización por hardware (KVM) → el proceso VMM está aislado con
  namespaces y chroot → la superficie de syscalls está restringida con seccomp.
- Es la base de Lambda y de Fargate, y sostiene esos 15 billones de
  invocaciones mensuales.

**Frase para el deck:** *"Serverless no es magia: es un hipervisor minimalista
en Rust que puede crear y destruir una máquina virtual entera en menos tiempo
del que tarda un parpadeo."* (un parpadeo son ~100–150 ms)

### 5.5 El modelo alternativo: isolates de V8 (Cloudflare Workers)

Cloudflare Workers ataca el mismo problema por otro lado. En vez de una microVM
por cliente, usa **isolates de V8**: contextos livianos del motor de JavaScript
de Chrome, cada uno con sus propias variables y su entorno seguro.

- Un solo proceso runtime hostea **cientos o miles de isolates**, cambiando
  entre ellos.
- Un isolate arranca **~100 veces más rápido** que un proceso Node en un
  contenedor o VM, y consume **un orden de magnitud menos memoria** al arrancar.
- El overhead del runtime JS se paga **una sola vez** al arrancar el contenedor,
  no una vez por función.

**Trade-off honesto:** el aislamiento es a nivel de motor (software), no de
hardware. A cambio: cold starts prácticamente nulos, pero estás limitado al
sandbox de V8 (JS/TypeScript/WASM), no podés correr cualquier binario.

```
   Lambda (microVM)                    Workers (isolate)
   ┌──────────┐ ┌──────────┐           ┌───────────────────────────┐
   │ microVM  │ │ microVM  │           │   1 proceso runtime V8    │
   │ ┌──────┐ │ │ ┌──────┐ │           │ ┌───┐┌───┐┌───┐┌───┐┌───┐ │
   │ │ func │ │ │ │ func │ │           │ │f1 ││f2 ││f3 ││f4 ││f5 │ │
   │ └──────┘ │ │ └──────┘ │           │ └───┘└───┘└───┘└───┘└───┘ │
   │  guest OS│ │  guest OS│           │      (isolates)           │
   └──────────┘ └──────────┘           └───────────────────────────┘
   aislamiento por hardware            aislamiento por motor JS
   ~ms de arranque, MB de RAM          ~µs de arranque, KB de RAM
   corre cualquier binario             corre JS / WASM
```

### 5.6 Modelo de concurrencia — la diferencia que casi nadie explica

Este punto es de los más útiles y suele estar mal entendido:

- **AWS Lambda: un request por entorno a la vez.** Cada entorno atiende muchas
  invocaciones a lo largo de su vida, pero **una sola a la vez**. Si llegan 100
  requests simultáneos, se crean 100 entornos.
- **Google Cloud Run: hasta 1000 requests concurrentes por instancia.** Una
  instancia multiplexa muchos requests, lo que **reduce la frecuencia de cold
  starts** y aprovecha mejor el I/O-bound.

De ahí sale una fórmula práctica (Ley de Little) que sirve para dimensionar y
para el examen:

```
concurrencia = requests_por_segundo × duración_promedio_en_segundos

ej: 100 req/s × 0,2 s = 20 entornos concurrentes
    100 req/s × 2,0 s = 200 entornos concurrentes
```

El límite por defecto de concurrencia en AWS es **1000** ejecuciones simultáneas
por cuenta y región (ampliable a pedido). Con la fórmula de arriba: una función
de 2 segundos satura la cuenta entera con solo 500 req/s. Es la causa #1 de
throttling en producción.

---

## 6. La economía: cómo se factura y cuándo conviene

### 6.1 El modelo de precios (AWS Lambda, precios oficiales)

| Concepto | Precio |
|---|---|
| Capa gratuita permanente | 1.000.000 requests/mes + 400.000 GB-segundo/mes |
| Requests | USD 0,20 por millón |
| Duración x86 | USD 0,0000166667 por GB-segundo |
| Duración ARM (Graviton) | USD 0,0000133334 por GB-segundo (~20% menos) |
| Granularidad de facturación | **1 milisegundo** |
| Provisioned Concurrency | USD 0,0000041667 por GB-s + USD 0,0000097222 por GB-s de ejecución |

La memoria se configura de **128 MB a 10.240 MB**, y **la CPU se asigna de forma
proporcional a la memoria**: pedir 256 MB da el doble de CPU que 128 MB. En
Lambda, **1.769 MB equivalen a 1 vCPU completo**.

> **Contraintuitivo, y buen punto para la presentación:** subir la memoria puede
> *bajar* el costo. Si duplicás la memoria (2x precio por segundo) pero la
> función tarda la mitad porque tiene el doble de CPU, pagás lo mismo — y si
> tarda menos de la mitad, pagás menos, con la mitad de latencia de regalo.

### 6.2 Ejemplo numérico completo

*(Cálculo propio a partir de los precios oficiales de AWS, región US East, x86.)*

**Escenario A — API con tráfico moderado:** 5.000.000 requests/mes, 200 ms
promedio, 512 MB de memoria.

```
Requests:  5.000.000 - 1.000.000 (free tier) = 4.000.000
           4 × USD 0,20                       = USD 0,80

Cómputo:   5.000.000 × 0,2 s × 0,5 GB         = 500.000 GB-s
           500.000 - 400.000 (free tier)      = 100.000 GB-s
           100.000 × USD 0,0000166667         = USD 1,67
                                        TOTAL ≈ USD 2,47 / mes
```

Una EC2 `t3.small` encendida 24×7 cuesta ~USD 15/mes. **Serverless gana 6 a 1.**

**Escenario B — carga sostenida:** la misma función, pero ejecutándose de forma
continua todo el mes (utilización ~100%).

```
2.592.000 s/mes × 0,5 GB          = 1.296.000 GB-s
1.296.000 × USD 0,0000166667      = USD 21,60 / mes de cómputo
```

Y esos 512 MB son apenas ~0,29 vCPU. Normalizando:

```
Lambda:  USD 0,0000166667 × 3600 s × (1,769 GB / 1 vCPU) ≈ USD 0,106 / vCPU-hora
EC2 c7g.large (2 vCPU, USD 0,0725/h)                     ≈ USD 0,036 / vCPU-hora
```

**El vCPU-hora de Lambda cuesta aproximadamente 3 veces el de una instancia
equivalente.** *(cálculo propio, orden de magnitud)*

### 6.3 La regla del pulgar

De los dos escenarios sale la conclusión que ordena toda la discusión de costos:

> **Serverless conviene mientras la utilización real esté por debajo de ~30-35%.
> Por encima de eso, una instancia dedicada sale más barata.**

```
  costo
   │                                       ┌──── Lambda (lineal con el uso)
   │                                    ┌──┘
   │                                 ┌──┘
   │  ─────────────────────────┬─────┴──────────  EC2 (fijo, encendido 24/7)
   │                           │
   │                        ┌──┘  punto de cruce ≈ 30-35% de utilización
   │                     ┌──┘
   │                  ┌──┘
   └──────────────────┴──────────────────────────► utilización
   0%                                          100%

  Lambda: costo 0 en reposo, pendiente alta.
  EC2:    costo alto en reposo, pendiente 0.
```

Por eso serverless brilla en cargas **espigadas, intermitentes o impredecibles**
(el caso de uso donde el modelo tradicional te obliga a provisionar para el pico
y desperdiciar el resto del tiempo), y pierde en cargas **constantes y
predecibles**.

**Confirmación de la tesis desde el propio AWS (2026):** lanzó *Lambda Managed
Instances*, que corre funciones Lambda sobre EC2 gestionadas, con "acceso a
configuraciones de cómputo especializadas y a las ventajas de precio de EC2",
y lo posiciona explícitamente para "cargas estables o predecibles que buscan
optimizar costos". Además permite **procesar requests en paralelo dentro de cada
entorno de ejecución** — es decir, AWS adoptó el modelo de concurrencia de Cloud
Run. Es la industria admitiendo el punto de cruce.

### 6.4 El costo que no aparece en la factura

Un ítem honesto que casi ninguna presentación incluye:

- **Costo de observabilidad:** el logging y tracing de miles de funciones
  efímeras suele costar más que el cómputo. Es un problema real de la
  arquitectura, no un detalle de facturación.
- **Costo de las llamadas entre servicios:** en arquitecturas con muchas
  funciones encadenadas, la orquestación (por ejemplo Step Functions, que cobra
  por transición de estado) puede dominar el gasto. Fue exactamente el problema
  de Prime Video (sección 10).
- **Costo de transferencia de datos:** mover datos entre funciones vía S3 o red
  se paga, y en pipelines de datos pesados es el rubro principal.

---

## 7. Panorama de plataformas

*(Datos combinados de documentación de proveedores y comparativas 2026;
verificar límites puntuales contra la doc oficial antes de la exposición,
porque cambian seguido.)*

| | **AWS Lambda** | **Google Cloud Run** | **Azure Functions** | **Cloudflare Workers** |
|---|---|---|---|---|
| Modelo | FaaS / microVM | contenedor serverless | FaaS | isolates V8 (edge) |
| Timeout máx. | 15 min | 60 min (2ª gen) | 10 min (plan Consumo) | límite de CPU-time, no de wall-clock |
| Memoria máx. | 10.240 MB | hasta 32 GB | según plan | limitada (sandbox JS) |
| Concurrencia por instancia | **1 request** | hasta **1000 requests** | según plan | muchos isolates por proceso |
| Límite de concurrencia | 1000 (default, ampliable) | 1000 instancias (default) | ilimitada en plan Premium | — |
| Tamaño de deploy | 250 MB descomprimido / 10 GB imagen | sin límite duro (imagen) | según plan | bundle chico |
| Cold start | ms a segundos según runtime | reducido por concurrencia | ms a segundos | prácticamente nulo |
| Fuerte en | ecosistema y madurez | portabilidad (contenedor estándar) | integración con stack Microsoft | latencia global / edge |

**Cómo presentar esta tabla:** no como "cuál es mejor" sino como **tres filosofías
distintas del mismo problema**: Lambda apuesta al aislamiento fuerte y al
ecosistema; Cloud Run apuesta a que la unidad sea el contenedor estándar (menos
lock-in, más portable); Cloudflare apuesta a la latencia sacrificando
generalidad.

---

## 8. Serverless más allá de las funciones

Un error común es equiparar serverless con FaaS. El modelo se extendió a otras
capas, y esta sección es la que más conecta con SGD porque toca datos.

### 8.1 Contenedores serverless

Corrés una **imagen de contenedor estándar**, pero la plataforma se encarga del
escalado (incluido a cero) y facturás por uso.

- **AWS Fargate**, **Google Cloud Run**, **Azure Container Apps**.
- Ventaja clave: **mucho menos lock-in**. Tu unidad de despliegue es un
  Dockerfile, que corre igual en cualquier lado.
- Es el punto medio entre "función" y "clúster de Kubernetes".

### 8.2 Bases de datos serverless

Misma idea aplicada a la persistencia: capacidad elástica, escala a cero,
facturación por consumo.

| Producto | Modelo | Cómo funciona |
|---|---|---|
| **Amazon Aurora Serverless v2** | relacional (MySQL/Postgres) | un daemon de escalado sobre el mismo cómputo y storage de Aurora, que ajusta capacidad según demanda; se cobra solo lo consumido |
| **Amazon DynamoDB (on-demand)** | NoSQL clave-valor | escalado transparente, sin provisionar capacidad de lectura/escritura |
| **Neon** | Postgres serverless (open source) | **separa cómputo de almacenamiento**: los datos viven en object storage y los nodos de cómputo escalan a cero cuando no hay actividad; ante una query nueva el cómputo levanta en segundos y se reengancha al historial de datos sin mover nada |
| **Firebase / Firestore, Supabase** | BaaS de datos | base + auth + API expuestas como servicio |

**El truco arquitectónico central** — y esto es directamente material de SGD:
**desacoplar cómputo de almacenamiento**. Esa separación es lo que permite
apagar el cómputo sin perder los datos. Es la misma idea que hace posible
serverless en la capa de aplicación, aplicada a la capa de datos.

**Advertencia técnica importante:** las funciones serverless y las bases de datos
relacionales tradicionales **chocan**. Si 500 entornos concurrentes abren cada
uno su conexión a Postgres, matás la base (los límites de conexiones son de
cientos, no de miles). Soluciones: *connection pooler* externo (RDS Proxy,
PgBouncer), o bases con API HTTP (DynamoDB, Neon serverless driver). Este es un
problema clásico y una excelente pregunta para hacerle a la clase.

### 8.3 Edge computing

La función no corre en una región, corre en el **PoP más cercano al usuario**,
en cientos de ubicaciones.

- Cloudflare Workers, Vercel Edge Functions, Deno Deploy.
- Casos: autenticación, redirects, A/B testing, personalización, e
  **inferencia de IA cerca del usuario**.
- Es serverless llevado al extremo: la unidad de despliegue es tan chica que
  se puede replicar en todo el planeta.

---

## 9. Cuándo sí y cuándo no

### Buen encaje (según CNCF)

Serverless funciona bien cuando la carga es:

- **Asíncrona y paralelizable** — unidades de trabajo independientes.
- **Infrecuente o de demanda muy variable** — escalado impredecible.
- **Stateless y efímera** — sin requisito de arranque instantáneo.
- **Cambiante** — donde importa la velocidad de desarrollo.

**Casos concretos que lista la CNCF:**

| Categoría | Ejemplo |
|---|---|
| Procesamiento multimedia | generar thumbnails al subir una imagen |
| Triggers de base de datos | reaccionar a un cambio (change data capture) |
| IoT | procesar mensajes de sensores |
| Stream processing | procesar streams a escala |
| Chatbots | interfaces conversacionales |
| Tareas batch / programadas | backups nocturnos, envío masivo de emails en paralelo |
| APIs REST y web apps | backend HTTP |
| Backends móviles | API para app nativa |
| CI | pipelines de integración continua |

### Mal encaje (según CNCF)

- **Cargas long-running y siempre encendidas** → capacidad pre-provisionada
  sale más barata.
- **Aplicaciones con estado** → que necesitan conexiones persistentes o estado
  compartido entre invocaciones.
- **Sistemas críticos en latencia** → el cold start es inaceptable.
- **Servicios complejos e interdependientes** → cadenas de funciones que
  aumentan la superficie operativa.
- **Microservicios fuertemente acoplados** → mejor servidos por orquestación de
  contenedores.

**Regla de bolsillo para cerrar la sección:**

> Si tu carga es **espigada, event-driven y stateless** → serverless.
> Si es **constante, de baja latencia o con estado** → contenedores o VMs.

---

## 10. Limitaciones y críticas

Sección obligatoria: una presentación que solo elogia una tecnología no
convence a nadie que ya la usó.

### 10.1 Cold start

Ya cubierto en 5.3. Lo importante conceptualmente: **es el precio inevitable de
escalar a cero**. Si querés costo cero en reposo, alguien tiene que arrancar
algo cuando llega el primer request. Todas las mitigaciones (provisioned
concurrency, min instances) son en realidad renunciar parcialmente al escalar a
cero.

### 10.2 Vendor lock-in

Es la crítica más fuerte y la más citada.

- Las implementaciones difieren sustancialmente entre proveedores: migrar
  requiere cambiar código, herramientas operativas **y rediseño arquitectónico**.
- La CNCF lo señala como una brecha de estandarización de la industria.
- El lock-in real **no está en la función** (mover 200 líneas de Python es
  trivial) sino **en todo lo que la rodea**: el modelo de eventos, IAM, la base
  de datos propietaria, la orquestación, la observabilidad. Migrar de Kinesis a
  otro proveedor no es posible sin migrar la infraestructura entera.
- **Mitigación parcial:** contenedores serverless (Cloud Run, Fargate) y
  frameworks portables como Knative.

### 10.3 Statelessness

Las funciones no retienen datos entre invocaciones. El estado tiene que
externalizarse a una base o caché, que es **sustancialmente más lenta** que la
memoria local. Impacta directamente en caching y manejo de sesiones.

### 10.4 Límites de ejecución

15 minutos en Lambda. Cualquier tarea más larga hay que rearquitecturarla en
funciones coordinadas — lo cual introduce orquestación, y la orquestación
introduce costo y complejidad (ver el caso de abajo).

### 10.5 Testing, debugging y observabilidad

- El testing de integración se complica porque las dependencias externas son
  obligatorias, y el entorno local **no puede simular del todo** el entorno cloud.
- La naturaleza efímera de las instancias rompe el monitoreo tradicional.
- La CNCF señala directamente la inmadurez del ecosistema: documentación,
  herramientas y buenas prácticas menos estables que en plataformas
  consolidadas.

### 10.6 El caso Prime Video (2023) — el contraejemplo que hay que contar

**Qué pasó:** el equipo de Prime Video tenía un sistema de monitoreo de calidad
que analizaba cada stream visto por los clientes, construido con Step Functions
y Lambda.

**El problema:** Step Functions hacía múltiples transiciones de estado **por cada
segundo de stream**, y con miles de streams concurrentes llegaron rápido a los
límites de la cuenta. Además, pasar los datos entre componentes obligaba a
mandar grandes volúmenes por red o vía S3.

**La solución:** consolidaron todo en una arquitectura **monolítica sobre Amazon
ECS**, con el conversor de medios y el detector de defectos corriendo en el
mismo proceso — eliminando el paso de datos por red.

**El resultado: 90% de reducción de costos.**

**La polémica:** como Amazon es el principal impulsor de serverless, el post se
leyó como una autocrítica, y disparó un debate público sobre si todo el
movimiento serverless/microservicios estaba sobrevendido. DHH (creador de Rails)
lo amplificó.

**La lectura correcta, y la que conviene bajar a la clase:**

1. No fue "serverless es malo": fue **una arquitectura mal elegida para ese
   problema**. Un pipeline de datos de alto volumen y baja latencia, donde el
   costo dominante es mover datos entre etapas, es el peor caso posible para
   funciones aisladas.
2. La lección es de **granularidad**: cuando el costo de la comunicación supera
   el costo del cómputo, hay que juntar los componentes, no separarlos.
3. La arquitectura cloud es cuestión de **trade-offs, no de soluciones
   definitivas**. Y como respondieron algunos críticos: pocos equipos tienen la
   capacidad de cambiar su arquitectura de raíz sin que los usuarios lo noten.

### 10.7 La crítica académica (Berkeley, 2019)

El paper *"Cloud Programming Simplified: A Berkeley View on Serverless
Computing"* (arXiv 1902.03383) es la referencia académica del tema. Sirve para
darle peso a la presentación.

- **Tesis central:** serverless simplifica la programación cloud de manera
  comparable al salto **del assembler a los lenguajes de alto nivel**. Es la
  mejor analogía del paper y funciona muy bien en una slide.
- **Limitaciones identificadas:**
  - Almacenamiento inadecuado para operaciones de grano fino.
  - Falta de coordinación de grano fino entre funciones.
  - Mal rendimiento en patrones de comunicación estándar (ej. broadcast, shuffle
    — justo lo que necesita el procesamiento distribuido de datos).
  - Desafíos de red.
  - Desafíos de seguridad: provisión de claves privadas con grano fino,
    delegación de privilegios entre funciones, fuga de información por patrones
    de comunicación.
- **Predicción:** los autores anticipan que serverless **va a dominar el futuro
  del cloud computing**, con dos desafíos abiertos: mejorar la seguridad y
  acomodar los avances de costo-rendimiento de los procesadores de propósito
  específico (GPUs, aceleradores).

Nota para el cierre: el paper es de 2019 y varias de sus predicciones se
cumplieron (adopción masiva, contenedores serverless), mientras que las
limitaciones de comunicación de grano fino siguen vigentes — y son exactamente
las que hicieron fallar a Prime Video.

---

## 11. Seguridad

La superficie de ataque cambia de forma, no desaparece.

### Modelo de responsabilidad compartida

El proveedor es responsable de la seguridad de **redes, servidores, sistema
operativo, su configuración y actualización**. El desarrollador es responsable
de la seguridad del **código, la lógica y la configuración de la aplicación**.

Traducción: serverless **elimina de tu lista** el parcheo del SO y del runtime
(una ventaja real y grande), pero **agranda** tu responsabilidad sobre permisos
y validación de entradas.

### OWASP Serverless Top 10 — los riesgos propios del modelo

- **Event injection.** El más específico de serverless. En una app web
  tradicional, la entrada llega por HTTP y podés poner un WAF adelante. En
  serverless, una función puede dispararse desde S3, una cola, un mail, un
  evento de IoT o un cambio en la base — **y en esos caminos no hay dónde poner
  un firewall**. Cada fuente de eventos es una entrada potencialmente
  controlada por un atacante.
- **Funciones sobre-permisionadas.** Roles IAM demasiado amplios. Es el
  problema #1 en la práctica: como cada función debería tener su rol mínimo, la
  cantidad de políticas explota y la gente termina poniendo comodines.
- **Entradas de eventos sin validar** desde API Gateway, S3, Pub/Sub, IoT.
- **Autorización rota**, exposición de datos sensibles, vulnerabilidades en
  dependencias.
- **Fuga de datos por cold start / reutilización de entorno**: si guardás datos
  de un usuario en una variable global, la siguiente invocación —posiblemente de
  otro usuario— los ve.

**Principio a transmitir:** en serverless, **el perímetro deja de existir**. La
seguridad se corre al nivel de cada función y de cada permiso individual.

---

## 12. Casos reales con números

*(Todos de fuentes secundarias / case studies de vendor. Presentarlos como
"reportado por", no como medición independiente.)*

### Coca-Cola — vending machines

- Telemetría de ~**1,4 millones de máquinas expendedoras** en todo el mundo,
  workload que antes requería middleware propio en servidores dedicados.
- Costo: de ~**USD 13.000 por máquina/año** a ~**USD 4.500** → **~66% de
  reducción**.
- Durante la pandemia, los sistemas Freestyle manejaron ~**80 millones de
  consultas por mes** con experiencia touchless, contra los 30 millones
  proyectados. Es el argumento de elasticidad hecho realidad: 2,7x el tráfico
  previsto sin reprovisionar nada.

### iRobot (Roomba)

- Procesa **más de 20 millones de eventos IoT por día** con AWS IoT + Lambda +
  Kinesis.
- **30% de reducción de costos cloud** frente a servidores tradicionales.
- Las funciones analizan telemetría en tiempo real y disparan acciones como
  actualizaciones de firmware.

### Netflix

- Migró parte del pipeline de transcodificación de video a Lambda, eliminando la
  necesidad de provisionar para el pico de carga de encoding.

### Y el contraejemplo

**Prime Video: -90% de costo yéndose de serverless** (sección 10.6). Poner los
dos juntos en la misma slide es el mejor cierre posible: la misma tecnología,
resultados opuestos, según el encaje con el problema.

---

## 13. Serverless open source y on-premise

Sirve para responder la pregunta inevitable: *"¿esto solo existe en la nube de
los grandes?"*. No.

| Framework | Características |
|---|---|
| **Knative** | El más maduro y desplegado. Dos componentes: *Serving* (autoescalado por request, incluido scale-to-zero) y *Eventing* (disparo por eventos). Escala a cero tras 30 s sin tráfico por defecto. Gestionado por la comunidad desde octubre de 2020. Es la base de Google Cloud Run. |
| **OpenFaaS** | Popular y simple. Recomienda mantener al menos una réplica viva para funciones que necesiten respuesta rápida. A diferencia de los otros, **también corre sobre Docker Swarm**, no solo Kubernetes. Usado por VMware, DigitalOcean, Citrix. |
| **Apache OpenWhisk** | El motor detrás de IBM Cloud Functions. |
| **Fission** | Enfocado en cold starts bajos. |

Preferencia de la comunidad (según relevamiento citado): Knative ~27%,
OpenFaaS ~10%.

**Punto conceptual importante:** estos frameworks demuestran que serverless es un
**modelo de ejecución**, no un producto de un vendor. Podés tener serverless
on-premise sobre tu propio Kubernetes — resignando la ventaja económica (el
clúster lo pagás igual), pero ganando el modelo de programación y evitando el
lock-in.

---

## 14. Estado del arte 2026 y hacia dónde va

*(Sección corta y de cierre. Datos de 2026, varias fuentes secundarias.)*

### 14.1 El modelo se está "des-purificando"

La tendencia más significativa de 2026 es que las plataformas están **relajando
los dogmas** del serverless original para cubrir sus puntos flojos:

- **AWS Lambda Managed Instances** (2026): funciones Lambda sobre EC2
  gestionadas, con acceso a hardware especializado, precios de EC2 (incluidos
  Savings Plans y Reserved Instances) y **procesamiento de requests en paralelo
  dentro de un mismo entorno**. Es Lambda renunciando al "un request por
  entorno" y al "pago solo por milisegundo" para las cargas estables.
- **AWS Lambda MicroVMs** (anunciado el 10 de julio de 2026): un primitivo nuevo
  con **aislamiento a nivel VM, arranque casi instantáneo y retención de
  estado**. Sesiones de **hasta 8 horas**, con estado que sobrevive a
  suspensiones y reanudaciones, endpoint HTTPS propio por microVM, baseline de
  2 GB / 1 vCPU escalable hasta 8 GB / 4 vCPU y escalado vertical automático
  hasta 4x. Facturación de baseline + consumo, con descuento por suspensión en
  reposo.

  **Esto es enorme conceptualmente:** rompe dos de los tres dogmas originales
  (efímero y stateless). Los casos de uso que cita AWS son entornos de
  desarrollo interactivos, plataformas de analytics de larga duración,
  **asistentes de IA de código** que necesitan mantener contexto entre
  iteraciones, y sandboxes de CI/CD. Es serverless orientado a **sesión** en vez
  de a **invocación**.

### 14.2 IA + edge

- Las cargas de inferencia de IA son el nuevo driver del serverless: hay
  adopción creciente de GPUs, que cambia las herramientas de autoescalado y la
  arquitectura de cómputo (Datadog, 2025).
- Cloudflare Workers, Vercel Edge Functions y Deno Deploy operan en 300+
  datacenters; se reporta inferencia con respuestas sub-50 ms en el edge.
- **WebAssembly** aparece como el runtime del edge: se reportan cold starts
  sub-milisegundo, porque WASM no necesita ni microVM ni proceso Node.

### 14.3 Estado con garantías: durable execution

Cloudflare **Durable Objects** ofrece estado fuertemente consistente y
single-threaded en el edge. Es la respuesta directa a la crítica de
statelessness: cómputo serverless que sí puede tener estado coordinado.

### 14.4 ARM está ganando

La proporción de funciones Lambda corriendo en **Arm** en vez de x86 creció de
**9% a 19% en dos años** (Datadog, 2025). AWS publicita hasta **34% mejor
precio-rendimiento** en Graviton. Es una decisión de una línea de configuración
que baja el costo ~20%, y casi nadie la toma.

### 14.5 Convergencia con contenedores

**66% de las organizaciones que usan funciones serverless también usan al menos
un servicio de orquestación de contenedores** (Datadog, 2025). El futuro no es
"serverless reemplaza a Kubernetes": es arquitecturas híbridas donde cada carga
va donde corresponde.

---

## 15. Preguntas que probablemente nos hagan (y las respuestas)

| Pregunta | Respuesta corta |
|---|---|
| "¿No hay servidores?" | Hay. No son tuyos y no los administrás. Como *wireless*. |
| "¿Es más barato?" | Depende de la utilización. Debajo de ~30% sí, muy; arriba, no. |
| "¿Y si mi función tarda una hora?" | No entra: Lambda corta a los 15 min. Hay que partirla, usar Cloud Run (60 min) o directamente contenedores. |
| "¿Cómo debuggeo esto?" | Es una debilidad real del modelo. Logs y tracing distribuido; el entorno local no reproduce el cloud. |
| "¿Cómo manejo la conexión a la base?" | Ese es *el* problema clásico: connection pooler (RDS Proxy) o bases con API HTTP. Ver 8.2. |
| "¿Me quedo atado a AWS?" | En la función no, en todo lo que la rodea sí. Contenedores serverless y Knative mitigan. |
| "¿Sirve para machine learning?" | Para inferencia liviana y batch sí; para entrenamiento no (timeout y GPU). Está cambiando en 2026. |
| "¿Es seguro correr mi código al lado del de otro?" | Sí: aislamiento por virtualización de hardware (Firecracker + KVM + seccomp), no por confianza. |

---

## 16. Fuentes

**Primarias / documentación oficial**

- [CNCF Serverless Whitepaper v1.0](https://github.com/cncf/wg-serverless/blob/master/whitepapers/serverless-overview/README.md) — definiciones, ciclo de vida, casos de uso y anti-patrones.
- [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/) — precios exactos y capa gratuita.
- [AWS Lambda FAQs](https://aws.amazon.com/lambda/faqs/) — límites de memoria, timeout, CPU proporcional.
- [Announcing Lambda MicroVMs (AWS Compute Blog, 10-jul-2026)](https://aws.amazon.com/blogs/compute/announcing-lambda-microvms-serverless-compute-environments-with-vm-level-isolation-and-near-instant-startup/)
- [Introducing AWS Lambda Managed Instances (AWS News Blog, 2026)](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)
- [AWS Lambda Managed Instances — página de producto](https://aws.amazon.com/lambda/lambda-managed-instances/)
- [Firecracker — sitio oficial](https://firecracker-microvm.github.io/) — microVMs, boot < 125 ms, 5 MiB de overhead.
- [Cloudflare — How Workers works](https://developers.cloudflare.com/workers/reference/how-workers-works/) — modelo de isolates de V8.
- [Aurora Serverless v2 — documentación AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html)
- [OWASP Serverless Top 10](https://owasp.org/www-project-serverless-top-10/) y [OWASP Serverless FaaS Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Serverless_FaaS_Security_Cheat_Sheet.html)

**Académicas**

- [Cloud Programming Simplified: A Berkeley View on Serverless Computing (arXiv 1902.03383)](https://arxiv.org/abs/1902.03383) — el paper de referencia. [PDF](https://arxiv.org/pdf/1902.03383)
- [Architectural Implications of Function-as-a-Service Computing (Shahrad et al., MICRO '19, Princeton)](https://parallel.princeton.edu/papers/micro19-shahrad.pdf)
- [Rise of the Planet of Serverless Computing: A Systematic Review (arXiv)](https://arxiv.org/pdf/2206.12275)

**Reportes con datos propios**

- [Datadog — State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/) — 65% Lambda, 70% Cloud Run, 56% App Service, 9%→19% ARM, 66% de solapamiento con contenedores.
- [Datadog — Key learnings del reporte 2025](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)

**Análisis y opinión**

- [Martin Fowler / Mike Roberts — Serverless Architectures](https://martinfowler.com/articles/serverless.html) — la referencia conceptual sobre BaaS vs FaaS y los drawbacks. *Ojo: es de 2018; el timeout que menciona (5 min) y la facturación de 100 ms están desactualizados.*
- [The Morning Paper — resumen del Berkeley View](https://blog.acolyer.org/2019/03/13/cloud-computing-simplified-a-berkeley-view-on-serverless-computing/)
- [DevClass — Reduce costs by 90% moving from microservices to monolith (caso Prime Video)](https://www.devclass.com/ci-cd/2023/05/05/reduce-costs-by-90-by-moving-from-microservices-to-monolith-amazon-internal-case-study-raises-eyebrows/1621790)
- [Network World — 6 lessons from the Prime Video serverless vs. monolith flap](https://www.networkworld.com/article/972298/6-lessons-from-the-amazon-prime-video-serverless-vs-monolith-flap.html)
- [Palark — Overview of self-hosted serverless frameworks for Kubernetes](https://blog.palark.com/open-source-self-hosted-serverless-frameworks-for-kubernetes/) — Knative, OpenFaaS, OpenWhisk, Fission.
- [Dashbird — Serverless case study: Coca-Cola](https://dashbird.io/blog/serverless-case-study-coca-cola/)
- [What is Firecracker? MicroVMs behind AWS Lambda (Browserbase)](https://www.browserbase.com/blog/what-is-firecracker)

---

## Apéndice — Glosario para la presentación

| Término | Definición corta |
|---|---|
| **FaaS** | Function as a Service. Código event-driven que escala a cero. |
| **BaaS** | Backend as a Service. Servicios de backend consumidos como API gestionada. |
| **Cold start** | Latencia extra de la primera invocación en un entorno nuevo. |
| **Warm start** | Invocación que reutiliza un entorno ya inicializado. |
| **Entorno de ejecución** | El sandbox (microVM) donde corre la función. Se reutiliza y se congela entre invocaciones. |
| **Escalar a cero** | Que la plataforma apague todas las instancias cuando no hay tráfico. |
| **GB-segundo** | Unidad de facturación: memoria asignada × tiempo de ejecución. |
| **microVM** | VM minimalista, sin hardware legacy, que bootea en milisegundos. |
| **Isolate** | Contexto liviano de V8 que aísla código dentro de un mismo proceso. |
| **Provisioned concurrency** | Entornos pre-calentados que se pagan por hora para evitar cold starts. |
| **Vendor lock-in** | Dependencia de un proveedor que hace costosa la migración. |
| **Idempotencia** | Que reejecutar una operación no cambie el resultado. Crítico porque las plataformas reintentan invocaciones asíncronas. |
