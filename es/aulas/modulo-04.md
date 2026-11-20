# Módulo 4 — Costo y elección del primer caso

Calcular la viabilidad incluyendo el trabajo que ocurre después del modelo.

## Clase 4.1 — La cuenta de diez mil tokens

Se debe convertir una tarifa por millón de tokens antes de multiplicarla por el volumen de llamadas. En la referencia de precios consultada el 18/09/2026, la entrada de Jev cuesta US$ 0,042 por millón. Para 10.000 tokens totales de entrada, dividimos 10.000 entre un millón y multiplicamos por 0,042. El resultado es US$ 0,00042.

Mil llamadas iguales costarían US$ 0,42 de entrada; diez mil, US$ 4,20; cien mil, US$ 42. Observa las cifras decimales. Un error con cero cambia toda la comparación. Trabaja en una sola moneda y mantén separadas la estimación y el cobro real.

Los tokens no son palabras, caracteres ni documentos. Un contexto largo y criterios detallados pueden consumir más entrada. Para el presupuesto definitivo, usa el conteo devuelto por el servicio y verifica la tarifa de la ruta utilizada. El laboratorio permite editar el precio para actualizar la cuenta sin reescribir el curso.

### Ejemplo resuelto

Costo = llamadas × tokens totales promedio ÷ 1.000.000 × precio por millón. En 10.000 × 10.000 tokens, la estimación es US$ 4,20.

### Es tu turno

Calcula 100.000 llamadas de 2.000 tokens en la tarifa de referencia.

<details>
<summary>Revisar la respuesta comentada</summary>

100.000 × 2.000 ÷ 1.000.000 × 0,042 = US$ 8,40. Es solo la entrada del modelo, sin otros costos.

</details>

## Clase 4.2 — Costo de todo el proceso

Una llamada barata no garantiza un proceso barato. Después del triaje puede haber modelo generativo, revisión humana, extracción de texto, almacenamiento y retrabajo. Si el error envía una solicitud al equipo equivocado, el costo real incluye el tiempo de corregir el encaminamiento.

Compara dos operaciones completas. En la referencia, todos los eventos siguen el flujo actual. En el híbrido, todos pasan por el triaje y una parte sigue al modelo mayor o a la revisión. Las llamadas residuales pueden ser justo las más difíciles y caras; no asumas que cuestan el mismo promedio que las anteriores.

Incluye además el esfuerzo de implementación amortizado durante el período de uso. Un proceso de poco volumen puede no justificar una integración compleja, incluso con una gran economía porcentual de tokens. Haz un análisis de sensibilidad: ¿el resultado sigue siendo positivo si la tasa de fallback se duplica o si la revisión humana tarda el doble?

### Ejemplo resuelto

Escenario ficticio: baseline US$ 1.000; Jev US$ 8,40; LLM residual US$ 200. Economía bruta US$ 791,60, antes de revisión, infraestructura e implementación.

### Es tu turno

Agrega US$ 500 de revisión y US$ 400 de implementación amortizada al escenario. ¿Aún economiza?

<details>
<summary>Revisar la respuesta comentada</summary>

No. El híbrido suma US$ 1.108,40 y supera la baseline de US$ 1.000. La economía de tokens se consumió en los otros costos.

</details>

## Clase 4.3 — Elegir un piloto

El primer piloto debe responder una pregunta de negocio pequeña y verificable. “Automatizar toda la empresa” no ofrece un criterio de conclusión. “Sugerir la cola de tickets en portugués sin aumentar el retrabajo” permite reunir ejemplos, revisar los resultados y decidir si vale la pena avanzar.

Prefiere un caso con alternativas claras, datos disponibles, frecuencia suficiente y consecuencia reversible. También es necesario alguien que sepa decir qué es correcto. Si ni las personas están de acuerdo sobre las categorías, la primera tarea es ajustar el proceso y el etiquetado, no elegir el modelo.

La matriz de prioridad puede combinar volumen, tiempo humano por caso, facilidad para obtener referencia e impacto del error. No uses la matriz como matemática exacta: hace visible el debate. Un caso llamativo de navegador o agentes puede venir después de un triaje simple que demuestre el valor y revele las limitaciones del dominio.

### Profundización de la versión 1.2.0

El costo de una llamada no mide el flujo. En la calculadora ampliada, incluye porcentaje de fallback, precio por intento del LLM, minutos de revisión e infraestructura. Un costo desconocido después de fallar o hacer retry no debe lanzarse como cero.

### Ejemplo resuelto

Piloto recomendado: sugerir soporte, cobro o ventas en tickets. Fase inicial: solo observar la sugerencia y compararla con el encaminamiento humano.

### Es tu turno

Compara el triaje de tickets con la ejecución automática de reembolsos. ¿Cuál empieza primero y por qué?

<details>
<summary>Revisar la respuesta comentada</summary>

Triaje: consecuencia reversible, revisión más simple y menor necesidad de permisos. El reembolso exige un proyecto separado de reglas, autorización y control.

</details>

[Volver al índice](../README.md)
