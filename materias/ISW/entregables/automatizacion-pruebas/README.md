# Automatización de pruebas — aplicación bancaria (ISW, parte práctica)

## 1. Script de automatización

**Software probado.** El procedimiento de operaciones de la *aplicación bancaria* del enunciado
que ya usamos en la tarea de casos de prueba por valores límite
(`../tarea-casos-prueba-valores-limite.md`). Se implementó en `banco.py`: recibe código del
banco, código de sucursal, número de cuenta, clave personal y orden; valida cada campo y devuelve
si la operación se acepta, el mensaje y los documentos a entregar.

| Archivo | Contenido |
|---|---|
| `banco.py` | Sistema bajo prueba |
| `test_valores_limite.py` | 53 casos por **valores límite** (CP01–CP53 de la tarea anterior), uno por partición o frontera |
| `test_tabla_decision.py` | 7 casos por **tabla de decisión** (reglas R1–R5) |

**Valores límite.** Cada caso se probó por campo: se varía un atributo y el resto queda con un
valor válido fijo. Por ejemplo, para el código del banco (rango 200–999) se prueban 200, 201,
998 y 999 (válidos) y 199 y 1000 (inválidos). Los casos están en una lista y el test se
parametriza con ella, así que agregar un caso es agregar una fila.

**Tabla de decisión.**

| | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| C1 Datos de acceso válidos | S | S | S | S | N |
| C2 Orden | En blanco | Talonario | Movimientos | Otro valor | – |
| A1 Entregar talonario | X | X | | | |
| A2 Entregar movimientos | X | | X | | |
| A3 Informar orden no reconocida | | | | X | |
| A4 Informar error del dato | | | | | X |

Cada columna es un caso de prueba. En R5 la orden es indiferente (–): se prueba con una orden
válida, una en blanco y una inválida para demostrar que el resultado no cambia.

**Ejecución.**

```bash
pip install -r requirements.txt
pytest -v                                    # corre las 60 pruebas
pytest --cov=banco --cov-branch              # además mide la cobertura
```

Resultado: **60 pruebas pasadas, 100 % de cobertura de sentencias y decisiones** sobre
`banco.py`. Como prueba de que los tests detectan errores, se introdujo a propósito un error
típico de frontera (`<= 1` cambiado por `< 1` en la validación del banco): el caso **CP06
(entrada 199)** falló y los otros 59 siguieron pasando.

## 2. Herramientas utilizadas

| Herramienta | Uso | Por qué |
|---|---|---|
| **Python 3.12** | Lenguaje del sistema y de las pruebas | Sintaxis simple y sin compilación; el foco queda en los casos de prueba, no en el lenguaje |
| **pytest** | Framework de pruebas | Gratuito y de código abierto. Las pruebas son funciones con `assert` simples; `@pytest.mark.parametrize` permite cargar las tablas de casos como datos (un caso por fila), que es exactamente como se diseñan los casos con valores límite y tablas de decisión. Informa cada caso por su identificador (CP06, R4…) |
| **pytest-cov** | Medición de cobertura | Mide la cobertura de sentencias y de decisiones (caja blanca) para saber qué parte del código ejercitaron las pruebas |
| **Visual Studio Code** (con la extensión de Python) | Entorno de desarrollo | Gratuito; detecta los tests de pytest y permite ejecutarlos y depurarlos desde el editor |
| **Git** | Control de versiones | Los scripts de prueba se versionan junto con el código, como pide la gestión de configuración |

Se descartó Selenium porque el sistema no tiene interfaz web: probar la lógica directamente
es más rápido y más estable. Se descartó JUnit porque requiere Java y más código repetitivo
para la misma prueba parametrizada.
