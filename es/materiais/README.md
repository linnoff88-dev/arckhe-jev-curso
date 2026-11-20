# Laboratorios — material ficticio y de autoría

Cada archivo incluye plantillas para autocorrección. Intenta resolver antes de consultar la respuesta. Ningún dataset representa tráfico operacional real.

| Laboratorio | Archivo | Actividad y criterio |
|---|---|---|
| L1 — formular | [12 tareas](l1-formulacao.csv) | Elegir regla, Choice, Noul, Score o generación y justificar. |
| L2 — hotel | [6 políticas](l2-hoteis.json) | Distinguir dinero, crédito, falta de devolución, conflicto e insuficiencia. |
| L3 — atención | [30 tickets](l3-tickets.json) | Clasificar colas; comparar con la etiqueta y explicar divergencias. |
| L4 — evidencias | [8 pares y 4 cláusulas](l4-evidencias.json) | Identificar respaldo y omisión solo en el material proporcionado. |
| L5 — rutas | [12 tareas](l5-rotas.json) | Elegir capacidad; definir permiso y límite de intentos por separado. |
| L6 — DOM | [5 listas](l6-dom.json) | Seleccionar candidato, abstenerse o pedir revisión por permiso. |
| L7 — economía | [Planilla CSV](l7-custos.csv) | Rehacer costos y agregar fallback, trabajo humano e implementación. |
| L8 — umbrales | [10 predicciones simuladas](l8-predicoes-simuladas.json) | Comparar cobertura y error al aceptar confidence ≥0,90 o ≥0,95. |

## Solucionario comentado del L8

En ≥0,90: seis aceptadas, cuatro correctas; cobertura 60%, precisión entre aceptadas 66,67%.
En ≥0,95: cuatro aceptadas, tres correctas; cobertura 40%, precisión entre aceptadas 75%.
El error con confidence 0,97 permanece aceptado en ambos casos. Aumentar el umbral no elimina todos los errores. Estos números son inventados para el ejercicio, no resultados Jev.

## Integración con la aplicación

[Diez casos completos](dez-casos.json) contienen estado, preguntas, criterios, respuesta simulada y comentario. El [laboratorio web](https://inematds.github.io/jev/app/) permite explorar los mismos casos.

## Entrega final

Completa el [modelo de proyecto](projeto-final.md). Aprobación sugerida: 75/100 en la rúbrica, sin presentar una simulación como medición ni asignar permisos al modelo. La nota es una autoevaluación educativa, no una certificación de seguridad operacional.

## Profundización — L9 a L12

Todos incluyen situaciones ficticias y solucionarios.

| Laboratorio | Material | Entrega |
|---|---|---|
| L9 — Skills | [Ocho pedidos](l9-skills.json) | Seleccionar una skill o ninguna; justificar según la intención. |
| L10 — Código | [Seis situaciones](l10-comentarios-diff.json) | Separar corrección, utilidad y evidencia de prueba. |
| L11 — Evidencias | [Seis pasajes](l11-evidencias.json) | Preservar contradicciones, negaciones e IDs. |
| L12 — Demos | [Ocho alegaciones](l12-auditoria-demos.json) | Emitir un veredicto y listar la evidencia aún necesaria. |

[Veinte casos de la aplicación](vinte-casos.json) incluyen las tres primitivas y preguntas combinadas. El archivo anterior con diez casos permanece como material inicial. Para práctica técnica, usa la [guía de experimentos](https://github.com/inematds/jev/blob/main/docs/08-experimentos.md).

## Guía complementaria actualizada

[Flujos prácticos: 17 paquetes, lotes y evaluación por pregunta](fluxos-praticos.md). Complementa las clases existentes y los 12 laboratorios; no agrega un laboratorio numerado.
