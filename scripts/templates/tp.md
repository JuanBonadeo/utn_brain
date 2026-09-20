---
# ── Carátula ────────────────────────────────────────────────────────────────
# Institución, facultad, carrera, alumno y legajo salen de
# scripts/datos-alumno.json. Acá va solo lo que cambia por trabajo.
# Borrá las líneas que no apliquen (grupo, etapa, subtitulo son opcionales).

codigo: XXX                      # IO, IYS, SIM, RD, ASI, ICS, LEG, TPA, SGD, IPP
materia: Nombre completo de la materia
tipo: Trabajo Práctico N.º 1     # o "Trabajo Final Integrador", "Informe", etc.
titulo: Título del trabajo
subtitulo: Bajada opcional, una línea o dos
comision:                        # si se omite, la toma de datos-alumno.json según el código
grupo:
etapa:
fecha: DD/MM/AAAA

profesores:
  - Nombre Apellido

# Para trabajo grupal, una línea por integrante en orden alfabético:
# alumnos:
#   - Apellido, Nombre | correo@ejemplo.com | 00000
#   - Bonadeo, Juan Cruz | juancruzbonadeo04@gmail.com | 53533
---

## 1. Introducción

Cada `## ` de este archivo entra automáticamente al índice. Numerá los títulos
a mano (`## 1.`, `## 2.`) porque así aparecen en el índice.

Texto normal: sale justificado, Arial 10, interlineado 1.5. **Negrita** e
*itálica* funcionan. Las listas y las citas también:

- Primer ítem
- Segundo ítem

> Una cita textual va así, y abajo la referencia.
> — Autor, *Obra*, Editorial, año.

## 2. Desarrollo

### 2.1 Un subtítulo

Las tablas se numeran a mano y **se mencionan en el cuerpo** (la cátedra suele
pedirlo explícitamente): como muestra la Tabla 1, …

**Tabla 1.** Título descriptivo de la tabla

| Columna A | Columna B |
|---|---|
| dato | dato |

*Fuente: elaboración propia.*

## 3. Conclusiones

## 4. Referencias bibliográficas

Apellido, N. (Año). *Título de la obra*. Ciudad: Editorial.

## 5. Anexos
