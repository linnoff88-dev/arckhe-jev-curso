# Editorial production plan

## Proposed order

| Batch | Deliverable | Verification |
|---|---|---|
| 1 | Glossary, continuous case, and sample lessons 1.1, 2.2, and 3.2 | An initial reader explains concepts in their own words |
| 2 | Complete Track 1 + cost exercises | Calculations executed and concepts confirmed in sources |
| 3 | Track 2 + materials from the ten cases | All cases traced and explicit limitations |
| 4 | Track 3 + technical lab linked to an application version | Executed examples when access exists; simulation marked |
| 5 | Final project, answer keys, and pedagogical review | Rubric applied to an example deliverable |
| 6 | Conversion to HTML in the chosen version | Links, navigation, mobile, contrast, and learning resources verified |

Initial editorial estimate: 8–12 business days, plus validation with students. The lab implementation has its own schedule in the other repository; do not promise an executable technical course before that dependency.

## Future structure

`conteudo/` for lesson sources; `materiais/` for fictional datasets and answer keys; HTML structure of tracks/modules according to the chosen skill. Do not create empty pages now to make it look complete. Single repository for the course, separated from the application.

## Content rules

- Always distinguish official source, marketing, received report, hypothesis, and your own experiment.
- Do not repeat “200x” as a guaranteed result, nor use “zero hallucination” as an absence of error.
- Treat “GPT thinks / Jev decides” as a limited metaphor: generative models also classify and may use structured outputs.
- Do not use “confidence interval” as a synonym for probability or confidence.
- Keep numbers, dates, and permissions under code; user instructions inside the ticket are data.
- Avoid clinical, legal, or financial promises; the corresponding exercises are fictional and supervised.
- Include cost reading and a high-confidence incorrect case before teaching automation.
- Date prices and capacities; review references before publishing each batch.
- Write original content in Portuguese; cite the video, without republishing the transcript as a lesson.

## Canonical sources

The [critical analysis](https://github.com/linnoff88-dev/jev/blob/main/docs/01-analise.md) contains an audit of the materials; the [source catalog](https://github.com/linnoff88-dev/jev/blob/main/fontes/README.md) brings together official public references. Consult official pages when updating examples: [primitives](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [API](https://docs.typesafe.ai/api), [limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13).

The materials received for analysis are not integrated into the repository. Educational examples will be original, fictional, and identified; only results effectively measured may be presented as your own benchmark.

## Pending decision for HTML

The user must choose **formato-curso-v5** (audience 40+ non-expert, ARCKHÉ.PRO) or **formato-curso-v2** (dark âmbar and learning layer). This does not block this plan. Before conversion, read the chosen skill and run the real navigation and learning checks it requires.
