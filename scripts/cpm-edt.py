# -*- coding: utf-8 -*-
"""CPM y aplanamiento de recursos sobre la EDT de la Etapa 3 del TPI de ASI.

De acá salen TODOS los números de planificación del punto 10 del entregable
(`materias/ASI/entregables/etapa3.md`). Si se toca una duración, una
dependencia o un perfil, hay que volver a correrlo y actualizar el documento:
los números del punto 10 alimentan además el punto 5 (cantidad de personas por
perfil) y el punto 11 (horas por perfil).

    .venv/Scripts/python.exe scripts/cpm-edt.py          # informe completo
    .venv/Scripts/python.exe scripts/cpm-edt.py --json   # vuelca cpm.json

Qué calcula:
  1. Pasada adelante y atrás: ES, EF, LS, LF y holgura total de cada actividad.
  2. Camino crítico y duración teórica a fechas tempranas.
  3. Histograma de recursos y detección de sobreasignación, suponiendo que
     cada actividad consume una unidad de cada perfil que tiene asignado.
  4. Aplanamiento por método serial, con capacidad configurable por perfil.
  5. Búsqueda del refuerzo mínimo: qué perfiles conviene duplicar y cuánto
     ahorra cada combinación.

Resultados vigentes al 2026-08-23, con la EDT de abajo:
    duración teórica ....................... 187 días hábiles
    aplanada con 1 persona por perfil ...... 215 días  (+28)
    aplanada con +1 EI y +1 QA ............. 192 días  <- la adoptada
    aplanada sumando además +1 RO .......... 189 días  (no justifica la persona)
"""
import itertools
import json
import sys
from collections import defaultdict

JORNADA = 8       # horas por día
MES = 21          # días hábiles por mes

# ---------------------------------------------------------------------------
# EDT. id: (nombre, [predecesoras], duración en días hábiles, [perfiles])
#
# Perfiles: JP jefe de proyecto · AF analista funcional · EI especialista de
# integraciones · ES especialista de seguridad · CP consultor de la plataforma
# (lo aporta el proveedor) · UX diseño de experiencia de uso · QA responsable de
# pruebas · CA capacitador · RO referente de operaciones.
# ---------------------------------------------------------------------------
EDT = {
    '1.1':  ('Elaborar el Acta de Proyecto',                       [],                    3,  ['JP']),
    '1.2':  ('Conformar el equipo y asignar dedicaciones',         ['1.1'],               2,  ['JP']),
    '1.3':  ('Realizar la reunión de arranque',                    ['1.2'],               1,  ['JP']),
    '2.1':  ('Relevar el proceso actual',                          ['1.3'],               8,  ['AF', 'RO']),
    '2.2':  ('Especificar requerimientos funcionales',             ['2.1'],              10,  ['AF']),
    '2.3':  ('Especificar requerimientos de integración',          ['2.1'],               6,  ['EI']),
    '2.4':  ('Medir las líneas base O1-O4',                        ['2.1'],              15,  ['AF', 'RO']),
    '2.5':  ('Especificar requerimientos de seguridad',            ['2.1'],               5,  ['ES']),
    '2.6':  ('Validar requerimientos con usuarios clave',          ['2.2', '2.3', '2.5'], 3,  ['AF', 'RO']),
    '3.1':  ('Elaborar y emitir el RFI',                           ['2.6'],               5,  ['JP', 'AF']),
    '3.2':  ('Analizar respuestas y conformar la lista corta',     ['3.1'],               5,  ['JP', 'AF']),
    '3.3':  ('Elaborar y emitir el RFP',                           ['3.2'],               7,  ['JP', 'AF', 'ES']),
    '3.4':  ('Evaluar propuestas',                                 ['3.3'],               8,  ['JP', 'AF', 'EI', 'ES']),
    '3.5':  ('Negociar y firmar el contrato',                      ['3.4'],               6,  ['JP']),
    '4.1':  ('Configurar flujos, estados y roles',                 ['3.5'],              10,  ['CP', 'AF']),
    '4.2':  ('Parametrizar matriz impacto/urgencia y SLA',         ['4.1'],               6,  ['CP', 'AF']),
    '4.3':  ('Configurar el motor de asignación',                  ['4.2'],               8,  ['CP', 'AF']),
    '4.4':  ('Relevar y cargar la matriz de competencias',         ['3.5'],               7,  ['RO']),
    '4.5':  ('Diseñar y validar la experiencia de uso',            ['3.5'],               8,  ['UX']),
    '4.6':  ('Configurar la aplicación de campo',                  ['4.3', '4.5'],        8,  ['CP', 'UX']),
    '4.7':  ('Configurar los tableros de indicadores',             ['4.2'],               4,  ['CP']),
    '5.1':  ('Integrar con el SGOT',                               ['4.1'],              10,  ['EI']),
    '5.2':  ('Integrar con el CRM',                                ['5.1'],               8,  ['EI']),
    '5.3':  ('Integrar con la base de datos',                      ['5.2'],               6,  ['EI']),
    '5.4':  ('Integrar con el NMS',                                ['5.3'],               5,  ['EI']),
    '5.5':  ('Implementar SSO y doble factor',                     ['3.5'],               6,  ['ES']),
    '5.6':  ('Implementar mínimo privilegio y baja automática',    ['5.5'],               8,  ['ES', 'EI']),
    '6.1':  ('Migrar órdenes de trabajo abiertas',                 ['5.3'],               4,  ['EI']),
    '6.2':  ('Cargar padrón de técnicos y datos maestros',         ['4.4'],               3,  ['RO']),
    '7.1':  ('Diseñar plan y casos de prueba',                     ['2.6'],               6,  ['QA']),
    '7.2':  ('Ejecutar pruebas funcionales',                       ['4.6', '4.7', '7.1'], 8,  ['QA', 'AF']),
    '7.3':  ('Ejecutar pruebas de integración',                    ['5.4', '6.1', '7.1'], 6,  ['QA', 'EI']),
    '7.4':  ('Ejecutar pruebas de carga',                          ['7.3'],               4,  ['QA']),
    '7.5':  ('Ejecutar pruebas de seguridad',                      ['5.6', '7.1'],        5,  ['ES', 'QA']),
    '7.6':  ('Corregir observaciones y volver a probar',           ['7.2', '7.4', '7.5'], 6,  ['CP', 'EI']),
    # 2.4 es predecesora de 8.1: la línea base debe medirse ANTES de que el
    # piloto empiece a cambiar el proceso, o no hay contra qué comparar.
    '8.1':  ('Preparar el piloto',                                 ['7.6', '2.4'],        4,  ['JP', 'RO']),
    '8.2':  ('Ejecutar el piloto en zona acotada',                 ['8.1', '6.2'],       15,  ['RO', 'CP']),
    '8.3':  ('Ajustar reglas y experiencia de uso',                ['8.2'],               8,  ['CP', 'UX']),
    '8.4':  ('Informe de piloto y decisión de avance',             ['8.3'],               2,  ['JP']),
    '9.1':  ('Elaborar el material de capacitación',               ['7.2'],               8,  ['CA', 'AF']),
    '9.2':  ('Capacitar supervisores, despacho y NOC',             ['8.4', '9.1'],        4,  ['CA']),
    '9.3':  ('Capacitar técnicos de campo por olas',               ['9.2'],              10,  ['CA']),
    '9.4':  ('Evaluar la capacitación',                            ['9.3'],               3,  ['CA']),
    '10.1': ('Desplegar la ola 1',                                 ['9.2'],               6,  ['CP', 'RO']),
    '10.2': ('Desplegar la ola 2',                                 ['10.1'],              6,  ['CP', 'RO']),
    '10.3': ('Desplegar la ola 3',                                 ['10.2'],              6,  ['CP', 'RO']),
    '11.1': ('Acompañar la operación (estabilización)',            ['10.3'],             15,  ['CP', 'RO']),
    '11.2': ('Alta del CI en la CMDB y cierre ante el CAB',        ['10.3'],              3,  ['EI']),
    # 9.4 es predecesora de 11.3: la evaluación de la capacitación es insumo
    # del traspaso a operación. Sin esto quedaba colgada, con holgura irreal.
    '11.3': ('Transferir a operación y documentar',                ['11.1', '9.4'],       5,  ['JP', 'AF']),
    '11.4': ('Acta de cierre y lecciones aprendidas',              ['11.2', '11.3'],      3,  ['JP']),
}

PERFILES = sorted({r for v in EDT.values() for r in v[3]})
REFUERZO = {'EI': 2, 'QA': 2}   # la dotación adoptada tras el aplanamiento


def orden_topologico(edt):
    orden, estado = [], {}

    def visitar(k):
        if estado.get(k) == 2:
            return
        if estado.get(k) == 1:
            raise SystemExit('ciclo de dependencias en %s' % k)
        estado[k] = 1
        for p in edt[k][1]:
            visitar(p)
        estado[k] = 2
        orden.append(k)

    for k in edt:
        visitar(k)
    return orden


def cpm(edt):
    """Devuelve ES, EF, LS, LF, holgura, duración total y camino crítico."""
    for k, (_, preds, dur, _) in edt.items():
        for p in preds:
            if p not in edt:
                raise SystemExit('predecesora inexistente %s en %s' % (p, k))
        if dur <= 0:
            raise SystemExit('duración no positiva en %s' % k)

    orden = orden_topologico(edt)
    ES, EF = {}, {}
    for k in orden:
        ES[k] = max([EF[p] for p in edt[k][1]], default=0)
        EF[k] = ES[k] + edt[k][2]
    T = max(EF.values())

    suc = defaultdict(list)
    for k in edt:
        for p in edt[k][1]:
            suc[p].append(k)
    LS, LF = {}, {}
    for k in reversed(orden):
        LF[k] = min([LS[s] for s in suc[k]], default=T)
        LS[k] = LF[k] - edt[k][2]

    H = {k: LS[k] - ES[k] for k in edt}
    critico = [k for k in sorted(edt, key=lambda x: (ES[x], x)) if H[k] == 0]
    return ES, EF, LS, LF, H, T, critico


def conflictos(edt, ES, EF):
    """Tramos en que un perfil tiene más de una actividad simultánea."""
    carga = defaultdict(lambda: defaultdict(int))
    for k, (_, _, _, perf) in edt.items():
        for d in range(ES[k], EF[k]):
            for r in perf:
                carga[r][d] += 1

    out = {}
    for r in sorted(carga):
        dias = sorted(d for d, v in carga[r].items() if v > 1)
        if not dias:
            continue
        tramos, ini, prev = [], dias[0], dias[0]
        for d in dias[1:]:
            if d != prev + 1:
                tramos.append((ini, prev))
                ini = d
            prev = d
        tramos.append((ini, prev))
        detalle = []
        for a, b in tramos:
            acts = sorted([k for k in edt if r in edt[k][3] and ES[k] <= b and EF[k] > a],
                          key=lambda k: ES[k])
            detalle.append((a, b + 1, acts))
        out[r] = {'pico': max(carga[r].values()), 'tramos': detalle}
    return out


def nivelar(edt, LS, ES, capacidad):
    """Aplanamiento serial: prioridad por fecha de inicio tardía, capacidad
    fija por perfil. Devuelve (duración, inicios, finales)."""
    ocupado = {r: [0] * capacidad.get(r, 1) for r in PERFILES}
    ini, fin = {}, {}
    pendientes = sorted(edt, key=lambda k: (LS[k], ES[k], k))
    hechas = set()

    while pendientes:
        for k in list(pendientes):
            if not all(p in hechas for p in edt[k][1]):
                continue
            t0 = max([fin[p] for p in edt[k][1]] + [0])
            elegidos = {}
            for r in edt[k][3]:
                u = min(range(len(ocupado[r])), key=lambda i: ocupado[r][i])
                elegidos[r] = u
                t0 = max(t0, ocupado[r][u])
            ini[k], fin[k] = t0, t0 + edt[k][2]
            for r, u in elegidos.items():
                ocupado[r][u] = fin[k]
            hechas.add(k)
            pendientes.remove(k)
            break
        else:
            raise SystemExit('el aplanamiento se bloqueó')
    return max(fin.values()), ini, fin


def carga_por_perfil(edt, ini, fin, capacidad):
    filas = []
    for r in PERFILES:
        acts = [k for k in edt if r in edt[k][3]]
        dias = sum(edt[k][2] for k in acts)
        a, b = min(ini[k] for k in acts), max(fin[k] for k in acts)
        pers = capacidad.get(r, 1)
        ded = min(100.0, 100.0 * dias / max(1, b - a) / pers)
        filas.append((r, pers, dias, dias * JORNADA, a, b, ded))
    return filas


def informe():
    ES, EF, LS, LF, H, T, critico = cpm(EDT)
    print('=' * 78)
    print('CPM — duración teórica a fechas tempranas: %d días hábiles (~%.1f meses)'
          % (T, T / MES))
    print('Camino crítico (%d actividades):' % len(critico))
    print('  ' + ' -> '.join(critico))
    print()
    print('%-6s %-46s %4s %4s %4s %4s %4s %5s' % ('ID', 'Actividad', 'Dur', 'ES', 'EF', 'LS', 'LF', 'Hol'))
    for k in sorted(EDT, key=lambda x: (ES[x], x)):
        print('%-6s %-46s %4d %4d %4d %4d %4d %5d%s'
              % (k, EDT[k][0][:46], EDT[k][2], ES[k], EF[k], LS[k], LF[k], H[k],
                 '  *' if H[k] == 0 else ''))

    print()
    print('CONFLICTOS DE RECURSO a fechas tempranas')
    for r, d in conflictos(EDT, ES, EF).items():
        for a, b, acts in d['tramos']:
            print('  %-3s d%d-d%d (pico %d): %s' % (r, a, b, d['pico'], ', '.join(acts)))

    print()
    print('APLANAMIENTO')
    base = {r: 1 for r in PERFILES}
    T1, _, _ = nivelar(EDT, LS, ES, base)
    print('  1 persona por perfil ......... %3d días (+%d sobre el teórico)' % (T1, T1 - T))
    for r in PERFILES:
        c = dict(base, **{r: 2})
        Tr, _, _ = nivelar(EDT, LS, ES, c)
        print('    +1 %-3s ..................... %3d días (+%d)' % (r, Tr, Tr - T))
    print('  combinaciones de dos refuerzos, las mejores:')
    res = []
    for a, b in itertools.combinations(PERFILES, 2):
        c = dict(base, **{a: 2, b: 2})
        res.append((nivelar(EDT, LS, ES, c)[0], a, b))
    for Tr, a, b in sorted(res)[:3]:
        print('    +1 %-3s +1 %-3s ............. %3d días (+%d)' % (a, b, Tr, Tr - T))

    Tf, ini, fin = nivelar(EDT, LS, ES, dict(base, **REFUERZO))
    print()
    print('  ADOPTADA: %s -> %d días hábiles (~%.1f meses)'
          % (' y '.join('+1 %s' % r for r in sorted(REFUERZO)), Tf, Tf / MES))
    print()
    print('  Corrimientos respecto de fechas tempranas:')
    for k in sorted(EDT, key=lambda x: ini[x]):
        if ini[k] != ES[k]:
            print('    %-5s %-44s d%-3d -> d%-3d (corre %2d, holgura %d)'
                  % (k, EDT[k][0][:44], ES[k], ini[k], ini[k] - ES[k], H[k]))

    print()
    print('CARGA POR PERFIL (jornada de %d h)' % JORNADA)
    print('  %-4s %-9s %-11s %-8s %-16s %s' % ('Perf', 'Personas', 'Días-pers', 'Horas', 'Ventana', 'Dedicación'))
    total = 0
    for r, pers, dias, horas, a, b, ded in carga_por_perfil(EDT, ini, fin, dict(base, **REFUERZO)):
        total += horas
        print('  %-4s %-9d %-11d %-8d d%-3d - d%-8d %.0f%%' % (r, pers, dias, horas, a, b, ded))
    print('  TOTAL: %d horas-persona' % total)

    if '--json' in sys.argv:
        with open('cpm.json', 'w', encoding='utf-8') as f:
            json.dump({'T': T, 'T_nivelado': Tf, 'ES': ES, 'EF': EF, 'LS': LS, 'LF': LF,
                       'holgura': H, 'critico': critico, 'ini_nivelado': ini, 'fin_nivelado': fin},
                      f, ensure_ascii=False, indent=1)
        print('\ncpm.json escrito')


if __name__ == '__main__':
    informe()
