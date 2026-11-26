# Jev en la práctica

**v1.5.0** · Curso autoral en portugués: **3 trilhas, 12 módulos, 36 clases y 12 laboratorios**.

[Abrir el curso HTML v2](https://linnoff88-dev.github.io/arckhe-/). Progreso, dudas, anotaciones, apariencia, ejercicios y guion personal con exportación local. Las clases también siguen disponibles en Markdown. Ningún dato recibido para análisis se publica.

[Aplicación y guía](https://linnoff88-dev.github.io/arckhe-/guia/) · [Laboratorio de 20 casos](https://linnoff88-dev.github.io/arckhe-/app/)

## Empieza por aquí

Recorrido conceptual: módulos 1–8, sin exigir código. Recorrido técnico: módulos 9–12, con nociones de JSON, terminal y Python. Estimación de 18 horas incluyendo ejercicios y proyecto; la lectura aislada es más corta.

## Trilha — Entender

- [Módulo 1 — Donde Jev entra](aulas/modulo-01.md)

- [Módulo 2 — Los tres tipos de pregunta](aulas/modulo-02.md)

- [Módulo 3 — Confianza y error](aulas/modulo-03.md)

- [Módulo 4 — Costo y elección del primer caso](aulas/modulo-04.md)

## Trilha — Aplicar

- [Módulo 5 — Atención y transcripciones](aulas/modulo-05.md)

- [Módulo 6 — Documentos y evidencias](aulas/modulo-06.md)

- [Módulo 7 — Modelos y agentes](aulas/modulo-07.md)

- [Módulo 8 — Navegador y aplicaciones sensibles](aulas/modulo-08.md)

## Trilha — Construir y evaluar

- [Módulo 9 — Integrar sin mezclar responsabilidades](aulas/modulo-09.md)

- [Módulo 10 — Medir calidad de verdad](aulas/modulo-10.md)

- [Módulo 11 — Operar y observar](aulas/modulo-11.md)

- [Módulo 12 — Proyecto final](aulas/modulo-12.md)

## Práctica con los recursos actuales

[Guion: 17 paquetes, lotes y evaluación por pregunta](materiais/fluxos-praticos.md). Incluye OpenRouter, skill para Codex/Claude Code y observación en OpenPCBot. Los siete paquetes nuevos tienen ejemplos simulados; no son benchmark ni conectores listos.

## Laboratorios

[Materiales, actividades y soluciones](materiais/README.md) · [Proyecto final](materiais/projeto-final.md)

## Cómo estudiar

Lee la situación, resuelve el ejercicio antes de abrir la respuesta y anota dónde faltó información. En los laboratorios, diferencia el dato ficticio, la respuesta simulada y la inferencia real. Ninguna simulación comprueba el desempeño de Jev.

## Límites y referencias

Curso educativo independiente. Los casos clínicos, jurídicos y financieros son ficticios y están supervisados. No hay diagnóstico, aprobación contractual ni transacción automática. La tarifa usada en los ejercicios se consultó el 18/09/2026; consulta actualizaciones en la [documentación de TypeSafe](https://docs.typesafe.ai/models).

[Exageraciones y dudas — análisis técnico](https://github.com/linnoff88-dev/jev/blob/main/docs/07-exageros-e-duvidas.md) · [Modelos, precios y límites oficiales](https://docs.typesafe.ai/models) · [Experimentos reproducibles](https://github.com/linnoff88-dev/jev/blob/main/docs/08-experimentos.md)

## Mantenimiento

La fuente original de las clases está en `conteudo/curso.json`. Para regenerar Markdown: `python3 scripts/export_markdown.py`. Para generar las 18 páginas y el artefacto público: `python3 scripts/build_site.py`. El plan pedagógico original permanece en `planejamento/`.
