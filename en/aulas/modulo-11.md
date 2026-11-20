# Module 11 — Run and observe

Prepare logs, monitoring, and feedback without losing control of the operation.

## Lesson 11.1 — Observe before automating

Observation mode means the new stage computes a suggestion, but the previous flow remains responsible for the decision. That way, we can compare the behavior to the real operation without automatically applying the pilot’s errors.

Record agreements and disagreements. Reviewing only disagreements isn’t enough, because humans and the model can agree on an incorrect response. Also inspect a sample of agreements. Observe the volume of each class and the messages that don’t fit the taxonomy.

Define the output of this phase before you start. Accuracy, coverage, cost, review time, and the absence of integration failures can be part of the criteria. If the goals aren’t demonstrated, keep observing or end the test. Automating because “it’s been running for a week” isn’t a quality criterion.

### Practice with the current resources

To experiment without a key at the root of the jev repo: python3 -m pacotes.executar reunioes; python3 -m pacotes.qualidade reunioes; python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl. The first two use simulated data and responses; the third only does a preview. The complementary script details the step to your own data.

### Solved example

The team receives the suggested queue shown next to the current routing. No external change happens just because of the model’s response.

### Your turn

A pilot had only a few billing-class events. Is it enough to release all queues?

<details>
<summary>Check the commented answer</summary>

Not necessarily. You may be missing evidence for that class. Collect more examples or limit the release to routes that were actually evaluated.

</details>

## Lesson 11.2 — Record and understand failures

A useful log links the event to the question version, the policy, and the model used. It also records time, tokens, result, and any eventual correction. Without that information, it’s hard to tell whether a behavior change came from the model, the context, or a code change.

Don’t confuse traceability with keeping everything forever. Minimize data, limit access, and define retention according to the real environment. For public reports, use fictional or authorized examples. Credentials never go into the log.

When fixing an error, look for the smallest sufficient protection. A missing field may call for validation; a duplicate may call for idempotency; a loop may call for a cap; an incorrect decision may call for clearer criteria and a new test. The failure category helps: judgment quality, context preparation, contract, network, or operational policy.

### Practice with the current resources

A batch can use from one to four workers and stagger the start of the queries. This staggering doesn’t control each HTTP retry and doesn’t replace a token-based distributed limit. Event limits are not a dollars budget. After retries, preserve unknown cost when only the last response’s consumption is available.

### Solved example

Event 42: question v2, policy v1, fixed model, valid response, corrected sales suggestion for support. The sensitive text is kept out of the public report.

### Your turn

A retry processes the same ticket twice. Rewriting the question fixes it?

<details>
<summary>Check the commented answer</summary>

No. The fix is execution-related: an idempotent identifier and duplicate control, with a test that reproduces the retry.

</details>

## Lesson 11.3 — Update or roll back

A model alias can point to a new version without changing your request. This makes updates easier, but makes it harder to attribute variation when thresholds were adjusted for an earlier version. Record the resolved identifier and pin versions in the experiments that need to be reproduced.

Before changing the production version, run the evaluation set and compare errors. A better average may hide regression in an important class. If the policy depends on confidence, verify the thresholds and coverage again.

Have a simple way to disable the new stage and go back to the previous flow. The rollback shouldn’t require rebuilding the application. Suspension criteria include a relevant error, persistent unavailability, and unexpected cost. Updating is a controlled change, not just replacing a name in the configuration.

### Deep dive for version 1.2.0

For code triage, separate correct comments from useful comments. The classifier may point to a weakened test, but tests and static analysis are still needed. Also sample what the filter discarded to find false negatives. Practice in L10.

### Solved example

A new version arrives: evaluate with the same questions and reserved data; review metrics by class; release gradually or keep the previous version.

### Your turn

What should be recorded to reproduce a decision after an update?

<details>
<summary>Check the commented answer</summary>

Resolved model, question version and criteria, policy version, and identification of the authorized context used in the event.

</details>

[Back to the index](../README.md)
