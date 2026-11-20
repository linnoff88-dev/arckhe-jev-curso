# Módulo 2 — Los tres tipos de pregunta

Distinguir Choice, Noul y Score según el tipo de respuesta necesaria.

## Clase 2.1 — Choice: elegir una alternativa

Choice sirve para elegir entre alternativas descritas previamente. En un proceso de triaje, las opciones pueden representar equipos. Los nombres deben ser estables para el código y los criterios deben ser comprensibles para quien etiqueta ejemplos. No basta con escribir una lista de palabras vagas: “financiero” y “administrativo” pueden superponerse si no se explican las fronteras.

Una buena opción incluye lo que la caracteriza. El cobro puede abarcar factura, pago duplicado y solicitud de reembolso. El soporte puede abarcar acceso, error de inicio de sesión y falla de uso. Si la persona habla de dos problemas independientes, el producto necesita decidir si elige una cola principal, abre dos tareas o pide revisión. Una Choice aislada selecciona una opción; por sí sola no resuelve esa decisión de producto.

La respuesta documentada incluye la alternativa y una distribución de probabilidades. Lee esa distribución como salida del modelo, no como la cantidad real de personas de cada equipo. Antes de ejecutar cualquier acción, valida que la opción exista y que la política permita el encaminamiento.

### Ejemplo resuelto

“Pagué dos veces” → cobro. “La contraseña no funciona” → soporte. “Necesito una contraseña nueva y reembolso” → regla de múltiples intenciones o revisión.

### Es tu turno

Define criterios para ventas y soporte que no se confundan cuando alguien pregunta cómo contratar.

<details>
<summary>Revisar la respuesta comentada</summary>

Ventas trata de interés en planes o contratación; soporte trata de dificultad técnica en el servicio. Una pregunta comercial sobre contratación no es automáticamente un problema técnico.

</details>

## Clase 2.2 — Noul: probabilidad de sí

Noul responde una pregunta binaria con un número entre cero y uno. El valor representa la probabilidad de “sí” según el modelo. Cerca de uno apunta a sí; cerca de cero apunta a no. El valor intermedio no representa una intensidad intermedia del tema: indica que las alternativas no están bien separadas.

Si la pregunta es “¿hay un pedido de reembolso?”, 0,05 no significa baja confianza en la respuesta negativa. Significa poca probabilidad de sí. No copies una política de Choice que lee el campo confidence: la primitiva Noul no devuelve ese campo por separado. Si necesitas tres estados operativos, tu código puede aplicar dos umbrales y dejar una franja de revisión en medio.

Escribe la pregunta de manera afirmativa y literal. Evita la doble negación “¿no es verdad que no pidió reembolso?”. Si la falta de contexto necesita ser una categoría explícita, considera Choice o una pregunta separada de suficiencia. No asumas que un número cercano a cero prueba que la información necesaria estaba presente.

### Ejemplo resuelto

Política didáctica, aún no calibrada: p ≥ 0,90 sugiere sí; p ≤ 0,10 sugiere no; los demás valores piden revisión. Estos límites son ejemplos, no garantías.

### Es tu turno

Interpreta Noul=0,50 para “¿la persona tiene experiencia en Python?”. ¿Es experiencia media?

<details>
<summary>Revisar la respuesta comentada</summary>

No. Es una respuesta binaria sin una preferencia fuerte por sí o por no. Para medir nivel de experiencia, define niveles en Score.

</details>

## Clase 2.3 — Score: niveles ordenados

Score es adecuado cuando existe una escala con descripciones. “¿Cómo está la prioridad?” solo funciona bien si cada nivel tiene un significado operativo. Baja puede significar duda sin bloqueo; media, dificultad con una alternativa de contorno; alta, bloqueo del trabajo sin alternativa. El objetivo es hacer revisable la rúbrica por personas.

La salida puede caer entre niveles porque proviene de una distribución sobre ellos. Un valor 1,6 en niveles 0, 1 y 2 no es necesariamente un error. Tampoco es una medida física precisa. Score no es un sustituto de calcular valores monetarios, contar ítems ni comparar fechas con exactitud.

Separa dimensiones independientes. Urgencia, impacto y tono emocional son cosas diferentes. Una persona puede escribir con calma sobre un problema grave. Pregunta por la dimensión y combina los resultados en una regla explícita. Cuando la empresa cambie la prioridad de cada factor, se podrá modificar la regla sin esconder el cambio en una pregunta amplia.

### Profundización de la versión 1.2.0

En el laboratorio ampliado, edita Choice, Noul y Score y haz varias preguntas al mismo contexto. Score usa de dos a diez niveles textuales en este proyecto y devuelve una leyenda; Noul no devuelve confidence separado. Los criterios editados invalidan la respuesta simulada anterior.

Para componer rúbricas con cantidades diferentes de niveles, divide cada Score entre el último índice y haz un promedio con pesos explícitos. Relevancia 3 en cinco niveles se vuelve 0,75; urgencia 1 en tres niveles se vuelve 0,5. Pesos 2 y 1 dan 0,6667. Esto es un índice de prioridad, no confianza; la fórmula aproxima los intervalos ordinales como equivalentes. Preserva requisitos obligatorios fuera del promedio. Prueba la calculadora en el guion de decisión.

### Ejemplo resuelto

Niveles: 0 = sin bloqueo; 1 = bloqueo con alternativa; 2 = bloqueo sin alternativa. Un tono cordial no impide el nivel 2.

### Es tu turno

Crea una rúbrica de tres niveles para dificultad de acceso. Evita usar “bueno”, “medio” y “malo” sin explicar.

<details>
<summary>Revisar la respuesta comentada</summary>

0: accede normalmente y tiene duda de uso. 1: parte del contenido falla, pero hay una alternativa funcional. 2: no puede acceder al contenido necesario y no hay alternativa.

</details>

[Volver al índice](../README.md)
