# -*- coding: utf-8 -*-
"""Programacion aplanada adoptada (192 dias) y holguras sobre esa programacion."""
from data import ACT, NIVEL

D = {a[0]: a for a in ACT}
IDS = [a[0] for a in ACT]
succ = {k: [] for k in D}
for a in ACT:
    for p in a[1]:
        succ[p].append(a[0])

START = {k: NIVEL.get(k, D[k][3]) for k in D}          # d[3] = ES
FIN   = {k: START[k] + D[k][2] for k in D}
FINPROY = max(FIN.values())

# verificacion de precedencias sobre la programacion aplanada
viol = [(p, k, FIN[p], START[k]) for k in D for p in D[k][1] if FIN[p] > START[k]]

# pasada hacia atras sobre las fechas aplanadas -> holgura de red
LFv, LSv = {}, {}
for k in reversed(IDS):
    pass
order = []
seen = set()
def _v(k):
    if k in seen: return
    for p in D[k][1]: _v(p)
    seen.add(k); order.append(k)
for k in IDS: _v(k)
for k in reversed(order):
    LFv[k] = min([LSv[s] for s in succ[k]], default=FINPROY)
    LSv[k] = LFv[k] - D[k][2]
HOLG = {k: LFv[k] - FIN[k] for k in D}
CRIT = {k for k in D if D[k][7] == 0}                   # criticas segun el CPM del documento

PERFILES = ["JP", "AF", "EI", "ES", "CP", "UX", "QA", "CA", "RO"]
PERFIL_NOMBRE = {
    "JP": "Jefe de proyecto", "AF": "Analista funcional",
    "EI": "Especialista de integraciones", "ES": "Especialista de seguridad",
    "CP": "Consultor de la plataforma", "UX": "Diseno de experiencia de uso",
    "QA": "Responsable de pruebas", "CA": "Capacitador",
    "RO": "Referente de operaciones",
}
def carga(perfil):
    """Personas requeridas de `perfil` en cada dia habil [0, FINPROY)."""
    v = [0] * FINPROY
    for k in D:
        if perfil in D[k][8]:
            for d in range(START[k], FIN[k]):
                v[d] += 1
    return v

if __name__ == "__main__":
    print("fin proyecto aplanado:", FINPROY)
    print("violaciones de precedencia:", viol if viol else "NINGUNA")
    print("holguras negativas:", [(k, HOLG[k]) for k in D if HOLG[k] < 0] or "NINGUNA")
    for p in PERFILES:
        v = carga(p)
        print(f"  {p}: pico {max(v)}  dias-persona {sum(v)}")
    print("total dias-persona:", sum(sum(carga(p)) for p in PERFILES))

# Holgura remanente tras el aplanamiento: holgura total del CPM menos el
# corrimiento aplicado a la actividad. Las 30 criticas quedan en cero, como en
# la tabla del punto 10; las corridas muestran solo lo que les quedo disponible.
CORRIM = {k: START[k] - D[k][3] for k in D}
HOLG_REM = {k: max(0, D[k][7] - CORRIM[k]) for k in D}
