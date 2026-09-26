#!/bin/sh
# Hook SessionStart: sincroniza main con origin antes de que el agente lea o
# escriba nada (OPERACIÓN: GIT del CLAUDE.md). Lo que imprime entra al
# contexto de la sesión. Nunca bloquea el arranque: siempre sale con 0.
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0

branch=$(git symbolic-ref --short -q HEAD) || exit 0
if [ "$branch" != main ]; then
  echo "sync: rama '$branch' (worktree/worker), no se hizo pull; sólo se sincroniza main."
  exit 0
fi

# Si el usuario dejó un rebase/merge a medias, no tocar nada.
for p in rebase-merge rebase-apply MERGE_HEAD; do
  if [ -e "$(git rev-parse --git-path "$p")" ]; then
    echo "sync: hay un rebase/merge en curso; no se hizo pull. Avisale al usuario."
    exit 0
  fi
done

before=$(git rev-parse --short HEAD)
if out=$(git pull --rebase --autostash -q origin main 2>&1); then
  after=$(git rev-parse --short HEAD)
  if [ "$before" = "$after" ]; then
    echo "sync: main ya estaba al día con origin ($after)."
  else
    echo "sync: main actualizado con origin ($before -> $after)."
  fi
else
  git rebase --abort >/dev/null 2>&1
  echo "sync: FALLÓ git pull --rebase; se abortó y el árbol quedó como estaba."
  echo "Avisale al usuario antes de seguir. Detalle:"
  printf '%s\n' "$out" | tail -5
fi
exit 0
