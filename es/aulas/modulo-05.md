# Módulo 5 — Atención y transcripciones

Aplicar decisiones a mensajes y distinguir ausencia de evidencia de respuesta negativa.

## Clase 5.1 — Encaminar tickets

Empieza por la definición de las colas. El ejemplo del laboratorio usa soporte para dificultad técnica, cobro para asuntos de pago y ventas para interés en contratar. Un mensaje que no permite distinguir esas intenciones queda como insuficiente. Los equipos reales pueden necesitar otra taxonomía, pero la regla debe ser explícita.

Para evaluar, usa textos variados. “Pagué dos veces” y “el dinero salió duplicado” expresan algo cercano con palabras diferentes. Una baseline léxica puede reconocer la primera y fallar con la segunda. Eso hace útil comparar un modelo, sin asumir que ganará en todas las clases.

El resultado del cribado es una sugerencia. La interfaz debe permitir que la persona corrija y registre esa corrección sin perder el historial. No inventes un mensaje para el cliente ni confirmes un reembolso a partir de la clasificación. La aplicación de esta entrega no ejecuta esas acciones: ayuda a probar la decisión antes de conectarla a una operación.

### Práctica con los recursos actuales

Aplicación ampliada: bandeja de entrada, comentarios de YouTube y comunidades pueden compartir el mismo núcleo, pero necesitan criterios propios. Un recibo no es una duda de soporte; una manifestación de insatisfacción no comprueba intención de salir. En el proyecto, estos flujos están en los paquetes bandeja-entrada, comentarios-youtube y comunidades.

### Ejemplo resuelto

Abre el caso “Cribado de atención” en el laboratorio. La respuesta simulada sugiere cobro y explica por qué esa sugerencia no autoriza un reembolso.

### Es tu turno

Clasifica: “no puedo entrar”, “¿cuánto cuesta participar?” y “hola, necesito ayuda”.

<details>
<summary>Revisar la respuesta comentada</summary>

Soporte, ventas e insuficiente, respectivamente. El último mensaje no ofrece una intención específica.

</details>

## Clase 5.2 — Ventas y agendamiento juntos

Una transcripción puede registrar varias cosas al mismo tiempo. La persona puede mostrar interés comercial, agendar una reunión y pedir material de seguimiento. Forzar estas dimensiones a competir en una sola Choice elimina información útil: elegir agendamiento no significa que dejó de ser una conversación comercial.

Pregunta cada hecho por separado. ¿Hubo interés comercial explícito? ¿Hubo confirmación de agendamiento? ¿Existe pedido de seguimiento? También define qué cuenta como confirmación: “¿podemos hablar mañana?” es una propuesta; “confirmado para mañana a las 10” tiene otro valor. Estas distinciones deben aparecer en los criterios y en los ejemplos de etiquetado.

Después, el código combina las respuestas. Dos etiquetas pueden generar dos tareas, pero la creación debe evitar duplicados. Si falta la fecha o la zona horaria, una etiqueta positiva de agendamiento no basta para registrar un evento en el calendario. Extracción, validación y acción siguen siendo etapas diferentes.

Identifica quién dijo cada frase. Si el agente pregunta si el cliente quiere comprar y el cliente dice que solo necesita recuperar la contraseña, la oferta no prueba intención de compra. Si el cliente pide precio y corrección de acceso, dos preguntas atómicas pueden registrar ambas intenciones. Compara esos límites con la transcripción ausente: la ausencia de texto debe continuar como información insuficiente.

### Ejemplo resuelto

“Tengo interés en el plan de equipo. Confirmo la conversación de mañana a las 10.” → intención comercial y agendamiento pueden ser positivos juntos.

### Es tu turno

¿Qué dato aún falta antes de crear automáticamente un evento a partir de la frase del ejemplo?

<details>
<summary>Revisar la respuesta comentada</summary>

Necesitamos resolver la fecha absoluta de “mañana”, la zona horaria, los participantes y las posibles reglas de autorización. La etiqueta de agendamiento no proporciona todo eso.

</details>

## Clase 5.3 — Información faltante

Una frase incompleta exige cuidado. “Cerrado” puede confirmar una reunión, aceptar el envío de material o cerrar la conversación. Sin los mensajes anteriores, no lo sabemos. Un modelo presionado a responder solo sí o no puede elegir una alternativa incluso cuando falta el objeto de la confirmación.

Trata la suficiencia como parte del producto. Una opción insuficiente puede llevar a buscar el fragmento anterior, pedir aclaración o canalizar hacia revisión. Esta estrategia no garantiza que el modelo detecte siempre el vacío, pero evita que el flujo tenga que adivinar cuándo aparece.

Los datos ausentes también pueden surgir al preparar la información. Una transcripción truncada, un anexo ignorado o una búsqueda que recuperó el fragmento equivocado cambian lo que el modelo puede decidir. Al investigar errores, compara la fuente con el estado efectivamente enviado. A veces la corrección más pequeña está en el extractor, no en la pregunta.

### Profundización de la versión 1.2.0

Separa asunto e intención: “Wi-Fi” puede aparecer en una solicitud para consultar un caso existente. Para solicitudes de ventas y agendamiento juntos, usa dos etiquetas y evalúa si falta confirmación del horario. El texto transcrito puede perder una negación; revisa casos de frontera.

### Práctica con los recursos actuales

En reuniones, pregunta por separado si hay decisión, próxima acción, responsable y plazo. La existencia de esas señales no extrae automáticamente la tarea ni resuelve fechas. En notas transcritas, preserva intenciones simultáneas: un mensaje puede contener una tarea y una idea. En la selección de recortes, evalúa claridad textual; la retención real exige datos de audiencia.

### Ejemplo resuelto

“¡Confirmado!” sin contexto → insuficiente. “Confirmo nuestra reunión del viernes a las 14” → evidencia explícita, aún sujeta a validación de la fecha y la zona horaria.

### Es tu turno

Un resumen eliminó la negación “no” antes del análisis. ¿Corregir solo la pregunta es suficiente?

<details>
<summary>Revisar la respuesta comentada</summary>

No. La información de entrada fue alterada. Corrige la preparación del contexto y vuelve a probar el flujo completo.

</details>

[Volver al índice](../README.md)
