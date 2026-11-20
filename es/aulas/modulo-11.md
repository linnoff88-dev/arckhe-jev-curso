# Módulo 11 — Operar y observar

Preparar logs, seguimiento y retorno sin perder control de la operación.

## Clase 11.1 — Observar antes de automatizar

El modo de observación significa que la nueva etapa calcula una sugerencia, pero el flujo anterior sigue siendo responsable de la decisión. Así podemos comparar el comportamiento con la operación real sin aplicar automáticamente los errores del piloto.

Registra las concordancias y los desacuerdos. Revisar solo los desacuerdos no basta, porque humano y modelo pueden concordar en una respuesta errada. Inspecciona también una muestra de concordancias. Observa el volumen de cada clase y los mensajes que no caben en la taxonomía.

Define la salida de esta fase antes de empezar. Precisión, cobertura, costo, tiempo de revisión y ausencia de fallas de integración pueden formar parte de los criterios. Si las metas no se demuestran, mantén la observación o finaliza la prueba. Automatizar porque “ya lleva una semana corriendo” no es un criterio de calidad.

### Práctica con los recursos actuales

Para experimentar sin clave en la raíz del repo jev: python3 -m pacotes.executar reunioes; python3 -m pacotes.qualidade reunioes; python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl. Las dos primeras usan datos y respuestas simulados; la tercera solo hace una vista previa. El guion complementario detalla el paso a tus propios datos.

### Ejemplo resuelto

El equipo recibe la cola sugerida al lado del encaminamiento actual. No sucede ningún cambio externo solo por la respuesta del modelo.

### Es tu turno

Un piloto tuvo pocos eventos de la clase cobro. ¿Es suficiente liberar todas las colas?

<details>
<summary>Revisar la respuesta comentada</summary>

No necesariamente. Puede faltar evidencia en esa clase. Reúne más ejemplos o limita la liberación a las rutas que realmente se evaluaron.

</details>

## Clase 11.2 — Registrar y entender fallas

Un log útil vincula el evento con la versión de la pregunta, la política y el modelo usado. También registra el tiempo, los tokens, el resultado y cualquier corrección. Sin esa información, es difícil saber si un cambio de comportamiento vino del modelo, del contexto o de una alteración en el código.

No confundas trazabilidad con guardar todo para siempre. Minimiza datos, limita el acceso y define la retención según el entorno real. Para reportes públicos, usa ejemplos ficticios o autorizados. Las credenciales nunca entran en el log.

Al corregir un error, busca la menor protección suficiente. Un campo ausente puede pedir validación; un duplicado puede pedir idempotencia; un bucle puede pedir un tope; una decisión incorrecta puede pedir criterios más claros y una prueba nueva. La categoría de la falla ayuda: calidad del juicio, preparación del contexto, contrato, red o política operativa.

### Práctica con los recursos actuales

Un lote puede usar de uno a cuatro workers y espaciar el inicio de las consultas. Ese espaciamiento no controla cada retry HTTP y no sustituye un límite distribuido por tokens. Límite de eventos no es presupuesto en dólares. Después de retries, conserva el costo desconocido cuando solo está disponible el consumo de la última respuesta.

### Ejemplo resuelto

Evento 42: pregunta v2, política v1, modelo fijado, respuesta válida, sugerencia corregida de ventas para soporte. El texto sensible queda fuera del reporte público.

### Es tu turno

Un retry procesa dos veces el mismo ticket. ¿Reescribir la pregunta resuelve?

<details>
<summary>Revisar la respuesta comentada</summary>

No. La corrección es de ejecución: identificador idempotente y control de duplicados, con una prueba que reproduzca el retry.

</details>

## Clase 11.3 — Actualizar o volver atrás

Un alias de modelo puede apuntar a una versión nueva sin cambiar tu solicitud. Esto facilita las actualizaciones, pero dificulta atribuir la variación cuando los umbrales se ajustaron para una versión anterior. Registra el identificador resuelto y fija versiones en los experimentos que deban reproducirse.

Antes de cambiar la versión en operación, ejecuta el conjunto de evaluación y compara los errores. Una media mejor puede esconder una regresión en una clase importante. Si la política depende de confidence, vuelve a verificar umbrales y cobertura.

Ten una forma simple de desactivar la nueva etapa y volver al flujo anterior. El retorno no debería exigir reconstruir la aplicación. Los criterios de suspensión incluyen error relevante, indisponibilidad persistente y costo inesperado. Actualizar es un cambio controlado, no solo reemplazar un nombre en la configuración.

### Profundización de la versión 1.2.0

Para triaje de código, separa comentario correcto de comentario útil. El clasificador puede señalar una prueba debilitada, pero las pruebas y el análisis estático siguen siendo necesarios. Muestra también lo que el filtro descartó para descubrir falsos negativos. Practica en el L10.

### Ejemplo resuelto

Llega una versión nueva: evalúa con las mismas preguntas y datos reservados; revisa métricas por clase; libera gradualmente o mantén la versión anterior.

### Es tu turno

¿Qué registrar para reproducir una decisión después de una actualización?

<details>
<summary>Revisar la respuesta comentada</summary>

Modelo resuelto, versión de las preguntas y criterios, versión de la política e identificación del contexto autorizado usado en el evento.

</details>

[Volver al índice](../README.md)
