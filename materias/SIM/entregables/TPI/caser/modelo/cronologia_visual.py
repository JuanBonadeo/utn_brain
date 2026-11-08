#!/usr/bin/env python3
"""Cronología de la animación (2026-11-08): qué pasa y cuándo en el experimento Visual (semilla 1, sin
calentamiento), para preparar la demo y el video. Corre las mismas funciones del .alp en el motor del verificador.

Uso, desde la raíz del repo:
    .venv/Scripts/python.exe -I materias/SIM/entregables/TPI/caser/modelo/cronologia_visual.py [dias]

Imprime, para E0 y para E3, cada cambio de estado del horno con su fecha (t = 0 es el lunes 18/08/2025), la cola en
ese momento, si la campaña fue por urgencia y las horas acumuladas de horno caliente sin carga.
"""
import datetime as dt
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import verificar_modelo as vm  # noqa: E402

DIAS = int(sys.argv[1]) if len(sys.argv) > 1 else 120
NOMBRE = ["Apagado", "Acumulando", "Calentando", "Procesando", "Caliente sin carga", "Enfriando"]

JAVA = r"""import java.util.*;
public class CaserCronologia {
public static void main(String[] a) {
  int esc = Integer.parseInt(a[0]); double dias = Double.parseDouble(a[1]);
  final CaserLogicCheck m = new CaserLogicCheck(); int index = esc * 30;
  %ESCENARIO%
  m.semilla = 1; m.calentamientoModeloDias = 0; m.horizonteDias = 730; m.startup();
  final int[] prev = {-1};
  for (int k = 0; k <= dias * 24 * 4; k++) {
    m.agendar(k * 0.25, () -> {
      m.acumularVis();
      int e = m.estadoVis();
      if (e != prev[0]) {
        System.out.println(String.format(Locale.US, "EV;%.2f;%d;%d;%b;%.1f;%d", m.time(), e, m.nEnCola, m.campanaPrioridad,
          m.visHoras[4], m.visEncendidos));
        prev[0] = e;
      }
    });
  }
  m.agendar(dias * 24, () -> { m.acumularVis(); System.out.println(String.format(Locale.US, "FIN;%.1f;%.1f;%d;%.1f",
    m.visHoras[4], m.visHoras[3], m.visEncendidos, m.visTotal() / 1e6)); m.finishSimulation(); });
  m.correr(dias * 24 + 1);
}
}"""


def main():
    vm.jdk()
    x = vm.extraer(AQUI / "CaserHorno.alp")
    with tempfile.TemporaryDirectory(prefix="caser-crono-") as tmp:
        d = Path(tmp)
        vm.compilar_harness(x, d)
        esc = " ".join(f"m.{k} = {v};" for k, v in x.cor.items() if v and k not in ("archivoSalida", "semilla"))
        (d / "CaserCronologia.java").write_text(JAVA.replace("%ESCENARIO%", esc), encoding="utf-8")
        r = subprocess.run([str(vm.JAVAC), "-encoding", "UTF-8", "-nowarn", "-cp", str(d), "-d", str(d),
                            str(d / "CaserCronologia.java")], capture_output=True, text=True)
        if r.returncode:
            print(r.stdout, r.stderr)
            sys.exit("FALLA: no compila")
        t0 = dt.datetime(2025, 8, 18)
        for esc_i, nombre in ((0, "E0 regla actual"), (3, "E3 apagar enseguida")):
            r = subprocess.run([str(vm.JAVA), "-Xss8m", "-cp", str(d), "CaserCronologia", str(esc_i), str(DIAS)],
                               capture_output=True, text=True)
            if r.returncode:
                print(r.stdout, r.stderr)
                sys.exit("FALLA al correr " + nombre)
            print(f"\n## {nombre} · semilla 1 · primeros {DIAS} días")
            for ln in r.stdout.splitlines():
                p = ln.split(";")
                if p[0] == "EV":
                    t = float(p[1])
                    f = (t0 + dt.timedelta(hours=t)).strftime("%a %d/%m %H:%M")
                    urg = " (por urgencia)" if p[4] == "true" and int(p[2]) >= 0 and NOMBRE[int(p[2])] == "Calentando" else ""
                    print(f"día {t / 24:6.1f}  {f}  {NOMBRE[int(p[2])]:<20}{urg:<16} cola {p[3]:>3}  "
                          f"caliente sin carga acumulado {float(p[5]):6.1f} h  encendidos {p[6]}")
                elif p[0] == "FIN":
                    print(f"TOTAL {DIAS} días: caliente sin carga {p[1]} h, procesando {p[2]} h, encendidos {p[3]}, "
                          f"costo {p[4]} M$")


if __name__ == "__main__":
    main()
