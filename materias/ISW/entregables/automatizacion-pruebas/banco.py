"""Sistema bajo prueba: procedimiento de operaciones de la aplicación bancaria.

Implementa el enunciado de la tarea de valores límite de ISW:

- Código del banco: en blanco o número de 3 dígitos, el primero mayor que 1.
- Código de sucursal: número de 4 dígitos, el primero mayor que 0.
- Número de cuenta: número de 5 dígitos.
- Clave personal: valor alfanumérico de 5 posiciones.
- Orden: en blanco, "Talonario" o "Movimientos".
  "Talonario" entrega un talonario de cheques, "Movimientos" entrega los
  movimientos del mes en curso y en blanco entrega los dos documentos.

Los campos se validan en el orden del formulario y se informa el primer error.
"""

from dataclasses import dataclass, field

TALONARIO = "Talonario de cheques"
MOVIMIENTOS = "Movimientos del mes en curso"

MSG_BANCO = "El código del banco debe ser de 3 dígitos y el primero mayor que 1"
MSG_SUCURSAL = "El código de sucursal debe ser de 4 dígitos y el primero mayor que 0"
MSG_SUCURSAL_OBLIGATORIA = "El código de sucursal es obligatorio"
MSG_CUENTA = "El número de cuenta debe tener 5 dígitos"
MSG_CUENTA_OBLIGATORIA = "El número de cuenta es obligatorio"
MSG_CLAVE = "La clave personal debe tener 5 posiciones alfanuméricas"
MSG_CLAVE_OBLIGATORIA = "La clave personal es obligatoria"
MSG_CLAVE_CARACTERES = "La clave personal admite solo letras y números"
MSG_ORDEN = "Orden no reconocida. Valores admitidos: Talonario, Movimientos o en blanco"
MSG_SOLO_NUMEROS = "Ingrese únicamente números"
MSG_ENTERO = "Ingrese un número entero"


@dataclass
class Resultado:
    aceptada: bool
    mensaje: str = ""
    documentos: list = field(default_factory=list)


def _es_negativo(valor: str) -> bool:
    return valor.startswith(("-", "−")) and valor[1:].isdigit()


def _es_decimal(valor: str) -> bool:
    for sep in (",", "."):
        partes = valor.split(sep)
        if len(partes) == 2 and all(p.isdigit() for p in partes):
            return True
    return False


def _solo_digitos(valor: str) -> bool:
    return valor.isascii() and valor.isdigit()


def validar_banco(valor: str):
    if valor == "":
        return None  # en blanco es válido
    if _es_negativo(valor):
        return MSG_BANCO
    if _es_decimal(valor):
        return MSG_ENTERO
    if not _solo_digitos(valor):
        return MSG_SOLO_NUMEROS
    if len(valor) != 3 or int(valor[0]) <= 1:
        return MSG_BANCO
    return None


def validar_sucursal(valor: str):
    if valor == "":
        return MSG_SUCURSAL_OBLIGATORIA
    if _es_negativo(valor):
        return MSG_SUCURSAL
    if not _solo_digitos(valor):
        return MSG_SOLO_NUMEROS
    if len(valor) != 4 or valor[0] == "0":
        return MSG_SUCURSAL
    return None


def validar_cuenta(valor: str):
    if valor == "":
        return MSG_CUENTA_OBLIGATORIA
    if not _solo_digitos(valor):
        return MSG_SOLO_NUMEROS
    if len(valor) != 5:
        return MSG_CUENTA
    return None


def validar_clave(valor: str):
    if valor == "":
        return MSG_CLAVE_OBLIGATORIA
    if len(valor) != 5:
        return MSG_CLAVE
    if not (valor.isascii() and valor.isalnum()):
        return MSG_CLAVE_CARACTERES
    return None


def documentos_de_la_orden(orden: str):
    """Devuelve los documentos a entregar, o None si la orden no es válida."""
    if orden == "":
        return [TALONARIO, MOVIMIENTOS]
    if orden == "Talonario":
        return [TALONARIO]
    if orden == "Movimientos":
        return [MOVIMIENTOS]
    return None


def procesar_operacion(banco: str, sucursal: str, cuenta: str, clave: str, orden: str) -> Resultado:
    for validar, valor in (
        (validar_banco, banco),
        (validar_sucursal, sucursal),
        (validar_cuenta, cuenta),
        (validar_clave, clave),
    ):
        error = validar(valor)
        if error:
            return Resultado(aceptada=False, mensaje=error)

    documentos = documentos_de_la_orden(orden)
    if documentos is None:
        return Resultado(aceptada=False, mensaje=MSG_ORDEN)
    return Resultado(aceptada=True, mensaje="Operación aceptada, se procesa la orden", documentos=documentos)
