# Guion del video — automatización de pruebas (ISW, parte práctica)

Duración objetivo: **4 a 5 minutos**. Una sola toma de pantalla (VS Code + terminal integrada),
con voz en off. Cada bloque indica qué mostrar y qué decir.

## Antes de grabar

- Abrir la carpeta `automatizacion-pruebas/` en VS Code. Fuente del editor y de la terminal en
  16–18 para que se lea en el video.
- Activar el entorno: `source ../../../../.venv/bin/activate` (o `pip install -r requirements.txt`
  en un venv nuevo). Probar una vez `pytest -q` para asegurarse de que corre.
- Borrar cachés para que el árbol se vea limpio: `rm -rf .pytest_cache __pycache__ .coverage`.
- Cerrar notificaciones (No molestar) y pestañas que no se usan.
- Grabar con `Cmd + Shift + 5` → "Grabar toda la pantalla" (o una porción), con micrófono activado
  en *Opciones*.

## 1. Presentación — 0:00 a 0:30

**Pantalla:** el `README.md` en vista previa (`Cmd + Shift + V`).

> Este es el trabajo práctico de automatización de pruebas de Ingeniería y Calidad de Software.
> Probamos el procedimiento de operaciones de la aplicación bancaria que ya habíamos usado en la
> tarea de valores límite. Lo implementamos en Python y automatizamos las pruebas con pytest,
> usando dos técnicas de caja negra: valores límite y tabla de decisión.

## 2. El sistema bajo prueba — 0:30 a 1:15

**Pantalla:** `banco.py`. Mostrar el docstring de arriba y después bajar hasta `validar_banco`
(línea 57) y `procesar_operacion`.

> El sistema recibe cinco campos: código de banco, sucursal, cuenta, clave personal y orden.
> Cada campo tiene su regla: por ejemplo, el código de banco puede ir en blanco o ser un número de
> tres dígitos con el primero mayor que uno. Los campos se validan en orden y se informa el
> primer error. Si todo es válido, según la orden se entrega el talonario, los movimientos o ambos.

## 3. Pruebas por valores límite — 1:15 a 2:15

**Pantalla:** `test_valores_limite.py`. Mostrar `VALIDOS`, la función `casos()` y la lista
`CODIGO_BANCO`.

> Son los 53 casos de la tarea anterior. Cada caso varía un solo campo y deja el resto con un
> valor válido fijo, que es este diccionario. Los casos están cargados como datos: cada tupla es
> número de caso, partición, entrada y salida esperada. Para el código del banco, el rango válido
> es 200 a 999, así que probamos 200, 201, 998 y 999 como válidos, y 199 y 1000 como inválidos.
> Con `parametrize`, pytest convierte cada fila en una prueba con su propio identificador, así que
> agregar un caso es agregar una fila.

## 4. Pruebas por tabla de decisión — 2:15 a 2:50

**Pantalla:** primero la tabla del `README.md`, después `test_tabla_decision.py`.

> La segunda técnica es una tabla de decisión con dos condiciones —si los datos de acceso son
> válidos y qué orden se pide— y cinco reglas. Cada columna es un caso de prueba. En la regla 5
> la orden es indiferente, así que la probamos con tres órdenes distintas para demostrar que el
> resultado no cambia. En total son 7 casos.

## 5. Ejecución — 2:50 a 3:30

**Pantalla:** terminal integrada (`Ctrl + ñ` o *Terminal → New Terminal*).

```bash
pytest -v
```

Dejar que termine y subir un poco para mostrar los identificadores (`CP06-PI1-199`, `R4-…`).

> Corremos las 60 pruebas. Cada una aparece con el identificador del caso, así que si una falla
> sabemos exactamente qué partición y qué valor la rompió. Pasan las 60.

```bash
pytest --cov=banco --cov-branch
```

> Además medimos la cobertura con pytest-cov: tenemos el 100 % de sentencias y de decisiones de
> `banco.py`, o sea que las pruebas de caja negra también recorren todo el código.

## 6. Las pruebas detectan errores — 3:30 a 4:20

**Pantalla:** `banco.py`, línea 66. Cambiar `<= 1` por `< 1` y guardar.

```python
if len(valor) != 3 or int(valor[0]) <= 1:   # original
if len(valor) != 3 or int(valor[0]) < 1:    # con el error
```

> Para comprobar que las pruebas sirven, metemos a propósito un error típico de frontera:
> cambiamos "menor o igual" por "menor". Ahora el sistema aceptaría un código de banco que
> empieza con 1.

```bash
pytest -q
```

Debe salir **1 failed, 59 passed** con `CP06-PI1-199`.

> Falla exactamente el caso 6, la entrada 199, que es el valor límite inválido justo debajo del
> rango. Las otras 59 siguen pasando. Esto es lo que justifica probar las fronteras.

Deshacer el cambio (`Cmd + Z`, guardar) y correr `pytest -q` otra vez: **60 passed**.

## 7. Herramientas y cierre — 4:20 a 4:50

**Pantalla:** tabla de herramientas del `README.md` (o `tabla-herramientas.png`).

> Usamos Python 3.12, pytest como framework, pytest-cov para la cobertura, VS Code como entorno
> y Git para versionar los scripts junto con el código. Descartamos Selenium porque el sistema no
> tiene interfaz web, y JUnit porque exige Java y más código para la misma prueba parametrizada.
> Gracias.

## Chequeo final

- [ ] Se lee el código y la salida de la terminal.
- [ ] Se ven las 60 pasadas, el 100 % de cobertura y el fallo de CP06.
- [ ] `banco.py` quedó como estaba (`git diff banco.py` vacío).
