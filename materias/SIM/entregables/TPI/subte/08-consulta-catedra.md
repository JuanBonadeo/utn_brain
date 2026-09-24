---
title: "Consulta a la cátedra - TPI Subte Constitución"
subject: "Simulación"
status: "Borrador para enviar (T0.1). Lo envía Juan; Claude no manda nada."
---

# Consulta a la cátedra (borrador)

**Canal:** Classroom o correo a los docentes. **Asunto sugerido:** TPI Bonadeo-Estevez (molinetes de
Constitución): cinco consultas antes de producir corridas.

Cuando llegue la respuesta, registrarla en `materias/SIM/SIM.md` (sección del TPI subte y Log) y marcar en
[`07-plan-tpi.md`](07-plan-tpi.md) §3 qué decisiones pasan de provisorias a firmes.

---

Buenas tardes, profesores:

Somos Juan Cruz Bonadeo y Matías Estevez (comisión 401), con el TPI sobre el acceso desde el Roca a la Línea C
en Constitución. Antes de lanzar las corridas de producción queremos confirmar cinco puntos.

**1. Cantidad de molinetes de E1.** Al procesar el dataset abierto de SBASE ("Subte: Viajes Molinetes",
2026) encontramos que el vestíbulo Principal tiene 22 identificadores de molinete, no 28. Los 28 que
mencionamos en la propuesta eran el total de la estación, contando los 8 de Plaza. Proponemos:

- E0 = 20 molinetes habilitados (la disponibilidad observada por ventana es de 19,5 en promedio);
- E1 = los 22 del vestíbulo Principal;
- si el tiempo de cómputo alcanza, un alternativo con una ampliación hipotética a 28, declarando que el
  espacio físico no está verificado.

¿Les parece correcto reemplazar "abrir los 28" por "habilitar los 22 del vestíbulo Principal"?

**2. Parámetros sin dato publicado.** Pedimos datos a SBASE/Emova y a Trenes Argentinos, pero todavía no
respondieron y no podemos medir en persona. Proponemos trabajar con rangos tomados de fuentes técnicas
citables, con un valor intermedio para la comparación principal y los extremos como análisis de sensibilidad:

| Parámetro | Optimista | Intermedio | Pesimista | Fuente |
|---|---:|---:|---:|---|
| Tiempo de validación por pasajero | 2,0 s | 2,4 s | 3,0 s | TCQSM 3.ª ed. (TRB, 2013), Exh. 10-27; Station Planning Standards de London Underground (2012) §3.3; cota del propio dataset SBASE (≤ 3,66 s) |
| Tiempo de descarga de un tren al vestíbulo | ≈ 45 s | ≈ 75 s | 120 s | TCQSM Exh. 8-12 (tiempo por pasajero y puerta); criterio de vaciado en 2 min del SPSG |
| Demora del andén del Roca al vestíbulo | D/1,25 + h/0,30 | D/0,95 + h/0,30 | D/0,63 + h/0,20 | Velocidades de marcha y escaleras del TCQSM y del SPSG; D y h medidos sobre imagen satelital |
| Proporción de la demanda que llega en trenes del Roca | 0,70 | 0,80 | 0,90 | Supuesto explícito: no encontramos una fuente pública de transferencia Roca → Línea C |

¿Aceptan este enfoque de rangos con fuente? Si en el camino llegan datos de los organismos, reemplazan al
valor intermedio.

**3. Alcance de E2 y E3.** E2 (desvío a Plaza) exige modelar un segundo vestíbulo del que no tenemos
geometría, y E3 (validación EMV/QR) no tiene un tiempo de validación citable; además, el único molinete
EMV/QR está en Plaza. Proponemos dejarlos como extensiones implementadas en el modelo lógico, sin resultados,
y como trabajo futuro. El informe compararía E0 contra E1. ¿Están de acuerdo?

**4. Formato del informe y entregas parciales.** ¿Hay una plantilla LaTeX o unas "pautas de entregas
parciales" para 2026? ¿Hay avances parciales obligatorios antes de la entrega final? ¿Cuáles son las fechas
de entrega y de presentación?

**5. Carátula.** ¿La carátula lleva los nombres de los docentes? ¿La comisión se escribe 401 o 4K01?

Muchas gracias.

Juan Cruz Bonadeo (legajo 53533) y Matías Estevez (legajo 53528)

---

## Notas para el envío

- Confirmá los legajos y la comisión antes de mandarlo (vienen de `scripts/datos-alumno.json` y del plan).
- Si el formulario del tema hay que reenviarlo (T7.4), conviene mandar las dos cosas juntas.
- Las fuentes completas están en [`07-plan-tpi.md`](07-plan-tpi.md) §14; no hace falta adjuntarlas salvo que
  las pidan.
