# Guía complementaria — de la pregunta al flujo

Acompaña el curso v1.3.0 y el proyecto Jev v1.6.1. Ejecuta los comandos en la raíz del clone **jev**, no en el clone del curso. Esta guía complementa las 36 clases y los 12 laboratorios.

## 1. Elegir el problema

El proyecto tiene 17 paquetes: los diez iniciales y siete nuevos para bandeja de entrada, comentarios de YouTube, comunidades, reuniones, cortes por transcripción, notas y curaduría.

```bash
git clone https://github.com/inematds/jev.git
cd jev
python3 -m pacotes.executar --list
python3 -m pacotes.executar reunioes
```

Identifica la decisión principal y las preguntas auxiliares. En el paquete de reuniones, pregunta si hay decisión, siguiente paso, responsable y plazo. No confundas “hay un responsable” con extraer su nombre, ni “hay plazo” con calcular una fecha.

**Ejercicio:** “Necesitamos mejorar el tutorial; hablamos después.” ¿Es suficiente para crear una tarea asignada y agendada?

**Respuesta:** no. Puedes indicar intención, pero falta encaminamiento explícito. Jev clasifica señales; la aplicación todavía necesita confirmar la tarea y resolver el calendario.

## 2. Leer las métricas de todas las preguntas

```bash
python3 -m pacotes.qualidade reunioes
python3 -m pacotes.qualidade cortes
```

Estos comandos usan fixtures inventadas y referencias de autoría. Revisa `origins: ["simulation"]`. Choice mide acierto de etiqueta; Noul mide exactitud y Brier; Score mide error absoluto y error normalizado. El reporte también muestra cobertura y errores.

**Ejercicio:** si hay error de contrato en la mitad de los registros, ¿basta con mostrar Brier bajo en los restantes?

**Respuesta:** no. Brier considera respuestas válidas, pero la cobertura cayó. Las fallas permanecen en el denominador de la exactitud. Presentar solo el subconjunto válido ocultaría problemas operacionales.

## 3. Preparar un lote sin consumir API

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl
```

Revisa `mode: preview` y `calls: 0`. Cada fila contiene `id` y `state`. El ejecutor rechaza IDs duplicados y entradas inválidas antes de consultar al proveedor. Para este ejercicio no hace falta base de datos ni un servicio de colas.

**Ejercicio:** ¿dos eventos con el mismo ID y textos diferentes pueden tratarse como la misma ocurrencia?

**Respuesta:** no en este lote; el ejecutor los rechaza. Corrige la identificación en el origen antes de enviarlos.

## 4. Entender el paso al modo real

Con llave configurada en el backend y datos autorizados:

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl --live --provider openrouter --workers 2 --interval 1 --out runs/reunioes.jsonl
```

El modo real envía datos y consume créditos. Repetir el mismo comando retoma resultados guardados, incluyendo errores. Una caída entre respuesta y guardado todavía puede repetir consumo; no hay garantía de cobro único. No modifiques el lote ni la plantilla para reutilizar el mismo checkpoint.

El intervalo controla el inicio de las consultas, no cada retry interno. Compara concurrencia y condiciones equivalentes al evaluar velocidad. Un lote rápido no prueba calidad, calibración ni una ganancia universal.

## 5. Hacer la entrega del piloto

Define, con referencia humana independiente:

- Preguntas y alternativas, incluida insuficiencia.
- Datos mínimos y autorización de envío.
- Etiquetas esperadas por pregunta, sin copiar la predicción del modelo.
- Métricas de calidad, cobertura, costo completo y latencia.
- Revisión de falsos negativos entre los ítems descartados.
- Criterio para adoptar, recolectar más evidencia o no automatizar.

Para Codex y Claude Code, la skill `jev-decidir` consulta al cliente como herramienta. En OpenPCBot v3, `/jev observar` usa la pasarela propia y solo compara sugerencias; `/ajuda jev` explica el recurso. Los paquetes de notas y reuniones aún no son comandos nativos nuevos del bot.

[Instrucciones completas de integración y formato de referencia](https://github.com/inematds/jev/blob/main/docs/11-fluxos-praticos.md) · [Paquetes](https://github.com/inematds/jev/tree/main/pacotes) · [Volver al curso](../README.md).
