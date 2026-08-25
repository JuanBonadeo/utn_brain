[ASI26\_TPIntegrador\_Etapa3 - Proyecto de TI](https://docs.google.com/document/d/1cFn3_HxwwDUijrEShWo-lDDR51-ZMMi7i5Xd8Nv89yQ/edit?tab=t.0#heading=h.kx0qvelh4y4)  
—

| Clase 28/07  Definan el problema ¿Qué está fallando o qué oportunidad detectaron? Ejemplo: muchos tickets repetidos, procesos manuales, falta de trazabilidad, sistema obsoleto, demoras, errores, baja disponibilidad. Formulen el proyecto “Vamos a implementar/desarrollar/mejorar/adquirir una solución de TI para resolver X problema en Y proceso.” Delimiten alcance Qué incluye y qué no incluye. Esto evita proyectos gigantes tipo “digitalizar toda la empresa”. Redacten objetivos medibles No escriban sólo “mejorar el sistema”. Mejor: Reducir en un 30% los tiempos de respuesta en 6 meses. Disminuir en un 40% los tickets repetidos. Alcanzar un 95% de disponibilidad mensual. Planteen alternativas Al menos dos o tres formas de resolver el mismo problema: desarrollo interno, solución SaaS, tercerización, mejora del sistema actual, reemplazo completo, integración con herramienta existente. Elijan una y justifiquen No alcanza con decir “elegimos esta porque es mejor”. Tienen que justificar por costo, tiempo, riesgo, integración, seguridad, mantenimiento y conocimiento disponible. Después recién planifican A partir de la alternativa elegida definen: ciclo de vida, fases, EDT, actividades, responsables, tiempos, recursos, adquisiciones, costos y factibilidad.  |
| :---- |

La idea central:

> **En la Etapa 3 dejan de analizar la organización y pasan a transformar los problemas, riesgos y necesidades detectados en las etapas anteriores en un proyecto de TI concreto, planificado, presupuestado y evaluado.**

## **Bloque 1 — Qué se espera realmente en la Etapa 3**

Comenzaría mostrando esta cadena:

> Problema o necesidad detectada → Proyecto de TI → Objetivos → Alternativas → Solución seleccionada → EDT → Recursos → Tiempo → Costos → Factibilidad.

La explicación clave sería:

> No deberían desarrollar cada apartado como una respuesta independiente. Todo tiene que estar relacionado. Los perfiles surgen de las actividades de la EDT; las adquisiciones surgen de la solución seleccionada; el Gantt surge de las actividades, duraciones y dependencias; los costos surgen de los recursos y adquisiciones; y la factibilidad evalúa si todo lo anterior puede realizarse.

### **Pregunta disparadora**

> ¿Qué problema relevante de su organización quieren resolver y qué resultado debería existir cuando termine el proyecto?

## **Bloque 2 — Definir correctamente el proyecto**

### **Qué deberían presentar**

Una descripción que responda:

* ¿Qué problema resuelve?  
* ¿Qué solución se propone?  
* ¿Qué proceso o servicio afecta?  
* ¿Quiénes serán sus usuarios?  
* ¿Qué incluye?  
* ¿Qué no incluye?

### **Ejemplo incompleto**

> Implementar inteligencia artificial en la empresa.

### **Ejemplo correcto**

> Implementar un asistente virtual interno integrado a Microsoft Teams para responder consultas operativas frecuentes, reducir la carga de tickets de nivel 1 y derivar a soporte humano las consultas no resueltas.

## **Bloque 3 — Objetivos cuantificables**

La consigna no pide únicamente “objetivos”, sino criterios que permitan evaluar avance y cumplimiento.

Explicaría que cada objetivo debería tener:

* resultado;  
* indicador;  
* valor inicial o meta;  
* plazo;  
* forma de medición.

### **Ejemplo**

> Reducir en un 30% la cantidad mensual de tickets de soporte de nivel 1 durante los primeros seis meses posteriores a la implementación, utilizando los reportes del sistema ITSM.

### **Error frecuente**

Definir actividades como objetivos:

> “Capacitar al personal” o “desarrollar el sistema”.

Esas son actividades o entregables. El objetivo debería expresar el resultado:

> Lograr que el 90% de los usuarios complete satisfactoriamente la evaluación posterior a la capacitación.

## **Bloque 4 — Alternativas y selección**

Las alternativas deben resolver **el mismo problema**, pero de maneras diferentes.

### **Ejemplo**

| Alternativa | Descripción |
| ----- | ----- |
| Desarrollo interno | El equipo propio diseña y desarrolla toda la solución. |
| Solución SaaS configurable | Se contrata una plataforma existente y se personaliza. |
| Desarrollo tercerizado | Un proveedor construye la solución según requerimientos. |

### **Criterios para comparar**

* costo;  
* tiempo;  
* calidad;  
* riesgo;  
* conocimientos disponibles;  
* dependencia de proveedores;  
* seguridad;  
* escalabilidad;  
* mantenimiento;  
* integración con sistemas actuales.

Pueden usar una matriz sencilla:

| Criterio | Peso | Interno | SaaS | Tercerizado |
| ----- | ----- | ----- | ----- | ----- |
| Costo | 25% | 3 | 4 | 2 |
| Tiempo | 20% | 2 | 5 | 3 |
| Integración | 20% | 5 | 3 | 4 |
| Seguridad | 20% | 4 | 4 | 3 |
| Mantenimiento | 15% | 3 | 4 | 3 |

La conclusión no debería ser:

> Elegimos SaaS porque es la mejor.

Debería ser:

> Se selecciona SaaS porque obtiene el mayor resultado ponderado, reduce el plazo de implementación y se integra con la infraestructura existente, aunque genera dependencia del proveedor y costos recurrentes.

## **Bloque 5 — Ciclo de vida, fases y EDT**

### **Primero: ciclo de vida**

No deben elegir “ágil”, “cascada” o “híbrido” porque suene moderno.

Deben justificarlo:

* **Predictivo/cascada:** requerimientos estables, alta regulación, entregables claramente definidos.  
* **Iterativo o incremental:** se requieren entregas parciales y retroalimentación.  
* **Ágil:** alta incertidumbre y necesidad de revisar prioridades frecuentemente.  
* **Híbrido:** algunas etapas son previsibles y otras necesitan iteración.

### **Segundo: fases**

Ejemplo para una implementación de software:

1. Inicio.  
2. Relevamiento y análisis.  
3. Diseño.  
4. Adquisición o configuración.  
5. Desarrollo e integración.  
6. Pruebas.  
7. Capacitación y puesta en producción.  
8. Cierre.

### **Tercero: EDT**

Explicaría que una EDT no debería ser solamente una lista general como:

* analizar;  
* desarrollar;  
* probar;  
* implementar.

Debería descomponerse hasta un nivel que permita estimar responsable, duración, costo y entregable.

| ID | Paquete/actividad | Predecesora | Duración | Perfil | Entregable |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1.1 | Elaborar Acta del Proyecto | — | 2 días | PM | Acta aprobada |
| 1.2 | Relevar requerimientos | 1.1 | 5 días | Analista funcional | Documento de requerimientos |
| 1.3 | Validar requerimientos | 1.2 | 2 días | Analista \+ usuario clave | Requerimientos aprobados |
| 2.1 | Configurar plataforma | 1.3 | 7 días | Especialista técnico | Entorno configurado |
| 2.2 | Integrar con sistemas | 2.1 | 10 días | Desarrollador | Integración funcional |
| 3.1 | Ejecutar pruebas | 2.2 | 5 días | Tester | Informe de pruebas |
| 3.2 | Capacitar usuarios | 3.1 | 3 días | Capacitador | Usuarios capacitados |
| 3.3 | Salida a producción | 3.2 | 1 día | Equipo técnico | Sistema operativo |

### **Idea fundamental**

> La EDT es la fuente principal del resto de la planificación.

## **Bloque 6 — Del EDT al diagrama de Red y al Gantt**

Mostraría este flujo:

> Actividades \+ predecesoras \+ duraciones → Diagrama de Red → camino crítico → fechas → Gantt → asignación de recursos → aplanamiento.

La explicación práctica:

* El **diagrama de Red** muestra dependencias y permite determinar el camino crítico.  
* El **Gantt** ubica las actividades en el tiempo.  
* La asignación de recursos permite detectar sobrecarga.  
* El **aplanamiento** modifica fechas o asignaciones para evitar que un mismo recurso esté realizando tareas incompatibles simultáneamente.

### **Lo que deberían informar**

* fecha o período estimado de inicio;  
* duración total;  
* camino crítico;  
* actividades con holgura;  
* cantidad de personas por perfil;  
* conflictos de recursos detectados;  
* ajustes realizados al cronograma.

## **Bloque 7 — Recursos Humanos**

Los perfiles deben surgir de la solución y de la EDT. No deberían crear una lista extensa de puestos porque “podrían participar”.

Para cada perfil:

| Perfil | Responsabilidades | Competencias | Cantidad | Dedicación |
| ----- | ----- | ----- | ----- | ----- |
| Project Manager | Coordinar alcance, tiempo, costo y comunicación | Liderazgo, planificación, negociación | 1 | Parcial durante todo el proyecto |
| Analista funcional | Relevar y validar requerimientos | Análisis de procesos, documentación | 1 | Inicio y validaciones |
| Especialista técnico | Configurar o desarrollar la solución | Tecnología elegida e integraciones | 1–2 | Desarrollo |
| Tester | Diseñar y ejecutar pruebas | Testing funcional y no funcional | 1 | Etapa de pruebas |
| Capacitador | Preparar materiales y capacitar | Comunicación y conocimiento funcional | 1 | Implementación |

Podés remarcar:

> “Perfil requerido” no significa necesariamente una persona exclusiva. Una persona puede cubrir más de un rol, pero deben justificarlo y reflejar su disponibilidad en el Gantt.

## **Bloque 8 — Higiene y Seguridad Laboral**

La consigna pide un **layout real de los sectores afectados** y medidas preventivas para las personas de esos sectores.

No alcanza con listar:

* silla ergonómica;  
* pausas activas;  
* matafuegos.

Deben relacionar:

> sector → personas → riesgo → medida preventiva → representación en el layout.

### **Para proyectos administrativos o digitales**

* puestos y distancias;  
* circulación;  
* iluminación;  
* ubicación de pantallas;  
* cableado;  
* salidas de emergencia;  
* ventilación;  
* ruido;  
* ergonomía;  
* fatiga visual;  
* pausas;  
* riesgos psicosociales.

En trabajos anteriores aparecen, por ejemplo, mobiliario ergonómico, pantallas a la altura de los ojos, iluminación y pausas activas, que pueden servir como referencia para proyectos de oficina.

### **Para proyectos industriales, logísticos o de campo**

* circulación de peatones y vehículos;  
* señalización;  
* trabajos eléctricos;  
* altura;  
* instalación de sensores;  
* zonas restringidas;  
* EPP;  
* bloqueo de energía;  
* emergencias y evacuación.

### **Actividad rápida**

Cada grupo completa:

| Sector | Riesgo | Personas expuestas | Medida |
| ----- | ----- | ----- | ----- |
| Oficina de soporte | Fatiga visual y mala postura | Operadores | Monitor regulable, silla ergonómica y pausas |
| Sala técnica | Riesgo eléctrico | Infraestructura | Acceso restringido, señalización y procedimiento seguro |
| Zona operativa | Circulación de vehículos | Técnicos | Senderos, chaleco y coordinación con operaciones |

## **Bloque 9 — Adquisiciones, RFI y RFP**

La consigna requiere identificar activos, especificaciones y modalidad de adquisición.

### **Tabla esperada**

| Activo o servicio | Cantidad | Características mínimas | Forma de adquisición | Justificación |
| ----- | ----- | ----- | ----- | ----- |
| Licencias de plataforma | 50 | SSO, auditoría, SLA, integración API | SaaS anual | Reduce tiempo de implementación |
| Servicio cloud | Según consumo | Escalabilidad, backup, región y cifrado | Pago por uso | Demanda variable |
| Dispositivos de prueba | 3 | Diferentes sistemas y capacidades | Compra | Necesarios para validación |
| Consultoría especializada | 120 horas | Experiencia comprobable | Outsourcing | Competencia no disponible internamente |

### **RFI**

Se utiliza cuando todavía necesitan explorar:

* qué ofrece el mercado;  
* tecnologías disponibles;  
* proveedores;  
* rangos de precio;  
* capacidades generales.

### **RFP**

Se utiliza cuando los requerimientos están definidos y se desea recibir una propuesta:

* técnica;  
* económica;  
* cronograma;  
* equipo;  
* SLA;  
* condiciones contractuales.

No deberían limitarse a definir las siglas: deben explicar **en qué adquisición concreta de su proyecto utilizarían cada documento**.

## **Bloque 10 — Costos y factibilidad**

### **Variables de costos**

Como mínimo:

* horas por perfil;  
* valor hora;  
* licencias;  
* hardware;  
* servicios cloud;  
* proveedores;  
* capacitación;  
* implementación;  
* mantenimiento inicial;  
* viáticos;  
* costos indirectos;  
* reserva de contingencia.

### **Fórmula sencilla**

> Costo RRHH \= cantidad de horas × valor hora por perfil.

> Costo total \= RRHH \+ adquisiciones \+ servicios \+ indirectos \+ contingencia.

### **Factibilidad técnica**

Deben evaluar:

* disponibilidad de tecnología;  
* compatibilidad;  
* infraestructura existente;  
* conocimientos del equipo;  
* capacidad;  
* seguridad;  
* integración;  
* soporte;  
* riesgos técnicos.

### **Factibilidad económica**

Deben comparar:

* inversión inicial;  
* costos operativos;  
* costos evitados;  
* ahorros;  
* mejoras de productividad;  
* beneficios cuantificables;  
* plazo de recuperación, cuando sea posible.

No deberían escribir únicamente:

> “Es económicamente factible porque traerá beneficios.”

Tendrían que mostrar, aunque sea con estimaciones:

> El proyecto cuesta X; reduce Y horas mensuales; el valor de esas horas es Z; además evita determinados costos o pérdidas.

> 

