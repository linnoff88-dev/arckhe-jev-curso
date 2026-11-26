# Plan de producción editorial

## Orden propuesto

| Lote | Entrega | Verificación |
|---|---|---|
| 1 | Glosario, caso continuo y muestra de las clases 1.1, 2.2 y 3.2 | Un lector principiante explica conceptos con sus propias palabras |
| 2 | Trilha 1 completa + ejercicios de costo | Cálculos ejecutados y conceptos verificados en las fuentes |
| 3 | Trilha 2 + materiales de los diez casos | Todos los casos trazados y limitaciones explícitas |
| 4 | Trilha 3 + laboratorio técnico vinculado a la versión de la aplicación | Ejemplos ejecutados cuando haya acceso; simulación marcada |
| 5 | Proyecto final, soluciones y revisión pedagógica | Rúbrica aplicada a una entrega de ejemplo |
| 6 | Conversión a HTML en la versión elegida | Enlaces, navegación, móvil, contraste y recursos de aprendizaje verificados |

Estimación editorial inicial: 8–12 días hábiles, más validación con alumnos. La implementación del laboratorio tiene un cronograma propio en el otro repositorio; no prometer un curso técnico ejecutable antes de esa dependencia.

## Estructura futura

`conteudo/` para fuentes de las clases; `materiais/` para datasets ficticios y soluciones; estructura HTML de trilhas/módulos según la skill elegida. No crear ahora páginas vacías para aparentar conclusión. Repositorio único para el curso, separado de la aplicación.

## Reglas de contenido

- Distinguir siempre fuente oficial, marketing, relato recibido, hipótesis y experimento propio.
- No repetir “200x” como resultado garantizado, ni usar “zero alucinaçêo” como ausencia de error.
- Tratar “GPT pensa / Jev decide” como metáfora limitada: los modelos generativos también clasifican y pueden usar salidas estructuradas.
- No usar “intervalo de confianza” como sinónimo de probability o confidence.
- Mantener números, fechas y permisos bajo código; las instrucciones del usuario dentro del ticket son datos.
- Evitar promesas clínicas, jurídicas o financieras; los ejercicios correspondientes son ficticios y supervisados.
- Incluir lectura de costo y un caso incorrecto de alta confianza antes de enseñar automatización.
- Datificar precios y capacidades, revisar referencias antes de publicar cada lote.
- Escribir contenido autoral en portugués; citar el video, sin republicar la transcripción como clase.

## Fuentes canónicas

La [análisis crítico](https://github.com/inematds/jev/blob/main/docs/01-analise.md) contiene la auditoría de los materiales; el [catálogo de fuentes](https://github.com/inematds/jev/blob/main/fontes/README.md) reúne referencias públicas oficiales. Consultar páginas oficiales al actualizar ejemplos: [primitivas](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [API](https://docs.typesafe.ai/api), [limitaciones](https://docs.typesafe.ai/model-jaggedness/jev-1.13).

Los materiales recibidos para análisis no integran el repositorio. Los ejemplos didácticos serán autorales, ficticios e identificados; solo resultados efectivamente medidos podrán presentarse como benchmark propio.

## Decisión pendiente para HTML

El usuario deberá elegir **formato-curso-v5** (público 40+ legos, INEMA.PRO) o **formato-curso-v2** (dark âmbar y capa de aprendizaje). Esto no bloquea este plan. Antes de la conversión, leer la skill elegida y ejecutar las verificaciones reales de navegación y aprendizaje que ella exija.
