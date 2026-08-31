# Etapa 3 — Guion de exposición

> Diez minutos, 22 láminas, cuatro expositores. Es un guion para **decir**, no un
> resumen para leer: está calibrado a 145 palabras por minuto y verificado con
> `scripts/guion-timing.py`. Son **9:17 de habla**; con los cambios de expositor
> cierra cerca de **9:49**, o sea al filo. Los recortes marcados no son opcionales
> si un bloque se pasa.
>
> **Reparto.** Bonadeo 1–6 · Casermeiro 7–10 · Lezcano 11–16 · Lurati 17–21 ·
> Casermeiro cierra con la 22.
>
> **Regla del tiempo.** Ninguna tabla se lee en voz alta. Las láminas 4, 9, 13 y 19
> son de consulta: se enuncia lo que significan y se sigue. Cada bloque lleva marcado
> qué se recorta primero si el reloj apura.

---

## BONADEO · láminas 1 a 6 · cierra en 2:20

### Lámina 1 — Portada · 13 s

Buenas. Grupo 310, comisión 403. Presentamos la Etapa 3 del Trabajo Práctico
Integrador: la planificación de un proyecto de TI para Personal, sobre el proceso de
instalación de internet con fibra óptica.

### Lámina 2 — El problema · 26 s

El proceso tiene tres debilidades: no hay trazabilidad de la orden, la cola no tiene
criterio de priorización, y no se controla la competencia del técnico al asignarle
una orden.

Las dos últimas son los riesgos **R07 y R04** de la Etapa 2, severidad 12, y son los
únicos que quedaron sin plan de tratamiento. Este proyecto es el tratamiento de los
dos.

### Lámina 3 — El proyecto · 23 s

El proyecto es una plataforma de gestión de órdenes de trabajo con aplicación móvil
de campo: motor de asignación por competencia certificada, aplicación *offline-first*
con checklist y conformidad del cliente, cuatro integraciones y capa de seguridad.

Interviene las actividades 3 a 9 del proceso, y lo que queda afuera es lo que ya tiene
tratamiento propio.

### Lámina 4 — Objetivos · 20 s

Cuatro objetivos, con indicador, línea base, meta y plazo. Dos cosas. Las líneas base
son **supuestos declarados**, porque las etapas anteriores no relevaron indicadores, y
medirlas es un entregable de la fase 2. Y O4 no tiene línea base: esa imposibilidad de
medir es la definición del riesgo R07.

### Lámina 5 — Alternativas · 28 s

Tres alternativas. No son tres formas de construir lo mismo: son **tres proyectos
distintos**. Elegimos el primero porque trata riesgos sin tratamiento, ejecuta un
objetivo ya comprometido en la Etapa 1 y es el único que interviene el proceso
crítico.

Se construye como **SaaS**: no desarrollamos el producto, lo configuramos. La
contrapartida: los datos de clientes salen del perímetro y eso agrava el R05. Se
compensa por contrato.

### Lámina 6 — Ciclo de vida · 30 s

El ciclo de vida es híbrido, y no por compromiso.

**Predictivo** para la selección del proveedor, la contratación y el cumplimiento
normativo: requerimientos cerrables por anticipado. **Incremental** para la
configuración, la experiencia de uso y el despliegue: la usabilidad con guantes y sin
conectividad no se especifica de antemano, se calibra con un piloto.

No es cascada porque entregarla recién al final arriesga que los técnicos no la
adopten. No es ágil porque hay contratos, plazos de entrega y un presupuesto aprobado
por anticipado.

> **Si vas corto:** en la 5, decí solo *«tres proyectos distintos, elegimos el primero
> por R04 y R07»* y pasá a SaaS.
>
> **Paso a Casermeiro:** «Con el ciclo de vida definido, así se organiza el trabajo.»

---

## CASERMEIRO · láminas 7 a 10 · cierra en 4:07

### Lámina 7 — Las once fases · 22 s

Once fases, cada una con un entregable verificable. Señalo tres: la fase 2 mide las
líneas base, que es lo que habilita evaluar los objetivos; la fase 3 es el proceso
formal de compras; y la fase 11 cierra el circuito con la Etapa 2, dando de alta el
sistema en la CMDB.

### Lámina 8 — EDT · 27 s

De ahí sale la EDT: once paquetes de primer nivel y **cincuenta paquetes de trabajo**,
cada uno con predecesora, duración, perfil y entregable. No descomponemos por debajo
del nivel en que un paquete tiene un entregable verificable y un responsable.

Y los solapamientos están puestos **a propósito**: varias actividades comparten perfil
en la misma ventana. Es el insumo del análisis de sobreasignación que viene después.

### Lámina 9 — Recursos humanos · 25 s

Nueve perfiles, once personas, **4.240 horas-persona**. Ningún perfil figura acá sin
ser responsable de al menos un paquete de la EDT: la carga sale de sumar esas
duraciones.

Ninguno alcanza dedicación completa, así que todos conservan sus tareas de línea. Hay
dos personas en integraciones y dos en pruebas: no es volumen, es aplanamiento, y
evita veintitrés días de atraso.

### Lámina 10 — Higiene y seguridad · 25 s

Analizamos los sectores del proceso crítico, incluido el campo, que es donde están los
riesgos graves. Ordenamos las medidas por los cuatro niveles de prevención primaria:
diseño, origen, medio y persona. Asumimos que el equipo de protección personal es el
**escalón más débil**, porque depende de una conducta diaria.

Y hay un caso donde el propio sistema es la medida preventiva: la habilitación vigente
pasa a ser condición de despacho.

> **Si vas corto:** la 7 se resuelve en una frase — *«once fases, cada una con
> entregable verificable; la 11 cierra el circuito con la CMDB de la Etapa 2»*.
>
> **Paso a Lezcano:** «Esas medidas se materializan en dos planos.»

---

## LEZCANO · láminas 11 a 16 · cierra en 6:30

### Lámina 11 — Plano de la base operativa · 18 s

Plano de la base operativa, escala 1:125. Lo que hay que ver: circulaciones peatonal
y vehicular separadas, matafuegos identificados por clase, y recorridos de evacuación
hasta el punto de encuentro.

Las cotas son mínimos de diseño supuestos, a validar con Higiene y Seguridad.

### Lámina 12 — Croquis de trabajo en campo · 27 s

El trabajo en campo es donde están los riesgos graves: altura, riesgo eléctrico y
espacio confinado.

Dos cosas. El vehículo se ubica aguas arriba y actúa como **barrera física**: es
prevención en el medio, no sobre la persona. Y en el domicilio, la lista de
verificación **bloquea el inicio de la orden** si no se completa: el control deja de
depender de la memoria del técnico.

### Lámina 13 — Activos y forma de adquisición · 21 s

No voy a leer la tabla: importa la última columna. Cada modalidad se elige por una
razón de riesgo. Suscripción anual porque en SaaS no hay licencia perpetua. Bolsa de
horas con tope porque un precio cerrado obligaría a congelar la configuración antes
del piloto, que es cuando está previsto ajustarla.

### Lámina 14 — RFI y RFP · 28 s

La selección usa dos instrumentos sucesivos. El **RFI** reduce la incertidumbre sobre
el mercado: qué plataformas existen, qué integran de forma nativa, dónde alojan los
datos. El **RFP** reduce la incertidumbre sobre la oferta: propuesta comparable y
vinculante.

Los criterios se ponderan antes de abrir las propuestas y los tres primeros suman el
65%. Hay un umbral excluyente: sin alojamiento en la región, la propuesta queda
afuera.

### Lámina 15 — Tiempos · 25 s

Sobre los cincuenta paquetes calculamos el camino crítico: **187 días hábiles** a
fechas tempranas, con treinta actividades críticas.

Pero eso supone recursos ilimitados. Contra una persona por perfil aparecen seis
tramos de sobreasignación: con nivelación pura el proyecto se va a 215 días;
reforzando integraciones y pruebas queda en **192 días**, unos 9,1 meses. Adoptamos
esa, y el fundamento es económico.

### Lámina 16 — Diagrama de red · 16 s

En rojo, las treinta actividades críticas. La cadena pasa por el arranque, por los
treinta y un días de selección del proveedor —el tramo más largo y menos
comprimible— y por las cuatro integraciones encadenadas sobre un mismo especialista.

> **Si vas corto:** la 13 se resuelve con un solo ejemplo, el de la bolsa de horas.
> Y la 16 con una frase: *«en rojo el camino crítico; el cuello de botella es la
> selección del proveedor y la cadena de integraciones»*.
>
> **Paso a Lurati:** «Ese cronograma, en el tiempo, se ve así.»

---

## LURATI · láminas 17 a 21 · cierra en 8:51

### Lámina 17 — Gantt · 22 s

Cronograma aplanado, en **meses relativos al día cero**, que es la aprobación del
Acta: no lo fechamos en calendario porque la fecha de inicio real no está definida.

Relevamiento y selección hasta el mes 3, configuración e integración hasta el 5,
pruebas y piloto hasta el 7, despliegue y estabilización hasta el 9.

### Lámina 18 — Histograma de recursos · 18 s

Mismo eje de tiempo, perfil por perfil. Las barras celestes claras son los picos de
dos personas: son exactamente las ventanas que justificaron el refuerzo en
integraciones y pruebas. La línea de puntos es la dotación asignada, y no se supera
ningún día.

### Lámina 19 — Costos · 32 s

El costo del año 1: recursos humanos propios 112.624 dólares, dispositivos 39.060,
servicios 103.150. Da 254.834 de costo directo. Con 12% de indirectos y 15% de
contingencia, el presupuesto del año 1 es de **328.226 dólares**.

La contingencia no es un porcentaje de estilo: se justifica con R03, R04, R05 y R07.

A tres años el costo total de propiedad es de 531.460, y el **38% es recurrente**: ese
es el rasgo económico del modelo contratado como servicio.

### Lámina 20 — Factibilidad técnica · 29 s

Técnicamente no requerimos tecnología por desarrollar: las plataformas de Field
Service Management son un producto maduro.

El problema está en otro lado, y lo declaramos como **riesgo abierto**, no como
hipótesis favorable: no está documentado si el SGOT, el CRM y el NMS exponen
interfaces de programación, y de eso dependen cuatro paquetes del camino crítico. Se
verifica en el paquete 2.3 y dejamos un plan alternativo cotizado en el RFP.

### Lámina 21 — Factibilidad económica · 32 s

Económicamente: valor actual neto de **más 31.515 dólares** a cinco años, tasa interna
de retorno del 19% contra una tasa de corte del 15%, y repago a los 3,14 años.

Es viable, pero el margen es estrecho y conviene decirlo: a tres años todavía no se
repaga. El umbral de indiferencia está en el 85% de realización de los beneficios.

La sensibilidad no está en los costos sino en los beneficios, y el más frágil es O1.

> **Si vas corto:** en la 19 basta con *«328.226 el año 1, 531.460 a tres años, y el
> 38% es recurrente porque es SaaS»*. **La 21 no se recorta:** es el remate del
> trabajo.
>
> **Paso a Casermeiro:** «Queda la dimensión legal, y con eso la conclusión.»

---

## CASERMEIRO · lámina 22 · cierra en 9:49

### Lámina 22 — Factibilidad legal y conclusión · 50 s

Alojar datos personales en una plataforma contratada como servicio los saca del
perímetro: el proveedor pasa a ser encargado del tratamiento, el alojamiento fuera del
país configura transferencia internacional, y el deber de seguridad sigue siendo
nuestro.

La conclusión es en tres partes. **Técnicamente factible**, con un supuesto crítico
declarado: las interfaces. **Económicamente viable pero de margen estrecho**: a tres
años no se repaga. Y **legalmente factible bajo condición contractual**: sin las
cláusulas del punto 8 el proyecto agravaría el R05 en lugar de contenerlo.

Por eso la decisión de despliegue masivo no se toma con la aprobación del Acta, sino
en el **paquete 8.4**: una vez medidas las líneas base, verificadas las interfaces y
cerrados los precios. Muchas gracias.

---

## Reloj de control

| Corte | Quién termina | Dura | Reloj |
|---|---|---|---|
| Lámina 6 | Bonadeo | 2:20 | 2:20 |
| Lámina 10 | Casermeiro | 1:39 | 4:07 |
| Lámina 16 | Lezcano | 2:15 | 6:30 |
| Lámina 21 | Lurati | 2:13 | 8:51 |
| Lámina 22 | Casermeiro | 0:50 | 9:49 |

El reloj ya incluye 8 segundos por cambio de expositor. Queda poco más de un cuarto
de minuto de colchón: si un bloque se pasa de su corte, el siguiente aplica sus
recortes marcados: **no se recupera
tiempo acelerando la lectura**, se recupera sacando contenido.

## Preguntas probables

- **¿Por qué SaaS y no desarrollo propio?** Reduce plazo y riesgo técnico, a cambio de
  costo recurrente y de sacar los datos del perímetro, que es lo que se compensa por
  contrato.
- **¿Por qué dos personas en integraciones y en pruebas?** Con una por perfil el
  proyecto pasa de 192 a 215 días. Los conflictos caen sobre actividades críticas, así
  que no se resuelven corriendo tareas dentro de la holgura.
- **¿Por qué el VAN es tan ajustado?** Porque los beneficios descansan sobre líneas
  base que hoy son supuestos. Está dicho a propósito, y por eso la decisión de
  despliegue se difiere al paquete 8.4.
- **¿Por qué el cronograma no tiene fechas?** Porque la fecha de inicio real no está
  definida. Va en meses relativos al día cero.
- **¿Qué pasa si el SGOT no tiene API?** Hay plan alternativo en tres vías: base de
  datos intermedia, intercambio por lotes o automatización de interfaz. Cada una se
  cotiza en el RFP; las tres cuestan más horas del especialista de integraciones.
