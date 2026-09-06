#!/usr/bin/env python3
"""Vuelca la estructura logica de un .bpm de Bizagi Modeler a texto legible.

Un .bpm es un ZIP; adentro hay uno o mas .diag, que a su vez son ZIPs con un
Diagram.xml. Este script recorre esa anidacion y lista pools, lanes, elementos
de flujo y conectores, que es lo que hace falta para auditar un diagrama sin
mirarlo como imagen.
"""
import io, re, sys, zipfile
import xml.etree.ElementTree as ET


def localname(tag):
    return tag.rsplit('}', 1)[-1]


def dump(path):
    print(f"===== {path}")
    with zipfile.ZipFile(path) as outer:
        diags = [n for n in outer.namelist() if n.endswith('.diag')]
        if not diags:
            print("  (sin .diag)")
            return
        for dn in diags:
            with zipfile.ZipFile(io.BytesIO(outer.read(dn))) as inner:
                if 'Diagram.xml' not in inner.namelist():
                    continue
                xml = inner.read('Diagram.xml').decode('utf-8', 'replace')
                root = ET.fromstring(xml)
                nodes, edges = {}, []
                for el in root.iter():
                    t = localname(el.tag)
                    a = el.attrib
                    name = (a.get('Name') or a.get('name') or '').strip()
                    oid = a.get('Id') or a.get('id')
                    if t in ('Pool', 'Lane', 'Process'):
                        print(f"  [{t}] {name or '(sin nombre)'}")
                    elif t in ('Activity', 'Task', 'SubProcess', 'Event', 'Gateway',
                               'StartEvent', 'EndEvent', 'IntermediateEvent'):
                        sub = a.get('ActivityType') or a.get('EventType') or a.get('GatewayType') or ''
                        trig = a.get('Trigger') or a.get('TriggerType') or ''
                        if oid:
                            nodes[oid] = name or f'({t})'
                        print(f"    <{t}{'/' + sub if sub else ''}"
                              f"{'/' + trig if trig else ''}> {name or '(SIN NOMBRE)'}")
                    elif t in ('SequenceFlow', 'MessageFlow', 'Association', 'Flow'):
                        edges.append((t, a.get('From') or a.get('SourceRef'),
                                      a.get('To') or a.get('TargetRef'), name))
                if edges:
                    print("  --- conectores ---")
                    for t, s, d, name in edges:
                        print(f"    {t}: {nodes.get(s, s)} -> {nodes.get(d, d)}"
                              f"{'   [' + name + ']' if name else '   [SIN ETIQUETA]'}")


if __name__ == '__main__':
    for p in sys.argv[1:]:
        dump(p)
