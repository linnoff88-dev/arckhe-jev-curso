# Module 4 — Cost and choosing the first case

Calculate feasibility including the work that happens after the model.

## Lesson 4.1 — The ten thousand tokens account

A per-million-token fee needs to be converted before multiplying by the call volume. In the price reference checked on 18/09/2026, Jev’s input costs US$ 0.042 per million. For a total of 10,000 input tokens, divide 10,000 by one million and multiply by 0.042. The result is US$ 0.00042.

Ten thousand equal calls would cost US$ 0.42 for input; one hundred thousand, US$ 4.20; a hundred thousand, US$ 42. Watch the decimal places. A zero error changes the whole comparison. Work in a single currency and keep the estimate separate from actual billing.

Tokens are not words, characters, or documents. A long context and detailed criteria can consume more input. For the final budget, use the count returned by the service and verify the route’s fee used. The lab allows you to edit the price to update the account without rewriting the course.

### Solved example

Cost = calls × average total tokens ÷ 1,000,000 × price per million. For 10,000 × 10,000 tokens, the estimate is US$ 4.20.

### Your turn

Calculate 100,000 calls of 2,000 tokens using the reference rate.

<details>
<summary>Check the commented answer</summary>

100,000 × 2,000 ÷ 1,000,000 × 0,042 = US$ 8,40. This is only the model’s input, with no other costs.

</details>

## Lesson 4.2 — Cost of the entire process

A cheap call doesn’t guarantee a cheap process. After triage, there may be a generative model, human review, text extraction, storage, and rework. If the error routes a request to the wrong team, the real cost includes the time spent correcting the misrouting.

Compare two complete operations. In the reference, all events follow the current flow. In the hybrid, all go through triage, and part proceeds to the larger model or to review. Residual calls may be exactly the most difficult and expensive ones; don’t assume they cost the same average as the earlier ones.

Also include the deployment effort amortized over the usage period. A low-volume process may not justify a complex integration, even with a large percent token savings. Do a sensitivity analysis: does the result stay positive if the fallback rate doubles or if human review takes twice as long?

### Solved example

Fictitious scenario: baseline US$ 1,000; Jev US$ 8.40; residual LLM US$ 200. Gross savings US$ 791.60, before review, infrastructure, and deployment.

### Your turn

Add US$ 500 for review and US$ 400 for amortized deployment effort to the scenario. Does it still save money?

<details>
<summary>Check the commented answer</summary>

No. The hybrid adds US$ 1,108.40 and exceeds the baseline of US$ 1,000. The token savings were consumed by the other costs.

</details>

## Lesson 4.3 — Choose a pilot

A first pilot should answer a small, verifiable business question. “Automate the whole company” doesn’t provide a clear completion criterion. “Suggest the ticket queue in Portuguese without increasing rework” lets you gather examples, review the results, and decide whether it’s worth moving forward.

Prefer a case with clear alternatives, available data, enough frequency, and a reversible consequence. You also need someone who knows how to say what’s correct. If people don’t even agree on the categories, the first task is to adjust the process and labeling, not to choose the model.

The priority matrix can combine volume, human time per case, how easy it is to obtain a reference, and the impact of the error. Don’t treat the matrix as exact math: it makes the debate visible. A flashy browser or agents case can come later after a simple triage that proves value and reveals domain limitations.

### Deep dive for version 1.2.0

The cost of a single call doesn’t measure the flow. In the expanded calculator, include fallback percentage, LLM price per attempt, review minutes, and infrastructure. An unknown cost after failure or retry shouldn’t be treated as zero.

### Solved example

Recommended pilot: suggest support, billing, or sales in tickets. Early phase: only observe the suggestion and compare it with human forwarding.

### Your turn

Compare ticket triage with automatic execution of refunds. Which starts first, and why?

<details>
<summary>Check the commented answer</summary>

Triage: reversible consequence, simpler review, and less need for permissions. Refunds require a separate rules project, authorization, and control.

</details>

[Back to the index](../README.md)
