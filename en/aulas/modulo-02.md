# Module 2 — The three types of questions

Distinguish Choice, Noul, and Score based on the type of response needed.

## Lesson 2.1 — Choice: choose an alternative

Choice is for choosing between alternatives described beforehand. In triage, the options may represent teams. The names must be stable for the code, and the criteria must be understandable for whoever labels examples. It’s not enough to write a list of vague words: “finance” and “administration” can overlap if the boundaries aren’t explained.

A good option includes what characterizes it. Billing can include invoice, duplicate payment, and a request for a refund. Support can include access, login error, and a usage failure. If the person mentions two independent problems, the product needs to decide whether to choose a single main queue, open two tasks, or ask for a review. An isolated Choice selects one option; it doesn’t, by itself, resolve that product decision.

The documented answer includes the alternative and a distribution of probabilities. Read that distribution as the model output, not as the true number of people in each team. Before taking any action, validate that the option exists and that the policy allows routing.

### Solved example

“I paid twice” → billing. “My password doesn’t work” → support. “I need a new password and a refund” → a multi-intent rule or a review.

### Your turn

Define criteria for sales and support that won’t get mixed up when someone asks how to sign up.

<details>
<summary>Check the commented answer</summary>

Sales is about interest in plans or signing up; support is about technical difficulty with the service. A sales question about signing up is not automatically a technical issue.

</details>

## Lesson 2.2 — Noul: probability of yes

Noul answers a binary question with a number between zero and one. The value represents the probability of “yes” according to the model. Closer to one points to yes; closer to zero points to no. The intermediate value does not represent an intermediate intensity of the subject: it indicates that the alternatives aren’t well separated.

If the question is “is there a refund request?”, 0.05 doesn’t mean low confidence in the negative answer. It means there’s a low probability of yes. Don’t copy a Choice policy that reads the confidence field: the Noul primitive doesn’t return that field separately. If you need three operational states, your code can apply two thresholds and leave a review band in the middle.

Write the question in an affirmative, literal way. Avoid the double negation “isn’t it true that they didn’t request a refund?”. If lack of context needs to be an explicit category, consider Choice or a separate sufficiency question. Don’t assume that a number near zero proves the necessary information was present.

### Solved example

Didactic policy, not yet calibrated: p ≥ 0.90 suggests yes; p ≤ 0.10 suggests no; other values ask for review. These thresholds are examples, not guarantees.

### Your turn

Interpret Noul=0.50 for “does the person have experience with Python?”. Is that average experience?

<details>
<summary>Check the commented answer</summary>

No. It’s a binary response without a strong preference for yes or no. To measure experience level, define levels with Score.

</details>

## Lesson 2.3 — Score: ordered levels

Score is suitable when there’s a scale with descriptions. “How is the priority?” only works well if each level has an operational meaning. Low can mean doubt without blocking; medium, difficulty with an alternative path; high, work blocked with no alternative. The goal is to make the rubric reviewable by people.

The output can fall between levels because it results from a distribution over them. A value 1.6 on levels 0, 1, and 2 isn’t necessarily an error. It’s also not a precise physical measure. Score is not a substitute for calculating monetary values, counting items, or exact date comparisons.

Separate independent dimensions. Urgency, impact, and emotional tone are different things. A person can write calmly about a serious problem. Ask by dimension and combine the results into an explicit rule. When the company changes the priority of each factor, it will be possible to change the rule without hiding the change in a broad question.

### Deep dive for version 1.2.0

In the expanded lab, edit Choice, Noul, and Score and ask several questions to the same context. Score uses two to ten textual levels in this project and returns labels; Noul doesn’t return separate confidence. Edited criteria invalidate the earlier simulated answer.

To compose rubrics with different quantities of levels, divide each Score by the last index and compute an average with explicit weights. Relevance 3 across five levels becomes 0.75; urgency 1 across three levels becomes 0.5. Weights 2 and 1 give 0.6667. This is a priority index, not confidence; the formula approximates ordinal intervals as equivalent. Preserve mandatory requirements outside the average. Try the calculator in the decision script.

### Solved example

Levels: 0 = no blocking; 1 = blocking with an alternative; 2 = blocking without an alternative. A cordial tone doesn’t prevent level 2.

### Your turn

Create a three-level rubric for difficulty of access. Avoid using “good”, “average”, and “bad” without explaining.

<details>
<summary>Check the commented answer</summary>

0: accesses normally and has usage questions. 1: part of the content fails, but there’s a functional alternative. 2: can’t access the necessary content and has no alternative.

</details>

[Back to the index](../README.md)
