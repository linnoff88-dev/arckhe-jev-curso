# Module 1 — Where Jev fits in

Choose between a rule, a bounded decision, and a generative response.

## Lesson 1.1 — Decide, generate, or calculate

Imagine a course team’s inbox. One message asks for a new password, another wants the price, and a third disputes a charge. Before writing a reply, the team needs to decide who should handle each request. That choice has few known alternatives and can be studied separately from the writing of the reply.

TypeSafe presents Jev as a model aimed at structured decisions. That doesn’t mean every decision needs it. Adding an invoice, checking whether a field is empty, or looking up an exact code are tasks conventional software can handle. Writing a customized explanation is a text-generation job. Classifying an expressed intent in multiple ways is a candidate for a decision model.

The first project question is: which part of the work requires interpretation? Separate that part from the exact rules and the actions. The system can classify a charge without having permission to process a refund. This separation allows you to test judgment without changing the outside world.

### Solved example

Calculate 3 × R$ 50 → code. Determine whether the message asks for access support → bounded decision. Write an access-recovery explanation → text generation.

### Your turn

Separate these tasks: add requests, choose the responsible team, and write a welcoming reply. What output should each step produce?

<details>
<summary>Check the commented answer</summary>

The sum produces a number via calculation; triage produces a label among permitted options; the reply produces text. Don’t use AI for the sum when the data is already structured.

</details>

## Lesson 1.2 — Context, question, and options

A decision depends on three elements. The context contains the material to evaluate. The question states exactly the desired judgment. The options bound the responses the system knows how to interpret. If any of them is poorly defined, the output may be valid in format and useless for the operation.

Consider a hotel that advertises free cancellation. The policy clarifies that the value comes back as credit for another stay. If someone needs the money back, this condition doesn’t cover it. The question “is the hotel good?” mixes preferences; “does the policy provide a cash refund?” is more specific. A classification across money, credit, and insufficient information makes the next step clear.

The absence of information doesn’t prove the negative alternative. If the policy says only “cancellation allowed,” we still don’t know how the value is returned. It’s useful to reserve an explicit option for insufficient information, in addition to a policy that recognizes ambiguity. The model shouldn’t complete the document with a condition that seems likely.

### Solved example

Context: “refund as credit valid for 12 months.” Question: “how will the refund be issued?” Options: cash / credit / not provided. Answer key: credit.

### Your turn

Rewrite the question for someone who needs their money back and handle the policy that doesn’t mention a refund.

<details>
<summary>Check the commented answer</summary>

Ask whether the excerpt confirms a cash refund. Use options confirms / contradicts / insufficient. The omission goes to insufficient, without inventing a condition.

</details>

## Lesson 1.3 — Read promises carefully

An ad can show a huge speed difference between two systems. To understand the number, we need to know which task was used, how much context went in, which model it compared against, what configuration it had, and what counts as a correct response. A maximum observed number doesn’t become a fixed advantage for any use.

You also need to separate structural validity from semantic validity. If the options are sales, support, and billing, a reply “billing” can perfectly follow the contract and still be wrong. A system that never leaves the list isn’t automatically protected from incorrect interpretations.

When reading a benchmark, look for the unit of measurement. A single call can answer multiple questions. Getting all questions in a call correct is different from getting most labels correct. Look for real data, human reference, class-wise distribution, and full cost. The useful stance is to turn a promise into a hypothesis that can be tested.

### Deep dive for version 1.2.0

Audit a demonstration by separating input, judgment, execution, and evidence of effect. Ready-made options can solve real work; they don’t demonstrate arbitrary generation. A game with a text state doesn’t prove vision or physical autonomy. Consult the L12 lab.

In a consulted educational reference, the home page calls the transcriptions real, but a lesson describes them as synthetic. This difference limits what we can conclude. Label-level correctness and getting all labels in a call are also different metrics. Check provenance and the denominator before comparing percentages.

### Solved example

“200 times faster” becomes: “the vendor reported this gain in certain workflows; we’ll still measure our support in Portuguese.”

### Your turn

Correct: “Since the output is always an allowed option, we can trust every decision.”

<details>
<summary>Check the commented answer</summary>

A valid option avoids certain format errors, but it can still represent the wrong judgment. We need to measure error by class and define what to revise.

</details>

[Back to the index](../README.md)
