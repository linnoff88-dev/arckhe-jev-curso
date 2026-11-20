# Módulo 3 — Confianza y error

Usar la incertidumbre sin transformarla en autorización automática.

## Clase 3.1 — Probabilidad y confidence

En Choice, la distribución informa un valor para cada alternativa. El campo confidence resume una propiedad de esa distribución según la implementación del proveedor. No presumimos que sea igual a la probabilidad más alta. Al registrar un resultado, guardamos ambos campos con nombres distintos.

Una tercera idea es el intervalo estadístico de una tasa medida. Si revisamos un conjunto de predicciones y contamos aciertos, podemos estimar la tasa y su incertidumbre muestral. Ese intervalo depende del experimento y no es el campo confidence recibido de una llamada. Mezclar los conceptos da una impresión de precisión que los datos no respaldan.

La calibración es una propiedad observada en grupos de predicciones: los valores de probabilidad deben compararse con frecuencias de resultados correctos. Una sola respuesta no comprueba que el sistema esté calibrado. El dominio y el idioma también importan. La política de nuestro servicio debe evaluarse en nuestros ejemplos, no solo en un gráfico genérico.

### Ejemplo resuelto

Distribución ficticia: soporte 0,94; cobro 0,04; ventas 0,02. Confidence ficticia: 0,91. Ninguno de esos valores es un intervalo de confianza de la exactitud del sistema.

### Es tu turno

Una pantalla llama confidence=0,91 a “91% de garantía”. ¿Qué corrección se debe hacer?

<details>
<summary>Revisar la respuesta comentada</summary>

Cambiar por una descripción del campo del modelo y explicar que la decisión puede estar equivocada. La garantía individual no se deriva de esa estadística.

</details>

## Clase 3.2 — Alta confianza, respuesta incorrecta

Crea un caso ficticio: la persona escribe “no quiero cancelar; solo necesito cambiar la fecha”. El modelo elige cancelación con probabilidad alta. La salida es estructuralmente válida, pero la interpretación falló en la negación. Este ejemplo no necesita ser un benchmark real para revelar una falla de arquitectura: ejecutar una acción irreversible solo porque el número es alto.

Cuando ocurra un error, registra el contexto necesario, la pregunta, los criterios y la versión del modelo. Primero verifica si la pregunta era ambigua o si faltaban opciones importantes. Corregir una instrucción puede ser suficiente, pero es necesario volver a probar con un conjunto independiente; acertar el caso usado en el ajuste no prueba una mejora general.

No todo error pide una pregunta más larga. A veces falta una regla: cancelar requiere confirmación explícita, cualquiera que sea la clasificación. Esta protección debe existir fuera del modelo. La mejor corrección suele preservar el sistema y reducir la consecuencia del error, en lugar de añadir otra secuencia ilimitada de juicios.

### Ejemplo resuelto

Error ficticio: “no quiero cancelar” fue clasificado como cancelación. Protección: el triaje solo sugiere la cola; la cancelación nunca se ejecuta por él.

### Es tu turno

Propón una corrección en el texto de la pregunta y otra en el flujo operativo.

<details>
<summary>Revisar la respuesta comentada</summary>

Pregunta: distinguir pedido explícito de cancelación de mención o negación. Flujo: exigir confirmación y permiso fuera del modelo antes de cancelar.

</details>

## Clase 3.3 — Cuándo pedir revisión

El próximo paso depende tanto de la incertidumbre como del costo de equivocarse. Mostrar una cola sugerida y borrar una cuenta tienen consecuencias diferentes. No hay un umbral universal que vuelva equivalentes las dos acciones. El proyecto debe definir qué acciones son reversibles, cuáles requieren confirmación y cuáles quedan solo para personas autorizadas.

Una política inicial puede producir tres resultados: sugerir, pedir más información o encaminar a revisión. Esta política necesita funcionar también cuando el servicio falla, cuando la respuesta no respeta el contrato y cuando llega una categoría desconocida. En esos casos no debemos inventar una clasificación para mantener el flujo andando.

La revisión humana tiene costo y capacidad limitada. Mide cuántos eventos recibe y cuánto tiempo toma. Si casi todo va a revisión, la ganancia puede desaparecer. Si casi nada va, revisa si los criterios quedaron demasiado permisivos. El equilibrio se elige con evidencia y con quién responde por la operación.

### Profundización de la versión 1.2.0

Repetir diez veces una entrada evalúa estabilidad, no equivale a diez ejemplos independientes. Un error estable sigue siendo un error. Usa la primera repetición para calidad y un indicador separado para variación; las probabilidades ficticias sirven solo para estudiar la política.

### Ejemplo resuelto

Sugerir soporte es reversible. Confirmar una fecha puede requerir validación. Eliminar una cuenta exige un flujo propio de autorización, incluso con alta confianza.

### Es tu turno

Define el destino de una respuesta inválida, incompleta y con pedido de eliminación.

<details>
<summary>Revisar la respuesta comentada</summary>

Respuesta inválida: error operativo y revisión. Dato incompleto: pedir información o revisar. Exclusión: flujo autorizado y confirmación, sin ejecución por parte del triaje.

</details>

[Volver al índice](../README.md)
