# Módulo 1 — Dónde entra Jev

Elegir entre una regla, una decisión estructurada y una respuesta generativa.

## Clase 1.1 — Decidir, generar o calcular

Imagina la bandeja de entrada de un equipo de cursos. Un mensaje pide una nueva contraseña, otro quiere saber el precio y un tercero cuestiona un cobro. Antes de escribir una respuesta, el equipo necesita decidir a quién corresponde atender cada solicitud. Esta elección tiene pocas alternativas conocidas y puede estudiarse por separado de la redacción de la respuesta.

Jev es presentado por TypeSafe como un modelo enfocado en decisiones estructuradas. Esto no significa que toda decisión tenga que apoyarse en él. Sumar una factura, verificar si un campo está vacío o buscar un código exacto son tareas que el software convencional puede resolver. Escribir una explicación personalizada es trabajo de generación de texto. Clasificar una intención expresada de varias maneras es un candidato a modelo decisor.

La primera pregunta del proyecto es: ¿qué parte del trabajo exige interpretación? Separa esa parte de las reglas exactas y de las acciones. El sistema puede clasificar un cobro sin tener permiso para hacer un reembolso. Esta separación permite probar el juicio sin alterar el mundo externo.

### Ejemplo resuelto

Calcular 3 × R$ 50 → código. Identificar si el mensaje pide soporte → decisión delimitada. Redactar una explicación de recuperación de acceso → generación de texto.

### Es tu turno

Separa estas tareas: sumar pedidos, elegir el equipo responsable y escribir una respuesta acogedora. ¿Qué salida debe producir cada etapa?

<details>
<summary>Revisar la respuesta comentada</summary>

La suma produce un número mediante cálculo; la clasificación produce una etiqueta entre opciones permitidas; la respuesta produce texto. No uses IA para la suma cuando los datos ya están estructurados.

</details>

## Clase 1.2 — Contexto, pregunta y opciones

Una decisión depende de tres elementos. El contexto contiene el material a evaluar. La pregunta declara exactamente el juicio deseado. Las opciones delimitan las respuestas que el sistema sabe interpretar. Si cualquiera de estos está mal definido, la salida puede ser válida en el formato y no servir para la operación.

Considera un hotel que anuncia cancelación gratuita. La política aclara que el valor se devuelve como crédito para otra estancia. Quien necesita el dinero de vuelta no queda cubierto por esa condición. La pregunta “¿el hotel es bueno?” mezcla preferencias; “¿la política prevé reembolso en dinero?” es más específica. Una clasificación entre dinero, crédito e información insuficiente deja claro el siguiente paso.

La ausencia de una información no prueba la alternativa negativa. Si la política dice solo “cancelación permitida”, todavía no sabemos cómo regresa el valor. Es útil reservar una opción explícita para insuficiencia, además de una política que reconozca la ambigüedad. El modelo no debería completar el documento con una condición que parece probable.

### Ejemplo resuelto

Contexto: “reembolso en crédito válido por 12 meses”. Pregunta: “¿cuál es la forma de devolución?”. Opciones: dinero / crédito / no informada. Respuesta correcta: crédito.

### Es tu turno

Reescribe la pregunta para alguien que necesita dinero de vuelta y trata la política que no menciona reembolso.

<details>
<summary>Revisar la respuesta comentada</summary>

Pregunta si el fragmento confirma reembolso en dinero. Usa opciones confirma / contradice / insuficiente. La omisión va a insuficiente, sin inventar una condición.

</details>

## Clase 1.3 — Leer las promesas con cuidado

Un anuncio puede mostrar una gran diferencia de velocidad entre dos sistemas. Para entender el número, necesitamos saber qué tarea se usó, cuánta información de contexto entró, con qué modelo se comparó, qué configuración tenía y qué cuenta como respuesta correcta. Un máximo observado no se convierte en una ventaja fija para cualquier uso.

También es necesario separar la validez estructural de la validez semántica. Si las opciones son ventas, soporte y cobro, una respuesta “cobro” puede cumplir perfectamente el contrato y aun así estar equivocada. Un sistema que nunca sale de la lista no está automáticamente protegido contra interpretaciones erróneas.

Al leer un benchmark, busca la unidad de medida. Una llamada puede responder varias preguntas. Acertar todas las preguntas de una llamada es diferente de acertar la mayoría de las etiquetas. Busca datos reales, referencia humana, distribución por clase y costo total. La postura útil es convertir una promesa en una hipótesis que pueda ponerse a prueba.

### Profundización de la versión 1.2.0

Audita una demostración separando entrada, juicio, ejecución y evidencia del efecto. Las opciones listas pueden resolver trabajo real; no demuestran generación arbitraria. Un juego con estado textual no comprueba visión ni autonomía física. Consulta el laboratorio L12.

En una referencia educativa consultada, la página de inicio llama a las transcripciones reales, pero una lección las describe como sintéticas. Esta diferencia limita lo que podemos concluir. Acertar por etiqueta y acertar todas las etiquetas de una llamada también son métricas diferentes. Verifica el origen y el denominador antes de comparar porcentajes.

### Ejemplo resuelto

“200 veces más rápido” se vuelve: “el proveedor reportó esa ganancia en ciertos flujos de trabajo; todavía vamos a medir nuestro soporte en portugués”

### Es tu turno

Corrige: “Como la salida es siempre una opción válida, podemos confiar en toda decisión”.

<details>
<summary>Revisar la respuesta comentada</summary>

Una opción válida evita ciertos errores de formato, pero puede representar el juicio equivocado. Necesitamos medir el error por clase y definir la revisión.

</details>

[Volver al índice](../README.md)
