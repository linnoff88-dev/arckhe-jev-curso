# Module 5 — Support and Transcripts

Apply decisions to messages and distinguish absence of evidence from a negative response.

## Lesson 5.1 — Routing tickets

Start with the definitions of queues. The lab example uses support for technical difficulty, billing for payment matters, and sales for hiring interest. A message that does not allow distinguishing these intents is insufficient. Real teams may need a different taxonomy, but the rule should be explicit.

To evaluate, use varied texts. “I paid twice” and “the money left in duplicate” express something close using different words. A lexical baseline may recognize the first and miss the second. That makes it useful to compare a model, without assuming it will win in all classes.

The triage result is a suggestion. The interface must allow the person to correct it and to record that correction without losing the history. Don’t invent a message for the customer nor confirm a refund based on the classification. Applying this delivery does not execute these actions: it helps test the decision before connecting it to an operation.

### Practice with the current resources

Expanded application: an inbox, YouTube comments, and communities can share the same core, but need their own criteria. A receipt is not a support question; a display of dissatisfaction does not prove an intent to leave. In the project, these flows are in the inbox-packages, youtube-comments, and communities.

### Solved example

Open the case “Customer support triage” in the lab. The simulated response suggests billing and explains why that suggestion does not authorize a refund.

### Your turn

Classify: “I can’t log in,” “How much does it cost to participate?” and “Hi, I need help.”

<details>
<summary>Check the commented answer</summary>

Support, sales, and insufficient, respectively. The last message does not provide a specific intent.

</details>

## Lesson 5.2 — Sales and scheduling together

A transcript can record several things at the same time. The person can show commercial interest, schedule a meeting, and ask for follow-up materials. Forcing these dimensions to compete in a single Choice removes useful information: choosing scheduling does not mean the conversation is no longer a commercial one.

Ask each fact separately. Was there explicit commercial interest? Was there confirmation of scheduling? Is there a request for follow-up? Also define what counts as confirmation: “we can talk tomorrow?” is a proposal; “confirmed for tomorrow at 10” has another value. These distinctions should appear in the criteria and in the labeling examples.

Then, the code combines the responses. Two labels can generate two tasks, but creation must avoid duplicates. If the date or time zone is missing, a positive scheduling label is not enough to record an event on the calendar. Extraction, validation, and action remain different steps.

Identify who said each sentence. If the agent asks whether the customer wants to buy and the customer says they only need to recover their password, the offer does not prove purchase intent. If the customer asks for a price and an access correction, two atomic questions can record both intents. Compare these boundaries with the missing transcript: lack of text should continue to be insufficient information.

### Solved example

“I’m interested in the team plan. I confirm our conversation tomorrow at 10.” → both commercial intent and scheduling can be positive together.

### Your turn

What data is still missing before automatically creating an event from the example sentence?

<details>
<summary>Check the commented answer</summary>

We need to resolve the absolute date of “tomorrow,” the time zone, the participants, and any authorization rules. The scheduling label does not provide all of this.

</details>

## Lesson 5.3 — Missing information

An incomplete sentence requires care. “Agreed” can confirm a meeting, accept sending materials, or end the conversation. Without the previous messages, we don’t know. A model forced to answer only yes or no may choose an alternative even when the object of the confirmation is missing.

Treat sufficiency as part of the product. An insufficient option can lead to looking for the previous excerpt, requesting clarification, or routing it to review. This strategy does not guarantee the model always detects the gap, but it prevents the flow from having to guess when it appears.

Missing data can also arise during preparation. A truncated transcript, an ignored attachment, or a search that retrieved the wrong excerpt changes what the model can decide. When investigating mistakes, compare the source with the state that was actually sent. Sometimes the smallest correction is in the extractor, not in the question.

### Deep dive for version 1.2.0

Separate topic and intent: “Wi‑Fi” might appear in a request to check an existing ticket. For requests that combine sales and scheduling, use two labels and evaluate whether there is missing time confirmation. The transcribed text may lose a negation; revise borderline cases.

### Practice with the current resources

In meetings, ask separately whether there is a decision, next action, responsible person, and deadline. The existence of these signals does not automatically extract the task or resolve dates. In transcribed notes, preserve simultaneous intentions: one message can contain both a task and an idea. When selecting cut points, assess textual clarity; true retention requires audience data.

### Solved example

“Confirmed!” without context → insufficient. “I confirm our meeting on Friday at 2 p.m.” → explicit evidence, still subject to validating the date and time zone.

### Your turn

A summary removed the negation “no” before analysis. Correcting only the question is enough?

<details>
<summary>Check the commented answer</summary>

No. The input information was changed. Correct the context preparation and retest the full flow.

</details>

[Back to the index](../README.md)
