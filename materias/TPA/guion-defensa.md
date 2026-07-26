# TPA — Guion de defensa oral

> Presentación ~8 min, lenguaje simple. La idea es **contar todo el sistema
> nosotros** para dejar poco que preguntar. La técnica fina (números, IMC,
> anti-windup, etc.) NO va en el speech: queda en la cabeza y en
> [`banco-preguntas.md`](banco-preguntas.md) para cuando pregunten.

## Reglas de entrega
- **No lo reciten de memoria.** Practíquenlo hasta que sea suyo y suene natural.
- Hablen **seguros y despacio**. Mejor pausar que ametrallar.
- Van a interrumpir con preguntas igual — está bien. Respondés, y retomás.
- Donde dice **[mostrar]**, va el dashboard en vivo o el video.

---

## Apertura

Buenas. Nuestro trabajo es un sistema que **controla la iluminación de un LED** y
que se puede **supervisar y manejar por internet**, desde un dashboard web. En una
frase: metimos un LED y un sensor de luz en una caja cerrada, y el sistema
**mantiene solo el nivel de luz que le pedimos**, corrigiéndose todo el tiempo. Y
todo eso se ve y se ajusta de forma remota desde la nube. Lo armamos en **cuatro
etapas**.

## Etapa 1 — La planta y su modelo

Lo que se controla es un **LED** (actuador) y un **LDR**, una fotorresistencia
(sensor), enfrentados dentro de una caja de cartón cerrada que aísla la luz de
afuera —así el sensor solo mide la luz del LED—. Antes de controlar, hay que
entender cómo se comporta: le dimos un **salto de potencia** al LED y medimos cómo
reaccionaba el sensor. De ahí sacamos dos números que describen la planta:
**cuánto** cambia la luz por cada empujón, y **qué tan rápido** reacciona. Ese
modelo no es perfecto —el sensor es no lineal—, pero nos daba un **punto de
partida** para diseñar el control. Y para eso sirvió.

## Etapa 2 — El controlador

El cerebro es un **PID**: mira el **error** —la diferencia entre la luz que querés y
la que hay— y decide cuánto corregir. Lo corre el Arduino, cientos de veces por
segundo. Lo interesante fue comparar dos versiones: una con solo la parte
**proporcional**, que reacciona al error del momento y siempre deja un error
residual; y otra que le suma la parte **integral**, que acumula el error hasta
eliminarlo. Y ahí está el resultado más claro del trabajo: al sumar la integral,
**el error final cayó más de un 90%** — el sistema pasó de quedarse corto a clavar
el valor pedido. Un punto honesto que sabemos explicar: los números reales no
dieron idénticos a la simulación, porque el sensor no es lineal — pero el sistema
quedó **estable y cumpliendo**, que es lo que importa. Con eso el control andaba,
pero solo local.

## Etapa 3 — Integración con la nube

La siguiente etapa fue **llevarlo a internet**, con una regla: **no tocar el
control**. El Arduino sigue haciendo lo suyo, intacto. Para eso sumamos una segunda
placa, un **NodeMCU**, que tiene WiFi y hace de **puente** entre el Arduino e
internet. Que sea una placa aparte es a propósito: el control tiene que ser
rapidísimo, e internet es lento e impredecible; si los mezcláramos, la red
arruinaría el control. Por eso **el control va pegado a la planta, y la nube es solo
para mirar y ajustar**. El NodeMCU habla con una plataforma en la nube,
**ThingsBoard**, usando un protocolo típico de IoT, **MQTT**. Por ahí **suben** los
datos en tiempo real y **bajan** los comandos del dashboard. Probamos los dos
sentidos y funcionan.

## Etapa 4 — El dashboard

La última etapa fue el **dashboard**, la cara web del sistema. Tiene dos partes:
**supervisión** —gráficos en vivo de la luz medida contra la pedida, la señal de
control, y un indicador de si el equipo está conectado— y **control** remoto
—cambiar el valor deseado, ajustar el controlador, y pasar de automático a manual—.
**[mostrar dashboard en vivo o el video]**

## Cierre

Y para cerrar, lo que más nos gustó: para agregar **toda** esta interfaz web de
supervisión y control, **no tuvimos que cambiar ni una línea** del programa del
Arduino ni del NodeMCU; el dashboard reusa exactamente los comandos que ya
teníamos. Eso es la prueba de que la decisión de diseño central —**separar el
control, la comunicación y la visualización en capas independientes**— fue la
correcta. El sistema cubre el ciclo completo: identificar la planta, diseñar el
control, integrarlo con la nube y operarlo por web. Y funciona de punta a punta.
Gracias.

---

## Si te interrumpen con una pregunta
Respondé corto y volvé al hilo. Para las preguntas difíciles (de dónde salen los
números, anti-windup, por qué esos topics, etc.) está todo en
[`banco-preguntas.md`](banco-preguntas.md). Las tres joyas si aprietan con el
control: el PI baja el error >90%, el modelo es un punto de partida (planta no
lineal), y la separación en capas es la decisión que valida todo.
