# Serverless — cuestionario para la clase

10 preguntas sobre la presentación (8 de opción múltiple, 2 de V/F), 1 punto
cada una. El Google Form se genera con `cuestionario-form.gs`: pegarlo en
script.google.com, ejecutar `crearCuestionario` y copiar del log el link para
compartir. Si se cambia una pregunta acá, se cambia también en el `.gs`.

La correcta está marcada con **✓**. Entre paréntesis, la lámina de donde sale.

1. **(V/F) Serverless significa que la aplicación se ejecuta sin servidores.** (L2)
   - Verdadero
   - **✓ Falso**: los servidores existen; los administra el proveedor, no vos.

2. **Según la definición de la CNCF que usamos, ¿cuál NO es una propiedad de serverless?** (L3)
   - a) No administrás infraestructura
   - b) Escala hasta cero cuando no hay pedidos
   - **✓ c) La función mantiene el estado en memoria entre pedidos**
   - d) Pagás por uso real, no por tener algo encendido

3. **¿Cuál es la diferencia entre FaaS y BaaS?** (L4)
   - a) FaaS es para el frontend y BaaS para el backend
   - **✓ b) FaaS es tu código, que se dispara con eventos; BaaS son servicios gestionados que consumís por API (base, autenticación, almacenamiento)**
   - c) Son lo mismo con distinto nombre según el proveedor
   - d) FaaS se cobra por hora y BaaS por milisegundo

4. **¿Qué es el cold start?** (L5–6)
   - **✓ a) La demora extra de una invocación que tiene que preparar un entorno nuevo (fase INIT) porque no había uno disponible**
   - b) El tiempo que tarda en desplegarse una nueva versión del código
   - c) Un error que ocurre cuando la función supera el tiempo máximo de ejecución
   - d) El apagado del entorno después de varios minutos sin pedidos

5. **(V/F) Como el entorno se reutiliza entre invocaciones, una función puede guardar datos en memoria y confiar en que el siguiente pedido los va a encontrar.** (L5)
   - Verdadero
   - **✓ Falso**: es stateless por contrato; el estado va a una base o a un caché externo.

6. **¿Cómo aísla AWS Lambda el código de distintos clientes en la misma máquina física?** (L7)
   - a) Con contenedores que comparten el kernel del host
   - b) Con máquinas virtuales tradicionales completas
   - c) Con isolates de V8, como Cloudflare Workers
   - **✓ d) Con microVMs de Firecracker, que arrancan en ~125 ms con aislamiento por hardware**

7. **¿Cómo factura AWS Lambda?** (L8)
   - a) Una tarifa fija por hora por cada función desplegada
   - b) Solo por la cantidad de datos transferidos
   - **✓ c) Por cantidad de pedidos más la duración en GB-segundo (memoria × tiempo), medida al milisegundo**
   - d) Por la cantidad de líneas de código desplegadas

8. **Comparando Lambda con un servidor equivalente encendido todo el tiempo, ¿a partir de qué uso aproximado deja de convenir serverless?** (L9)
   - a) Alrededor del 5 %
   - **✓ b) Alrededor de un tercio (~34 %)**
   - c) Alrededor del 90 %
   - d) Nunca: serverless siempre es más barato

9. **500 funciones corren a la vez y cada una abre su propia conexión a una base Postgres. ¿Qué pasa y cómo se resuelve?** (L10)
   - **✓ a) Se agotan las conexiones de la base; se resuelve con un pooler (RDS Proxy, PgBouncer) o con bases que se consultan por HTTP**
   - b) No pasa nada: Postgres soporta miles de conexiones simultáneas
   - c) Las funciones entran en cold start; se resuelve con Provisioned Concurrency
   - d) La base pasa a modo serverless automáticamente

10. **Prime Video bajó un 90 % el costo de su monitoreo de calidad al sacarlo de serverless. ¿Cuál fue la causa principal?** (L12)
    - a) Lambda tenía cold starts demasiado largos
    - b) AWS subió el precio de Lambda en 2023
    - **✓ c) Mover datos entre muchas funciones encadenadas costaba más que procesarlos; lo juntaron en un solo proceso**
    - d) Serverless no soporta procesamiento de video

**Clave rápida:** 1 F · 2 c · 3 b · 4 a · 5 F · 6 d · 7 c · 8 b · 9 a · 10 c
