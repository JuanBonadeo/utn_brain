# -*- coding: utf-8 -*-
"""Modelo de costos y evaluación económica de la Etapa 3 del TPI de ASI.

De acá salen los números de los puntos 11 y 12 del entregable
(`materias/ASI/entregables/etapa3.md`). Los dos puntos comparten esta única
base: si se cambia un parámetro hay que actualizar AMBOS, porque el 12 descuenta
flujos construidos sobre los costos del 11.

    .venv/Scripts/python.exe scripts/costos-etapa3.py

Ya pasó una vez que los dos puntos se escribieron con dotaciones distintas —el
11 sobre 220 técnicos y el 12 sobre 60— y hubo que reconciliar todo a mano. Este
script existe para que eso no vuelva a pasar: hay un solo lugar donde tocar.

Las horas por perfil NO se inventan acá: salen de `scripts/cpm-edt.py`, que las
deriva de la EDT y del aplanamiento. Si cambia la EDT, correr primero ese.

Todos los importes en dólares estadounidenses. La elección está justificada en
el propio punto 11: el licenciamiento y los servicios de implantación se cotizan
en esa moneda y así la estimación no queda desactualizada por el tipo de cambio.
"""

# ---------------------------------------------------------------------------
# PARÁMETROS. Todos son supuestos declarados como tales en el documento y deben
# validarse en la fase de relevamiento, antes de comprometer presupuesto.
# ---------------------------------------------------------------------------
TECNICOS = 60          # dotación de técnicos instaladores en el alcance
USUARIOS = 78          # licencias: 60 técnicos + 8 supervisión/despacho + 6 NOC + 4 comercial
USUARIOS_CFG = 15      # licencias durante configuración y piloto
DISPOSITIVOS = 63      # uno por técnico más 3 de reserva

LICENCIA = 45          # por usuario y por mes
CONSULTOR = 65         # hora del consultor del proveedor
PRECIO_DISP = 620      # por dispositivo rugerizado
MDM = 4                # por dispositivo y por mes
MAPAS = 900            # por mes
AMBIENTE = 500         # ambiente no productivo, por mes
SOPORTE_EST = 2500     # soporte reforzado de estabilización, por mes

INDIRECTOS = 0.12      # sobre el costo directo
CONTINGENCIA_A1 = 0.15  # año del proyecto
CONTINGENCIA_REG = 0.05  # en régimen de operación
INDEXACION_LIC = 0.05   # ajuste contractual anual del licenciamiento, desde el año 3
INDEXACION_OP = 0.025   # ajuste del costo operativo en la evaluación

TASA = 0.15            # costo de capital para el VAN
HORIZONTE = 5          # años de evaluación
RAMPA_A1 = 0.60        # realización de beneficios el primer año de operación

# Perfil, personas, horas, valor hora. Horas: salen de scripts/cpm-edt.py.
# CP no figura: lo aporta el proveedor y se imputa en el servicio de implantación.
RRHH = [
    ('Jefe de proyecto (JP)',                 1, 408, 45),
    ('Analista funcional (AF)',               1, 848, 32),
    ('Especialista de integraciones (EI)',    2, 560, 38),
    ('Especialista de seguridad (ES)',        1, 312, 42),
    ('Diseñador de experiencia de uso (UX)',  1, 192, 30),
    ('Responsable de pruebas (QA)',           2, 232, 28),
    ('Capacitador (CA)',                      1, 200, 25),
    ('Referente de operaciones (RO)',         1, 704, 22),
]
HORAS_CP = 784         # horas del consultor de la plataforma

# Beneficios anuales en régimen. Cada uno se justifica en el punto 12.
BENEFICIOS = [
    ('O1', '+5% de productividad = 3 técnicos de capacidad sin ampliar dotación', 54000),
    ('O2', 'Menor carga administrativa de cierre diferido de órdenes',            57700),
    ('O3', 'Visitas fallidas evitables reducidas a la mitad',                    103000),
    ('--', 'Costos evitados por reclamos y consultas duplicadas',                  7700),
]


def money(x):
    return format(int(round(x)), ',d').replace(',', '.')


def main():
    # ---- recursos humanos propios --------------------------------------
    horas = sum(r[2] for r in RRHH)
    rrhh = sum(r[2] * r[3] for r in RRHH)
    print('RECURSOS HUMANOS PROPIOS')
    for n, p, h, v in RRHH:
        print('  %-38s %d  %5d h  x %2d  = %9s' % (n, p, h, v, money(h * v)))
    print('  %-38s    %5d h  medio %.2f = %9s' % ('TOTAL', horas, rrhh / horas, money(rrhh)))
    print('  (CP aporta %d h más, imputadas en implantación: %d horas-persona en total)'
          % (HORAS_CP, horas + HORAS_CP))

    # ---- adquisiciones y servicios del año 1 ---------------------------
    adq = [
        ('Licenciamiento FSM — configuración y piloto', USUARIOS_CFG * 4 * LICENCIA),
        ('Licenciamiento FSM — producción',             USUARIOS * 5 * LICENCIA),
        ('Servicio de implantación e integración',      HORAS_CP * CONSULTOR),
        ('Bolsa de horas adicionales del proveedor',    120 * CONSULTOR),
        ('Dispositivos móviles rugerizados',            DISPOSITIVOS * PRECIO_DISP),
        ('Administración de dispositivos móviles',      DISPOSITIVOS * 5 * MDM),
        ('Servicio de mapas y geolocalización',         5 * MAPAS),
        ('Ambiente de pruebas no productivo',           10 * AMBIENTE),
        ('Capacitación — material y plataforma',        3000),
        ('Capacitación — horas improductivas',          TECNICOS * 4 * 12),
        ('Soporte reforzado de estabilización',         3 * SOPORTE_EST),
    ]
    total_adq = sum(v for _, v in adq)
    bienes = DISPOSITIVOS * PRECIO_DISP
    print()
    print('ADQUISICIONES Y SERVICIOS — AÑO 1')
    for n, v in adq:
        print('  %-46s %9s' % (n, money(v)))
    print('  %-46s %9s   (bienes %s / servicios %s)'
          % ('TOTAL', money(total_adq), money(bienes), money(total_adq - bienes)))

    # ---- estructura del costo total ------------------------------------
    directo = rrhh + total_adq
    ind = round(directo * INDIRECTOS)
    sub = directo + ind
    cont = round(sub * CONTINGENCIA_A1)
    presupuesto = sub + cont
    print()
    print('ESTRUCTURA DEL COSTO — AÑO 1')
    print('  costo directo ................ %9s' % money(directo))
    print('  indirectos (%.0f%%) ............. %9s' % (INDIRECTOS * 100, money(ind)))
    print('  subtotal ..................... %9s' % money(sub))
    print('  contingencia (%.0f%%) ........... %9s' % (CONTINGENCIA_A1 * 100, money(cont)))
    print('  PRESUPUESTO AÑO 1 ............ %9s' % money(presupuesto))

    # ---- costo total de propiedad a tres años --------------------------
    lic = USUARIOS * LICENCIA * 12
    recurrente = [
        ('Licenciamiento de la plataforma', lic),
        ('Administración de dispositivos',  DISPOSITIVOS * MDM * 12),
        ('Servicio de mapas',               MAPAS * 12),
        ('Soporte del proveedor',           12000),
        ('Evolución de integraciones',      300 * 32),
        ('Reposición de dispositivos (20%)', round(DISPOSITIVOS * 0.20 * PRECIO_DISP)),
    ]
    r2 = sum(v for _, v in recurrente)
    r3 = r2 + round(lic * INDEXACION_LIC)

    def anio_regimen(dir_):
        i = round(dir_ * INDIRECTOS)
        s = dir_ + i
        c = round(s * CONTINGENCIA_REG)
        return dir_, i, c, s + c

    d2, i2, c2, t2 = anio_regimen(r2)
    d3, i3, c3, t3 = anio_regimen(r3)
    tco = presupuesto + t2 + t3
    print()
    print('COSTO TOTAL DE PROPIEDAD A TRES AÑOS')
    print('  año 1 (proyecto) ............. %9s' % money(presupuesto))
    print('  año 2 (régimen) .............. %9s   directo %s' % (money(t2), money(d2)))
    print('  año 3 (régimen, +%.0f%% lic.) .... %9s   directo %s'
          % (INDEXACION_LIC * 100, money(t3), money(d3)))
    print('  TCO .......................... %9s   (%.0f%% año 1, %.0f%% recurrente)'
          % (money(tco), 100 * presupuesto / tco, 100 * (tco - presupuesto) / tco))

    # ---- evaluación económica ------------------------------------------
    # La inversión que se descuenta excluye la reserva de contingencia: es una
    # previsión ante riesgo, no una erogación esperada. El presupuesto a
    # autorizar sí la incluye. La distinción está explicada en el punto 12.
    inversion = sub
    beneficio = sum(v for _, _, v in BENEFICIOS)
    print()
    print('BENEFICIOS ANUALES EN RÉGIMEN')
    for o, d, v in BENEFICIOS:
        print('  %-3s %-58s %9s' % (o, d[:58], money(v)))
    print('  %-62s %9s' % ('TOTAL', money(beneficio)))

    # Los dos primeros años del costo operativo son los ya calculados en el TCO
    # (t2 y t3, este último con la indexación contractual del licenciamiento);
    # de ahí en adelante se indexa al 2,5% anual.
    op = [t2, t3] + [round(t3 * (1 + INDEXACION_OP) ** k) for k in range(1, HORIZONTE - 1)]
    flujos = [-inversion] + [beneficio * (RAMPA_A1 if k == 0 else 1) - op[k]
                             for k in range(HORIZONTE)]

    def van(tasa):
        return sum(v / (1 + tasa) ** k for k, v in enumerate(flujos))

    lo, hi = 0.0, 2.0
    for _ in range(300):
        m = (lo + hi) / 2
        if van(m) > 0:
            lo = m
        else:
            hi = m
    tir = lo

    acum, repago = 0, None
    for k, v in enumerate(flujos):
        prev = acum
        acum += v
        if k and prev < 0 <= acum:
            repago = k - 1 + (-prev) / v
            break

    print()
    print('EVALUACIÓN ECONÓMICA')
    print('  presupuesto a autorizar ...... %9s  (incluye contingencia)' % money(presupuesto))
    print('  inversión que se descuenta ... %9s  (sin la reserva)' % money(inversion))
    print('  flujos:')
    for k, v in enumerate(flujos):
        print('    t%d  %10s' % (k, money(v)))
    for tasa in (0.10, 0.12, TASA, 0.20):
        print('  VAN al %2.0f%% ................... %9s' % (tasa * 100, money(van(tasa))))
    print('  TIR .......................... %8.1f%%' % (tir * 100))
    print('  repago ....................... %8.2f años' % repago)
    print('  tasa de retorno en régimen ... %8.0f%%' % ((beneficio - op[1]) / inversion * 100))

    # umbral de indiferencia
    lo, hi = 0.0, 2.0
    for _ in range(200):
        m = (lo + hi) / 2
        f = [-inversion] + [beneficio * m - op[k] for k in range(HORIZONTE)]
        if sum(v / (1 + TASA) ** k for k, v in enumerate(f)) < 0:
            lo = m
        else:
            hi = m
    print('  umbral de indiferencia ....... %8.0f%% de realización de beneficios' % (hi * 100))
    pes = [-inversion] + [beneficio * RAMPA_A1 - op[k] for k in range(HORIZONTE)]
    print('  VAN si la realización se queda en %.0f%%: %s'
          % (RAMPA_A1 * 100, money(sum(v / (1 + TASA) ** k for k, v in enumerate(pes)))))


if __name__ == '__main__':
    main()
