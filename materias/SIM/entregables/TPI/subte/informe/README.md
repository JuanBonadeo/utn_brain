# Informe LaTeX del TPI subte

Fuente del informe final (consigna: "generado en LaTeX"). Se compila en **Overleaf** (decisión D6 del
[plan](../07-plan-tpi.md)); no hay TeX instalado localmente.

- `tpi-subte.tex`: documento principal (article, A4, 11 pt, `babel` en castellano, `siunitx` con coma
  decimal, `biblatex-apa` + Biber).
- `capitulos/`: un archivo por sección del plan §8.2, uno por paso de la consigna. Cada uno indica de qué
  sección de `03-informe-tpi.md` sale y qué tarea lo completa (T5.3: pasos 1-7; T5.4: pasos 8-10 y anexos).
- `referencias.bib`: solo fuentes verificadas del plan §14. Nada de Wikipedia.
- `empaquetar-overleaf.sh`: arma `informe-overleaf.zip` con las figuras `tpi-subte-*` de `materias/SIM/figs/`.

Flujo: editar acá → `./empaquetar-overleaf.sh` → Overleaf, *New Project > Upload Project* → compilar con
pdfLaTeX (Overleaf corre Biber solo). Si alguien edita en Overleaf, se baja el `.zip`, se copian los `.tex`
de vuelta y se commitea: la fuente de verdad es el repo. El PDF final se guarda en esta carpeta como
`tpi-subte.pdf`.
