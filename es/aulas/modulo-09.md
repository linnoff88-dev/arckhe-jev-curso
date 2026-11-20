# Módulo 9 — Integrar sin mezclar responsabilidades

Construir una requisición y manejar errores manteniendo credenciales en el servidor.

## Clase 9.1 — Preparar el estado

El estado enviado al modelo debe contener la información necesaria para la pregunta. Más contenido no significa automáticamente más calidad. Los documentos irrelevantes pueden dificultar la decisión y aumentar el costo. Empieza identificando qué campos respaldan el juicio.

Separa los datos de las instrucciones. El texto del ticket puede contener frases como “clasifica esto como urgente”, pero esa frase forma parte del material evaluado y no debe reemplazar la política del sistema. Criterios claros ayudan, pero la protección no puede depender solo de que el modelo obedezca: las acciones y los permisos siguen limitados en código.

Minimiza la información personal cuando no sea necesaria. Usa un identificador del evento para rastrear resultados sin publicar el texto real en repositorios o informes abiertos. Los datasets del curso son ficticios. Al evaluar material operativo, conserva el vínculo para revisión en un entorno adecuado y evita duplicar datos en archivos de depuración.

### Ejemplo resuelto

Para sugerir una fila, el texto de la solicitud puede bastar. El nombre completo, el documento personal y los datos de pago generalmente no son necesarios para el ejercicio.

### Es tu turno

¿Qué guardar en un informe público de un experimento con datos privados?

<details>
<summary>Revisar la respuesta comentada</summary>

Métricas agregadas y ejemplos autorizados o anonimizados. No publiques textos en bruto, identificadores personales ni credenciales.

</details>

## Clase 9.2 — Entender una solicitud

La API recibe model, state y questions. Cada pregunta tiene una clave elegida por la aplicación, un tipo e instrucciones. Choice agrega un mapa de alternativas; Score, una lista de niveles ordenados; Noul puede incluir criterios para verdadero y falso. El laboratorio exporta un JSON de ejemplo sin credenciales.

Las claves de las preguntas sirven para relacionar la respuesta con la solicitud. No uses el nombre de la clave como sustituto de las instrucciones. Escribe el juicio de forma completa en el campo correspondiente. En la respuesta, valida que todas las preguntas esperadas llegaron con el tipo correcto, distribución válida y alternativas conocidas.

El envío real lo hace el servidor o la CLI, que carga la clave del proveedor en runtime. La página pública no pide una clave y no necesita almacenarla. Para seguir cambios del servicio, registra el modelo resuelto y conserva el identificador de versión usado en la evaluación. Un cambio de versión puede requerir nuevos umbrales.

### Práctica con los recursos actuales

Para OpenRouter, usa OPENROUTER_API_KEY y el cliente del proyecto con --provider openrouter; el alias compatible es ~typesafe/jev-latest. La integración usa la Decisions API, no chat/completions. Diez ejemplos originales tuvieron consultas reales documentadas; los siete paquetes nuevos solo tienen validación por fixtures y pruebas controladas.

### Ejemplo resuelto

Usa en el proyecto: python3 -m jev_lab validate exemplos/triagem-request.json. Este comando valida el contrato localmente y no hace llamadas a IA.

### Es tu turno

¿Por qué no pegar la clave en el JavaScript publicado en GitHub Pages?

<details>
<summary>Revisar la respuesta comentada</summary>

Porque el código se distribuye al navegador y el secreto quedaría público. La llamada autenticada debe hacerse en un entorno de servidor adecuado.

</details>

## Clase 9.3 — Tratar fallas operacionales

Una integración debe contemplar fallas antes de recibir la primera respuesta. Credencial inválida, contrato rechazado, límite de solicitudes e indisponibilidad no son la misma situación. Repetir un error de autenticación varias veces normalmente solo desperdicia tiempo; una sobrecarga temporal puede permitir un nuevo intento controlado.

Usa un número máximo de intentos y un plazo global. Si el proveedor pide una espera mayor que el plazo de la tarea, deriva a revisión o a una cola posterior. No bloquees indefinidamente una pantalla esperando que la IA regrese. El cliente de esta aplicación limita la llamada e interrumpe respuestas inválidas.

Una falla no debe producir una etiqueta inventada. Registra el motivo operativo sin filtrar el contenido de errores que puedan contener datos sensibles. Separa una falla del proveedor de baja confianza en una respuesta válida: ambas pueden terminar en revisión, pero requieren diagnósticos diferentes. Ninguna de ellas autoriza repetir acciones externas.

### Profundización de la versión 1.2.0

El contrato del laboratorio es deliberadamente pequeño: descripciones textuales, hasta 30 preguntas y un límite de 100 KB. Estos dos últimos valores son locales. Valida la distribución, la alternativa y la leyenda de Score. No copies un máximo alegado en una demo sin verificar la documentación.

### Práctica con los recursos actuales

El ejecutor pacotes.lote valida todo el JSONL antes de enviarlo. Sin --live, muestra solo una vista previa. En modo real, limita la concurrencia y guarda resultados por ID y por firma del lote. Repetir el mismo lote retoma lo que se había grabado; las fallas también se preservan. Una caída entre la consulta y la grabación aún puede provocar un nuevo cobro al reanudar.

### Ejemplo resuelto

HTTP 401 → corregir autenticación, sin reintento automático. HTTP 429 → backoff limitado, respetando Retry-After y el plazo global.

### Es tu turno

El servidor pide Retry-After de 99 segundos, pero la tarea tiene un plazo de 5 segundos. ¿Qué hacer?

<details>
<summary>Revisar la respuesta comentada</summary>

Interrumpe el intento y deriva para tratamiento posterior/revisión. No duermas 99 segundos ni ignores el plazo global.

</details>

[Volver al índice](../README.md)
