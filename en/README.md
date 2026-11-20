# Jev in practice

**v1.5.0** · Original Portuguese course: **3 tracks, 12 modules, 36 lessons, and 12 labs**.

[Open HTML course v2](https://inematds.github.io/jev-curso/). Progress, questions, notes, appearance, exercises, and your personal roadmap with local export. Lessons are also available in Markdown. No received data for analysis is published.

[Application and guide](https://inematds.github.io/jev/guia/) · [Lab of 20 cases](https://inematds.github.io/jev/app/)

## Start here

Conceptual path: modules 1–8, without requiring code. Technical path: modules 9–12, with notions of JSON, terminal, and Python. Estimate of 18 hours including exercises and project; isolated reading is shorter.

## Track — Understand

- [Module 1 — Where Jev fits](aulas/modulo-01.md)

- [Module 2 — The three types of question](aulas/modulo-02.md)

- [Module 3 — Confidence and error](aulas/modulo-03.md)

- [Module 4 — Cost and choosing the first case](aulas/modulo-04.md)

## Track — Apply

- [Module 5 — Support and transcriptions](aulas/modulo-05.md)

- [Module 6 — Documents and evidence](aulas/modulo-06.md)

- [Module 7 — Models and agents](aulas/modulo-07.md)

- [Module 8 — Browser and sensitive applications](aulas/modulo-08.md)

## Track — Build and evaluate

- [Module 9 — Integrate without mixing responsibilities](aulas/modulo-09.md)

- [Module 10 — Measure truth quality](aulas/modulo-10.md)

- [Module 11 — Operate and observe](aulas/modulo-11.md)

- [Module 12 — Final project](aulas/modulo-12.md)

## Practice with the current resources

[Learning track: 17 packages, batches, and question-by-question evaluation](materiais/fluxos-praticos.md). Includes OpenRouter, a skill for Codex/Claude Code, and observation in OpenPCBot. The seven new packages have simulated examples; they are neither benchmarks nor ready-made connectors.

## Labs

[Materials, activities, and answer keys](materiais/README.md) · [Final project](materiais/projeto-final.md)

## How to study

Read the scenario, solve the exercise before opening the answer, and note what information was missing. In the labs, distinguish fictional data, simulated responses, and real inference. No simulation proves Jev performance.

## Limits and references

Independent educational course. Clinical, legal, and financial cases are fictional and supervised. There is no diagnosis, contractual approval, or automatic transaction. The fee used in the exercises was checked on 18/09/2026; review updates in the [TypeSafe documentation](https://docs.typesafe.ai/models).

[Exaggerations and doubts — technical analysis](https://github.com/inematds/jev/blob/main/docs/07-exageros-e-duvidas.md) · [Official models, prices, and limits](https://docs.typesafe.ai/models) · [Reproducible experiments](https://github.com/inematds/jev/blob/main/docs/08-experimentos.md)

## Maintenance

The original source for the lessons is in `conteudo/curso.json`. To regenerate Markdown: `python3 scripts/export_markdown.py`. To generate the 18 pages and the public artifact: `python3 scripts/build_site.py`. The original pedagogical plan remains in `planejamento/`.
