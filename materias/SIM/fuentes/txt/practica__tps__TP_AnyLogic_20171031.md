**SIMULACION DEL SISTEMA DE PEAJE DEL PUENTE ROSARIO - VICTORIA CON SOFTWARE ANYLOGIC**

Joel Arnold, Alexis Castaño, Damián Ciancio, Luciano Guadagnoli, Rodrigo Ponce

UTN Facultad Regional Rosario - Zeballos 1341, Rosario, Santa Fe, Argentina - 31/10/2017

![](data:image/jpeg;base64...)

|  |  |
| --- | --- |
| **DESCRIPCION, SUPUESTOS Y ALCANCE**  El Peaje del puente Rosario - Victoria posee cuatro cabinas de atención manual, dos que atienden a los vehículos que van en dirección hacia Victoria y dos a los que se dirigen en sentido contrario.  Para el presente estudio se considera el sentido del tránsito en una sola dirección (de Rosario a Victoria).  Los tiempos entre llegadas de los vehículos y los tiempos de servicio de las cabinas de peaje son aleatorios.  Se considerará una tasa de arribo única que corresponde al horario de 7.00 a 8.00 horas, de lunes a jueves.  Los tiempos entre arribos de los vehículos que llegan a las cabinas de peaje siguen una distribución exponencial con una tasa media de 24 segundos.  La cola sigue una disciplina de atención FIFO. | Cada vehículo que llega al peaje se ubica en el carril más corto y no puede cambiarse.  El tiempo medio de servicio es de 12 segundos por vehículo, siendo este exponencial.  El tiempo de servicio contempla el período que transcurre desde que el empleado de la cabina de peaje abre la ventanilla hasta que levanta la barrera.  **OBJETIVO**  Para el sistema bajo estudio comparar y determinar la mejor opción de cantidad de cabinas de peaje a habilitar para procurar que la demora promedio de cada vehículo en el sistema no supere los 30 segundos.  **OPCION A)** Habilitar solo una de las cabinas de peaje.  **OPCION B)** Habilitar las dos cabinas de peaje disponibles. |

![](data:image/png;base64...)

**Fig. 1.** Desarrollo del modelo de simulación utilizando la herramienta AnyLogic 8 Personal Learning Edition 8.1.0

![](data:image/png;base64...)

**Fig. 2.** Ejecución e inicio de una corrida de la simulación con el sistema en estado de ocio

![](data:image/png;base64...)

**Fig. 3.** Análisis y observación de las variables para la opción B

![](data:image/png;base64...)

![](data:image/png;base64...)**Fig. 4.** Fin de la corrida con las *dos cabinas de peaje disponibles habilitadas*

**Fig. 5.** Fin de la corrida con *solo una de las cabinas habilitada*

![](data:image/png;base64...)

|  |  |
| --- | --- |
| ![](data:image/png;base64...)  **Fig. 6.** Medidas de rendimiento para la opción A  **CONCLUSIONES**  Después de correr nuestro programa observamos como fluctúan las variables de interés en función del tiempo y analizamos los resultados.  Para la opción B el porcentaje de utilización de la primer cabina fue del 56% mientras que la segunda se utilizó solo en un 16%, es decir, ambas se vieron ociosas gran parte del tiempo. | Para la opción A) el factor de utilización aumentó (73%) aunque no llegó a saturar la capacidad de atención de la cabina.  Los tiempos de espera de los vehículos en el sistema tampoco registran una variabilidad significativa (12.7 segundos con las dos cabinas habilitadas y 14.7 segundos con una sola).  Al comparar los resultados finales obtenidos no se visualiza una clara diferencia entre las opciones evaluadas.  Confirmamos que **al ser pequeña la tasa promedio de llegadas respecto a la tasa media de servicio, un incremento en la capacidad de servicio (en este caso otra cabida de peaje habilitada) dará solo una ligera disminución del tiempo esperado en el sistema**, es decir, no se justifica habilitar una cabina adicional.  Por todo lo expuesto concluimos que la alternativa más adecuada es la opción A.  **FUENTES**  Información sobre estadísticas de tránsito y servicio ofrecidas por:   * Caminos del Río Uruguay S.A. - Estación "Isla La Deseada" - Ruta Nac. 174 km 5,2 (<https://www.crusa.com.ar>) * OCCOVI - Órgano de Control de Concesiones Viales - Dirección Nacional de Vialidad (<https://argentina.gob.ar/occovi>) * Instituto Nacional de Estadísticas y Censos ([www.indec.gov.ar](http://www.indec.gov.ar)) |

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

![](data:image/x-emf;base64...)

![](data:image/png;base64...)![](data:image/png;base64...)