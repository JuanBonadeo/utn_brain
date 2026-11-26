UNIVERSIDAD TECNOLÓGICA NACIONAL![](data:image/png;base64...)

Facultad Regional Rosario

Ingeniería en Sistemas de Información

**Asignatura:** Comunicación de datos

**Profesores:** Germán Bernardo Baró y Cristian Medin

**Comisión:** 303

**Integrantes:**

* Juan Pedro Casañas (Legajo: 50373)
* Maria Sofia Ochoa (Legajo: 50452)
* Martin Quagliardi (Legajo: 51657)
* Mateo Regodesebes (Legajo: 51079)

**Trabajo Práctico:** Seguridad en la transmisión de datos: Encriptación de los metadatos – Certificación – etc.

**Año:** 2024

**Índice**

[**Introducción 2**](#_u1pdjxt4l6mb)

[**Desarrollo 3**](#_9rnsoh1svtwr)

[¿Qué es la criptografía? 3](#_rug808tt4dvr)

[Diferencias con el cifrado 3](#_p539h0a2bauv)

[Claves simétricas vs Claves asimétricas 3](#_ewuvis1q9pdg)

[Autenticación 5](#_vp7w1rqiku9j)

[Hashing y autenticación 6](#_coiqeh3m7fof)

[Ocultación, cifrado de información 8](#_q0goyhjqymc2)

[Algoritmos hash comunes 9](#_4sd152ui0zdv)

[Secure Hash Algorithm (SHA) 9](#_85qrvw71rl9s)

[Otras funciones hash 10](#_dtkvyna17b6k)

[Códigos de autenticación 10](#_91wmtkq33rmb)

[Hashing aplicados a derivación de Claves 11](#_izepdtc07q6d)

[Ejemplos de hashing en la actualidad 11](#_y5qgsj91ldyc)

[Infraestructura de clave pública 14](#_76anw5qd53ko)

[Certificados digitales, relación de confianza y autoridades de certificación 15](#_vrg690vqquwb)

[Componentes de una PKI 18](#_eat1kwuu1ypp)

[El documento de prácticas de certificación 18](#_37wvzfbhj6pz)

[La Autoridad de Certificación 19](#_3d5j91wpt58m)

[La Autoridad de Registro 20](#_xrfu7luejo15)

[El Directorio 21](#_cz4zcgn8v8bd)

[Protocolos de seguridad en la transmisión de datos 21](#_nf79nh66g8zd)

[SSL/TLS 22](#_wcn26fw5bmbj)

[SSL 22](#_5i9ecs66nsao)

[TLS 22](#_16dediox66m3)

[¿Cuál es la diferencia entre TLS y SSL? 23](#_q4uecmeaw1ib)

[¿Cómo funciona TLS? 24](#_ls2126midf8f)

[Paso a paso del handshake 24](#_34nsyq9c3q9l)

[**Seguridad en redes VPN 25**](#_q9qtyyiu7hwa)

[Funcionamiento de una VPN 27](#_bhffohp5z8j2)

[Seguridad en las VPN 28](#_679s3o1yv5rp)

[Necesidades de las VPN 29](#_5gw10kass6ri)

[Protocolos de seguridad para IoT 30](#_1iraqtl0f0k8)

[Protocolos que implementan seguridad para IoT 30](#_hk3lx5etb5q5)

[Desafíos en la seguridad 32](#_qe8tahsclmx6)

[Vulnerabilidades en SSL/TLS 32](#_yyqsfdu7dqu6)

[Ataque Man in the middle (MitM) 33](#_4yf6vqvlal5d)

[**Conclusiones 35**](#_nhpslxn7r6cp)

[**Bibliografía 37**](#_6fzzz58ajrd6)

[**Anexo: Autoevaluación con Preguntas y Respuestas 38**](#_pfedr5ofnfgc)

# Introducción

En la era digital actual, la seguridad en la transmisión de datos es esencial para garantizar la integridad, confidencialidad y disponibilidad de la información. Los datos, desde transacciones bancarias hasta comunicaciones personales, fluyen constantemente a través de redes que pueden ser objeto de ataques.

La idea principal de la seguridad en estos casos es proteger el contenido de los datos, que muchas veces es sensible. Sin embargo, también es importante tener en cuenta la protección de los metadatos, que con frecuencia son igual de valiosos para los atacantes. Para resolver estos problemas, se utilizan una variedad de métodos de criptografía y certificación que mejoran la seguridad durante el intercambio de datos.

El concepto de seguridad en la transmisión de datos se remonta mucho antes del auge de la informática. La necesidad de proteger información sensible ha existido en distintas formas, desde los mensajes cifrados en las antiguas civilizaciones hasta los códigos secretos en tiempos de guerra. Un ejemplo histórico clave es el Código Enigma, utilizado por las fuerzas alemanas durante la Segunda Guerra Mundial para encriptar sus comunicaciones militares. Este código fue considerado prácticamente indescifrable hasta que el matemático británico Alan Turing y su equipo en Bletchley Park lograron romperlo mediante el desarrollo de una máquina electromecánica llamada "Bombe". Este avance no solo fue crucial para la victoria aliada, sino que también sentó las bases de la ciencia de la criptografía moderna y del desarrollo de las computadoras, vinculando la seguridad de los datos a la informática de una manera trascendental.

El foco principal de este trabajo es recorrer las diferentes formas de seguridad en la transmisión de datos, atravesando conceptos de criptografía, certificados y encriptación entre otros.

# Desarrollo

## ¿Qué es la criptografía?

Si buscamos el concepto de criptografía en algún diccionario veremos que se define a la criptografía como el arte de escribir con claves secretas o de manera misteriosa. En otras palabras, el conjunto de métodos utilizados para ocultar información de los demás.

Actualmente y por la implementación de algoritmos, podemos *actualizar* esa definición a que la criptografía es una práctica que consiste en la construcción y análisis de protocolos, algoritmos o hashes que prevengan que los mensajes privados sean leídos por terceros no deseados.

En los últimos tiempos han surgido nuevas aplicaciones que utilizan estas técnicas. Por ejemplo, crear una firma electrónica que solo el dueño de una clave oculta puede hacer.

### Diferencias con el cifrado

El cifrado, por su parte, consiste en convertir información legible (*texto plano*) en texto ininteligible sin sentido (*texto cifrado*), que sólo puede leerse invirtiendo el proceso (**descifrado**).

El emisor de un mensaje cifrado (**codificado**) comparte la técnica de descifrado (**descodificación**) sólo con los destinatarios previstos para impedir el acceso de los adversarios.

### Claves simétricas vs Claves asimétricas

Las técnicas de cifrado basadas en el uso de claves simétricas consisten en el uso de un secreto compartido entre las partes que desean compartir una información. Este secreto es el que se utiliza tanto para cifrar como para descifrar una información, de ahí el nombre de clave simétrica. Este método plantea un problema de difícil solución, y es el de hacer llegar a todos los participantes en una conversación el secreto que han de compartir por un canal que se considere seguro, así como de conseguir que estos mantengan las claves a buen recaudo.

Ejemplos de métodos de cifrado que utilizan claves simétricas son:

* **DES** (Estándar de cifrado de datos o, en inglés, Data Encryption Standard)
* **AES** (Estándar avanzado de cifrado o, en inglés,Advanced Encryption Standard)

![](data:image/png;base64...)

Figura 1. Funcionamiento de clave secreta.

A diferencia de las de clave simétrica, las técnicas criptográficas que hacen uso de las claves asimétricas no exigen que se comparta ningún tipo de secreto. Cada participante en la comunicación tiene un par de claves, que tienen la particularidad de que lo que una de ellas cifra es descifrado por la otra y viceversa.

En este esquema cada una de las partes hace pública una de las claves y mantiene secreta la otra. Así, cuando uno de los participantes en la comunicación desee enviar un mensaje a otro lo cifrará con la clave pública del destinatario, garantizando de esta forma que sólo el destinatario será capaz de leerlo.

![](data:image/png;base64...)

Figura 2. Funcionamiento de pareja de claves.

Ahora, entendiendo ambos conceptos, ¿cuando resulta conveniente utilizar claves simétricas y cuando claves asimétricas?:

La criptografía simétrica (particularmente con hardware) puede ser muy eficaz porque el cifrado y el descifrado no causan retrasos significativos de tiempo. La criptografía simétrica también brinda cierta autenticidad porque los datos cifrados con una clave simétrica no se pueden descifrar con cualquier otra clave. Como resultado, siempre que la clave simétrica se mantenga en secreto entre las dos partes que la utilizan para cifrar las comunicaciones, cada una de las partes puede estar segura de que se está comunicando con la otra siempre que los mensajes descifrados sigan teniendo sentido.

Por el otro lado, el principal beneficio de la criptografía asimétrica es el aumento de la seguridad de los datos. Es el proceso de cifrado más seguro porque los usuarios nunca tienen que revelar o compartir sus claves privadas, lo que disminuye las posibilidades de que un ciberdelincuente descubra la clave privada de un usuario durante la transmisión.

### Autenticación

Si seguimos con la idea de una comunicación con claves asimétricas, en la que cada participante dispone de una pareja de claves, si uno de los participantes cifra una cierta información con su clave privada, el resto de los implicados puede saber que la información proviene realmente de él.

La forma de hacerlo será descifrar el mensaje enviado con la clave pública del remitente y comprobar que el resultado coincide con la información esperada.

Es posible plantear entonces un mecanismo de autenticación de desafío-respuesta. En él una de las partes envía a otra, a la que quiere identificar, un desafío consistente en un pequeño mensaje que el destinatario devolverá cifrado. La primera de las partes puede comprobar si al descifrar con la clave del supuesto interlocutor el mensaje recibido de vuelta, se obtiene el desafío que ella envió. Si es así, el interlocutor queda perfectamente identificado.

![](data:image/png;base64...)

Figura 3. Mecanismo de autenticación desafío-respuesta.

## Hashing y autenticación

Muy relacionadas con las funciones criptográficas aparecen otras funciones llamadas comúnmente **hashing**. Este tipo de funciones tienen como objetivo reducir una cantidad significativa de información en un mensaje más pequeño.

Siempre hay un resumen específico para una información específica, y si la función de hash está bien diseñada, la probabilidad de que dos informaciones similares produzcan el mismo resumen es muy baja. Tanto el SHA-1 como el MD5 son dos de los algoritmos de hashing más utilizados.

Cuando se desea comprobar que un mensaje no ha sido alterado durante la transmisión, este tipo de algoritmos es útil. Si el remitente de un mensaje aplica una función de hashing sobre la información que desea transmitir, obtendrá un resumen de pequeño tamaño relacionado casi biunívocamente con el texto original. A continuación, puede cifrar este resumen utilizando su clave privada y agregar el resultado al mensaje antes de enviarlo. Esto es lo que se denomina la firma digital de un mensaje.

![](data:image/png;base64...)

Figura 4. Hashing

El resultado es que cuando el destinatario recibe el mensaje, aplicará el mismo algoritmo de hashing a la información y obtendrá un resumen del mensaje. Descifrará la firma adjunta al mensaje recibido y comprobará si coincide con el resumen que él había obtenido. De ser así, el mensaje proviene del remitente esperado y se puede estar seguro de que no ha sido modificado mientras se transmite.

### Ocultación, cifrado de información

Volviendo al propósito original de la criptografía: prevenir que nuestra información sea leída por terceros no deseados. El uso de parejas de claves públicas y privadas significa que la información debe cifrarse de manera diferente según quién la lea. En otras palabras, no se puede usar la misma clave para un fichero en nuestro disco duro para asegurarse de que solo nosotros podamos verlo, que para un mensaje de correo para enviarlo a otra persona, o incluso a varias personas.

A diferencia de crear una firma digital, para cifrar una información debe utilizarse la **clave pública del destinatario**, de tal forma que sólo él pueda descifrar lo cifrado. Esto plantea un pequeño problema cuando se desea enviar la misma información a varios destinatarios. Si debemos cifrar el mensaje con la clave pública de cada uno de ellos, habrá que crear un mensaje en el que aparezca la información que deseamos enviar tantas veces como destinatarios, cifrada cada vez con una clave pública diferente.

Para solventarlo suele cifrarse la información con una clave simétrica, y se compone el mensaje con la información cifrada y con tantas copias de la clave simétrica como destinatarios, cada una cifrada con la clave pública correspondiente. Esto es lo que se denomina sobre electrónico y, al igual que los sobres tradicionales, cumple su misión de ocultar la información que va contenida en el mismo.

![](data:image/png;base64...)

Figura 5. Cifrado de información usando clave simétrica.

Cuando se cifra información para ser almacenada, surge una cuestión a la que hay que dar respuesta: ¿qué ocurre si el propietario de la clave privada, con la que se descifraría la información, pierde la clave?

La respuesta es que no se puede recuperar lo cifrado, lo que te obliga, en casi todas los casos, a hacer una copia de seguridad de la pareja de claves. Para evitarlo, habitualmente se generan **dos pares de claves para cada usuario**, una para firma, de la que no se guarda ninguna copia, y otra para cifrado, de la que se guarda una copia con las debidas medidas de seguridad.

### Algoritmos hash comunes

Los hashes criptográficos cuentan con una serie de fortalezas que los hace útiles para su uso en seguridad. En general, cuando se habla de algoritmos de hash en seguridad se hace referencia a estos:

**Message Digest (MD)**

* **MD**: Creada por Ron Rivest en el MIT, incluye algoritmos como MD2, MD4, MD5 y MD6.
  + **MD2**: Desarrollada en 1988, genera un hash de 128 bits. Ha sido atacada y no es segura.
  + **MD4**: Con un hash de 128 bits, influyó en algoritmos posteriores. Se conocen debilidades, pero versiones basadas en él (como SHA-2) son seguras.
  + **MD5**: Lanzada en 1992, también genera un hash de 128 bits. Aunque fue segura inicialmente, se han descubierto colisiones y vulnerabilidades, recomendándose su reemplazo por SHA-2 o SHA-3.

####

#### Secure Hash Algorithm (SHA)

* **SHA-1**: Establecido en 1995 por el NIST, genera un hash de 160 bits. Se ha demostrado que es vulnerable a colisiones.
* **SHA-2**: Introducido en 2001, mejora SHA-1 con variantes de 256 y 512 bits. Actualmente se considera seguro.

####

#### Otras funciones hash

* **RIPEMD-160**: Diseñado para reemplazar MD4 y MD5, genera un hash de 160 bits y se utiliza en Bitcoin.
* Otros algoritmos populares incluyen HAVAL, Snefru, GOST, MDC-2, N-Hash, Panamá, Spectral, Tangle, CubeHash y Fugue.

En resumen, las funciones hash han evolucionado, y aunque algunas como MD5 y SHA-1 han demostrado ser inseguras, otras como SHA-2 y RIPEMD-160 siguen siendo utilizadas en la actualidad.

### Códigos de autenticación

Los códigos de autenticación de mensaje o funciones MAC son funciones hash que utilizan una clave compartida entre el remitente y el destinatario. Se dividen en los siguientes grupos:

* **CBC-MAC**: Este algoritmo cifra el mensaje en modo CBC y descarta todo el texto cifrado excepto el último bloque. Convierte un algoritmo de cifrado simétrico de bloques en una función de autenticación de mensaje.
* **HMAC**: Utiliza una función hash para implementar una función MAC. HMAC-SHA-256 es una de las opciones más populares, combinando una función de hash con una clave secreta para generar el código de autenticación.
* **UMAC**: Conocido como hash universal, es un método que elige aleatoriamente una función hash de un conjunto disponible para construir el MAC. Se especifica en el RFC 4418.

Las funciones MAC añaden una capa de autenticación utilizando claves secretas, garantizando la integridad y autenticidad de los mensajes.

### Hashing aplicados a derivación de Claves

Aunque las funciones hash son útiles para la gestión de contraseñas, presentan el inconveniente de que las GPUs pueden calcular hashes a gran velocidad, permitiendo a un atacante probar múltiples contraseñas rápidamente (Conocido como un ataque de fuerza bruta).

Para contrarrestar esto, han surgido funciones hash diseñadas para tener un coste computacional y espacial configurable, conocidas como PBKDF (Password Based Key-Derivation Function). Estas funciones son más lentas y dificultan los ataques, además de generar claves a partir de contraseñas.

Entre los algoritmos PBKDF más comunes se encuentran:

* **PBKDF2**: Estándar de internet desde el año 2000, se basa en repetir una función hash convencional mediante un bucle. Aunque es utilizado por Microsoft y Apple, es menos efectivo contra GPUs, ya que usa funciones hash que son fácilmente calculables en estos dispositivos.
* **BCRYPT**: Introducido en 1999, utiliza el cifrador Blowfish en su diseño. Requiere una cantidad modesta de memoria RAM, lo que limita el paralelismo de las GPUs y las ralentiza.
* **SCRYPT**: Basado en el cifrador Salsa20, utiliza grandes cantidades de memoria RAM, lo que lo hace más efectivo contra ataques de GPUs. Ha ganado popularidad en la gestión de contraseñas y en criptomonedas alternativas como Litecoin y Dogecoin.
* **ARGON2**: Derivado de la función hash BLAKE2b, fue elegido como ganador en el concurso Password Hashing Competition y está en auge en el ámbito de las funciones PBKDF.

### Ejemplos de hashing en la actualidad

Un claro ejemplo del uso de hashing como vimos anteriormente es en el manejo de contraseñas. Muchos servicios en línea generan un hash cuando los usuarios crean sus contraseñas, y no almacenan las contraseñas en texto plano. Si lo hicieran, sería un gran riesgo en caso de sufrir un ataque a su base de datos. Al almacenar sólo la función hash de las contraseñas, se dificulta considerablemente la tarea de descifrar cuál es la contraseña original, lo que brinda mayor seguridad y protege la información de los usuarios.

En el caso de la protección de los archivos y valorar los derechos de autoría con Películas y Canciones, los autores pueden generar una función Hash de su archivo, ya sea este un libro, película, canción, o cualquier otro, de manera que si alguien de alguna forma logra apoderarse de este archivo y lo desea compartir no le sea tan fácil, ya que ese archivo puede encontrarse en una lista negra de archivos protegidos.

Otro uso común de hashing se da en las descargas donde comúnmente se implementan **checksums** (También conocido como sumas de verificación o sumas de chequeo). Un checksum es un conjunto de caracteres alfanuméricos, resultado de aplicar una función hash, con el objetivo de comprobar que los datos no hayan sufrido modificaciones. Esta comprobación se realiza comparando el checksum proporcionado en la página de descarga con el checksum generado que se obtiene del archivo descargado, ya sea con alguna aplicación o herramienta online. Esta verificación sirve para cumplir con uno de los principios de la seguridad de la información, la integridad, que es la capacidad de garantizar que los datos no han sido modificados de manera accidental o malintencionada previniendo así cambios no autorizados.

Finalmente, un ámbito en el que se le está dando un gran uso a las funciones de hashing es aquel de las criptomonedas y el blockchain en general. Por ejemplo, en el ecosistema de bitcoin, las transacciones (es decir, una transferencia de bitcoins de un usuario a otro) se agrupan en bloques creados periódicamente. Cada bloque se identifica de forma única por un valor hash de su encabezado, que a su vez está compuesto por varios elementos incluyendo un valor hash obtenido a partir del contenido del bloque. El encabezado también almacena el valor hash del bloque pasado. Por lo tanto, el nuevo bloque “apunta” al anterior, como se muestra en la siguiente figura:

![](data:image/png;base64...)

Figura 6. Estructura de una blockchain.

La esencia del blockchain radica en el uso de valores hash que conectan bloques de información. Cada bloque en la cadena incluye el hash del bloque anterior en su encabezado, creando así una “cadena de bloques”. Esta estructura garantiza que cualquier modificación a la información de un bloque sea detectable. Por ejemplo, si un hacker altera el contenido del bloque N-2 (donde N representa el tamaño actual de la cadena), el hash del bloque N-1 dejaría de coincidir con el hash modificado de N-2. Para ocultar su ataque, el hacker tendría que modificar el hash de N-1, lo que a su vez desajustaría el hash del bloque N. Así, el hacker tendría que alterar todos los bloques sucesivos para mantener la apariencia de integridad, un proceso que se vuelve exponencialmente complicado.

Una pregunta común es: ¿por qué no se pueden volver a calcular fácilmente todos los hashes necesarios? La respuesta radica en el mecanismo de prueba de trabajo (proof-of-work)[[1]](#footnote-0) que hace que alterar los hashes sea extremadamente costoso en términos de recursos computacionales. Además, los hashes deben cumplir con condiciones específicas, lo que limita las posibilidades de alteración.

Es importante mencionar que un blockchain actúa como una base de datos distribuida. La cantidad de copias del blockchain en diferentes nodos es considerable; así, incluso si un bloque fuera alterado en una instancia, la mayoría de los nodos rechazarían esa versión alterada. De este modo, el blockchain emula una de las características más valiosas de los libros de contabilidad tradicionales: una vez registrada, una transacción es prácticamente irreversible.

## Infraestructura de clave pública

La Infraestructura de Clave Pública (PKI) se define como un conjunto integral de hardware, software, personas, políticas y procedimientos necesarios para crear, administrar, almacenar, distribuir y revocar certificados de clave pública basados en criptografía de clave pública. Esta infraestructura proporciona el marco necesario para garantizar la autenticidad y seguridad de las comunicaciones digitales.

Una PKI abarca varios componentes, incluyendo protocolos, servicios y estándares que respaldan aplicaciones basadas en criptografía de clave pública. Estos elementos permiten implementar soluciones de seguridad como la firma digital, el cifrado de datos y la autenticación de usuarios.

Las infraestructuras de clave pública (PKI) abordan cuatro aspectos fundamentales en las comunicaciones electrónicas, especialmente relevantes en transacciones electrónicas:

**1. Confidencialidad**

La confidencialidad asegura que la comunicación entre dos partes no sea visible ni interferida por terceros no autorizados. La tecnología PKI utiliza encriptación para proteger los datos críticos en tránsito, evitando que sean interceptados. Además, permite cifrar información valiosa almacenada en servidores conectados a Internet, lo que significa que, incluso si los datos son capturados, un atacante tendría que romper la encriptación para acceder a ellos.

**2. Autenticación**

La autenticación restringe el acceso a la comunicación electrónica a aquellos que pueden presentar las credenciales necesarias. El método más común es el uso de un nombre de usuario y una contraseña, aunque esto se considera un nivel bajo de seguridad y es susceptible a ataques. En contraste, la PKI utiliza certificados digitales como credenciales de identificación, proporcionando un nivel de autenticación más robusto.

**3. Integridad**

La integridad garantiza que los datos recibidos sean idénticos a los datos enviados, sin modificaciones durante la transmisión, ya sea por error o deliberadamente. La PKI emplea algoritmos hash para verificar la integridad de los datos. Se envía el mensaje junto con el valor de su hash; el receptor calcula el hash del mensaje recibido y lo compara con el hash enviado. Si coinciden, se confirma que el mensaje no ha sido alterado.

**4. No Repudio**

El no repudio implica que, en caso de una disputa sobre lo que ocurrió en una comunicación electrónica, habrá evidencia irrefutable que respalde lo que realmente sucedió. Este aspecto es crucial en operaciones que involucran la firma de contratos electrónicos, ya que previene que cualquiera de las partes niegue haber firmado. La tecnología PKI proporciona no repudio a través del uso de firmas digitales, asegurando que las acciones de cada parte puedan ser verificadas.

## Certificados digitales, relación de confianza y autoridades de certificación

Sobre la base matemática que sustenta la criptografía de clave pública, se han construido una serie de estándares de facto que rigen el uso de esta tecnología. En uno de ellos se describe lo que es y el formato que debe tener un certificado digital X.509.

Básicamente, un certificado digital es un documento público en el que aparece información relativa a un individuo, servidor u otra entidad, que se denomina **sujeto**, y que sirve para asociar la clave pública del mismo con su identidad. En el certificado aparecen, además, una serie de datos sobre la Autoridad de Certificación que emitió el certificado, el periodo de validez del mismo y otros de menor importancia.

![](data:image/png;base64...)

Figura 7. Serie de datos sobre la Autoridad de Certificación que emitió el certificado digital.

Un **nombre distinguido** (**DN**, Distinguished Name en inglés) suministra una identidad a un sujeto en un contexto específico, por ejemplo, un individuo podría tener un certificado personal para uso particular y otro para su identidad cómo empleado de una corporación. Un DN debe ser, por supuesto, único, y está formado por distintos campos definidos por el estándar X.509.

Además de la información relativa al sujeto, aparece en el certificado una referencia a la autoridad de certificación que lo emitió. En un entorno en el que se pretende establecer relaciones de confianza con otros sujetos de los que no se tiene información previa, es necesario confiar en una entidad, la **Autoridad de Certificación** (**AC**), que certifique la identidad de cada sujeto.

La **AC** es la encargada de la emisión de todos los certificados dentro de una jerarquía de confianza, aunque se pueden establecer relaciones de confianza entre autoridades de certificación, que darían lugar a jerarquías de confianza más complejas.

La forma que tiene una autoridad de certificación de dar validez a un certificado es incluir en él su firma, lo que indica que ha sido emitido por ella. A partir de ese momento, todos los sujetos que tengan un certificado emitido por la misma **AC** podrán confiar en el propietario del nuevo certificado.

Todos los estándares de facto que rigen el comportamiento de una **PKI** (Public Key Infrastructure) se denominan **PKCS** (Public-Key Cryptography Standards), con un número seguido. El PKCS#1 describe y define el estándar criptográfico de RSA, mientras que los demás PKCS discuten aspectos más específicos. Por ejemplo, el PKCS#7 habla sobre la sintaxis de los mensajes entre los componentes de una PKI, el PKCS#11 habla sobre cómo debe ser la interfaz de un dispositivo criptográfico, entre otros.

![](data:image/png;base64...)

Figura 8. Campos de un DN.

## Componentes de una PKI

Como vimos anteriormente, una *infraestructura de clave pública* (PKI) es el conjunto de herramientas que permiten cubrir el ciclo de vida de un certificado, los procedimientos asociados y la gestión administrativa que lo rodea.

![](data:image/png;base64...)

Figura 9. Componentes de una PKI

El ciclo de vida de un certificado comienza con la solicitud del mismo, continúa según los pasos definidos en el procedimiento correspondiente y finaliza cuando termina su periodo de validez. Durante el intervalo de validez de un certificado, éste puede ser válido o estar revocado. Todas las transiciones de entrada, salida o internas, en este ciclo de vida, deben estar perfectamente especificadas por algún procedimiento dentro de la PKI.

### El documento de prácticas de certificación

Es la parte más importante dentro de la PKI, la norma fundamental que rige todo el funcionamiento de la infraestructura de seguridad. En este documento, que debe ser público, se recogen todos los procedimientos por los que una entidad llega a estar en posesión de un certificado, la forma en que debe utilizarlo y para qué, cómo se revoca y cuándo deja de tener validez un certificado, etc.

Si alguna parte de este documento no debiera ser pública, como por ejemplo, determinados procedimientos de auditoría, se incluirá en documentos aparte, no públicos, que serán referenciados desde el documento de prácticas de certificación.

### La Autoridad de Certificación

Se trata de la pieza angular de la seguridad de la PKI. Se encarga de realizar las firmas "institucionales" dentro de la PKI. Es decir, de dar validez, o quitarla, a la información que deba ser tomada como buena por el resto de los sujetos.

Fundamentalmente, la Autoridad de Certificación (AC) debe firmar los certificados de todos y cada uno de los sujetos, así como las listas de certificados revocados. Un certificado empieza a existir como tal cuando la autoridad de certificación lo firma, y sólo será revocado cuando la AC lo incluya en una lista de certificados revocados y la firme.

Como puede verse, la importancia de que la clave privada de la AC sea secreta es enorme, puesto que de su seguridad depende la de toda la infraestructura. Por esta razón, la autoridad de certificación suele instalarse en una zona de alta seguridad tanto física como lógica.

El acceso a las dependencias donde esté instalada la AC debe estar perfectamente controlado. Además, la clave privada debe guardarse en un módulo hardware de alta seguridad (HSM) del que no podrá salir nunca. Este módulo, instalado en la AC, se encargará de:

* Generar la pareja de claves de la CA.
* Guardar la clave privada en una memoria que garantice su autodestrucción al intentar acceder a ella.
* Puesto que la clave privada no puede salir de él, debe realizar todas las operaciones matemáticas en las que se vea implicada dicha clave.

Igual que debe garantizarse la seguridad física de la AC, debe hacerse lo mismo con la seguridad lógica. Para ello, se la instalará en un segmento aislado de la red, al que sólo tendrá acceso la autoridad de registro, que es la encargada de ejercer como interfaz de la AC con el resto del mundo.

Si la autoridad de certificación es la raíz de una jerarquía de confianza, es decir, no existe ninguna otra autoridad superior, su certificado será el único en la jerarquía que esté auto-firmado, en otras palabras, que el emisor y el sujeto sean la misma entidad. Si por el contrario existe otra AC superior, será ésta quien firme el certificado.

Cualquier entidad, sea o no poseedora de un certificado emitido por una determinada AC puede confiar en ella. Es el caso por ejemplo, de los servidores web certificados por Verisign, aunque no tengamos un certificado de Verisign, podemos confiar en ellos y aceptar como buenos los certificados de servidor emitidos por esta empresa. La forma en que confiamos en una determinada AC es cargando su certificado (su clave pública en realidad) y utilizándolo para comprobar la validez de la firma de los certificados que nos presenten.

El procedimiento por el cual aceptamos un certificado de una autoridad de certificación es, por tanto, delicado y debemos estar seguros de que el certificado proviene de esa CA y no de otra entidad que intente suplantarla.

### La Autoridad de Registro

Si la Autoridad de Certificación debe estar en una red aislada para protegerla de posibles ataques, la Autoridad de Registro es la encargada de hacer las veces de interfaz hacia el exterior.

Su trabajo fundamental es el de llevar a cabo los procedimientos de registro para la emisión de nuevos certificados. En consonancia con la normativa escrita en dichos procedimientos, el registro puede ser presencial o remoto, online u offline, etc. En cualquier caso y tras haber comprobado la identidad del sujeto para el que se va a emitir el certificado, la Autoridad de Registro enviará a la Autoridad de Certificación una solicitud para firmar un nuevo certificado. Una vez firmado el nuevo certificado se publicará en el directorio y ya podrá ser utilizado.

Otra de las tareas de la autoridad de registro es recibir las solicitudes de revocación de un certificado. De acuerdo con los procedimientos adecuados, cuando éstas solicitudes sean verificadas se enviarán también a la AC, quien las

firmará. A continuación se publicarán en el directorio y desde ese momento cualquiera que consulte la lista de certificados revocados, verá que ese certificado ya no es válido.

### El Directorio

Es el repositorio fundamental de toda la infraestructura. En él se almacenan los certificados de los usuarios, las listas de certificados revocados y cualquier otra información que se desee acerca de los usuarios del sistema, por ejemplo, otros datos personales que no aparecen en el certificado.

Los estándares que rigen el acceso al directorio son habitualmente el LDAP (Protocolo Ligero de Acceso a Directorios) que especifica el protocolo de acceso, y el SSL (Capa de Sockets Seguros) para garantizar la seguridad en el mismo.

## Protocolos de seguridad en la transmisión de datos

El protocolo HTTP no es seguro, por lo que es susceptible de sufrir interceptaciones de intrusos, ya que los datos transferidos desde el navegador web al servidor web o entre dos terminales se transmiten como texto plano. De esta manera, puede haber terceros que intercepten y visualicen información confidencial, como datos de tarjetas de crédito o accesos a cuentas.

Existen protocolos de seguridad en la transmisión de datos que implementan un cierto cifrado y protección a la hora de la comunicación; los ejemplos más conocidos son SSL y, su sucesor, TLS. Estos protocolos garantizan que los datos estén cifrados y protegidos frente a interceptaciones al enviar o publicar datos en un navegador que utiliza **HTTPS**.

### SSL/TLS

#### SSL

Secure Sockets Layer (SSL) es un protocolo de seguridad que ofrece privacidad, autenticación e integridad a las comunicaciones en Internet.

El SSL proporciona un canal seguro entre dos computadoras o dispositivos que operan a través de Internet o de una red interna. Un ejemplo frecuente es el uso de SSL para proteger las comunicaciones entre un navegador web y un servidor web.

Este protocolo cambia la dirección del sitio web de HTTP a HTTPS, donde «S» significa «seguridad».

Desde el punto de vista técnico, el protocolo SSL es un método transparente para establecer una sesión segura que requiere una intervención mínima por parte del usuario final. En el caso de los navegadores, es posible determinar si un sitio web usa SSL cuando se muestra el candado o la barra de direcciones presenta la URL como HTTPS, en lugar de HTTP.

#### TLS

El término TLS significa "Capa de seguridad de transporte" (Transport Layer Security, en inglés) y es un protocolo criptográfico diseñado para garantizar la seguridad de los datos transmitidos entre dos aplicaciones a través de Internet. Este protocolo es fundamental para la navegación web segura, asegurando que toda la información enviada a un sitio web esté protegida contra interceptaciones maliciosas.

Además de comunicaciones web, el protocolo TLS puede ser usado en sistemas de:

* Mensajería instantánea
* Correo electrónico
* Transferencia de archivos
* Conferencias de audio y video
* Servicios de Internet como DNS y NTP

Es importante tener en cuenta que TLS **protege la transmisión de datos** entre sistemas finales, no los datos en los sistemas finales. En otras palabras, el protocolo TLS sólo protege los datos para que no los intercepten personas con malas intenciones; por lo tanto, es importante revisar la autenticidad de cualquier sitio web antes de ingresar información personal para evitar estafas.

#### ¿Cuál es la diferencia entre TLS y SSL?

Sabemos que el protocolo TLS evolucionó a partir de Secure Socket Layers, que fue desarrollado en 1994 por Netscape Communications Corporation para proteger las sesiones web de aquellos que podrían intentar espiar su comportamiento web. Si bien la versión 1.0 de SSL nunca se lanzó públicamente, fue seguida rápidamente por 2.0 y luego por 3.0, en la que se basa TLS.

RFC 7568 dejó obsoleto SSL 3.0 en 2015 porque se consideró inseguro y recomendó usar TLS 1.2 en el futuro. Después, TLS 1.3 se lanzó en 2020, ofreciendo un nivel de seguridad aún mayor y un protocolo de negociación aún más rápido, lo que lo convirtió rápidamente en un estándar en todos los servidores web.

Entre las vulnerabilidades con las que contaba SSL podemos denotar:

* TLS reemplazó a SSL porque es más rápido y menos propenso a la vulnerabilidad.
* Si bien TLS ha sido propenso a infracciones, ha mostrado grandes mejoras en términos de velocidad de negociación y encriptación sobre el protocolo SSL que ha reemplazado

En resumen entonces,TLS es una evolución del SSL.

#### ¿Cómo funciona TLS?

En general, un sitio web o una aplicación web debe tener un certificado TLS instalado en su servidor para poder usar TLS. Un certificado TLS se conoce más comúnmente como certificado SSL, a partir del cual evolucionó. Este certificado, junto con la clave pública del servidor, contiene información crucial sobre quién es el propietario del dominio. Se utilizan para validar y autenticar la identidad y la propiedad del servidor.

El protocolo de enlace TLS es lo que se utiliza para iniciar una conexión TLS. El dispositivo del usuario y el sitio web con el que se está comunicando realizan las siguientes operaciones durante el protocolo de enlace TLS:

* Se especifica qué versión de TLS se usará
* Se decide qué cifrado usará
* Autentican la identidad del servidor del sitio web usando el certificado TLS
* Se crean claves de sesión para el cifrado de datos, que se utilizarán una vez que se complete el protocolo de enlace

Una vez que se hayan cifrado los datos transmitidos y se haya autenticado el servidor del sitio web, se firma con un código de autenticación de mensajes (o MAC). Para verificar la integridad de los datos transmitidos desde el servidor, el dispositivo de los usuarios finales se asegurará de que el MAC esté completo y sin alteraciones.

#### Paso a paso del handshake

El concepto del handshaking de SSL/TLS es como un diálogo entre un servidor y un cliente, el paso a paso sería el siguiente:

1. El cliente solicita al servidor que establezca una conexión segura y ofrece un conjunto de cifrado que "entiende", así como una versión compatible de SSL/TLS.
2. El servidor comprueba el conjunto de cifrado enviado, lo compara con el suyo propio y envía una respuesta al cliente con un archivo de certificado y una clave pública.
3. El cliente comprueba el certificado y, si está bien, se ofrece a verificar la clave privada. Para ello, la genera y cifra la clave secreta compartida con la clave pública del servidor enviada previamente.
4. El servidor acepta la clave y la verifica con su clave privada. A continuación, crea un secreto maestro, que se utilizará para cifrar la información que se intercambia.

Por último, el cliente envía un mensaje de prueba al servidor, que está cifrado utilizando una técnica previamente acordada, y el servidor lo descifra y analiza. Esto finaliza el Handshake SSL/TLS, lo que permite que el cliente y el servidor continúen compartiendo datos.

Si la sesión finaliza y el cliente vuelve a ponerse en contacto con el servidor más tarde, todos los datos creados anteriormente y el secreto principal seguirán siendo válidos. Todo el proceso es en segundos y el usuario no lo nota.

# Seguridad en redes VPN

En la actualidad, muchas organizaciones abarcan amplias áreas geográficas, lo que plantea desafíos para garantizar una infraestructura tecnológica que permita la transmisión de datos de manera eficiente y segura. En el pasado, las empresas instalaban cables a largas distancias, lo cual resultaba poco práctico debido a los altos costos, el espacio necesario y el tiempo que tomaba.

En respuesta a esta problemática, las Redes Privadas Virtuales (VPN) son una solución comprobada y rentable para asegurar la transmisión de datos a grandes distancias.

Una Red Privada Virtual (VPN) es una tecnología que permite crear una conexión segura y cifrada entre un dispositivo (como una computadora o un teléfono) y una red, utilizando una infraestructura pública como Internet. Esta conexión simula un "túnel" privado que protege los datos transmitidos entre los extremos, lo que hace que parezca que se está utilizando una red privada aunque los datos estén viajando a través de una red pública.

Pero ¿Qué es un túnel privado? Un túnelprivado es un enlace virtual y cifrado que permite el envío seguro de datos entre dos puntos (como un dispositivo y un servidor) a través de una red pública, como Internet. Este "túnel" protege la información de manera que, aunque los datos pasen por una infraestructura compartida o pública, no puedan ser leídos o interceptados por terceros (Man in the middle attack por ejemplo). La privacidad del túnel se garantiza mediante tecnologías de cifrado, lo que asegura que solo los extremos de la conexión puedan interpretar los datos transmitidos.

Las VPNs son comúnmente utilizadas para:

* Proteger la privacidad al navegar por Internet.
* Acceder a recursos remotos (como servidores corporativos).
* Encriptar datos sensibles en tránsito para evitar que terceros los intercepten o alteren.

Una VPN permite crear conexiones seguras entre distintas ubicaciones utilizando la infraestructura de una red pública, como Internet. Las VPNs combinan dos conceptos importantes: redes virtuales y redes privadas. En una red virtual, los enlaces son lógicos y no físicos, por lo que el usuario solo ve la red virtual, sin percibir la red física subyacente.

Desde la perspectiva del usuario, una VPN es una conexión punto a punto entre su dispositivo (cliente VPN) y el servidor de la organización (servidor VPN), como si los datos se enviaran por un enlace privado.

Las principales razones por las que una empresa implementa una VPN incluyen:

* Proporcionar movilidad a sus empleados.
* Acceso remoto a la base de datos central.
* Conexión segura entre empleados a través de Internet.
* Intercambio de información en tiempo real.
* Acceso al correo electrónico corporativo.
* Teletrabajo.
* Flexibilidad y facilidad de uso.
* Maximizar la velocidad de transferencia de datos.
* Adaptación fácil a nuevas tecnologías.

Existen varios protocolos utilizados para implementar VPNs, como:

* PPTP (Point-to-Point Tunneling Protocol): Permite el intercambio seguro de datos a través de una VPN utilizando TCP/IP. Es ideal para usar Internet sin incurrir en el costo de líneas privadas alquiladas.
* L2TP (Layer 2 Tunneling Protocol): Encapsula tramas en paquetes IP, permitiendo el uso de IPsec para cifrar la información que viaja a través del túnel.
* IPsec (Internet Protocol Security): Un conjunto de protocolos que asegura las comunicaciones mediante la autenticación o cifrado de paquetes IP. También gestiona el establecimiento de claves de cifrado.
* NAT (Network Address Translation): Método para asignar direcciones IP dinámicas, útil cuando el número de dispositivos que necesitan acceder a Internet supera las direcciones IP públicas disponibles.

### Funcionamiento de una VPN

Una Red Privada Virtual (VPN) funciona mediante un protocolo de túnel, el cual cifra los datos que se transmiten entre los dos extremos de la VPN. El término "túnel" simboliza el hecho de que los datos están protegidos mediante cifrado desde el momento en que ingresan a la VPN hasta que salen de ella, lo que los hace incomprensibles para cualquier persona que no esté en uno de los extremos de la conexión, como si viajaran por un túnel invisible.

En una VPN, hay dos partes principales:

* El clienteVPN (dispositivo del usuario) se encarga de cifrar los datos antes de enviarlos y descifrarlos cuando los recibe.
* El servidorVPN (también conocido como servidor de acceso remoto) recibe y descifra los datos del lado de la organización, y luego los envía a la red interna.

Cuando un usuario accede a la VPN, su solicitud primero viaja sin cifrar al sistema de pasarela, que se conecta a la red remota usando una red pública (como Internet) como intermediaria. Después de que se establece esta conexión, los datos viajan cifrados a través del túnel. El servidor VPN recibe la solicitud cifrada, la descifra y responde también de forma cifrada. Finalmente, cuando el cliente VPN recibe los datos, los descifra para que el usuario pueda acceder a la información.

### Seguridad en las VPN

En los primeros días del diseño de redes, la seguridad no era una prioridad, ya que las redes solo eran utilizadas por universidades e investigadores, y no se consideraba la posibilidad de que alguien intentara interceptar mensajes. Sin embargo, con la adopción comercial de las redes y el auge de Internet, la seguridad pasó a ser un aspecto crucial al momento de implementar redes.

Con la llegada de Internet, cualquier computadora conectada es susceptible a ataques, lo que ha provocado pérdidas económicas significativas para las empresas. En el caso de las VPNs, donde la información privada de una organización atraviesa una red pública, es fundamental garantizar la confidencialidad, integridad y seguridad de los datos, además de impedir el acceso no autorizado a la red privada.

La seguridad en una VPN no solo implica el control de acceso seguro a los recursos, sino también la implementación de políticasdeseguridad que aseguren el funcionamiento adecuado de la VPN. Esto incluye establecer niveles de seguridad antes de que se inicie la conexión cifrada con una red remota o una oficina externa. Es esencial verificar el estado de seguridad de los dispositivos que se conectan a la red corporativa, asegurando que cumplan con los estándares establecidos, independientemente de si son sistemas corporativos o dispositivos utilizados en el teletrabajo.

Para mantener esta seguridad, es necesario contar con un sistemade chequeo que evalúe el estado de los dispositivos remotos conectados a través de la VPN. Este proceso debe ser percibido por el usuario como una ayuda a la seguridad general, no como una imposición, y debe ser lo suficientemente amplio para abarcar productos y sistemas de seguridad utilizados en el entorno doméstico.

Dos elementos clave en la seguridad de las VPNs son la autenticación de usuarios y la encriptación de datos. El uso de IPSec (Internet Protocol Security) es una de las tecnologías más seguras para proteger las comunicaciones dentro de una VPN, ya que permite el cifrado y autenticación de los datos que viajan por la red.

### Necesidades de las VPN

La competitividad y globalización han aumentado la necesidad de estar al tanto de los avances tecnológicos, y las redes VPN destacan como herramientas clave para obtener beneficios al maximizar su uso. Con el crecimiento de Internet y la reducción de costos de acceso, las VPNs se han convertido en una solución esencial en el mundo de las redes de información.

Una de las principales motivaciones para su uso es la reducción de costos en comunicaciones, tanto en llamadas de larga distancia como en vínculos dedicados. Antes de Internet, las empresas que deseaban conectar redes en diferentes ubicaciones tenían que invertir en costoso hardware y servicios de telecomunicaciones. Con la llegada de Internet, las VPNs permiten interconectar sedes geográficamente distantes con una inversión relativamente pequeña en hardware, aprovechando la infraestructura global de la red.

No obstante, a medida que aumenta el acceso remoto a redes corporativas, también crecen las amenazas de seguridad. Por ello, las empresas deben contar con tecnologías flexibles y herramientas de seguridad avanzadas para proteger sus VPNs. Características como la autenticación fuerte y políticas de seguridad robustas son cruciales para evitar vulnerabilidades.

### Protocolos de seguridad para IoT

A diferencia de los sistemas tradicionales de IT, los dispositivos de Internet de las Cosas (IoT) están diseñados con un enfoque más en la funcionalidad que en la seguridad. Muchos dispositivos IoT tienen capacidades limitadas de procesamiento y memoria, lo que dificulta la implementación de soluciones de seguridad robustas como las que se utilizan en otros entornos. Esto, combinado con la gran cantidad de dispositivos conectados, amplifica la superficie de ataque y expone a los sistemas IoT a diversas vulnerabilidades, como el acceso no autorizado, la manipulación de datos y ataques de denegación de servicio (DDoS).

Uno de los principales problemas de seguridad en IoT es la ausencia de encriptación y autenticación adecuadas en muchos dispositivos. Esto abre la puerta a ataques de interceptación (man-in-the-middle), suplantación de identidad y la manipulación de comandos. La falta de estandarización de protocolos de seguridad también dificulta una protección coherente a lo largo de diferentes plataformas y fabricantes.

#### Protocolos que implementan seguridad para IoT

Existen varios protocolos que entre sus funcionalidades, permiten abordar la seguridad en la transmisión de datos de los dispositivos IoT, proporcionar mecanismos de encriptación, autenticación y protección de la integridad de los datos.

* MQTT (Message Queuing Telemetry Transport):
  + Por sí mismo, MQTT no incluye seguridad, pero puede integrarse con TLS (Transport Layer Security) para asegurar la transmisión de mensajes entre dispositivos. Además, puede implementar autenticación basada en certificados o autenticación básica con usuario y contraseña.
* CoAP (Constrained Application Protocol)
  + CoAP se puede asegurar utilizando **DTLS (Datagram Transport Layer Security)**, una versión ligera de TLS que protege las comunicaciones sobre UDP, lo que lo hace ideal para dispositivos IoT que operan en redes no confiables.
* LoRaWAN (Long Range Wide Area Network)
  + Incluye mecanismos de seguridad en la capa de red, utilizando **encriptación AES** para proteger tanto la carga útil como la autenticación de dispositivos. Sin embargo, la clave compartida debe gestionarse adecuadamente para evitar compromisos de seguridad.
* Zigbee
  + Zigbee ofrece autenticación mutua y cifrado utilizando **AES-128**, un protocolo de cifrado bastante sólido para este tipo de dispositivos. También incluye características para gestionar las claves de cifrado de manera segura.

##

## Desafíos en la seguridad

### Vulnerabilidades en SSL/TLS

Pese a ser SSL/TLS un protocolo seguro, se han ido encontrando una serie de vulnerabilidades que explotan el propio protocolo SSL o alguna de las implementaciones que ha utilizado a lo largo de toda su historia.

Para encontrar las vulnerabilidades de dicho protocolo se utilizó una base de datos de vulnerabilidades de un CERT. En este caso la del INTECO (Instituto Nacional de tecnologías de comunicación) en colaboración con NVD (National Vulnerability Database). Las vulnerabilidades más recientes sobre el protocolo SSL/TLS se muestran en la siguiente figura:

![](data:image/png;base64...)

Figura 10. Vulnerabilidades en protocolos SSL/TLS

A pesar de haberse encontrado ciertas vulnerabilidades sobre este protocolo desde 1995, muchas se han ido solucionando con las nuevas versiones de dicho protocolo.

### Ataque Man in the middle (MitM)

Un ataque MitM se basa en la intercepción de la comunicación entre dos partes sin su conocimiento. El atacante se coloca como intermediario, simulando ser una de las partes legítimas para obtener acceso a información sensible o modificar el contenido de la comunicación.

Está compuesto de las siguientes fases:

1. ***Intercepción***: El atacante intercepta la comunicación entre dos partes, generalmente aprovechando una red Wi-Fi pública o no segura.
2. ***Descodificación***: Si la comunicación no está cifrada, el atacante puede leer y modificar el contenido de los mensajes.
3. ***Suplantación***: El atacante puede suplantar a una de las partes legítimas para enviar mensajes falsos o modificar los datos transmitidos.

Figura 11. Ataque Man in the Middle![](data:image/png;base64...)

Pero, ¿cómo se previene este tipo de ataques? Se pueden tomar algunas medidas para prevenirlos:

* **Siempre desconfíe de las redes Wi-Fi**: por definición, las redes Wi-Fi son más susceptibles a los ataques si alguien ha podido acceder a la red legítima de manera no autorizada o porque los actores maliciosos crean una red con el mismo nombre que la red legítima para engañar a los usuarios y que se conecten. Tenga siemprecuidado al utilizar redes Wi-Fi públicas. En caso de necesitar utilizarlas, evite compartir información importante y descargar archivos.
* **Sólo instale software de fuentes conocidas** - muchas amenazas se esconden detrás de software o archivos que parecen inofensivos. Por eso es importante asegurarse de que el software que necesita descargar provenga de una fuente confiable para disminuir las posibilidades de que la descarga haya sido manipulada. Si un ataque Man-in-the-Middle ya está en marcha, es posible que los ciberdelincuentes puedan cambiar el archivo de destino que se descargará. Si este es el caso, el siguiente consejo le ayudará a identificar el proceso.
* **Antivirus** - esta es una recomendación presente en casi todas las publicaciones relacionadas a amenazas informáticas de WeLiveSecurity, por el simple hecho de que es una de las formas más eficientes de prevenir la mayoría de las amenazas. Mientras recopilaba imágenes para la elaboración de este artículo olvidé deshabilitar mi software de protección y me alertó sobre una amenaza potencial en la red e identificó un ataque de envenenamiento de caché ARP.

# Conclusiones

La criptografía ha sido un pilar fundamental en el desarrollo de las comunicaciones digitales seguras y la protección de la información en un mundo cada vez más interconectado. A lo largo de este trabajo, hemos explorado los conceptos básicos de la criptografía, sus aplicaciones y la evolución de las técnicas utilizadas para asegurar la confidencialidad, integridad y autenticidad de los datos.

En primer lugar, es esencial entender qué es la criptografía y cómo se diferencia del simple cifrado. La criptografía abarca no solo el cifrado de datos, sino también procesos complejos que garantizan que la información sea accesible sólo para las partes autorizadas. La distinción entre claves simétricas y asimétricas resalta la diversidad de métodos disponibles para proteger la información, cada uno con sus ventajas y desventajas. Las claves simétricas ofrecen velocidad y eficiencia, mientras que las asimétricas proporcionan un nivel adicional de seguridad, especialmente en la autenticación y el intercambio seguro de claves.

La autenticación es otro componente crítico de la seguridad informática. A medida que las organizaciones adoptan tecnologías digitales, la necesidad de garantizar que los usuarios y dispositivos sean quienes dicen ser se vuelve primordial. Las técnicas de hashing, junto con la autenticación, juegan un papel clave en este proceso. La implementación de algoritmos hash comunes y su uso en la derivación de claves refuerzan la seguridad, asegurando que los datos no sean manipulados o comprometidos.

El uso de la infraestructura de clave pública (PKI) y los certificados digitales representa un avance significativo en la creación de relaciones de confianza en un entorno digital. La PKI proporciona un marco para gestionar las claves criptográficas y los certificados, asegurando que la información sea compartida de manera segura entre las partes. Los componentes de la PKI, como las autoridades de certificación y de registro, juegan un papel fundamental en la verificación de identidades y la gestión de la confianza en las comunicaciones.

El análisis de los protocolos de seguridad, como SSL y TLS, revela la importancia de estos estándares en la protección de datos en tránsito. La comprensión de cómo funciona TLS, incluida su fase de handshake, es crucial para cualquier profesional de seguridad que busque implementar medidas efectivas para proteger la información en la red. Sin embargo, a pesar de estos avances, los desafíos y vulnerabilidades en la seguridad de SSL/TLS, así como los ataques como el Man-in-the-Middle (MitM), destacan la necesidad de una vigilancia continua y la actualización de las medidas de seguridad.

Por otra parte, la seguridad en redes VPN se ha vuelto indispensable en el contexto actual, donde el teletrabajo y el acceso remoto se han incrementado notablemente. Las VPN no solo permiten la conexión segura entre redes distribuidas, sino que también protegen la información sensible que viaja a través de redes públicas. Comprender el funcionamiento de las VPN y las necesidades de seguridad que deben satisfacerse es esencial para garantizar la protección de la información empresarial y personal.

Finalmente, es crucial reconocer que la seguridad en el ámbito digital no es estática. Las amenazas evolucionan constantemente, lo que exige que las organizaciones adopten un enfoque proactivo hacia la seguridad. La implementación de protocolos de seguridad para el Internet de las Cosas (IoT) es un área que requiere atención especial, dado el rápido crecimiento de dispositivos conectados y la superficie de ataque que presentan.

En resumen, la criptografía y las tecnologías de seguridad son elementos esenciales en la protección de la información en la era digital. La comprensión de los conceptos y técnicas discutidos en este trabajo permitirá a los profesionales y organizaciones tomar decisiones informadas sobre cómo proteger sus datos y mantener la confianza en sus sistemas de información. A medida que continuamos enfrentando nuevos desafíos en el campo de la seguridad informática, es fundamental permanecer informados y adaptables para asegurar el futuro de la comunicación digital.

# Bibliografía

Andrade, A. (2019). Características y aplicaciones de las funciones resumen criptográficas en la gestión de contraseñas.

Caro Alonso-Rodríguez, A. J. (2013). Man in the middle attacks on SSL/TLS.

Castro Martínez, F. J. (2015). Gestor de certificados digitales con PKI.

Feced, J. P. Uso de checksum en la descarga online de aplicaciones.

Jiménez Cely, R. (2014). Seguridad en redes VPN (Bachelor's thesis, Universidad Piloto de Colombia).

PÚBLICA, C. La criptografía de clave pública y su aplicación a la información.

Qué es un ataque de Man-in-the-Middle y cómo funciona. (2021, 28 diciembre). <https://www.welivesecurity.com/la-es/2021/12/28/que-es-ataque-man-in-the-middle-como-funciona/>

Sánchez, S., Domínguez, P., & Velásquez, L. (2018). Hashing: Técnicas y Hash para la Protección de Datos. Universidad Tecnológica de Panamá, Grupo de Investigación.

Soriano, M. (2014). Seguridad en redes y seguridad de la información. Obtenido de <http://improvet.cvut.cz/project/download/C2ES/Seguridad_de_Red_e_Informacion.pdf>.

Zozaya, C., Incera, J., & Franzoni, A. L. (2019). Blockchain: un tutorial. Estudios, 17(129), 113-126.

# Anexo: Autoevaluación con Preguntas y Respuestas

1. **¿Qué es la criptografía? ¿En qué se diferencia con el cifrado?**

La criptografía es una práctica que consiste en la construcción y análisis de protocolos, algoritmos o hashes que prevengan que los mensajes privados sean leídos por terceros no deseados.

El cifrado, por su parte, consiste en convertir información legible (*texto plano*) en texto ininteligible sin sentido (*texto cifrado*), que sólo puede leerse invirtiendo el proceso (**descifrado**).

1. **¿Cuándo resulta conveniente utilizar claves simétricas y cuando claves asimétricas?**

La criptografía simétrica (particularmente con hardware) puede ser muy eficaz porque el cifrado y el descifrado no causan retrasos significativos de tiempo. La criptografía simétrica también brinda cierta autenticidad porque los datos cifrados con una clave simétrica no se pueden descifrar con cualquier otra clave. Como resultado, siempre que la clave simétrica se mantenga en secreto entre las dos partes que la utilizan para cifrar las comunicaciones, cada una de las partes puede estar segura de que se está comunicando con la otra siempre que los mensajes descifrados sigan teniendo sentido.

Por el otro lado, el principal beneficio de la criptografía asimétrica es el aumento de la seguridad de los datos. Es el proceso de cifrado más seguro porque los usuarios nunca tienen que revelar o compartir sus claves privadas, lo que disminuye las posibilidades de que un ciberdelincuente descubra la clave privada de un usuario durante la transmisión.

1. **¿En qué consiste el mecanismo de autenticación de desafío-respuesta?**

En el mecanismo de autenticación de desafío-respuesta, una de las partes envía a otra, a la que quiere identificar, un desafío consistente en un pequeño mensaje que el destinatario devolverá cifrado. La primera de las partes puede comprobar si al descifrar con la clave del supuesto interlocutor el mensaje recibido de vuelta, se obtiene el desafío que ella envió. Si es así, el interlocutor queda perfectamente identificado.

1. **¿Qué es el hashing? ¿Para qué se utiliza?**

El hashing es un tipo de funciones que tienen como objetivo reducir una cantidad significativa de información en un mensaje más pequeño.

Se utiliza cuando se desea comprobar que un mensaje no ha sido alterado durante la transmisión. Si el remitente de un mensaje aplica una función de hashing sobre la información que desea transmitir, obtendrá un resumen de pequeño tamaño relacionado casi biunívocamente con el texto original. A continuación, puede cifrar este resumen utilizando su clave privada y agregar el resultado al mensaje antes de enviarlo.

El resultado es que cuando el destinatario recibe el mensaje, aplicará el mismo algoritmo de hashing a la información y obtendrá un resumen del mensaje. Descifrará la firma adjunta al mensaje recibido y comprobará si coincide con el resumen que él había obtenido. De ser así, el mensaje proviene del remitente esperado y se puede estar seguro de que no ha sido modificado mientras se transmite.

1. **Los códigos de autenticación, ¿qué son? ¿En qué grupos se dividen?**

Los códigos de autenticación de mensaje o funciones MAC son funciones hash que utilizan una clave compartida entre el remitente y el destinatario. Se dividen en los siguientes grupos:

* **CBC-MAC**: Este algoritmo cifra el mensaje en modo CBC y descarta todo el texto cifrado excepto el último bloque. Convierte un algoritmo de cifrado simétrico de bloques en una función de autenticación de mensaje.
* **HMAC**: Utiliza una función hash para implementar una función MAC. HMAC-SHA-256 es una de las opciones más populares, combinando una función de hash con una clave secreta para generar el código de autenticación.
* **UMAC**: Conocido como hash universal, es un método que elige aleatoriamente una función hash de un conjunto disponible para construir el MAC. Se especifica en el RFC 4418.

1. **Enumerar los algoritmos PBKDF (Password Based Key-Derivation Function) más comunes.**

Los algoritmos Password Based Key-Derivation Function más comunes son:

* **PBKDF2**: Estándar de internet desde el año 2000, se basa en repetir una función hash convencional mediante un bucle. Aunque es utilizado por Microsoft y Apple, es menos efectivo contra GPUs, ya que usa funciones hash que son fácilmente calculables en estos dispositivos.
* **BCRYPT**: Introducido en 1999, utiliza el cifrador Blowfish en su diseño. Requiere una cantidad modesta de memoria RAM, lo que limita el paralelismo de las GPUs y las ralentiza.
* **SCRYPT**: Basado en el cifrador Salsa20, utiliza grandes cantidades de memoria RAM, lo que lo hace más efectivo contra ataques de GPUs. Ha ganado popularidad en la gestión de contraseñas y en criptomonedas alternativas como Litecoin y Dogecoin.
* **ARGON2**: Derivado de la función hash BLAKE2b, fue elegido como ganador en el concurso Password Hashing Competition y está en auge en el ámbito de las funciones PBKDF.

1. **Explicite al menos dos usos comunes de hashing en la actualidad.**

Un común de hashing se da en las descargas donde comúnmente se implementan checksums (También conocido como sumas de verificación o sumas de chequeo). Un checksum es un conjunto de caracteres alfanuméricos, resultado de aplicar una función hash, con el objetivo de comprobar que los datos no hayan sufrido modificaciones. Esta comprobación se realiza comparando el checksum proporcionado en la página de descarga con el checksum generado que se obtiene del archivo descargado, ya sea con alguna aplicación o herramienta online. Esta verificación sirve para cumplir con uno de los principios de la seguridad de la información, la integridad, que es la capacidad de garantizar que los datos no han sido modificados de manera accidental o malintencionada previniendo así cambios no autorizados.

Otro ámbito en el que se le está dando un gran uso a las funciones de hashing es aquel de las criptomonedas y el blockchain en general. Por ejemplo, en el ecosistema de bitcoin, las transacciones (es decir, una transferencia de bitcoins de un usuario a otro) se agrupan en bloques creados periódicamente. Cada bloque se identifica de forma única por un valor hash de su encabezado, que a su vez está compuesto por varios elementos incluyendo un valor hash obtenido a partir del contenido del bloque. El encabezado también almacena el valor hash del bloque pasado.

1. **¿Qué es una PKI?**

La Infraestructura de Clave Pública (PKI) se define como un conjunto integral de hardware, software, personas, políticas y procedimientos necesarios para crear, administrar, almacenar, distribuir y revocar certificados de clave pública basados en criptografía de clave pública. Esta infraestructura proporciona el marco necesario para garantizar la autenticidad y seguridad de las comunicaciones digitales.

Una PKI abarca varios componentes, incluyendo protocolos, servicios y estándares que respaldan aplicaciones basadas en criptografía de clave pública. Estos elementos permiten implementar soluciones de seguridad como la firma digital, el cifrado de datos y la autenticación de usuarios.

1. **Enumere los cuatro aspectos fundamentales que aborda la PKI en las comunicaciones electrónicas.**

**1. Confidencialidad:** La confidencialidad asegura que la comunicación entre dos partes no sea visible ni interferida por terceros no autorizados. La tecnología PKI utiliza encriptación para proteger los datos críticos en tránsito, evitando que sean interceptados. Además, permite cifrar información valiosa almacenada en servidores conectados a Internet, lo que significa que, incluso si los datos son capturados, un atacante tendría que romper la encriptación para acceder a ellos.

**2. Autenticación:** La autenticación restringe el acceso a la comunicación electrónica a aquellos que pueden presentar las credenciales necesarias. El método más común es el uso de un nombre de usuario y una contraseña, aunque esto se considera un nivel bajo de seguridad y es susceptible a ataques. En contraste, la PKI utiliza certificados digitales como credenciales de identificación, proporcionando un nivel de autenticación más robusto.

**3. Integridad:** La integridad garantiza que los datos recibidos sean idénticos a los datos enviados, sin modificaciones durante la transmisión, ya sea por error o deliberadamente. La PKI emplea algoritmos hash para verificar la integridad de los datos. Se envía el mensaje junto con el valor de su hash; el receptor calcula el hash del mensaje recibido y lo compara con el hash enviado. Si coinciden, se confirma que el mensaje no ha sido alterado.

**4. No Repudio:** El no repudio implica que, en caso de una disputa sobre lo que ocurrió en una comunicación electrónica, habrá evidencia irrefutable que respalde lo que realmente sucedió. Este aspecto es crucial en operaciones que involucran la firma de contratos electrónicos, ya que previene que cualquiera de las partes niegue haber firmado. La tecnología PKI proporciona no repudio a través del uso de firmas digitales, asegurando que las acciones de cada parte puedan ser verificadas.

1. **¿Por qué el protocolo HTTP no es seguro? Dé ejemplos de protocolos de seguridad.**

El protocolo HTTP no es seguro, por lo que es susceptible de sufrir interceptaciones de intrusos, ya que los datos transferidos desde el navegador web al servidor web o entre dos terminales se transmiten como texto plano. De esta manera, puede haber terceros que intercepten y visualicen información confidencial, como datos de tarjetas de crédito o accesos a cuentas.

Existen protocolos de seguridad en la transmisión de datos que implementan un cierto cifrado y protección a la hora de la comunicación. Los ejemplos más conocidos son:

* **Secure Sockets Layer (SSL):** Es un protocolo de seguridad que ofrece privacidad, autenticación e integridad a las comunicaciones en Internet. El SSL proporciona un canal seguro entre dos computadoras o dispositivos que operan a través de Internet o de una red interna. Un ejemplo frecuente es el uso de SSL para proteger las comunicaciones entre un navegador web y un servidor web.
* El término TLS significa "Capa de seguridad de transporte" (Transport Layer Security, en inglés) y es un protocolo criptográfico diseñado para garantizar la seguridad de los datos transmitidos entre dos aplicaciones a través de Internet. Este protocolo es fundamental para la navegación web segura, asegurando que toda la información enviada a un sitio web esté protegida contra interceptaciones maliciosas.

1. Queda fuera del alcance de este informe ya que es un concepto demasiado ligado a la tecnología de blockchain [↑](#footnote-ref-0)