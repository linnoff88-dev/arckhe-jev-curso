# Module 3 — Confidence and error

Use uncertainty without turning it into automatic authorization.

## Lesson 3.1 — Probability and confidence

In Choice, the distribution assigns a value to each alternative. The confidence field summarizes a property of that distribution according to the provider’s implementation. We don’t assume it’s equal to the highest probability. When recording a result, we store both fields with distinct names.

A third idea is the statistical interval of a measured rate. If we review a set of predictions and count correct answers, we can estimate the rate and its sampling uncertainty. This interval depends on the experiment, and it’s not the confidence field returned from a call. Mixing up these concepts creates an impression of precision that the data don’t support.

Calibration is a property observed in groups of predictions: probability values must be compared with frequencies of correct outcomes. A single answer doesn’t prove that the system is calibrated. Domain and language also matter. The policy of our support should be evaluated in our examples, not just on a generic chart.

### Solved example

Fictitious distribution: support 0.94; billing 0.04; sales 0.02. Fictitious confidence: 0.91. None of these values is a confidence interval of system accuracy.

### Your turn

A screen calls confidence=0.91 “91% guarantee”. What correction should be made?

<details>
<summary>Check the commented answer</summary>

Replace with a description of the model field and explain that the decision may be wrong. Individual “guarantee” does not follow from this statistic.

</details>

## Lesson 3.2 — High confidence, wrong answer

Create a fictitious scenario: the person writes “I don’t want to cancel; I just need to change the date”. The model chooses cancellation with high probability. The output is structurally valid, but the interpretation failed in the negation. This example doesn’t need to be a real benchmark to reveal an architecture flaw: executing an irreversible action just because the number is high.

When an error happens, record the necessary context, the question, the criteria, and the model version. First check whether the question was ambiguous or whether important options were missing. Fixing an instruction may be enough, but you need to retest an independent set; getting the case used for the adjustment right doesn’t prove general improvement.

Not every error calls for a longer question. Sometimes a missing rule is the issue: cancellation requires explicit confirmation, regardless of classification. This protection must exist outside the model. The best correction usually preserves the system and reduces the consequence of the error, instead of adding another unlimited sequence of judgments.

### Solved example

Fictitious error: “I don’t want to cancel” was classified as cancellation. Protection: triage only suggests the queue; cancellation is never executed by it.

### Your turn

Propose one correction in the question text and another in the operational flow.

<details>
<summary>Check the commented answer</summary>

Question: distinguish an explicit cancellation request from a mention or negation. Flow: require confirmation and permission outside the model before canceling.

</details>

## Lesson 3.3 — When to ask for a review

The next step depends on both uncertainty and the cost of being wrong. Showing a suggested queue and deleting an account have different consequences. There is no universal threshold that makes the two actions equivalent. The project must define which actions are reversible, which require confirmation, and which are only allowed for authorized people.

An initial policy may produce three outcomes: suggest, ask for more information, or route to review. This policy must work even when the service fails, when the response doesn’t follow the contract, and when an unknown category arrives. In these cases, we shouldn’t invent a classification just to keep the flow going.

Human review has cost and limited capacity. Measure how many events it receives and how long each one takes. If almost everything goes to review, the benefit may disappear. If almost nothing does, investigate whether your criteria are too permissive. The balance is chosen with evidence and with the people accountable for the operation.

### Deep dive for version 1.2.0

Repeating ten times an input measures stability, not the same as ten independent examples. A stable error is still an error. Use the first repetition for quality, and a separate indicator for variation; fictitious probabilities are for studying the policy only.

### Solved example

Suggesting support is reversible. Confirming a date may require validation. Deleting an account requires its own authorization flow, even with high confidence.

### Your turn

Define the destination for invalid responses, incomplete data, and a deletion request.

<details>
<summary>Check the commented answer</summary>

Invalid answer: operational error and review. Incomplete data: request information or review. Exclusion: authorized flow and confirmation, with no triage execution.

</details>

[Back to the index](../README.md)
