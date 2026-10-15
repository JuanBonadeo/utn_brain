"""Pruebas por valores límite (casos 1 a 53 de la tarea de valores límite).

Formato "por campo": en cada caso se varía un solo atributo y el resto queda
con un valor válido fijo. Cada tupla es (caso, partición, entrada, salida esperada).
"""

import pytest

from banco import (
    MSG_BANCO, MSG_CLAVE, MSG_CLAVE_CARACTERES, MSG_CLAVE_OBLIGATORIA, MSG_CUENTA,
    MSG_CUENTA_OBLIGATORIA, MSG_ENTERO, MSG_ORDEN, MSG_SOLO_NUMEROS, MSG_SUCURSAL,
    MSG_SUCURSAL_OBLIGATORIA, MOVIMIENTOS, TALONARIO, procesar_operacion,
)

OK = "aceptada"

# Valores válidos fijos para los campos que no se están probando.
VALIDOS = dict(banco="250", sucursal="1234", cuenta="12345", clave="A1b2C", orden="Talonario")


def ejecutar(**cambio):
    return procesar_operacion(**{**VALIDOS, **cambio})


def verificar(resultado, esperado):
    if esperado == OK:
        assert resultado.aceptada, resultado.mensaje
    else:
        assert not resultado.aceptada
        assert resultado.mensaje == esperado


def casos(lista):
    """Arma los parámetros con un id legible: 'CP06-PI1-199'."""
    return [pytest.param(e, s, id=f"CP{c:02d}-{p}-{e or 'blanco'}") for c, p, e, s in lista]


CODIGO_BANCO = [
    (1, "PV1", "", OK),
    (2, "PV2", "200", OK),
    (3, "PV2", "201", OK),
    (4, "PV2", "998", OK),
    (5, "PV2", "999", OK),
    (6, "PI1", "199", MSG_BANCO),
    (7, "PI1", "000", MSG_BANCO),
    (8, "PI2", "99", MSG_BANCO),
    (9, "PI3", "1000", MSG_BANCO),
    (10, "PI4", "-200", MSG_BANCO),
    (11, "PI5", "A25", MSG_SOLO_NUMEROS),
    (12, "PI6", "2#5", MSG_SOLO_NUMEROS),
    (13, "PI7", "250,5", MSG_ENTERO),
]

CODIGO_SUCURSAL = [
    (14, "PV1", "1000", OK),
    (15, "PV1", "1001", OK),
    (16, "PV1", "9998", OK),
    (17, "PV1", "9999", OK),
    (18, "PI1", "0999", MSG_SUCURSAL),
    (19, "PI1", "0000", MSG_SUCURSAL),
    (20, "PI2", "999", MSG_SUCURSAL),
    (21, "PI3", "10000", MSG_SUCURSAL),
    (22, "PI4", "", MSG_SUCURSAL_OBLIGATORIA),
    (23, "PI5", "-1000", MSG_SUCURSAL),
    (24, "PI6", "1B34", MSG_SOLO_NUMEROS),
    (25, "PI7", "12#4", MSG_SOLO_NUMEROS),
]

NUMERO_CUENTA = [
    (26, "PV1", "00000", OK),
    (27, "PV1", "00001", OK),
    (28, "PV1", "99998", OK),
    (29, "PV1", "99999", OK),
    (30, "PI1", "1234", MSG_CUENTA),
    (31, "PI2", "123456", MSG_CUENTA),
    (32, "PI3", "", MSG_CUENTA_OBLIGATORIA),
    (33, "PI4", "1234A", MSG_SOLO_NUMEROS),
    (34, "PI4", "1234#", MSG_SOLO_NUMEROS),
    (35, "PI5", "-1234", MSG_SOLO_NUMEROS),
]

CLAVE_PERSONAL = [
    (36, "PV1", "A1b2C", OK),
    (37, "PV1", "00000", OK),
    (38, "PV1", "aaaaa", OK),
    (39, "PV1", "ZZZZZ", OK),
    (40, "PI1", "A1b2", MSG_CLAVE),
    (41, "PI2", "A1b2C3", MSG_CLAVE),
    (42, "PI3", "", MSG_CLAVE_OBLIGATORIA),
    (43, "PI4", "A1b2#", MSG_CLAVE_CARACTERES),
    (44, "PI4", "A1 2C", MSG_CLAVE_CARACTERES),
    (45, "PI4", "A1b2é", MSG_CLAVE_CARACTERES),
]

ORDEN_INVALIDA = [
    (49, "PI2", "talonario", MSG_ORDEN),
    (50, "PI3", "Talonarios", MSG_ORDEN),
    (51, "PI3", "Movimiento", MSG_ORDEN),
    (52, "PI4", "Talonario ", MSG_ORDEN),
    (53, "PI1", "Transferencia", MSG_ORDEN),
]


@pytest.mark.parametrize("entrada, esperado", casos(CODIGO_BANCO))
def test_codigo_banco(entrada, esperado):
    verificar(ejecutar(banco=entrada), esperado)


@pytest.mark.parametrize("entrada, esperado", casos(CODIGO_SUCURSAL))
def test_codigo_sucursal(entrada, esperado):
    verificar(ejecutar(sucursal=entrada), esperado)


@pytest.mark.parametrize("entrada, esperado", casos(NUMERO_CUENTA))
def test_numero_cuenta(entrada, esperado):
    verificar(ejecutar(cuenta=entrada), esperado)


@pytest.mark.parametrize("entrada, esperado", casos(CLAVE_PERSONAL))
def test_clave_personal(entrada, esperado):
    verificar(ejecutar(clave=entrada), esperado)


@pytest.mark.parametrize("entrada, documentos", [
    pytest.param("Talonario", [TALONARIO], id="CP46-PV1-Talonario"),
    pytest.param("Movimientos", [MOVIMIENTOS], id="CP47-PV2-Movimientos"),
    pytest.param("", [TALONARIO, MOVIMIENTOS], id="CP48-PV3-blanco"),
])
def test_orden_valida(entrada, documentos):
    resultado = ejecutar(orden=entrada)
    assert resultado.aceptada
    assert resultado.documentos == documentos


@pytest.mark.parametrize("entrada, esperado", casos(ORDEN_INVALIDA))
def test_orden_invalida(entrada, esperado):
    verificar(ejecutar(orden=entrada), esperado)
