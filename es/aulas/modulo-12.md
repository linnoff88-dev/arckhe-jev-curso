# Módulo 12 — Proyecto final

Entregar una decisión de adopción fundamentada, incluso cuando la respuesta sea no automatizar.

## Clase 12.1 — Especificar la clasificación

Tu proyecto final es un triaje de atención en portugués. Empieza describiendo quién recibe los tickets, qué colas existen y qué problema quieres reducir. Evita prometer automatización total. La primera entrega es una especificación que otra persona pueda revisar.

Define los criterios de cada alternativa, los casos ambiguos y el manejo de información ausente. Agrega cinco ejemplos difíciles: negación, dos intenciones, texto incompleto, sinónimo e instrucción indebida dentro del ticket. Muestra cómo debería tratarse cada uno y por qué.

Después, dibuja la política externa al modelo. Define acciones permitidas, revisión, fallas de contrato, plazo y límite de intentos. Incluye presupuesto y plan de evaluación. El proyecto sin código puede usar una hoja de cálculo; el técnico debe añadir requerimientos, pruebas y un informe reproducible. Ambos deben separar hechos, hipótesis y resultados.

### Ejemplo resuelto

Entrega: taxonomía + cinco casos difíciles + preguntas + política + diagrama + presupuesto + protocolo de evaluación + plan de retorno.

### Es tu turno

Escribe una frase que describa el éxito de tu piloto sin usar “IA más inteligente”.

<details>
<summary>Revisar la respuesta comentada</summary>

Ejemplo: reducir el tiempo de triaje manteniendo el error por cola dentro del límite acordado, con un costo total menor y posibilidad de corrección humana.

</details>

## Clase 12.2 — Evaluar la propuesta

Presente tu evaluación de modo que otra persona pueda repetirla. Identifica el dataset, su origen, las particiones y las configuraciones. Muestra la cantidad de casos por clase, los errores importantes y las limitaciones. Un gráfico de exactitud sin contexto no es suficiente.

Si ejecutaste solo la baseline de reglas, dilo. Si usaste respuestas simuladas, márcalas como simulación. Si hiciste una llamada real, registra el modelo y el uso reportado. Estas distinciones no disminuyen el proyecto; hacen tu conclusión confiable y muestran qué etapa aún falta.

La rúbrica considera formulación, política, evidencia, economía y reproducibilidad. Un proyecto que reconoce insuficiencia de datos puede ser mejor que un proyecto que anuncia éxito con números inventados. Incluye ejemplos en los que el sistema se equivocó y explica la corrección menor propuesta, sin ajustar y medir todo en el mismo conjunto.

### Ejemplo resuelto

Reporte honesto: “baseline léxica, 24 ejemplos ficticios, 20 aciertos; no mide Jev ni representa el tráfico de producción”.

### Es tu turno

¿Qué información falta para transformar el reporte del ejemplo en evidencia de adopción de Jev?

<details>
<summary>Revisar la respuesta comentada</summary>

Ejecución real de Jev y alternativas, datos representativos revisados, política calibrada en un conjunto separado, métricas finales y costo completo del flujo.

</details>

## Clase 12.3 — Decidir adopción

La última etapa es una decisión de proyecto. Hay tres salidas legítimas: continuar con una implementación limitada, recopilar más datos o no adoptar. La elección depende de calidad, costo, cobertura, esfuerzo de revisión y capacidad operativa, no de la popularidad del modelo.

Si decides continuar, limita la primera ruta a una acción reversible y sigue las correcciones. Si decides recopilar más datos, di exactamente qué duda falta resolver: una clase rara, un idioma, un tipo de ambigüedad o la diferencia de costo. Si decides no adoptar, conserva la evaluación para evitar repetir el mismo experimento sin aprender.

El principio que atraviesa el curso es simple: la interpretación probabilística funciona mejor dentro de software que conoce sus límites. Los modelos ayudan a juzgar; los criterios y la evidencia permiten evaluar; el código restringe la ejecución; las personas asumen las decisiones que exigen responsabilidad. Una arquitectura bien definida vale más que una promesa aislada de velocidad.

### Profundización de la versión 1.2.0

En el proyecto final, entrega un report.json y el análisis de los errores, o identifica claramente por qué el resultado aún está simulado. Defender recopilar más datos o no adoptar es una conclusión válida. La calidad, el costo completo y la cobertura deben sostener la decisión.

### Práctica con los recursos actuales

Elige uno de los 17 paquetes como punto de partida, sin confundir un template ejecutable con un conector listo. El piloto debe declarar quién recopila los eventos, quién revisa, dónde quedan los registros, cómo medir los descartes incorrectos y quién autoriza acciones. Mil clasificaciones rápidas no demuestran mil decisiones correctas.

### Ejemplo resuelto

Decisión posible: mantener reglas para casos exactos, observar Jev en los demás y exigir revisión hasta obtener evidencia suficiente en portugués.

### Es tu turno

Dale una condición objetiva a cada salida: continuar, recopilar más datos y no adoptar.

<details>
<summary>Revisar la respuesta comentada</summary>

Continuar: metas demostradas con volumen suficiente. Recopilar: resultado inconcluso en clases importantes. No adoptar: la calidad o el costo total no justifican el cambio después de una prueba adecuada.

</details>

[Volver al índice](../README.md)
