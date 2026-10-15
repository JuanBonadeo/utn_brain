"""Pruebas por tabla de decisión: qué documentos se entregan según los datos y la orden.

Condiciones
  C1  Datos de acceso válidos (banco, sucursal, cuenta y clave)
  C2  Valor de la orden
Acciones
  A1  Entregar talonario de cheques
  A2  Entregar movimientos del mes
  A3  Informar orden no reconocida
  A4  Informar el error del dato inválido

                         R1      R2         R3           R4      R5
  C1 Datos válidos       S       S          S            S       N
  C2 Orden               blanco  Talonario  Movimientos  otro    -
  ---------------------------------------------------------------------
  A1 Talonario           X       X
  A2 Movimientos         X                  X
  A3 Error de orden                                      X
  A4 Error de dato                                               X

Cada columna (regla) es un caso de prueba. En R5 el "-" significa que la orden
es indiferente: se prueba con una orden válida, una en blanco y una inválida
para demostrar que el resultado no cambia.
"""

import pytest

from banco import MSG_ORDEN, MSG_SUCURSAL, MOVIMIENTOS, TALONARIO, procesar_operacion

DATOS_VALIDOS = dict(banco="250", sucursal="1234", cuenta="12345", clave="A1b2C")
DATOS_INVALIDOS = dict(DATOS_VALIDOS, sucursal="0999")  # sucursal con primer dígito 0

TABLA_DE_DECISION = [
    # regla, datos,          orden,         aceptada, documentos,              mensaje de error
    ("R1", DATOS_VALIDOS,   "",            True,  [TALONARIO, MOVIMIENTOS], None),
    ("R2", DATOS_VALIDOS,   "Talonario",   True,  [TALONARIO],              None),
    ("R3", DATOS_VALIDOS,   "Movimientos", True,  [MOVIMIENTOS],            None),
    ("R4", DATOS_VALIDOS,   "Prestamo",    False, [],                       MSG_ORDEN),
    ("R5", DATOS_INVALIDOS, "Talonario",   False, [],                       MSG_SUCURSAL),
    ("R5", DATOS_INVALIDOS, "",            False, [],                       MSG_SUCURSAL),
    ("R5", DATOS_INVALIDOS, "Prestamo",    False, [],                       MSG_SUCURSAL),
]


@pytest.mark.parametrize(
    "datos, orden, aceptada, documentos, mensaje",
    [pytest.param(*fila[1:], id=f"{fila[0]}-orden={fila[2] or 'blanco'}") for fila in TABLA_DE_DECISION],
)
def test_tabla_de_decision(datos, orden, aceptada, documentos, mensaje):
    resultado = procesar_operacion(**datos, orden=orden)

    assert resultado.aceptada is aceptada
    assert resultado.documentos == documentos
    if mensaje:
        assert resultado.mensaje == mensaje
