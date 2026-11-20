# Módulo 10 — Medir calidad de verdad

Comparar métodos sin confundir ejemplos ajustados con evidencia independiente.

## Clase 10.1 — Construir referencia humana

Una evaluación comienza con definir qué es correcto. Si las etiquetas cambian de persona a persona, la métrica puede estar midiendo desacuerdo de proceso. Crea una guía de etiquetado, revisa ejemplos y documenta los casos que no encajan bien.

Separa desarrollo, calibración y prueba. Usa desarrollo para mejorar preguntas; calibración para elegir umbrales; prueba para verificar la política congelada. Los mensajes de la misma conversación no pueden quedar en particiones diferentes, porque eso facilita reconocer contenido ya visto. Cuando haya variación en el tiempo, evalúa también datos posteriores.

Los 24 tickets ficticios del laboratorio sirven para aprender a ejecutar y leer una evaluación. No son una muestra representativa de una empresa ni demuestran idoneidad para producción. Un dataset operativo debe cubrir clases, ambigüedades y cambios del tráfico real, con revisión humana y protección de los datos.

### Ejemplo resuelto

Una conversación con tres mensajes debe quedar completa en la misma partición. Dividir los mensajes entre entrenamiento de preguntas y prueba causa filtración de contexto.

### Es tu turno

¿Se puede ajustar la pregunta después de mirar el error de la prueba final y divulgar la nueva tasa en la misma prueba como independiente?

<details>
<summary>Revisar la respuesta comentada</summary>

No. La prueba se usó en el ajuste. Es necesario reservar otro conjunto para una nueva evaluación independiente.

</details>

## Clase 10.2 — Comparar alternativas

Usa la misma tarea y los mismos datos para comparar reglas, Jev, un modelo generativo con salida estructurada y un flujo híbrido. Registra configuraciones y versiones. Las diferencias en entrada o en criterios vuelven la comparación difícil de interpretar.

La exactitud informa la proporción total de aciertos, pero puede ocultar clases pequeñas. La matriz de confusión muestra hacia dónde se envió cada clase. Macro-F1 da el mismo peso a las clases, aunque también necesita leerse con los conteos. Observa especialmente el error que tiene mayor costo operativo.

Mide latencia extremo a extremo y el costo de todos los intentos. El resultado de la línea base léxica de este proyecto es reproducible por la CLI: presenta aciertos y errores conocidos en el conjunto ficticio. No compares este tiempo local de reglas con latencia de red como si fueran lo mismo. El experimento Jev real solo se podrá reportar después de ejecutarlo con acceso al servicio.

### Práctica con los recursos actuales

El evaluador complementario paquetes.calidad exige una referencia para cada pregunta. Choice mide exactitud; Noul mide exactitud con corte 0,5 y Brier; Score mide error absoluto y error normalizado por la escala. El corte usado en la métrica no define la política de acción. Los errores de contrato reducen cobertura y exactitud; MAE y Brier usan solo respuestas válidas, por eso deben leerse junto con la cobertura.

### Ejemplo resuelto

python3 -m jev_lab batch data/tickets-sinteticos.jsonl --out reports/baseline produ[c]e metrics.json y predictions.csv, usando reglas locales.

### Es tu turno

Una clase muy común tiene 99% de acierto y otra importante tiene 40%. ¿Con la media global basta?

<details>
<summary>Revisar la respuesta comentada</summary>

No. Reporta métricas por clase, soporte muestral, matriz de confusión y costo de los errores. La media puede ocultar la clase importante.

</details>

## Clase 10.3 — Elegir y congelar umbrales

Al aumentar un umbral, normalmente menos respuestas pasan a la sugerencia automática. Esto puede reducir algunos errores, pero aumenta la revisión y puede dejar pasar errores más confiables. Necesitamos medir dos cosas juntas: la calidad de los casos aceptados y la cobertura, la fracción de casos que la política acepta.

Elige el umbral en el conjunto de calibración y congélalo antes de la prueba. Registra si usa la probabilidad de la clase, confidence o ambos. No copies el umbral de una primitiva a otra, de un idioma a otro o de una versión a otra sin evaluación.

La incertidumbre de la medición importa. Si diez ejemplos pasaron sin error, todavía no tenemos evidencia de que la tasa de error sea pequeña. Cuanto más estrecha la meta, mayor tiende a ser la necesidad de datos. Cuando la muestra es insuficiente, la conclusión correcta puede ser recolectar más ejemplos, en lugar de declarar éxito.

### Profundización de la versión 1.2.0

La CLI experiment registra dataset, template, política, modelo, fallas y procedencia. El modo replay permite comparar respuestas externas, incluido LLM, pero no autentica el origen declarado. Una comparación de modelo aislado debe tener entrada equivalente; una comparación de flujo mide la tarea completa.

Agrupa las predicciones por rangos de confianza para investigar dónde aparecen los errores, preservando el tamaño de cada grupo y clase. Pocos ejemplos por rango generan conclusiones frágiles. Un cambio de criterio que corrige un caso conocido debe reejecutarse en un conjunto independiente; no basta con demostrar el caso corregido.

### Ejemplo resuelto

En el laboratorio didáctico, varía confidence de 0,90 a 0,95. La respuesta ficticia con confidence 0,91 pasa de sugerencia a revisión.

### Es tu turno

¿Por qué esta interacción con valores inventados no comprueba que 0,95 sea el umbral correcto?

<details>
<summary>Revisar la respuesta comentada</summary>

Porque no mide respuestas reales contra etiquetas independientes. Solo demuestra cómo reacciona una política a los números.

</details>

[Volver al índice](../README.md)
