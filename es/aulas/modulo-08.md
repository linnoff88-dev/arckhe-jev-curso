# Módulo 8 — Navegador y aplicaciones sensibles

Distinguir selección de candidatos de ejecución y supervisión profesional.

## Clase 8.1 — Elegir elemento por el texto

La modalidad documentada de Jev consultada para este curso es texto. Por lo tanto, un flujo de navegador necesita preparar una representación textual: elementos del DOM, nombres accesibles o una lista de candidatos. Enviar una captura de pantalla directamente no corresponde a este contrato.

Una Choice puede seleccionar el identificador de un candidato. El código consulta el DOM de nuevo antes de actuar, ya que la página pudo haber cambiado desde la extracción. Si el elemento no existe o su función es diferente, el flujo debe detenerse o actualizar los candidatos, sin hacer clic en una posición antigua por aproximación.

Incluye una opción ninguno y trata la ambigüedad entre elementos parecidos. Medir solo la rapidez del clasificador omite extracción, navegación y ejecución. El desempeño relevante es completar la tarea correctamente, con límites de acción. En este curso, el ejemplo solo elige un ID textual y no controla un navegador externo.

### Ejemplo resuelto

Lista: nav-home = Inicio; download-pdf = Descargar informe; remove-account = Eliminar cuenta. Para descargar el informe, el candidato es download-pdf.

### Es tu turno

El botón cambió después de la clasificación. ¿Reutilizar la coordenada antigua es aceptable?

<details>
<summary>Revisar la respuesta comentada</summary>

No. Valida el elemento actual por el identificador y su función, o vuelve a extraer. La decisión no es autorización para hacer clic en cualquier posición.

</details>

## Clase 8.2 — Organizar una revisión clínica ficticia

Este caso es un ejercicio administrativo con datos inventados. La tarea es reconocer si un campo obligatorio está completo y organizar una cola para revisión humana. No estamos clasificando enfermedades, recomendando tratamiento ni priorizando pacientes reales.

Una ficha con el campo de alergias vacío no demuestra que la persona no tenga alergias. Solo muestra ausencia de información. La política del ejercicio determina que este caso se derive al profesional responsable para completar la ficha. Incluso una respuesta muy confiada elimina la necesidad de esa revisión.

En un dominio sensible, es especialmente importante declarar el límite de la actividad. El mismo software usado para un ejercicio no se vuelve adecuado para uso clínico real solo por tener una interfaz bonita. Una implementación real exigiría un diseño específico, profesionales responsables y validación en el contexto correspondiente. Aquí aprendemos a mantener el alcance administrativo y la opción de insuficiencia.

### Ejemplo resuelto

Campo obligatorio vacío → revisar. Nunca traduzcas el vacío como “sin alergias”. El laboratorio mantiene revisión obligatoria en este caso.

### Es tu turno

¿Por qué un umbral más alto de confidence no convierte este ejercicio en un sistema de diagnóstico?

<details>
<summary>Revisar la respuesta comentada</summary>

Porque el tipo de tarea, los datos, la validación y la responsabilidad son diferentes. Un número alto no crea capacidad clínica ni autorización para usarlo.

</details>

## Clase 8.3 — Organizar alertas ficticias

Considera un flujo inventado de seguimiento de documentos financieros. La política del ejercicio indica que hay que revisar una rectificación, dar seguimiento a una actualización pertinente y archivar noticias sin relación con el tema. El objetivo es organizar información, no decidir inversiones.

Una clasificación debe basarse en la política y en el documento proporcionados. “El precio bajó” no define por sí solo qué acción tomar; el sistema necesita conocer la regla que está aplicando. Para un prototipo educativo, mantenemos la derivación supervisada y no conectamos la ejecución de transacciones.

El error más importante puede ser el descarte indebido de algo relevante. Por eso, la evaluación debe observar falsos negativos y no solo la proporción total de aciertos. Una cola que parece muy eficiente por archivar casi todo puede estar ocultando información. La revisión debe incluir muestras de los elementos archivados, además de las alertas destacadas.

### Profundización de la versión 1.2.0

En el navegador, elige por DOM, valida si el elemento todavía existe, ejecuta la acción permitida y prueba el efecto. Un campo completado puede usar un dato ya conocido; eso no significa generación libre por Jev. El tiempo de animación, el tiempo de inferencia y el éxito final deben separarse.

### Ejemplo resuelto

“El emisor rectificó el comprobante” + política “las rectificaciones van a revisión” → revisar. Sin orden de compra o venta.

### Es tu turno

Una evaluación revisa solo las alertas seleccionadas. ¿Qué problema deja de observar?

<details>
<summary>Revisar la respuesta comentada</summary>

Las alertas relevantes descartadas. También es necesario auditar lo archivado para medir falsos negativos.

</details>

[Volver al índice](../README.md)
