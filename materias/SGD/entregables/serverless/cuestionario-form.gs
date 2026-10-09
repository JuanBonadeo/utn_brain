/**
 * Cuestionario de la presentación de serverless (SGD) → Google Form en modo
 * cuestionario, con respuestas correctas, puntaje y devolución por pregunta.
 *
 * Uso: script.google.com → Nuevo proyecto → pegar este archivo → elegir
 * `crearCuestionario` → Ejecutar → autorizar. El log muestra el link para
 * editar y el link para compartir. El form queda en la raíz de tu Drive.
 *
 * Las preguntas son las mismas que `cuestionario.md`: si se cambia una, se
 * cambia en los dos lados.
 */

const TITULO = 'Serverless — cuestionario';
const DESCRIPCION =
  'Diez preguntas sobre la presentación que acabamos de dar. ' +
  'Opción múltiple y verdadero/falso, una sola respuesta correcta por pregunta.';

// correcta: índice (desde 0) de la opción correcta.
const PREGUNTAS = [
  {
    titulo: 'Serverless significa que la aplicación se ejecuta sin servidores.',
    opciones: ['Verdadero', 'Falso'],
    correcta: 1,
    devolucion:
      'Los servidores existen y alguien los mantiene: el proveedor. Lo que ' +
      'cambia es que no los administrás vos. Como wireless: los cables siguen estando.',
  },
  {
    titulo:
      'Según la definición de la CNCF que usamos, ¿cuál de estas NO es una ' +
      'propiedad de serverless?',
    opciones: [
      'No administrás infraestructura',
      'Escala hasta cero cuando no hay pedidos',
      'La función mantiene el estado en memoria entre pedidos',
      'Pagás por uso real, no por tener algo encendido',
    ],
    correcta: 2,
    devolucion:
      'Las tres propiedades son: no administrás infraestructura, escala hasta ' +
      'cero y pagás por uso. Mantener estado en memoria es justamente lo que no se puede.',
  },
  {
    titulo: '¿Cuál es la diferencia entre FaaS y BaaS?',
    opciones: [
      'FaaS es para el frontend y BaaS para el backend',
      'FaaS es tu código, que se dispara con eventos; BaaS son servicios ' +
        'gestionados que consumís por API (base, autenticación, almacenamiento)',
      'Son lo mismo con distinto nombre según el proveedor',
      'FaaS se cobra por hora y BaaS por milisegundo',
    ],
    correcta: 1,
    devolucion:
      'En una aplicación serverless real la mayor parte es BaaS, y tus ' +
      'funciones (FaaS) son el pegamento entre esos servicios.',
  },
  {
    titulo: '¿Qué es el cold start?',
    opciones: [
      'La demora extra de una invocación que tiene que preparar un entorno ' +
        'nuevo (fase INIT) porque no había uno disponible',
      'El tiempo que tarda en desplegarse una nueva versión del código',
      'Un error que ocurre cuando la función supera el tiempo máximo de ejecución',
      'El apagado del entorno después de varios minutos sin pedidos',
    ],
    correcta: 0,
    devolucion:
      'Es el precio de escalar a cero: si no hay nada corriendo, algo hay que ' +
      'arrancar. Depende mucho del lenguaje (Go/Rust < 100 ms, Java sin optimizar: segundos).',
  },
  {
    titulo:
      'Como el entorno se reutiliza entre invocaciones, una función puede ' +
      'guardar datos en memoria y confiar en que el siguiente pedido los va a encontrar.',
    opciones: ['Verdadero', 'Falso'],
    correcta: 1,
    devolucion:
      'Es stateless por contrato: no hay garantía de que dos pedidos caigan en ' +
      'el mismo entorno. El estado va a una base o a un caché externo.',
  },
  {
    titulo:
      '¿Cómo aísla AWS Lambda el código de distintos clientes que corre en la ' +
      'misma máquina física?',
    opciones: [
      'Con contenedores que comparten el kernel del host',
      'Con máquinas virtuales tradicionales completas',
      'Con isolates de V8, como Cloudflare Workers',
      'Con microVMs de Firecracker, que arrancan en ~125 ms con aislamiento por hardware',
    ],
    correcta: 3,
    devolucion:
      'Los contenedores solos comparten el kernel y las VMs tradicionales son ' +
      'lentas. Firecracker (Rust, open source) recorta todo lo que una función ' +
      'no necesita. Los isolates de V8 son el camino de Cloudflare, no de Lambda.',
  },
  {
    titulo: '¿Cómo factura AWS Lambda?',
    opciones: [
      'Una tarifa fija por hora por cada función desplegada',
      'Solo por la cantidad de datos transferidos',
      'Por cantidad de pedidos más la duración en GB-segundo (memoria × ' +
        'tiempo), medida al milisegundo',
      'Por la cantidad de líneas de código desplegadas',
    ],
    correcta: 2,
    devolucion:
      'USD 0,20 por millón de pedidos más la duración en GB-segundo. Hay capa ' +
      'gratuita mensual: 1 millón de pedidos y 400.000 GB-s.',
  },
  {
    titulo:
      'Comparando Lambda con un servidor equivalente encendido todo el tiempo, ' +
      '¿a partir de qué uso aproximado deja de convenir serverless?',
    opciones: [
      'Alrededor del 5 %',
      'Alrededor de un tercio (~34 %)',
      'Alrededor del 90 %',
      'Nunca: serverless siempre es más barato',
    ],
    correcta: 1,
    devolucion:
      'El servidor cuesta lo mismo ocupado o no; Lambda arranca en cero pero ' +
      'su vCPU-hora sale ~3 veces más cara. Se cruzan cerca de un tercio de ' +
      'uso. Es la analogía del auto propio contra el Uber.',
  },
  {
    titulo:
      '500 funciones corren a la vez y cada una abre su propia conexión a una ' +
      'base Postgres. ¿Qué pasa y cómo se resuelve?',
    opciones: [
      'Se agotan las conexiones de la base; se resuelve con un pooler (RDS ' +
        'Proxy, PgBouncer) o con bases que se consultan por HTTP',
      'No pasa nada: Postgres soporta miles de conexiones simultáneas',
      'Las funciones entran en cold start; se resuelve con Provisioned Concurrency',
      'La base pasa a modo serverless automáticamente',
    ],
    correcta: 0,
    devolucion:
      'Una base relacional soporta cientos de conexiones, no miles. El pooler ' +
      'reutiliza pocas conexiones para muchas funciones.',
  },
  {
    titulo:
      'Prime Video bajó un 90 % el costo de su sistema de monitoreo de calidad ' +
      'al sacarlo de serverless. ¿Cuál fue la causa principal?',
    opciones: [
      'Lambda tenía cold starts demasiado largos',
      'AWS subió el precio de Lambda en 2023',
      'Mover datos entre muchas funciones encadenadas costaba más que ' +
        'procesarlos; lo juntaron en un solo proceso',
      'Serverless no soporta procesamiento de video',
    ],
    correcta: 2,
    devolucion:
      'La lección no es que serverless sea malo: cuando comunicar cuesta más ' +
      'que computar, hay que juntar los componentes, no separarlos.',
  },
];

function crearCuestionario() {
  const form = FormApp.create(TITULO)
    .setDescription(DESCRIPCION)
    .setIsQuiz(true)
    .setShuffleQuestions(false)
    .setProgressBar(false);

  PREGUNTAS.forEach((p) => {
    const item = form.addMultipleChoiceItem();
    item
      .setTitle(p.titulo)
      .setChoices(p.opciones.map((texto, i) => item.createChoice(texto, i === p.correcta)))
      .setPoints(1)
      .setRequired(true)
      .setFeedbackForCorrect(FormApp.createFeedback().setText('Correcto. ' + p.devolucion).build())
      .setFeedbackForIncorrect(FormApp.createFeedback().setText(p.devolucion).build());
  });

  Logger.log('Editar:    ' + form.getEditUrl());
  Logger.log('Compartir: ' + form.getPublishedUrl());
}
