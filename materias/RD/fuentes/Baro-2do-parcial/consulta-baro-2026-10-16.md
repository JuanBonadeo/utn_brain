# Clase de consulta de Baró — 2do parcial práctico (2026-10-16)

> Resumen y transcripción automáticos de la grabación (Notion), tal como los pasó Juan. La transcripción tiene errores de reconocimiento de voz: "RRP" probablemente es ARP, "GFP/BGPP/GPP" es BGP, "OSFF/SPF" es OSPF, "RIRIP/RIP-RIP" es RIP, "K3" es capa 3.

## Summary

### Ítems de Acción

- [ ]  Leer en el libro los temas de ruteo y protocolos de enrutamiento (RIP, OSPF, BGP) para preparar el parcial
- [ ]  Revisar los conceptos de DHCP, ICMP y RRP, enfocándose en la finalidad de cada protocolo, no en el formato de sus campos
- [ ]  Practicar ejercicios de cálculo de subredes (redes, hosts, direcciones) para el parcial

### Formato del Parcial

- Se tomarán **2 o 3 ejercicios prácticos** de cálculo de IP: dado un bloque, calcular cantidad de subredes, hosts y direcciones
- Se tomarán **hasta 3 preguntas conceptuales** de teoría
- Se recomienda leer el libro y hacer zoom en los temas puntuales para responder las preguntas conceptuales

### Type of Service y Calidad de Servicio (QoS)

- El campo *Type of Service* del encabezado IP define prioridades del tráfico con una escala original de 0 a 7
- En la práctica, los proveedores aplican **3 o 5 niveles de prioridad**: sin prioridad, media y alta
    - **Prioridad alta**: video y audio en tiempo real, tráfico de control
    - **Prioridad media/baja**: correo electrónico, navegación web, servicios sin interacción en tiempo real
- Ejemplo real: durante la pandemia, la saturación de internet evidenció los límites de la QoS; la plataforma virtual de la URR pasó de ~400 conexiones diarias a conectar simultáneamente 4.000–5.000 usuarios, requiriendo esfuerzo de la universidad y los proveedores para sostener el servicio

### Sistemas Autónomos y Tipos de Ruteo

- Un **sistema autónomo** es generalmente un proveedor de internet, con políticas de ruteo propias e independientes
- **Ruteo interno** (dentro de un sistema autónomo): el proveedor elige libremente el protocolo (RIP, OSPF, etc.)
- **Ruteo externo** (entre sistemas autónomos): se utiliza exclusivamente el protocolo **BGP versión 4**
- Diferencia entre **switch capa 3** y **router**: ambos pueden rutear internamente, pero solo el router soporta BGP para interconectar sistemas autónomos

### Protocolos de Ruteo Internos

- **RIP** (Vector Distancia): protocolo original de internet, sencillo, dinámico, pero maneja poca información y es menos eficiente
- **OSPF** (Estado de Enlace): protocolo estándar abierto, maneja ancho de banda, retardo, pérdida de paquetes, distancia y costo; es más eficiente para elegir la mejor ruta
- **BGP** (Vector Distancia): protocolo de borde externo, estándar para comunicación entre sistemas autónomos
- Distinción conceptual: *protocolo* es un software estandarizado; *algoritmo* es el método de cálculo que el protocolo utiliza internamente — se usan como sinónimos en la bibliografía aunque no son exactamente lo mismo

### Tablas de Ruteo

- Los routers utilizan **tablas de ruteo** para saber qué redes son alcanzables y por qué interfaz enviar cada paquete
- La tabla puede ser cargada manualmente (rutas estáticas) o construida automáticamente por un protocolo dinámico
- En redes simples (como un router doméstico con dos interfaces) no es necesario un protocolo dinámico; en redes complejas con múltiples interfaces, sí

### Ruta por Defecto (Default Route)

- Es una interfaz asignada por la que el router envía los paquetes cuyo destino **no está en su tabla de ruteo**
- Se representa en la tabla con la dirección `0.0.0.0` como red destino
- El paquete sigue saltando de router en router por sus respectivas rutas default hasta que algún router reconozca el destino y lo encauce correctamente
- Diferencia con switch: el switch difunde por todos los puertos cuando no conoce el destino; el router usa la puerta default sin difundir

### Problema de Conteo al Infinito (Vector Distancia)

- En protocolos de vector distancia (como RIP), cada router solo conoce una parte de la información de la red
- Cuando una red de destino cae, el router vecino al destino lo detecta primero, pero sus vecinos más lejanos aún creen tener una ruta válida y siguen enviando paquetes erróneamente
- Esto genera un **bucle de información falsa** que tarda mucho tiempo en resolverse ("converger") — de ahí el nombre "conteo al infinito"
- Los protocolos de **estado de enlace** (OSPF) resuelven esto porque cada router tiene una visión completa de la topología y detecta caídas de forma inmediata

### ICMP

- Protocolo que opera en capa de red (capa 3) e informa cuando un paquete no llega a destino
- Solo se requiere conocer su finalidad, no el formato de sus campos

## Transcript (fragmentos relevantes; se corrigieron los errores obvios del reconocimiento de voz, el resto se omitió por ser charla o ruido)

> En realidad el protocolo cuando lo crearon, hicieron una escala de 1 a 7, digamos, por no decir 0-7, pero no se utilizó al principio porque no había servicios que discriminar. [...] Si vos tenés que contestar una pregunta de un parcial, contestala de acuerdo a lo que dice el libro, que es un cálculo de 0 a 7 que da la prioridad del paquete o la prioridad del tráfico, porque vos no mandás un paquete, mandás un flujo de datos que tienen que ver con una aplicación.

> La escala de prioridades sería sin prioridad, prioridad media y prioridad alta. Prioridad alta sería lo que es video y audio en tiempo real. Y tráfico de control, cuando el tráfico de control te está avisando que hay un problema tienen que llegar rápido. Todo lo demás, correo electrónico, navegación, todo lo que no requiere interacción en tiempo real, es de media o baja prioridad. Algunos proveedores tienen servicios que tienen 5 tipos de prioridad.

> ¿Cuántas preguntas van a hacer? — Dos o tres problemas de IP que tenemos en clase, y como máximo tres preguntas conceptuales. [...] Es como lo primero: de cuántas subredes, de cuántos hosts, de cuántas direcciones. Les doy la máscara y les digo cuántos hosts y que su red responda. Los primeros problemas que vimos. Esos problemas al final son de aplicación, pero no se los voy a dar. [...] Dos o tres ejercicios de práctica. Resolver. Y tres preguntas conceptuales de teoría.

> Fíjense, lean en el libro lo que dice ese tema y háganse un zoom puntual para contestar una pregunta de ese tipo.

> Los switches de capa 3 son switches que tienen funcionalidades de ruteo [...]. La diferencia entre un switch de capa 3 y un router es que los switches de capa 3 suelen no tener el protocolo de ruteo externo, el BGP; todo lo demás es igual a un router.

> El sistema autónomo es generalmente un proveedor de internet, se define como un área con políticas propias de ruteo. [...] Él elige qué protocolo usar, cómo usarlo. La administración técnica del ruteo es interna y es propia. Nadie le dice cómo tiene que ser. [...] Si un proveedor se conecta con otro proveedor [...] ahí va a tener que usar el protocolo BGP, que es el protocolo de enlace externo entre un sistema autónomo y el otro, y es el único protocolo que se utiliza, el estándar BGP versión 4.

> Los de vector distancia son los originales de Internet: funcionaron, funcionan bien, pero tienen limitaciones. [...] Dinámico significa que se va adaptando en función de todo lo que pasa en tiempo real. [...] El estado de enlace es mucho más rico en información de ruteo, y por eso es más eficiente. [...] Maneja simultáneamente ancho de banda, retardo, pérdida de paquetes, distancia entre origen y destino, y costo.

> Dentro de los sistemas autónomos se utiliza el RIP, se utiliza el OSPF, pero para rutear entre sistemas autónomos utilizamos el BGP. Es un protocolo de ruteo de borde o externo al sistema autónomo. [...] El BGP utiliza la filosofía de ruteo vector distancia; es un protocolo sencillo y utiliza vector distancia. Yo les pido que lean esos libros, que están bien explicados, con ejemplos.

> Los routers para rutear utilizan tablas [...]. Necesitan saber qué redes son alcanzables por ellos [...] y por qué puerto enviar los paquetes que van hacia ese destino. [...] ¿Quién arma la tabla? Puede ser el administrador, una persona que escriba la tabla de ruteo. O puede ser un software, un protocolo dinámico. Eso depende de dónde está el router. Si el router está en la casa de alguno de nosotros [...] tiene dos interfaces [...]. En cambio los routers dentro de una red compleja, por ejemplo de un proveedor, tienen múltiples interfaces y ahí sí se justifica usar un protocolo dinámico.

> El concepto de ruta default se refiere a que cada router del camino tiene una puertita por donde sacar los paquetes cuyas redes destino no conoce. [...] El router abre el paquete, mira la IP del destino y busca en su tabla. Si está, ya tiene asignada una interfaz de salida. [...] Si no, saca esos paquetes con destino desconocido por una interfaz asignada, y eso constituye la ruta default. [...] En la tabla del router, la ruta por defecto se especifica con cuatro ceros: 0.0.0.0. [...] El switch, cuando no conoce el destino, difunde por todos los puertos; el router no hace difusión, pero tiene una puerta asignada para que el paquete salga igual. [...] ¿Esa puertita es otro router? — Es una interface, una placa de red, el puerto de salida. [...] ¿Pueden quedar dando vueltas? — No, el paquete tiene tiempo de vida.

> Conteo al infinito: vector distancia [...] la única información que tiene es la cantidad de saltos. [...] Todos los routers que manejan ese protocolo tienen una parte de información. El router pegado al destino es el primero que se entera cuando la red destino no está más. [...] Le informa a su vecino y el vecino del otro lado le dice "yo sí llego", porque tiene una parte de información y no se enteró. Entonces el router confía en su vecino y le manda los paquetes pensando que hay otra ruta. Entran en un bucle de información falsa [...] hasta que todos se enteran de que se cayó el destino. Tardan mucho, pero convergen a la realidad. En cambio los routers con protocolos de estado de enlace como OSPF tienen en su tabla la información de toda la red, entonces se enteran enseguida si el destino se cayó. [...] Se llama conteo al infinito porque tarda; no infinitos pasos, pero tarda un montón en llegar a la conclusión de que esa red no existe.

> El RIP es un protocolo, el OSPF es un protocolo. A veces se dice protocolo y a veces algoritmo. El protocolo es algo estandarizado [...], un algoritmo es un cálculo. El protocolo utiliza algoritmos para elegir la mejor ruta. [...] Es como decir ancho de banda y velocidad: no es lo mismo pero se usa igual.

> ¿Nos podrías decir el DHCP, el ICMP y el ARP? — Yo no quiero que me digan el formato de cada protocolo, [...] simplemente la finalidad. [...] ICMP funciona en capa de red, y funciona cuando algo anda mal: cuando un paquete no llega, algo me va a decir que ese paquete no llegó.
