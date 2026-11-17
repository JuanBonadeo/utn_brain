## Clave para los objetivos de negocio y de TI

| | **Objetivo de negocio** | **Objetivo de TI** |
|---|---|---|
| **Qué es** | El **resultado** que quiere el banco | La **capacidad tecnológica** que lo habilita |
| **Cómo se te ocurre** | Partí de lo que el proyecto cambia y preguntá **"¿y eso para qué?"** hasta llegar a plata, clientes o tiempo | Partí del objetivo de negocio y preguntá **"¿cómo?"**: qué tiene que existir y funcionar en los sistemas para que pase |
| **De qué habla** | Ganar más · gastar menos · cliente más satisfecho o que reclame menos · hacer las cosas más rápido. Tres objetivos, tres dimensiones distintas | Disponibilidad · tiempo de respuesta · % de errores · cobertura · incidentes de seguridad |
| **Prueba del gerente** | Lo entiende alguien de Banca Minorista sin saber de tecnología. Si aparece API, token, servidor o "implementar", es de TI | Al revés: **sí** habla de sistemas, y lo mide el CIO |
| **Errores típicos** | Poner lo que se construye ("implementar X") · "mejorar la experiencia" sin número ni plazo | Copiar el alcance ("implementar la plataforma") sin condición medible · meter un resultado de negocio ("bajar los reclamos") |

### Para los dos

- **SMART:**

  ```
  [verbo de resultado] + [qué se mide] + de [línea base] a [valor] + antes de [fecha]
  ```

  La línea base podés suponerla, pero escribila.
- **Cadena:** cada objetivo de TI sostiene a uno de negocio. El de TI **vence antes**, porque la capacidad tiene que existir primero.
- **Alineación:** los dos tienen que estar alineados con la **visión y los valores** del contexto.

### Ejemplo encadenado (Omnicanalidad)

> **Negocio:** reducir del 25% al 15% la proporción de transferencias que los clientes inician en Home Banking o en la app y no confirman dentro de las 24 h, en 6 meses desde que se habilita terminar en un canal una operación empezada en el otro. *Métrica: no confirmadas sobre iniciadas, reporte mensual para Banca Minorista.*
>
> **De TI que lo sostiene:** se arma con el "¿cómo?":
> - ¿Dónde queda guardada la operación para que el otro canal la encuentre?
> - ¿Qué disponibilidad y tiempo de respuesta necesita?
> - ¿Un solo token para los dos canales?

*Sale de la cátedra (wiki U1 §6.8 y clase de repaso del 11/11): negocio vs TI, la cadena hacia arriba, SMART en los dos niveles, "primero desde el negocio y después SMART" y la alineación con visión y valores. Es método general, no de la cátedra: el "¿para qué?" / "¿cómo?" y las pruebas del gerente.*
