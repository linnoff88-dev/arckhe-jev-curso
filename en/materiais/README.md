# Labs — fictional and original material

Each file includes answer keys for self-grading. Try to solve before consulting the answer. No dataset represents real operational traffic.

| Lab | File | Activity and criterion |
|---|---|---|
| L1 — formulate | [12 tasks](l1-formulacao.csv) | Choose a rule, Choice, Noul, Score, or generation and justify. |
| L2 — hotel | [6 policies](l2-hoteis.json) | Distinguish money, credit, lack of refund, conflict, and insufficient funds. |
| L3 — support | [30 tickets](l3-tickets.json) | Classify queues; compare with the label and explain divergences. |
| L4 — evidence | [8 pairs and 4 clauses](l4-evidencias.json) | Identify support and omission only in the provided material. |
| L5 — routes | [12 tasks](l5-rotas.json) | Choose capacity; define permission and attempt limit separately. |
| L6 — DOM | [5 lists](l6-dom.json) | Select a candidate, refrain, or request review by permission. |
| L7 — economics | [CSV spreadsheet](l7-custos.csv) | Rework costs and add fallback, human work, and deployment. |
| L8 — thresholds | [10 simulated predictions](l8-predicoes-simuladas.json) | Compare coverage and error when accepting confidence ≥0,90 or ≥0,95. |

## Commented answer key for L8

At ≥0,90: six accepted, four correct; coverage 60%, accuracy among accepted 66,67%.
At ≥0,95: four accepted, three correct; coverage 40%, accuracy among accepted 75%.
The error with confidence 0,97 remains accepted in both. Raising the threshold doesn’t eliminate all errors. These numbers are invented for the exercise, not Jev results.

## Integration with the application

[Ten complete cases](dez-casos.json) include state, questions, criteria, a simulated answer, and a comment. The [web lab](https://linnoff88-dev.github.io/arckhe-/app/) lets you explore the same cases.

## Final delivery

Fill out the [project template](projeto-final.md). Suggested approval: 75/100 on the rubric, without presenting a simulation as measurement and without assigning permissions to the model. The grade is an educational self-assessment, not an operational safety certification.

## Deep dive — L9 to L12

All of them include fictional scenarios and answer keys.

| Lab | Material | Delivery |
|---|---|---|
| L9 — Skills | [Eight requests](l9-skills.json) | Select a skill or none; justify by intent. |
| L10 — Code | [Six situations](l10-comentarios-diff.json) | Separate correctness, usefulness, and test evidence. |
| L11 — Evidence | [Six passages](l11-evidencias.json) | Preserve contradictions, negations, and IDs. |
| L12 — Demos | [Eight claims](l12-auditoria-demos.json) | Render a verdict and list the evidence still needed. |

[Twenty application cases](vinte-casos.json) include the three primitives and combined questions. The previous file with ten cases remains as starter material. For technical practice, use the [experiment guide](https://github.com/linnoff88-dev/jev/blob/main/docs/08-experimentos.md).

## Updated companion roadmap

[Practical flows: 17 packages, batches, and per-question evaluation](fluxos-praticos.md). It complements the existing lessons and the 12 labs; it doesn’t add a numbered lab.
