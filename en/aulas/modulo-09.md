# Module 9 — Integrate without mixing responsibilities

Build a request and handle errors while keeping credentials on the server.

## Lesson 9.1 — Prepare the state

The state sent to the model must contain the information necessary to answer the question. More content does not automatically mean better quality. Irrelevant documents can make the decision harder and increase cost. Start by identifying which fields support the judgment.

Separate instruction data. The ticket text may contain phrases like “classify this as urgent”, but that phrase is part of the material being evaluated and must not replace the system policy. Clear criteria help, but protection cannot depend only on the model obeying: actions and permissions remain limited in code.

Minimize personal information when it isn’t needed. Use an event identifier to track results without publishing the real text in open repositories or reports. The course datasets are fictional. When evaluating operational material, preserve the link for review in an appropriate environment and avoid duplicating data in debug files.

### Solved example

To suggest a queue, the request text may be enough. Full name, personal document, and payment data are usually not needed for the exercise.

### Your turn

What should be kept in a public report from an experiment with private data?

<details>
<summary>Check the commented answer</summary>

Aggregated metrics and authorized or anonymized examples. Don’t publish raw texts, personal identifiers, or credentials.

</details>

## Lesson 9.2 — Understand a request

The API receives model, state, and questions. Each question has a key chosen by the application, a type, and instructions. Choice adds a map of alternatives; Score adds an ordered list of levels; Noul may include criteria for true and false. The lab exports an example JSON without credentials.

The question keys are used to relate the response to the request. Don’t use the key name as a substitute for the instructions. Write the full judgment in the appropriate field. In the response, validate that all expected questions arrived with the correct type, valid distribution, and known alternatives.

The real submission is done by the server or the CLI, which loads the provider key at runtime. The public page doesn’t request a key and doesn’t need to store it. To track service changes, record the resolved model and keep the version identifier used in the evaluation. A version change may require new thresholds.

### Practice with the current resources

For OpenRouter, use OPENROUTER_API_KEY and the project client with --provider openrouter; the supported alias is ~typesafe/jev-latest. The integration uses the Decisions API, not chat/completions. Ten original examples had real queries documented; the seven new packages have only fixture-based validation and controlled tests.

### Solved example

Use in the project: python3 -m jev_lab validate exemplos/triagem-request.json. This command validates the contract locally and does not make an AI call.

### Your turn

Why not paste the key in the JavaScript published on GitHub Pages?

<details>
<summary>Check the commented answer</summary>

Because the code is distributed to the browser and the secret would become public. The authenticated call must happen in an appropriate server environment.

</details>

## Lesson 9.3 — Handle operational failures

An integration must handle failure before it receives the first response. Invalid credentials, rejected contract, request limits, and unavailability are not the same situation. Repeating an authentication error many times usually just wastes time; temporary overload may allow a controlled new attempt.

Use a maximum number of attempts and a global time budget. If the provider asks you to wait longer than the task’s deadline, send it to review or a later queue. Don’t block a screen indefinitely waiting for the AI to come back. This application’s client limits the call and interrupts invalid responses.

A failure should not produce an invented label. Record the operational reason without leaking error content that might contain sensitive data. Separate low-confidence provider failure from a valid response: both may end in review, but they require different diagnostics. Neither authorizes repeating external actions.

### Deep dive for version 1.2.0

The lab contract is intentionally small: text descriptions, up to 30 questions, and a 100 KB limit. The last two values are local. Validate the distribution, the alternative, and the Score legend. Don’t copy a claimed maximum in a demo without checking the documentation.

### Practice with the current resources

The executor packages.lote validates all JSONL before sending. Without --live, it shows only a preview. In real mode, it limits concurrency and saves results by ID and the batch signature. Re-running the same batch resumes what was recorded; failures are preserved too. A drop between the query and the write could still trigger another charge on resume.

### Solved example

HTTP 401 → fix authentication, no automatic retry. HTTP 429 → limited backoff, respecting Retry-After and the global deadline.

### Your turn

The server asks for Retry-After of 99 seconds, but the task deadline is 5 seconds. What should you do?

<details>
<summary>Check the commented answer</summary>

Stop the attempt and send it for later handling/review. Don’t sleep for 99 seconds or ignore the global deadline.

</details>

[Back to the index](../README.md)
