#!/usr/bin/env python3
"""Ajustes v3 a la presentación (2026-10-07, IDE cerrado).

- Gráficos: siguen sin línea con datasets automáticos. Se pasa a DataSet propios (dsCola, dsUmbral,
  dsEnergia) que llena el evento eMuestreo cada 2 h, y los gráficos los leen directo (Expression2Flag
  false, como el ejemplo oficial "Measuring Length of Stay"). eMuestreo no usa números aleatorios ni
  cambia el estado: los resultados no cambian.
- El texto "En cola" pisaba el título del statechart: pasa al título de la zona de la cola.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ALP = Path(__file__).resolve().parent / "CaserHorno.alp"
s = ALP.read_text(encoding="utf-8")
if "<Name>eMuestreo</Name>" in s:
    sys.exit("Los ajustes v3 ya están aplicados.")
_id = [1820000000000]


def nid():
    _id[0] += 1
    return str(_id[0])


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:100], s.count(a))
    s = s.replace(a, b)


LABEL = "<Label><X>10</X><Y>0</Y></Label>"
FLAGS_OFF = "<PublicFlag>false</PublicFlag><PresentationFlag>false</PresentationFlag><ShowLabel>true</ShowLabel>"

# DataSet propios
vars_ = ""
for k, n in enumerate(("dsCola", "dsUmbral", "dsEnergia")):
    vars_ += (f'<Variable Class="PlainVariable"><Id>{nid()}</Id><Name>{n}</Name><X>1400</X><Y>{1100 + 22 * k}</Y>{LABEL}{FLAGS_OFF}'
              f'<Properties SaveInSnapshot="true" Constant="false" AccessType="public" StaticVariable="false"><Type>DataSet</Type>'
              f'<UnitType>NONE</UnitType><SdArray>false</SdArray><InitialValue Class="CodeValue"><Code>new DataSet(1000)</Code></InitialValue></Properties></Variable>')
i = s.index("</Variables>")  # el primero es el de Main
s = s[:i] + vars_ + s[i:]

body = escape("dsCola.add(time(), nEnCola);\ndsUmbral.add(time(), umbralULI);\ndsEnergia.add(time(), kWhTotal() / 1000);")
rep("</Functions>", f'<Function AccessType="public" StaticFunction="false"><ReturnModificator>VOID</ReturnModificator><ReturnType>void</ReturnType>'
                    f'<Id>{nid()}</Id><Name>muestrear</Name><X>1700</X><Y>1100</Y><PublicFlag>true</PublicFlag><PresentationFlag>false</PresentationFlag>'
                    f'<ShowLabel>true</ShowLabel>{LABEL}<Body>{body}</Body></Function></Functions>')
t = '<Code>1e12</Code><Unit Class="TimeUnits">HOUR</Unit>'
rep("</Events>", f'<Event><Id>{nid()}</Id><Name>eMuestreo</Name><X>1950</X><Y>1100</Y>{LABEL}{FLAGS_OFF}'
                 f'<Properties TriggerType="timeout" Mode="userControls"><Timeout Class="CodeUnitValue">{t}</Timeout>'
                 f'<Rate Class="CodeUnitValue"><Code>1</Code><Unit Class="RateUnits">PER_HOUR</Unit></Rate>'
                 f'<Id>{nid()}</Id><OccurrenceAtTime>true</OccurrenceAtTime><OccurrenceDate>1783584000000</OccurrenceDate>'
                 f'<OccurrenceTime Class="CodeUnitValue">{t}</OccurrenceTime><RecurrenceCode Class="CodeUnitValue">{t}</RecurrenceCode>'
                 f'<Condition>false</Condition></Properties><Action>muestrear(); eMuestreo.restart(2);</Action></Event></Events>')
rep("<StartupCode>inicializar();</StartupCode>", "<StartupCode>inicializar();\neMuestreo.restart(0);</StartupCode>")

# gráficos leen los DataSet
for ds in ("dsCola", "dsUmbral", "dsEnergia"):
    s, n = re.subn(rf"<Expression>{ds}</Expression>(<Color>-?\d+</Color>)<Expression2>[^<]*</Expression2><Expression2Flag>true</Expression2Flag>",
                   rf"<Expression>{ds}</Expression>\g<1><Expression2>0</Expression2><Expression2Flag>false</Expression2Flag>", s)
    assert n == 1, ds

# texto de la cola dentro de su zona
s, n = re.subn(r"<Text><Id>\d+</Id><Name>txtCola</Name>.*?</Alignment></Text>", "", s, flags=re.S)
assert n == 1
code = escape('"COLA DEL HORNO: " + nEnCola + " ULI (" + Math.round(kgEnCola) + " kg)   -   marca roja = umbral " + umbralULI')
s, n = re.subn(r"(<Name>txtColaTitulo</Name>.*?<Text>[^<]*</Text>)(<Font>)", rf"\g<1><TextCode>{code}</TextCode>\g<2>", s, count=1, flags=re.S)
assert n == 1

ET.fromstring(s.encode("utf-8"))
ALP.write_text(s, encoding="utf-8", newline="\n")
print("Ajustes v3 aplicados a", ALP.name)
