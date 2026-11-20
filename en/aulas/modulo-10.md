# Module 10 — Measure real quality

Compare methods without confusing tuned examples with independent evidence.

## Lesson 10.1 — Build a human reference

An evaluation starts with defining what is correct. If labels change from person to person, the metric may be measuring process disagreement. Create a labeling guide, review examples, and document the cases that don’t fit well.

Separate development, calibration, and testing. Use development to improve questions; calibration to choose thresholds; testing to verify the frozen policy. Messages from the same conversation can’t be in different partitions, because that makes it easier to recognize content already seen. When there’s time variation, also evaluate later data.

The lab’s 24 fictional tickets are for learning how to run and read an evaluation. They are not a representative sample of a company and do not prove suitability for production. An operational dataset needs to cover the classes, ambiguities, and changes in real traffic, with human review and data protection.

### Solved example

A conversation with three messages must stay entirely in the same partition. Splitting messages between question training and testing causes context leakage.

### Your turn

Can you adjust the question after looking at the final test error and publish the new rate in the same test as independent?

<details>
<summary>Check the commented answer</summary>

No. The test was used for the adjustment. You need to reserve another set for a new independent evaluation.

</details>

## Lesson 10.2 — Compare alternatives

Use the same task and the same data to compare rules, Jev, a generative model with structured output, and a hybrid flow. Record configurations and versions. Differences in input or criteria make the comparison hard to interpret.

Accuracy tells you the overall proportion of correct answers, but it can hide small classes. The confusion matrix shows where each class was routed. Macro-F1 gives the same weight to classes, but it also needs to be read with the counts. Pay special attention to the error that has the highest operational cost.

Measure end-to-end latency and the cost of all attempts. The lexical baseline result for this project is reproducible by the CLI: it reports known correct and incorrect outcomes on the fictional dataset. Don’t compare this local rule time with network latency as if they were the same thing. The real Jev experiment can only be reported after execution with access to the service.

### Practice with the current resources

The complementary evaluator packages.quality requires a reference for every question. Choice measures accuracy; Noul measures accuracy with cut 0.5 and Brier; Score measures absolute error and normalized error by the scale. The cut used in the metric does not define the action policy. Contract errors reduce coverage and accuracy; MAE and Brier use only valid responses, so they must be read together with coverage.

### Solved example

python3 -m jev_lab batch data/tickets-sinteticos.jsonl --out reports/baseline produces metrics.json and predictions.csv, using local rules.

### Your turn

A very common class has 99% accuracy and another important one has 40%. Is the global average enough?

<details>
<summary>Check the commented answer</summary>

No. Report metrics by class, sample support, the confusion matrix, and the cost of errors. The average can hide the important class.

</details>

## Lesson 10.3 — Choose and freeze thresholds

As you increase a threshold, usually fewer responses go to the automatic suggestion. This may reduce some errors, but it increases review and can let through the more confident errors. We need to measure two things together: quality on the accepted cases and coverage, the fraction of cases the policy accepts.

Choose the threshold on the calibration set and freeze it before testing. Record whether it uses the class probability, confidence, or both. Don’t copy a threshold from one primitive to another, one language to another, or from one version to another without evaluation.

Measurement uncertainty matters. If ten examples passed without error, we still don’t have proof that the error rate is small. The tighter the target, the more data you usually need. When the sample is insufficient, the correct conclusion may be to collect more examples instead of declaring success.

### Deep dive for version 1.2.0

The CLI experiment records dataset, template, policy, model, failures, and provenance. Replay mode lets you compare external responses, including LLMs, but it does not authenticate the stated source. A model-only comparison should have equivalent input; a flow comparison measures the entire task.

Group predictions by confidence ranges to investigate where the errors show up, while preserving the size of each group and class. Too few examples per range leads to fragile conclusions. A change in criteria that fixes a known case must be re-run on an independent set; it’s not enough to demonstrate the corrected case.

### Solved example

In the teaching lab, vary confidence from 0.90 to 0.95. The fictional response with confidence 0.91 moves from suggestion to review.

### Your turn

Why does this interaction with invented values not prove that 0.95 is the right threshold?

<details>
<summary>Check the commented answer</summary>

Because it doesn’t measure real responses against independent labels. It only shows how a policy reacts to numbers.

</details>

[Back to the index](../README.md)
