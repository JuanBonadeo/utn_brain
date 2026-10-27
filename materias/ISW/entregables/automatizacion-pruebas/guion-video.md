# Guion del video — automatización de pruebas (ISW)

Video del trabajo práctico de automatización de pruebas sobre la aplicación bancaria. Hay seis
partes, una por integrante. Cada parte dice qué tiene que verse en pantalla, el texto a leer y
los comandos. Duración aproximada: **5 minutos**.

## Reparto

| Integrante | Parte | Tiempo aprox. |
|---|---|---|
| Juan Cruz Bonadeo | 1. Presentación y sistema bajo prueba | 0:55 |
| Luis Parmigiani | 2. Pruebas por valores límite | 0:55 |
| Stéfano Conti | 3. Pruebas por tabla de decisión | 0:40 |
| Martín Redaelli | 4. Ejecución y cobertura | 0:45 |
| Agustín Dana | 5. Las pruebas detectan errores | 0:50 |
| Gonzalo Casermeiro | 6. Herramientas y cierre | 0:40 |

## Cómo grabarlo

- **Opción A (recomendada):** una videollamada (Meet o Discord) grabada. Una sola persona
  comparte la pantalla con VS Code y ejecuta todo lo que dice *En pantalla*; cada integrante
  habla en su parte.
- **Opción B:** cada uno graba su parte por separado con la pantalla de su compu y después se
  unen los clips. En ese caso cada uno necesita el proyecto andando en su máquina.

**Preparación de quien muestra la pantalla:**

- Abrir la carpeta `automatizacion-pruebas/` en VS Code. Fuente del editor y de la terminal en
  16–18, para que se lea en el video.
- Instalar las dependencias: `pip install -r requirements.txt`. Correr `pytest -q` una vez para
  confirmar que pasan las 60 pruebas.
- Borrar las cachés para que el árbol de archivos se vea limpio:
  `rm -rf .pytest_cache __pycache__ .coverage`.
- Activar el modo No molestar y cerrar las pestañas que no se usan.

---

## Parte 1 — Juan Cruz Bonadeo: presentación y sistema bajo prueba

*En pantalla:* el `README.md` en vista previa (`Cmd/Ctrl + Shift + V`). Después, `banco.py`:
el comentario de arriba, y bajar hasta `validar_banco` (línea 57) y `procesar_operacion`
(línea 114).

> Hola, este es nuestro trabajo práctico de automatización de pruebas de Ingeniería y Calidad de
> Software. Probamos el procedimiento de operaciones de la aplicación bancaria que ya habíamos
> usado en la tarea de valores límite. Lo implementamos en Python y automatizamos las pruebas con
> pytest, con dos técnicas de caja negra: valores límite y tabla de decisión.
>
> El sistema recibe cinco campos: código de banco, sucursal, cuenta, clave personal y orden. Cada
> campo tiene su regla. Por ejemplo, el código de banco puede ir en blanco o ser un número de tres
> dígitos con el primero mayor que uno. Los campos se validan en orden y se informa el primer
> error. Si todo es válido, según la orden se entrega el talonario, los movimientos o los dos.
>
> Luis nos muestra cómo armamos los casos por valores límite.

## Parte 2 — Luis Parmigiani: pruebas por valores límite

*En pantalla:* `test_valores_limite.py`. Mostrar el diccionario `VALIDOS`, la función `casos()`
y la lista `CODIGO_BANCO`.

> Son los 53 casos de la tarea anterior. En cada caso se varía un solo campo y el resto queda con
> un valor válido fijo, que es este diccionario. Los casos están cargados como datos: cada fila
> tiene número de caso, partición, entrada y salida esperada.
>
> Para el código del banco, el rango válido es de 200 a 999, así que probamos 200, 201, 998 y 999
> como válidos, y 199 y 1000 como inválidos. Con `parametrize`, pytest convierte cada fila en una
> prueba con su propio identificador, así que agregar un caso es agregar una fila.
>
> Stéfano sigue con la segunda técnica, la tabla de decisión.

## Parte 3 — Stéfano Conti: pruebas por tabla de decisión

*En pantalla:* primero la tabla de decisión del `README.md`; después `test_tabla_decision.py`.

> La tabla tiene dos condiciones, si los datos de acceso son válidos y qué orden se pide, y cinco
> reglas. Cada columna es un caso de prueba. En la regla 5 los datos son inválidos y la orden es
> indiferente, así que la probamos con tres órdenes distintas para mostrar que el resultado no
> cambia. En total son 7 casos.
>
> Martín los va a ejecutar.

## Parte 4 — Martín Redaelli: ejecución y cobertura

*En pantalla:* abrir la terminal integrada de VS Code y correr:

```bash
pytest -v
```

Cuando termine, subir un poco para que se vean los identificadores (`CP06-PI1-199`, `R4-…`).

> Corremos las 60 pruebas. Cada una aparece con el identificador de su caso, así que si una falla
> sabemos exactamente qué partición y qué valor la rompió. Pasan las 60.

```bash
pytest --cov=banco --cov-branch
```

> También medimos la cobertura con pytest-cov. Llegamos al 100 % de sentencias y de decisiones de
> `banco.py`: aunque diseñamos las pruebas como caja negra, recorren todo el código.
>
> Agustín va a mostrar que estas pruebas realmente encuentran errores.

## Parte 5 — Agustín Dana: las pruebas detectan errores

*En pantalla:* `banco.py`, línea 66. Cambiar `<= 1` por `< 1` y guardar.

```python
if len(valor) != 3 or int(valor[0]) <= 1:   # original
if len(valor) != 3 or int(valor[0]) < 1:    # con el error
```

> Para comprobar que las pruebas sirven, metemos a propósito un error típico de frontera:
> cambiamos "menor o igual" por "menor". Así, el sistema aceptaría un código de banco que empieza
> con 1.

```bash
pytest -q
```

Tiene que salir **1 failed, 59 passed**, con `CP06-PI1-199`.

> Falla exactamente el caso 6, la entrada 199, que es el valor límite inválido justo debajo del
> rango. Las otras 59 siguen pasando. Por eso conviene probar las fronteras.

Deshacer el cambio (`Cmd/Ctrl + Z`), guardar y correr `pytest -q` otra vez: **60 passed**.

> Gonzalo cierra con las herramientas que usamos.

## Parte 6 — Gonzalo Casermeiro: herramientas y cierre

*En pantalla:* la tabla de herramientas del `README.md` (o `tabla-herramientas.png`).

> Usamos Python 3.12 como lenguaje, pytest como framework de pruebas, pytest-cov para la
> cobertura, Visual Studio Code como entorno y Git para versionar los scripts junto con el código.
> Descartamos Selenium porque el sistema no tiene interfaz web, y JUnit porque exige Java y más
> código para la misma prueba parametrizada.
>
> Ese fue nuestro trabajo. Gracias.

---

## Chequeo antes de entregar

- [ ] Se leen el código y la salida de la terminal.
- [ ] Se ven las 60 pruebas pasadas, el 100 % de cobertura y la falla de CP06.
- [ ] `banco.py` quedó como estaba al final de la grabación.
