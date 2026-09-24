#!/usr/bin/env python3
"""Genera 04-resultados-corridas.xlsx desde cero, vacía de datos (T1.5).

Reconstruye las hojas `Corridas` y `Resumen` a partir del esquema canónico de
`cargar_corridas.py` (CAMPOS, columnas, semillas), para que planilla y cargador
nunca se desincronicen. Es reproducible: correrlo de nuevo regenera el mismo
archivo (salvo que se cambien los parámetros de la línea de comandos).

Cambios respecto de la planilla anterior (D4, T1.5):
- n de pares variable: la planilla se construye con `--max-pares` filas
  (semillas contiguas desde `--semilla-inicial`), no fijas en 30.
- El t crítico de la hoja Resumen se calcula con la fórmula
  `_xlfn.T.INV.2T(alfa, n-1)` (equivalente a T.INV.2T en Excel/LibreOffice),
  en función del n real cargado (COUNT) y de k (COUNTIF de "Primaria").
- Primarias (D4): P90 de espera, Proporción con espera mayor a 30 s y P90 de
  la cohorte pico, con alfa_s = alfa_global / k (Bonferroni, k=3 por COUNTIF).
  "Procesados con drenaje" y "Procesados a las 09:30" (throughput) pasan a
  controles de verificación (conservación; D≈0 esperado por diseño, ver plan
  §6.2), y el resto queda como secundarias con IC individual descriptivo.

Uso:
    python3 construir_planilla.py --salida 04-resultados-corridas.xlsx

Por defecto escribe sobre la planilla oficial (`--salida` opcional).
"""
from __future__ import annotations

import argparse
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

import cargar_corridas as cc

AQUI = Path(__file__).resolve().parent

# --- Parámetros de diseño (D4 y T1.5) ---------------------------------------
# MIN_PARES, OBJETIVO_PARES y SEMILLA_INICIAL viven en cargar_corridas.py (fuente única:
# la planilla y el cargador no se pueden desincronizar).
MIN_PARES = cc.MIN_PARES
OBJETIVO_PARES = cc.OBJETIVO_PARES
NIVEL_CONFIANZA_FAMILIAR = 0.95  # complemento de alfa global (Bonferroni) y de alfa individual

# Familia de cada campo (Primaria D4 / Secundaria descriptiva / Control de verificación)
# y criterio de decisión: "Menor" mejora si D<0, "Mayor" mejora si D>0, "Igual" se espera D=0.
FAMILIAS = {
    'Pasajeros generados':                 ('Control',    'Igual', 'pasajeros'),
    'Pasajeros desviados':                 ('Control',    'Igual', 'pasajeros'),
    'Procesados a las 09:30':              ('Control',    'Mayor', 'pasajeros'),
    'Procesados con drenaje':              ('Control',    'Mayor', 'pasajeros'),
    'Espera media':                        ('Secundaria', 'Menor', 's'),
    'P90 de espera':                       ('Primaria',   'Menor', 's'),
    'Proporción con espera mayor a 30 s':  ('Primaria',   'Menor', '%'),
    'Lq':                                  ('Secundaria', 'Menor', 'pasajeros'),
    'Cola máxima':                         ('Secundaria', 'Menor', 'pasajeros'),
    'Tiempo de disipación':                ('Secundaria', 'Menor', 's'),
    'Utilización media':                   ('Secundaria', 'Menor', '%'),
    'Dispersión de utilización':           ('Secundaria', 'Menor', '% (p.p.)'),
    'Pasajeros de la cohorte pico':        ('Secundaria', 'Igual', 'pasajeros'),
    'Espera media de la cohorte pico':     ('Secundaria', 'Menor', 's'),
    'P90 de la cohorte pico':              ('Primaria',   'Menor', 's'),
}
assert set(FAMILIAS) == set(cc.CAMPOS), 'FAMILIAS debe cubrir exactamente cc.CAMPOS'

AZUL_OSCURO = 'FF17365D'
AZUL_TAB = 'FF5B9BD5'
AZUL_CLARO = 'FFD9EAF7'
AMARILLO = 'FFFFF2CC'
GRIS = 'FFE7E6E6'
GRIS_TEXTO = 'FF1F1F1F'
GRIS_ITALICA = 'FF595959'
BLANCO = 'FFFFFFFF'

FUENTE = 'Arial'


def _fill(rgb: str) -> PatternFill:
    return PatternFill('solid', fgColor=rgb)


def _borde_fila() -> Border:
    delgado = Side(style='thin')
    return Border(bottom=delgado)


def construir_corridas(libro: openpyxl.Workbook, max_pares: int, semilla_inicial: int) -> None:
    ws = libro.create_sheet(cc.HOJA)
    ws.sheet_properties.tabColor = AZUL_TAB
    ultima_fila = cc.PRIMERA_FILA + max_pares - 1

    ws['A2'] = 'Corridas apareadas E0-E1'
    ws['A2'].font = Font(name=FUENTE, size=14, bold=True, color=AZUL_OSCURO)
    ws['A3'] = ('Cargar únicamente resultados de producción calibrados. '
                'Las columnas amarillas son entradas; las grises se calculan.')
    ws['A4'] = 'La misma fila debe usar la misma semilla y las mismas entradas aleatorias en E0 y E1.'
    ws['A5'] = ('Carga reproducible: python3 cargar_corridas.py corridas_peatonales.csv --escribir '
                '(valida pares, semillas y conservación antes de escribir).')
    ws['A6'] = (f'n de pares variable (T1.5): esta hoja admite hasta {max_pares} pares con semillas '
                f'contiguas desde {semilla_inicial}. El análisis (hoja Resumen) se habilita desde '
                f'n = {MIN_PARES} pares cargados.')
    for coord in ('A3', 'A4', 'A5', 'A6'):
        ws[coord].font = Font(name=FUENTE, size=10, italic=True, color=GRIS_ITALICA)

    ws.row_dimensions[7].height = 52
    ws.freeze_panes = 'C8'
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 14

    encabezado_fill = _fill(AZUL_OSCURO)
    encabezado_font = Font(name=FUENTE, size=10, bold=True, color=BLANCO)
    encabezado_align = Alignment(horizontal='center', vertical='center', wrap_text=True)

    ws.cell(cc.FILA_ENCABEZADO, 1, 'Réplica')
    ws.cell(cc.FILA_ENCABEZADO, cc.COLUMNA_SEMILLA, 'Semilla')
    for i, nombre in enumerate(cc.CAMPOS):
        c0, c1, cd = cc.columnas(i)
        ws.cell(cc.FILA_ENCABEZADO, c0, f'E0 {nombre}')
        ws.cell(cc.FILA_ENCABEZADO, c1, f'E1 {nombre}')
        ws.cell(cc.FILA_ENCABEZADO, cd, f'Diferencia {nombre}')
        ancho = get_column_letter(c0)
        ws.column_dimensions[ancho].width = 16
        ws.column_dimensions[get_column_letter(c1)].width = 16
        ws.column_dimensions[get_column_letter(cd)].width = 16
    ultima_columna = 3 + 3 * len(cc.CAMPOS) - 1
    for col in range(1, ultima_columna + 1):
        c = ws.cell(cc.FILA_ENCABEZADO, col)
        c.fill = encabezado_fill
        c.font = encabezado_font
        c.alignment = encabezado_align

    borde = _borde_fila()
    for fila in range(cc.PRIMERA_FILA, ultima_fila + 1):
        replica = fila - cc.PRIMERA_FILA + 1
        semilla = semilla_inicial + replica - 1
        c_a = ws.cell(fila, 1, replica)
        c_a.number_format = '0'
        c_a.fill = _fill(AZUL_CLARO)
        c_a.border = borde
        c_a.alignment = Alignment(vertical='center')
        c_b = ws.cell(fila, cc.COLUMNA_SEMILLA, semilla)
        c_b.number_format = '0'
        c_b.fill = _fill(AZUL_CLARO)
        c_b.border = borde
        for i in range(len(cc.CAMPOS)):
            c0, c1, cd = cc.columnas(i)
            numfmt = '0.0%' if i in cc.FRACCIONES or i == 11 else '#,##0.00'
            for col, fill_rgb in ((c0, AMARILLO), (c1, AMARILLO)):
                cell = ws.cell(fila, col)
                cell.number_format = numfmt
                cell.fill = _fill(fill_rgb)
                cell.border = borde
            l0, l1, ld = get_column_letter(c0), get_column_letter(c1), get_column_letter(cd)
            cell_d = ws.cell(fila, cd, f'=IF(OR({l0}{fila}="",{l1}{fila}=""),"",{l1}{fila}-{l0}{fila})')
            cell_d.number_format = numfmt
            cell_d.fill = _fill(GRIS)
            cell_d.border = borde


def construir_resumen(libro: openpyxl.Workbook, max_pares: int) -> None:
    ws = libro.create_sheet(cc.HOJA_RESUMEN, 0)  # Resumen va primero, como en la planilla anterior
    ws.sheet_properties.tabColor = AZUL_OSCURO
    ultima_fila_corridas = cc.PRIMERA_FILA + max_pares - 1

    ws['A2'] = 'Comparación apareada E0-E1'
    ws['A2'].font = Font(name=FUENTE, size=14, bold=True, color=AZUL_OSCURO)
    ws['A3'] = ('Cada diferencia se calcula como E1 menos E0. Un valor negativo mejora las medidas '
                'cuyo criterio es Menor.')
    ws['A3'].font = Font(name=FUENTE, size=10, italic=True, color=GRIS_ITALICA)

    filas_primarias = [11 + i for i, nombre in enumerate(cc.CAMPOS) if FAMILIAS[nombre][0] == 'Primaria']
    ref_e = ','.join(f'E{f}' for f in filas_primarias)

    ws['A5'] = 'Estado'
    ws['B5'] = (f'=IF(MIN({ref_e})=0,"Sin corridas cargadas",'
                f'IF(MIN({ref_e})<{MIN_PARES},"Corridas incompletas","Listo para análisis"))')
    ws['D5'] = (f'El intervalo se habilita al completar como mínimo n = {MIN_PARES} pares '
                f'(n0 del procedimiento secuencial, §7.3 del plan). El diseño de referencia sigue '
                f'siendo n = {OBJETIVO_PARES}, pero ya no es un mínimo fijo: t crítico se recalcula '
                f'con T.INV.2T según el n real.')

    ws['A6'] = 'Nivel de confianza familiar'
    ws['B6'] = NIVEL_CONFIANZA_FAMILIAR
    ws['D6'] = ('t crítico calculado con T.INV.2T(alfa, n-1): alfa_s = alfa/k (Bonferroni, k = '
                'comparaciones primarias) para las tres primarias, y 1 - nivel de confianza (individual, '
                'descriptivo) para las secundarias y los controles de verificación.')

    ws['A7'] = 'Comparaciones primarias'
    ws['B7'] = '=COUNTIF(B11:B{0},"Primaria")'.format(10 + len(cc.CAMPOS))
    ws['A8'] = 'Alfa por comparación primaria'
    ws['B8'] = '=(1-B6)/B7'

    ws['A9'] = ('Primarias (D4, alfa_s = alfa/k, IC Bonferroni): P90 de espera, proporción con espera > 30 s '
                'y P90 de la cohorte pico 08:15-08:45. Controles de verificación (conservación, D≈0 esperado; '
                'no forman parte de la familia Bonferroni): pasajeros generados/desviados, procesados a las '
                '09:30 (throughput) y procesados con drenaje. El resto son secundarias, IC individual 95% '
                'descriptivo.')
    ws['A9'].font = Font(name=FUENTE, size=10, italic=True, color=GRIS_ITALICA)

    for coord in ('A5', 'A6', 'A7', 'A8'):
        ws[coord].font = Font(name=FUENTE, size=10, bold=True, color=GRIS_TEXTO)
        ws[coord].fill = _fill(AZUL_CLARO)
    for coord in ('B5', 'B6', 'B7', 'B8'):
        ws[coord].font = Font(name=FUENTE, size=10, bold=True, color=GRIS_TEXTO)
        ws[coord].fill = _fill(AMARILLO)

    encabezados = ['Medida', 'Familia', 'Criterio', 'Unidad', 'n pares', 'Media E0', 'Media E1',
                   'Diferencia media', 'Desvío de diferencias', 'Error estándar', 't crítico',
                   'IC inferior', 'IC superior', 'Conclusión']
    fila_encabezado = 10
    for j, texto in enumerate(encabezados):
        c = ws.cell(fila_encabezado, 1 + j, texto)
        c.fill = _fill(AZUL_OSCURO)
        c.font = Font(name=FUENTE, size=10, bold=True, color=BLANCO)
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    ws.row_dimensions[fila_encabezado].height = 40

    anchos = [35, 14, 12, 11, 10, 13, 13, 15, 17, 14, 10, 12, 12, 28]
    for j, ancho in enumerate(anchos):
        ws.column_dimensions[get_column_letter(1 + j)].width = ancho

    for i, nombre in enumerate(cc.CAMPOS):
        fila = fila_encabezado + 1 + i
        familia, criterio, unidad = FAMILIAS[nombre]
        c0, c1, cd = cc.columnas(i)
        l0, l1, ld = get_column_letter(c0), get_column_letter(c1), get_column_letter(cd)
        rango = lambda letra: f'Corridas!${letra}$8:${letra}${ultima_fila_corridas}'

        ws.cell(fila, 1, nombre)
        ws.cell(fila, 2, familia)
        ws.cell(fila, 3, criterio)
        ws.cell(fila, 4, unidad)
        ws.cell(fila, 5, f'=COUNT({rango(ld)})')
        ws.cell(fila, 6, f'=IF(E{fila}=0,"",AVERAGE({rango(l0)}))')
        ws.cell(fila, 7, f'=IF(E{fila}=0,"",AVERAGE({rango(l1)}))')
        ws.cell(fila, 8, f'=IF(E{fila}=0,"",AVERAGE({rango(ld)}))')
        ws.cell(fila, 9, f'=IF(E{fila}<2,"",_xlfn.STDEV.S({rango(ld)}))')
        ws.cell(fila, 10, f'=IF(E{fila}<2,"",I{fila}/SQRT(E{fila}))')
        ws.cell(fila, 11,
                f'=IF(E{fila}<{MIN_PARES},"",_xlfn.T.INV.2T(IF(B{fila}="Primaria",$B$8,1-$B$6),E{fila}-1))')
        ws.cell(fila, 12, f'=IF(E{fila}<{MIN_PARES},"",H{fila}-K{fila}*J{fila})')
        ws.cell(fila, 13, f'=IF(E{fila}<{MIN_PARES},"",H{fila}+K{fila}*J{fila})')
        ws.cell(fila, 14,
                f'=IF(E{fila}<{MIN_PARES},"Pendiente",'
                f'IF(C{fila}="Igual",IF(AND(L{fila}<=0,M{fila}>=0),"Compatible con igualdad","Diferencia detectada"),'
                f'IF(C{fila}="Mayor",IF(L{fila}>0,"Mejora concluyente",IF(M{fila}<0,"Empeora concluyentemente","Sin evidencia suficiente")),'
                f'IF(M{fila}<0,"Mejora concluyente",IF(L{fila}>0,"Empeora concluyentemente","Sin evidencia suficiente")))))')
        for col in range(1, 15):
            ws.cell(fila, col).font = Font(name=FUENTE, size=10, color=GRIS_TEXTO)
        for col in (10, 11, 12, 13):
            ws.cell(fila, col).number_format = '#,##0.00'

    ultima_fila_tabla = fila_encabezado + len(cc.CAMPOS)
    ws.conditional_formatting.add(
        f'B11:B{ultima_fila_tabla}',
        CellIsRule(operator='equal', formula=['"Primaria"'], stopIfTrue=False,
                   font=Font(bold=True, color='FF274E13'), fill=_fill('FFD9EAD3')))
    ws.conditional_formatting.add(
        f'N11:N{ultima_fila_tabla}',
        CellIsRule(operator='equal', formula=['"Pendiente"'], stopIfTrue=False,
                   font=Font(bold=True, color='FF7F6000'), fill=_fill(AMARILLO)))


def construir(max_pares: int, semilla_inicial: int, salida: Path) -> None:
    libro = openpyxl.Workbook()
    libro.remove(libro.active)
    construir_corridas(libro, max_pares, semilla_inicial)
    construir_resumen(libro, max_pares)
    libro.active = libro.sheetnames.index(cc.HOJA_RESUMEN)
    libro.save(salida)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--max-pares', type=int, default=60,
                     help='cantidad máxima de pares que admite la hoja Corridas (default: 60)')
    ap.add_argument('--semilla-inicial', type=int, default=cc.SEMILLA_INICIAL,
                     help='primera semilla contigua (default: la del cargador, cc.SEMILLA_INICIAL)')
    ap.add_argument('--salida', type=Path, default=cc.PLANILLA_OFICIAL)
    args = ap.parse_args(argv)
    if args.max_pares < MIN_PARES:
        ap.error(f'--max-pares debe ser >= {MIN_PARES} (mínimo del diseño, D4/§7.3)')
    construir(args.max_pares, args.semilla_inicial, args.salida)
    print(f'OK: {args.salida} reconstruida con capacidad para {args.max_pares} pares '
          f'(semillas {args.semilla_inicial}..{args.semilla_inicial + args.max_pares - 1}), vacía de datos.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
