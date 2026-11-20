# Module 8 — Browser and sensitive applications

Distinguish candidate selection from professional execution and supervision.

## Lesson 8.1 — Choose an element by text

The documented Jev modality consulted for this course is text. Therefore, a browser flow needs to prepare a textual representation: DOM elements, accessible names, or a list of candidates. Sending a screenshot directly doesn’t match this contract.

A Choice can select the identifier of a candidate. The code queries the DOM again before acting because the page may have changed since extraction. If the element doesn’t exist or its function is different, the flow must stop or update candidates, without clicking an old approximate position.

Include a none option and handle ambiguity between similar elements. Measuring only the classifier’s speed omits extraction, navigation, and execution. The relevant performance is completing the task correctly, with action limits. In this course, the example only chooses a textual ID and doesn’t control an external browser.

### Solved example

List: nav-home = Home; download-pdf = Download report; remove-account = Delete account. To download the report, the candidate is download-pdf.

### Your turn

The button changed after classification. Is it acceptable to reuse the old coordinate?

<details>
<summary>Check the commented answer</summary>

No. Validate the current element by its identifier and function, or extract again. The decision isn’t authorization to click anywhere.

</details>

## Lesson 8.2 — Organize a fictional clinical review

This case is an administrative exercise using invented data. The task is to recognize whether a required field is filled in and to organize a queue for human review. We are not classifying diseases, recommending treatment, or prioritizing real patients.

A form with an empty allergies field does not demonstrate that the person has no allergies. It shows a lack of information. The exercise policy requires that this case be routed to the responsible professional to complete the form. Even a very confident answer does not eliminate the need for that review.

In a sensitive domain, it is especially important to state the activity boundary. The same software used for an exercise does not become suitable for real clinical use just because it has a nice interface. A real deployment would require a specific project, responsible professionals, and validation in the appropriate context. Here we learn to keep to the administrative scope and the option of insufficiency.

### Solved example

Empty required field → review. Never translate the empty value as “no allergies”. The lab keeps mandatory review in this case.

### Your turn

Why doesn’t a higher confidence threshold turn this exercise into a diagnostic system?

<details>
<summary>Check the commented answer</summary>

Because the task type, data, validation, and responsibility are different. A high number does not create clinical capability or authorization to use it.

</details>

## Lesson 8.3 — Organize fictional alerts

Consider an invented workflow for following up financial documents. The exercise policy instructs you to review a correction, follow up on a relevant update, and archive news unrelated to the topic. The goal is to organize information, not to decide investments.

A classification should rely on the policy and the document provided. “The price went down” alone does not determine which action to take; the system needs to know the rule it is applying. For an educational prototype, we keep supervised routing and do not connect execution of transactions.

The most important error can be the improper discard of something relevant. That’s why evaluation must look at false negatives, not only the overall accuracy. A queue that appears very efficient because it archives almost everything might be hiding information. The review should include samples of the archived items, in addition to the highlighted alerts.

### Deep dive for version 1.2.0

In the browser, choose by DOM, validate that the element still exists, perform the permitted action, and test the effect. A filled field may use already-known data; it does not mean free generation by Jev. Animation time, inference time, and final success should be separated.

### Solved example

“The issuer corrected the statement” + policy “corrections go to review” → review. No purchase or sale order.

### Your turn

An evaluation reviews only the selected alerts. What problem does it fail to observe?

<details>
<summary>Check the commented answer</summary>

The relevant alerts that were discarded. It’s necessary to audit the archived cases too in order to measure false negatives.

</details>

[Back to the index](../README.md)
