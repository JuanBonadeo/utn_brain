# 🎓 Resumen de Clase

## 📝 Idea Principal (TL;DR)
La sesión se centró en la profundización de la notación **BPMN (Business Process Model and Notation)**, explicando la simbología avanzada para el modelado de procesos de negocio, el concepto de *tokens* para simulación y el uso técnico de la herramienta **Bizagi Modeler** para la creación de diagramas profesionales.

## 🔑 Conceptos Clave
*   **Simbología BPMN Avanzada**: 
    *   **Eventos**: Se diferencian eventos de inicio (círculo simple), intermedios (círculos concéntricos) y de fin (línea gruesa). A diferencia de los diagramas de actividad, BPMN permite múltiples eventos de fin.
    *   **Gateways (Comuertas)**:
        *   *Exclusiva (X)*: El flujo sigue solo una rama.
        *   *Inclusiva (O)*: Pueden activarse una o varias ramas simultáneamente.
        *   *Paralela (+)*: Abre flujos simultáneos que **deben** converger obligatoriamente en otra compuerta paralela de cierre.
        *   *Basada en Eventos*: El proceso se detiene hasta que ocurre un evento externo (ej. recepción de un mensaje o cumplimiento de un temporizador).
    *   **Pools y Lanes**: El *Pool* representa a la organización completa (Business to Business), mientras que los *Lanes* (carriles) identifican a los actores o departamentos internos.
*   **Concepto de Token**: Se utiliza para explicar la lógica de ejecución. Un *token* es una ficha teórica que recorre el diagrama; permite monitorear instancias del proceso, realizar simulaciones y entender cómo se comportan las bifurcaciones y uniones.
*   **Tratamiento de Excepciones**: Uso de **eventos adjuntos** (boundary events) sobre tareas o subprocesos para manejar errores, escalamientos (elevar a un superior) o cancelaciones sin interrumpir el flujo principal si no es necesario.
*   **Modificadores de Tareas**: 
    *   *Tarea de Usuario*: Interacción humano-sistema.
    *   *Tarea Manual*: Acción física sin sistema (ej. entregar un paquete).
    *   *Tarea de Servicio*: Invocación automática de un Web Service o API.
    *   *Script*: Ejecución de código automático dentro del motor de BPM.

## 🚨 Avisos Importantes y Fechas
*   📅 **Entrega de Actividad**: Se solicitó pasar los ejemplos vistos en la presentación a la herramienta **Bizagi**. La entrega debe realizarse exclusivamente en formato **PDF** (exportado desde el modelador).
*   ⚠️ **Fecha Límite**: El profesor indicó que la tarea en el campus permanecerá abierta **hasta la noche** del día de la fecha.
*   ⚠️ **Nota Técnica**: Se recomienda el uso de **Bizagi Modeler versión 2.6** o superior, prestando especial atención a que los conectores (líneas de flujo) queden correctamente ligados a los objetos para que el diagrama sea válido.

## ✅ Tareas / Próximos Pasos (To-Do)
*   [ ] **Modelado en Bizagi**: Replicar el diagrama de "Reserva de Turismo" y "Gestión de Compras/Incidentes" explicados en clase.
*   [ ] **Exportación**: Generar el archivo PDF del diagrama asegurándose de que la vista preliminar encaje en las páginas correctamente.
*   [ ] **Carga en el Campus**: Subir el entregable antes del cierre del plazo (esta noche).
*   [ ] **Repaso Teórico**: Diferenciar claramente entre el uso de *subprocesos embebidos* y *subprocesos reutilizables* (marcados con el signo +).