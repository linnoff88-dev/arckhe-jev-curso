# Module 6 — Documents and Evidence

Assess what a passage supports without extrapolating to external truth.

## Lesson 6.1 — Is a claim supported?

The check in this exercise compares a claim to a passage provided. It does not search all the literature nor does it guarantee truth in the real world. This boundary is essential: the useful question is whether the available material supports the sentence as written.

An observational study can report an association. A headline that claims causality adds a conclusion that does not appear in the evidence. The options can distinguish supported, requires rewriting, and insufficient. The passage must remain identifiable so a person can verify the judgment.

Quality also depends on retrieving documents. A model that received the wrong excerpt can say insufficient even if there is good evidence on another page. Measuring only the classifier would hide this problem. In an editorial application, evaluate search, excerpt selection, and judgment as parts of the same flow, while keeping separate metrics to locate the failure.

### Solved example

Case “Claim checking”: the association between coffee and longevity does not, on its own, support the sentence “coffee causes greater longevity.”

### Your turn

Rewrite the headline without adding an unproven conclusion.

<details>
<summary>Check the commented answer</summary>

“A study found an association between coffee consumption and longevity.” You still need to provide population, design, and limitations when producing complete content.

</details>

## Lesson 6.2 — Clause checklist

This exercise uses a fictional clause to study the presence of information. We ask whether the excerpt contains cancellation conditions, not whether a contract is legally safe or valid. These are different judgments, with different context requirements.

A checklist rubric may use present, absent in the excerpt, and ambiguous. The phrase “in the excerpt” limits the conclusion: the complete document may contain the condition in another section. Keep page or clause identifiers so review is possible. If the system works with fragments, don’t turn local absence into absence in the entire contract.

The next step is to mark a point for the responsible professional. Don’t authorize a signature, send it to the client, or legal approval just because all fields seem to be present. Presence doesn’t mean suitability. The educational project shows evidence triage and leaves specialized interpretation to whoever can perform it.

### Solved example

“12 months validity” indicates duration. It doesn’t clarify the cancellation procedure or any penalty. The answer key for that excerpt is missing.

### Your turn

How can you change the question if only one paragraph of the contract was sent?

<details>
<summary>Check the commented answer</summary>

“Does the provided excerpt describe the cancellation conditions?” The answer should be limited to the excerpt, without asserting that the entire document omits the condition.

</details>

## Lesson 6.3 — What changed in the conversation?

In a sequence of emails, a proposal is not the same as a confirmed decision. To find a change, keep the sender, order, and time of the messages. Quoted text inside replies may also repeat an old decision; a simple word search could select the wrong day.

Split the task. First, identify which messages propose or confirm the change. Then the code uses reliable metadata to order the events. Dates, intervals, and time zones are compared with calendar functions—not by the model’s semantic impression.

If there are two incompatible confirmations, treat it as a conflict. If confirmation is missing, preserve it as insufficient. A useful interface shows the passage of evidence and lets you open the original message. The isolated “Friday” label is hard to audit when someone needs to understand why the schedule changed.

### Deep dive for version 1.2.0

A pre-filter should preserve the passage that contradicts the question, not just the one that confirms it. Keep ID, source, and excerpt. Choosing a value among candidate items extracted avoids re-writing numbers, but it doesn’t prove that the correct candidate was selected. Practice on L11.

### Solved example

Monday: expected Thursday. Tuesday: can we move to Friday? Wednesday: confirmed Friday. The most recent confirmation is Friday.

### Your turn

If a fifth message says “keep Thursday” without identifying the event, what should you do?

<details>
<summary>Check the commented answer</summary>

Don’t automatically overwrite the date. There could be a reference to another topic; search for context or flag a conflict/insufficiency.

</details>

[Back to the index](../README.md)
