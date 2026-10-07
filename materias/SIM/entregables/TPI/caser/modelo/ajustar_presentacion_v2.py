#!/usr/bin/env python3
"""Ajustes a la presentación tras la primera revisión en el IDE (2026-10-07). IDE cerrado.

- Gráficos sin línea: cada serie necesita un nombre de dataset en <Expression> (AnyLogic lo crea solo;
  así lo hacen todos los ejemplos oficiales). Estaba en `null`. Se quita <Persistent>, que ningún ejemplo usa.
- Cola: la grilla de ULI tapaba el título; se baja y se agranda la zona.
- Horno: se agranda el cuerpo para que el texto de la campaña no pise el borde.
- Statechart: el título se corre a la derecha de la flecha de entrada.
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ALP = Path(__file__).resolve().parent / "CaserHorno.alp"
s = ALP.read_text(encoding="utf-8")
if "<Expression>dsCola</Expression>" in s:
    sys.exit("Los ajustes v2 ya están aplicados.")


def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:100], s.count(a))
    s = s.replace(a, b)


# gráficos
rep("<Title>ULI en cola</Title><Expression>null</Expression>", "<Title>ULI en cola</Title><Expression>dsCola</Expression>")
rep("<Title>Umbral de encendido</Title><Expression>null</Expression>", "<Title>Umbral de encendido</Title><Expression>dsUmbral</Expression>")
rep("<Title>Energia acumulada (MWh)</Title><Expression>null</Expression>", "<Title>Energia acumulada (MWh)</Title><Expression>dsEnergia</Expression>")
rep("<Persistent>true</Persistent>", "", 2)

# cola: zona más alta, grilla 16 px más abajo, texto inferior debajo de la zona
rep("<Name>zonaCola</Name><X>180</X><Y>110</Y>", "<Name>zonaCola</Name><X>180</X><Y>110</Y>")
i = s.index("<Name>zonaCola</Name>")
j = s.index("<Height>200</Height>", i)
s = s[:j] + "<Height>222</Height>" + s[j + len("<Height>200</Height>"):]
rep("<Name>uliEnCola</Name><X>192</X><Y>136</Y>", "<Name>uliEnCola</Name><X>192</X><Y>152</Y>")
rep("<YCode>136 + (index / 24) * 14</YCode>", "<YCode>152 + (index / 24) * 14</YCode>")
rep("<YCode>136 + (umbralULI / 24) * 14 - 2</YCode>", "<YCode>152 + (umbralULI / 24) * 14 - 2</YCode>")
rep("<Name>txtCola</Name><X>186</X><Y>305</Y>", "<Name>txtCola</Name><X>186</X><Y>348</Y>")

# horno: cuerpo más alto, textos inferiores adentro
i = s.index("<Name>cuerpoHorno</Name>")
j = s.index("<Height>200</Height>", i)
s = s[:j] + "<Height>222</Height>" + s[j + len("<Height>200</Height>"):]
rep("<Name>txtResist</Name><X>590</X><Y>278</Y>", "<Name>txtResist</Name><X>590</X><Y>276</Y>")
rep("<Name>txtCampana</Name><X>590</X><Y>298</Y>", "<Name>txtCampana</Name><X>590</X><Y>304</Y>")

# statechart: título a la derecha de la flecha de entrada
rep("<Name>txtStatechart</Name><X>20</X><Y>352</Y>", "<Name>txtStatechart</Name><X>122</X><Y>356</Y>")

ET.fromstring(s.encode("utf-8"))
ALP.write_text(s, encoding="utf-8", newline="\n")
print("Ajustes v2 aplicados a", ALP.name)
