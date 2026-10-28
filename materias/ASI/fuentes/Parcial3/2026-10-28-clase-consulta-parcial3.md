# Clase de consulta — Parcial 3 (U5 + U6)

Notas organizadas de la clase de consulta del profesor (transcripción enviada el 2026-10-28). Lo que está entre comillas es casi textual.

---

## 1. Formato del examen

- **Comisiones 3 y 4 rinden el jueves** (2026-10-29). El resto "tiene margen de tiempo todavía".
- **No hay Gantt ni diagrama de red para hacer:** "No vamos a hacer Gantt. No vamos a hacer un diagrama de red tampoco. ¿Por qué? Porque no hay tiempo." Pero **hay que entenderlos**, porque "por ahí lo van a tener que justificar". Ante la pregunta de si podrían pedir completar algo y ver cuál es el camino crítico, respondió "Claro", sin desarrollar.
- **Puede haber preguntas teóricas:** "Se te puede preguntar, ¿qué es la tasa interna de retorno? Probablemente sea una especie de multiple choice, no sé todavía cómo." Y "Habrá cosas que escribir, seguro. Pero a lo mejor puede ser un mix."
- **Fórmulas:** No es importante acordárselas de memoria, sí **para qué sirve y qué mide cada indicador**. Excepción: Para la variación de costos dijo "Esto tiene que acordarse. Acuérdense cómo es la fórmula" (SV y CV).
- **Canvas:** Recomienda llevar una plantilla impresa "por las dudas", pero "lo más probable es que, si pedimos algo, lo escriban en una hoja". Probablemente pidan **"no el canvas, pero sí detallar parte del canvas"**.
- **Contexto:**
  - **Proyectos:** Siguen con los proyectos del "año 1" (Bancorp).
  - **Emprendedorismo:** **Temática bancaria, pero desde afuera**: "alguna aplicación, un producto que le vamos a ofrecer al banco, o un servicio... ahí ya no somos el banco. Somos alguien de afuera."
- **Consulta extra:** Ofreció media hora de dudas el jueves a la mañana (organizar escribiéndole).

---

## 2. Unidad 5 — Gestión de Proyectos

### Red de tareas y holguras (entender, no dibujar)

- **Convención que usa el profe:** La primera tarea empieza el **día 1**; FT = IT + duración − 1 (lunes + martes = 2 días: empieza el 1, termina el 2); la siguiente empieza **al día siguiente**. Mencionó que la herramienta arranca en 0, "pero es lo mismo".
- Con varias predecesoras, la tarea empieza **el día siguiente a la que termina más tarde**.
- **Pasada hacia atrás:** Se llena "de atrás para adelante" con la misma lógica.
- **Holgura total:** Cuánto puede demorarse una tarea **sin cambiar la fecha de fin del proyecto**. Holgura 0 = camino crítico: "Si me atraso en este, me cambia el número".
- **Holgura libre:** Cuánto puede demorarse **sin cambiar el inicio temprano de la sucesora**. "Es lo que menos me preocupa. Me interesa más la holgura de la izquierda", es decir, la total.
- **Para qué sirven las holguras: Nivelación de recursos.** Ej. del profe: Los primeros días se necesitaban 4,25 personas y después poco más de 2. Moviendo dentro de su holgura las tareas que la tienen (B dos días, C cuatro días), la carga queda pareja en 2,5 personas y no hace falta contratar gente por dos días. Efecto: **Al consumir holguras pueden aparecer nuevos caminos críticos** (en su ejemplo quedaron dos).

### Valor Ganado

- **Para qué:** Técnica de **seguimiento**. Compara si el proyecto está atrasado o adelantado (tiempo) y si gasta de más o de menos (costo), todo llevado a dinero "para unificar" y poder comparar.
- **BAC:** Presupuesto total, suma de lo estimado para cada tarea.
- **PV:** Lo que **según el plan** tendría que estar hecho al día de corte, valuado en dinero.
- **EV:** Lo que **realmente** se hizo, valuado al presupuesto.
- **AC:** "La plata que realmente gasté, lo que saqué de la billetera."
- **SV = EV − PV:** Negativo → atrasado. "No es que esté gastando menos. Es que estoy haciendo menos." Lo que se mide acá es tiempo, expresado en plata.
- **CV = EV − AC:** Negativo → gasto ineficiente.
- **Criterios para tareas en curso** (se define **al comienzo y es fijo para todo el proyecto**, para comparar "naranja con naranja"):
  - **0%:** Como si no hubiera empezado.
  - **100%:** Como si estuviera terminada.
  - **20/80:** Según haya avanzado poco o mucho.
  - **50/50:** La mitad. "Normalmente lo que hacemos es considerar 50, porque es más fácil."
- **Lo que pueden preguntar:** Si el proyecto es eficiente o ineficiente, y si está atrasado o adelantado, interpretando los números.

### Costos: Evaluación de proyectos (saber qué es y para qué sirve)

- **Contexto:** Como gerente de sistemas vas a tener que **defender tu proyecto ante la dirección** contra otros proyectos que compiten por el mismo dinero (sensores para galletitas vs. flota de camiones vs. máquinas nuevas).
- **Beneficios = ingresos + costos evitados:** Ej. de los sensores: Menos devoluciones, menos refabricación, menos logística, mejor imagen y más ventas. Todo hay que **monetizarlo** para comparar.
- **Tiempo de recuperación:** En cuánto tiempo se recupera la inversión. **Desventajas:** No considera beneficios posteriores al recupero (dos proyectos que recuperan en el mismo año empatan aunque uno gane el doble después) ni el rendimiento del dinero (un plazo fijo podría rendir más).
- **Tasa promedio de retorno:** Beneficios sobre inversión, en **porcentaje**; considera la **vida útil** del bien.
- **Valor actual y valor futuro:** "La plata trabaja." Un millón hoy vale más que un millón dentro de cuatro años. El VF dice cuánto valdrá la plata de hoy; el VA, cuánto vale hoy la plata futura. Sirven para **comparar en un mismo momento**.
- **VAN:** Valor actual de los beneficios menos valor actual de las inversiones. Conviene si **es mayor que 0**.
- **TIR:** Da una **tasa** en vez de un valor monetario, así que es más fácil de comparar entre proyectos. "Es importantísima al momento de defender un proyecto." **Cuanto más grande, mejor.** No considerar inflación. Tasa de descuento = costo de capital + % de riesgo.
- **ROI:** Cuánto beneficio entrega cada peso invertido.
- **Los más importantes:** "ROI, valor actual, TIR, que son los que sirven para comparar proyectos. Y qué ventajas y qué desventajas tienen."

### Adquisiciones ("tampoco es lo más crítico")

- **Planificar las compras en el tiempo:** No se compra todo al comienzo; se compra cuando se necesita.
- **Qué se adquiere:** Bienes, pero también servicios: Mano de obra, proveedores externos, consultores.
- **Cómo:** Hacerlo internamente, subcontratar o tercerizar (outsourcing). Para bienes: **Comprar, alquilar o leasing** (alquiler con opción de compra al final mediante un importe preestablecido; "no es un alquiler ni una compra").
- **Selección del proveedor:**
  - **Licitación:** "Algo sobre cerrado", con un proceso definido de antemano.
  - **Solicitud de propuesta (RFP).**
  - **Compra común:** Comparar presupuestos; para cosas no tan caras ni riesgosas.
- **TCO (costo total de propiedad):** "No le voy a pedir la fórmula." Hay que saber que no es solo el bien: Incluye costo inicial, soporte y mantenimiento. "Probablemente te preguntemos qué costos tiene que tener en cuenta." Las siglas (CIS, etc.) no importan.
- **Contratos:** Cómo se negocia el precio (por hora, con incentivos), **quién asume el riesgo** (proveedor o cliente), finalización anticipada y resolución de conflictos.
- **RFI vs. RFP:** RFI = pedir **información** a un proveedor (especificaciones, para después armar una propuesta). RFP = "el **presupuesto**", la propuesta.
- **Matrices de comparación:** "No le den mucha bolilla." No van a pedir armar un RFP, pero sí pueden preguntar **qué es un RFP**.

---

## 3. Unidad 6 — Emprendedorismo

### Lean Startup (conceptos que nombró explícitamente)

- **Qué es Lean Startup y por qué se basa en un ciclo:** Crear → validar → aprender → cambiar. Cuando se cambia aparece el **pivot**, y se vuelve a medir y validar con un nuevo MVP.
- **MVP:** La primera versión del producto que se lanza al mercado. "En realidad es el mayor producto: lo que más puedo hacer en menos tiempo", el producto más grande que puedo sacar en un mes para **validar ideas**.
- **Desarrollo de clientes:** Tener una propuesta de valor, salir a validarla con clientes y ver si están dispuestos a pagar. Si pagan y el mercado alcanza, crezco. Si el mercado es chico, crezco lento. Si no pagan, busco otros clientes.
- **Ejemplo del robot de golf (pivot):** El robot cortacésped se valida con campos de golf, pero el mercado es chico. Se suma una línea nueva: Importar cortadoras eléctricas chinas y **venderlas** con soporte posventa a los countries de Funes, mientras a los campos de golf se les **alquila** la máquina grande. Mismo objetivo (cortar pasto), modelo de negocio distinto por segmento.
- **Ajuste producto-mercado (product-market fit):** Encontrar la relación entre propuesta de valor y segmento: "Lo que yo ofrezco, que la gente me lo saque de las manos". Ej: Una herramienta agro que no compra el productor que vive en el campo, pero sí el ingeniero agrónomo asesor o la empresa con campos en todo el país que quiere monitorear desde Rosario.

### Lo más importante: Propuesta de valor ↔ segmento

- **"Nos va a interesar que hagan esa relación entre propuesta de valor y segmento de clientes."**
- **La misma solución tiene un valor distinto para cada segmento.** Ej. DeepAgro (cámaras con IA que solo fumigan la maleza, 70–80% menos herbicida):
  - **Productor agropecuario:** **Plata** (70% menos de costo en fumigación).
  - **Provincia o municipio:** **Ambiente** (70% menos contaminación, suelos más sanos). Le pido promoción, un stand, beneficios a quien compre.
  - **Empresas de servicio de pulverización:** **Trabajo** (te eligen más porque ofrecés algo ambiental y económicamente mejor).
- La propuesta de valor sirve para **captar la atención** de quien necesito que me escuche, yendo **"al dolor que tiene cada uno"**.
- **Segmentos específicos, no genéricos:** No "gente joven" sino "estudiantes de Rosario en los primeros años de la facultad, que vienen del interior, con ingresos superiores a tanto". "Si son muy genéricos, va a ser tirar el tiro al aire."
- **Lienzo de propuesta de valor:** "No vamos a pedir el lienzo", pero entenderlo ayuda a encontrar la propuesta.
- **Mercados, precios y rentabilidad:** "No vamos a preguntar en profundidad", pero leerlos ayuda a entender lo anterior.

### Socios clave (aclaración a una pregunta)

- **No son los socios de la sociedad (SRL):** Son los **asociados clave**, aquellos **de los que depende tu modelo de negocio**, aunque ni sepan que lo son.
- **Ejemplos:**
  - **Vercel:** Si cambia sus políticas, cobra más o cierra, hay que migrar y cambia todo.
  - **API de Mercado Pago o de Dólar Hoy:** Si cambian el protocolo o dejan de funcionar.
  - **Proveedor de remeras de algodón:** Si deja de traerlas y ofrece poliéster, la tintura no prende, hay que buscar otro más caro y subir precios.
  - **Proveedores de IA:** Si cambian el costo de los tokens.
  - **NVIDIA para DeepAgro:** Sus placas para reconocimiento de imágenes; cambiar de marca obliga a rehacer procesos. Además NVIDIA les daba soporte y productos antes del lanzamiento.
- **Por qué importan:** Cuando cambia un socio clave, **cambian las actividades, los recursos, los costos y el precio de venta**.

### Canales vs. relación con clientes (aclaración a una pregunta)

- **Canales:** **Cómo llega el producto** al cliente y **cómo se entera** de él. Ej. remeras: Tienda, puesto en la feria, sitio online, Instagram, envío por Mercado Libre.
- **Relación con clientes:** **Marketing, cómo vendés.** Se representa con el **doble embudo**:
  - **Get:** Conseguir clientes nuevos. Ej: 10.000 mails a 1 dólar → 1.000 clics → 100 consultan → 10 compran → 1.000 / 10 = **100 dólares por cliente**. Si en vez de mandar mails masivos se hace una campaña en un club donde están los compradores potenciales y cuesta 100 dólares, con los mismos 10 clientes el costo baja a **10 dólares por cliente**.
  - **Keep:** Que no se vayan, porque cada cliente perdido son los 100 dólares que costó más sus ventas futuras. Conviene más cuidar los clientes que conseguir nuevos.
  - **Grow:** Venderle más a los que ya tengo, a bajo costo porque están cautivos.
