# Anexo II — Documentación gráfica de la Etapa 3 de ASI

Genera las seis láminas A3 apaisadas que el entregable `materias/ASI/entregables/etapa3-v2.md`
promete como adjuntos: Diagrama de Red, Gantt, histograma de recursos, plano de la base
operativa y croquis de trabajo en campo.

## Cómo se regenera

```
python scripts/anexo-graficos/build.py materias/ASI/entregables/etapa3-anexo-graficos.html
```

Y después imprimir a PDF con Chrome sin encabezados:

```
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf=materias/ASI/entregables/etapa3-anexo-graficos.pdf \
  file:///<ruta-absoluta>/etapa3-anexo-graficos.html
```

El HTML lleva `@page { size: A3 landscape }`, así que el PDF sale en A3 sin más ajustes.
No hace falta Node ni dependencias: es Python puro de la biblioteca estándar.

## Qué hay en cada archivo

| Archivo | Qué es |
|---|---|
| `data.py` | Las 51 actividades de la EDT del punto 4.3 con predecesoras, duración, ES/EF/LS/LF, holgura y perfiles, más los corrimientos del aplanamiento del punto 10. **Transcripción literal de las tablas del entregable**: es el único lugar donde hay datos |
| `sched.py` | Programación aplanada (192 días), holgura remanente y carga diaria por perfil, derivadas de `data.py` |
| `fig1.py` | Figura 1, Diagrama de Red en actividad-en-el-nodo, en dos bandas |
| `fig2.py` | Figuras 2.a y 2.b, Gantt e histograma de recursos |
| `fig3.py` | Figura 3, plano de la base operativa, y el bloque de simbología |
| `fig4.py` | Figura 4, croquis tipo de trabajo en campo |
| `acentos.py` | Repone la acentuación castellana sobre los nodos de texto del HTML final |
| `build.py` | Arma el HTML: portada, CSS, marcadores SVG y las cinco láminas con su rótulo |

## Verificación

`data.py` no es solo un volcado: el CPM se recalcula a partir de él y debe reproducir los
números publicados en el punto 10. Para comprobarlo:

```
python -c "import sys; sys.path.insert(0,'scripts/anexo-graficos'); import sched; print(sched.FINPROY, sum(sum(sched.carga(p)) for p in sched.PERFILES))"
```

Tiene que imprimir `192 530`: 192 días hábiles de duración aplanada y 530 días-persona, que
por ocho horas dan las 4.240 horas-persona del entregable. La pasada hacia adelante y hacia
atrás sobre `data.py` arroja además 187 días a fechas tempranas y 30 actividades críticas.

## Si cambian los datos

Si se toca la EDT, hay que actualizar `data.py` y `NIVEL` en el mismo archivo, y verificar
que la comprobación de arriba siga dando los mismos valores que las tablas del punto 10.
Las láminas se redibujan solas.
