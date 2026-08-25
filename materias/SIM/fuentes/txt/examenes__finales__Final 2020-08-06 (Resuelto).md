**Examen Final 06/08/2020 - Modalidad Virtual.**

La modalidad fue remota por lo cual el examen fue totalmente oral donde iban tomando uno a uno de forma individual donde los demás que rendían esperaban en la sala. Particularmente a mi (desconozco si fue lo mismo para los demás) me pidieron que desarrolle los siguientes 3 temas

1- Inventario

2- Pasos para realizar una simulación

3- Modelo de Cola MM1.

Donde a medida que iba explicando te iban haciendo preguntas, Leale me pregunto cosas de inventario como por ejemplo que variable introduciría para ser medida.

En el punto 2 luego de comentar el nombre de cada paso, Jorge me pregunto sobre los tipos de escenarios que hay (Pesimista, optimista intermedio), y por último en el punto 3, Juan me pregunto qué relación tenía con el Modelo Analítico.

Hubo algunas preguntas puntuales más al respecto de los temas, pero no recuerdo bien.

**Resolución**

La modalidad fue remota por lo cual el examen fue totalmente oral donde iban tomando uno a uno de forma individual donde los demás que rendían esperaban en la sala. Particularmente a mí (desconozco si fue lo mismo para los demás) me pidieron que desarrolle los siguientes 3 temas:

1. **Inventario**

**Componentes**

* Tiempo entre demandas
* Tamaño de demanda
* Costo del pedido: K+i.Z ; siendo K el costo base, i el costo incremental y Z la cantidad.
* Retardo de envío.
* Política estacionaria (Punto de pedido, Tope) (s,S): define Z.Si I < s, Z=S-I, si I >=s, Z=0.
* I(t) Nivel de inventario
* I+(t) Ítems en posesión en inventario MAX(I(t), 0)
* I-(t) Nivel ítems faltantes en inventario MAX(-I(t), 0)
* h Costo de mantenimiento
* Ī+ Items promedio para el n-ésimo periodo de tiempo
* Ī+.h Promedio de costo de mantenimiento por unidad de tiempo
* π Costo faltante ítems por unidad de tiempo
* Ī- Ítems faltantes promedio para el n-ésimo periodo de tiempo
* Ī-.π Promedio de costos faltantes por unidad de tiempo

**Rutinas**

*Evento Arribo de orden*

Incrementar nivel de inventario a la cantidad previamente ordenada

Eliminar el evento arribo de consideración

Volver

*Evento Demanda*

Generar tamaño de demanda

Disminuir el inventario por tamaño de demanda

Definir el siguiente evento demanda

Volver

*Evento Evaluación de Inventario*

I<s?

Si lo es

Determinar la cantidad a ordenar

Calcular costo pedido y acumular

Determinar tiempo de arribo de orden

Determinar próxima evaluación de inventario

Volver

**Modelo de desencadenamiento de eventos**

Se hace antes de la simulación, ver el sistema con un alto nivel de abstracción.

⇒ Control inventario (Auto ref) ⇒ Arribo pedido

⇒ Demanda (Auto ref)

**Medidas de desempeño**

CCP=ACP/reloj; Costo Cantidad Pedida

ACP Acumulado Cantidad Pedida

CUI=AIP.h Costo Unidades en Inventario

AIP Acumulado Inventario Positivo

CUP=AIN.π/reloj Costo unidades perdidas

AIN Acumulado Inventario Negativo

CMP = CCP+CUI+CUP Costo Mensual Promedio

1. **Pasos para realizar una simulación**

**Definición del sistema bajo estudio**, Conocer el sistema a modelar. Saber que origina el estudio de la simulación y los supuestos del modelo. Contar con información suficiente como para establecer un modelo conceptual.

**Generación del sistema de simulación base**, Generación de un modelo de simulación base. No demasiado detallado.

**Recolección y análisis de los datos**, Recopilación de la información estadística de las variables. Determinar qué información es útil para determinar distribuciones. De no contar con información necesaria se realiza un estudio estadístico del comportamiento de las variables.

**Generación del modelo preliminar**, Integra el análisis de los datos, los supuestos del modelo y todos los datos necesarios para hacer un modelo lo más cercano a la realidad.

**Verificación del modelo**, Verificación de datos para comprobar la programación del modelo y que los parámetros usados funcionen correctamente.

**Validación del modelo**, Se le realizan una serie de pruebas al mismo, utilizando información de una entrada real para observar su comportamiento y analizar sus resultados.

**Generación del modelo final**, Una vez que el modelo se ha validado, está listo para realizar la simulación y estudiar el comportamiento del proceso. Modelo Raíz.

**Determinación de los escenarios para el análisis**, Se acuerda con el cliente los escenarios que desea analizar. Se suele utilizar un escenario pesimista, optimista, e intermedio.

**Análisis de sensibilidad**, Una vez obtenidos los resultados se realizan pruebas estadísticas que permitan comparar los escenarios con los mejores resultados finales

**Documentación del modelo, sugerencias y conclusiones**, Se efectúa la documentación del modelo. Permitirá el uso del modelo generado en caso que se requieran ajustes futuros. Se deben incluir los supuestos, las distribuciones asociadas a las variables, los alcances y limitaciones, junto con las consideraciones de programación. Sugerencias para el uso del modelo como para el uso de los resultados. Y por último conclusiones del modelo.

1. **Modelo de Cola M/M/1.**

Consta de lo siguiente:

1- Una población de clientes infinita

2- Un proceso de llegada en el que los clientes se presentan de acuerdo a un proceso de Poisson con una tasa promedio de λ clientes por unidad de tiempo.

3- Un proceso de colas con una sola línea de espera, con una disciplina FIFO.

4- Un proceso de servicio de un solo servidor en el que se atiende a los clientes de acuerdo con una distribución exponencial con un promedio de 𝝁 clientes por unidad de tiempo.

**Cálculo de las medidas de rendimiento**

Intensidad de tráfico ρ=λ/𝝁, mientras más cerca esté de 1 más cargado estará el sistema.

Probabilidad que no haya clientes en el sistema P0 =1-ρ

Número promedio en la fila Lq=ρ2/(1-ρ)

Tiempo promedio de espera en la cola Wq=Lq/λ

Tiempo promedio de espera en el sistema W=Wq+1/𝝁

Número promedio en el sistema L=λ\*W

Probabilidad de que un cliente que llegue tenga que esperar pw= 1-P0=ρ

Probabilidad de que hay n clientes en el sistema Pn=ρn\*P0

Utilización U=ρ

Nos interesa desarrollar un modelo para predecir(Analíticamente):

1. (tamaño promedio de la cola) La probabilidad de varios números de clientes en la cola (Número promedio esperado en cola)
2. El tiempo esperado o promedio que pasará un cliente en las “instalaciones” del servicio.
3. La probabilidad que las instalaciones del servicio estén ociosas (también llamado factor de utilización)

Donde a medida que iba explicando te iban haciendo preguntas, Leale me pregunto cosas de inventario como por ejemplo qué variable introduciría para ser medida.

punto 3, Juan me preguntó qué relación tenía con el Modelo Analítico.