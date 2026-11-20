# Module 12 — Final project

Deliver a well-founded adoption decision, even when the answer is not to automate.

## Lesson 12.1 — Specify the triage

Your final project is a customer-support triage in Portuguese. Start by describing who receives the tickets, what queues exist, and what problem you want to reduce. Avoid promising full automation. The first deliverable is a specification that someone else can review.

Define the criteria for each alternative, ambiguous cases, and how missing information is handled. Add five difficult examples: negation, two intents, incomplete text, synonym, and improper instruction inside the ticket. Show how each should be handled and why.

Then draw the external policy to the model. It defines allowed actions, review, contract failures, time window, and attempt limits. Include a budget and an evaluation plan. A no-code project can use a spreadsheet; the technical one must add requests, tests, and a reproducible report. Both must separate facts, hypotheses, and results.

### Solved example

Deliverable: taxonomy + five difficult cases + questions + policy + diagram + budget + evaluation protocol + rollback/return plan.

### Your turn

Write a sentence that describes the success of your pilot without using “smarter AI”.

<details>
<summary>Check the commented answer</summary>

Example: reduce triage time while keeping queue error within the agreed limit, with a lower total cost and the possibility of human correction.

</details>

## Lesson 12.2 — Evaluate the proposal

Present your evaluation so that another person can repeat it. Identify the dataset, its source, the partitions, and the configurations. Show the number of cases per class, important errors, and limitations. An accuracy chart without context isn’t enough.

If you only ran the rules baseline, say so. If you used simulated responses, mark them as simulation. If you made a real call, record the model and the reported usage. These distinctions don’t weaken the project; they make your conclusion reliable and show what stage is still missing.

The rubric considers formulation, policy, evidence, economics, and reproducibility. A project that recognizes insufficient data can be better than a project that announces success with invented numbers. Include examples where the system failed and explain the smallest proposed correction, without adjusting and measuring everything on the same set.

### Solved example

Honest report: “lexical baseline, 24 fictional examples, 20 correct; it doesn’t measure Jev or represent production traffic”.

### Your turn

What information is missing to turn the example report into evidence for Jev adoption?

<details>
<summary>Check the commented answer</summary>

Real Jev execution and alternatives, representative reviewed data, a policy calibrated together in a separate set, final metrics, and full end-to-end flow cost.

</details>

## Lesson 12.3 — Decide adoption

The last step is a design decision. There are three legitimate outcomes: continue with a limited rollout, collect more data, or don’t adopt. The choice depends on quality, cost, coverage, review effort, and operational capacity—not on the model’s popularity.

If you decide to continue, limit the first route to a reversible action and track the fixes. If you decide to collect more data, say exactly which unanswered doubt must be resolved: a rare class, a language, a type of ambiguity, or the cost difference. If you decide not to adopt, preserve the evaluation to avoid repeating the same experiment without learning.

The principle that runs through the course is simple: probabilistic interpretation works better inside software that knows its limits. Models help with judgment; criteria and evidence enable evaluation; code constrains execution; people make the decisions that require responsibility. A well-defined architecture is worth more than an isolated promise of speed.

### Deep dive for version 1.2.0

In the final project, deliver a report.json and the error analysis, or clearly identify why the result is still simulated. Arguing to collect more data or not to adopt is a valid conclusion. Quality, full cost, and coverage must support the decision.

### Practice with the current resources

Choose one of the 17 packages as your starting point, without confusing an executable template with a ready-made connector. The pilot must declare who collects the events, who reviews, where the logs live, how to measure incorrect discards, and who authorizes actions. A thousand fast classifications don’t demonstrate a thousand correct decisions.

### Solved example

Possible decision: keep rules for exact cases, observe Jev for the rest, and require review until you have sufficient evidence in Portuguese.

### Your turn

Give an objective condition for each outcome: continue, collect more data, and don’t adopt.

<details>
<summary>Check the commented answer</summary>

Continue: goals demonstrated with sufficient volume. Collect: inconclusive results in important classes. Don’t adopt: quality or total cost don’t justify the change after an adequate test.

</details>

[Back to the index](../README.md)
