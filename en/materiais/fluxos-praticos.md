# Companion roadmap — from the question to the flow

It follows course v1.3.0 and the Jev project v1.6.1. Run the commands in the root of the **jev** clone, not in the course clone. This roadmap complements the 36 lessons and the 12 labs.

## 1. Choose the problem

The project has 17 packages: the ten initial ones and seven new ones for inbox, YouTube comments, communities, meetings, transcript cut-downs, notes, and curation.

```bash
git clone https://github.com/inematds/jev.git
cd jev
python3 -m pacotes.executar --list
python3 -m pacotes.executar reunioes
```

Identify the main decision and the supporting questions. In the meetings package, ask whether there is a decision, next step, owner, and deadline. Don’t confuse “there is an owner” with extracting their name, nor “there is a deadline” with calculating a date.

**Exercise:** “We need to improve the tutorial; we’ll talk later.” Is that enough to create an assigned, scheduled task?

**Answer:** no. It can indicate intent, but it lacks explicit routing. Jev classifies signals; the application still needs to confirm the task and resolve the calendar.

## 2. Read the metrics of all questions

```bash
python3 -m pacotes.qualidade reunioes
python3 -m pacotes.qualidade cortes
```

These commands use invented fixtures and original references. Check `origins: ["simulation"]`. Choice measures label accuracy; Noul measures accuracy and Brier; Score measures absolute error and normalized error. The report also shows coverage and errors.

**Exercise:** if there is a contract error in half the records, is it enough to show low Brier on the remaining ones?

**Answer:** no. Brier accounts for valid answers, but coverage dropped. Failures remain in the denominator of accuracy. Presenting only the valid subset would hide operational problems.

## 3. Prepare a batch without consuming an API

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl
```

Check `mode: preview` and `calls: 0`. Each row contains `id` and `state`. The executor rejects duplicate IDs and invalid inputs before consulting the provider. You don’t need a database or a queue service for this exercise.

**Exercise:** can two events with the same ID and different texts be treated as the same occurrence?

**Answer:** not in this batch; the executor rejects them. Fix the identification at the source before sending.

## 4. Understand the transition to real mode

With a configured key in the backend and authorized data:

```bash
python3 -m pacotes.lote reunioes data/reunioes-eventos.jsonl --live --provider openrouter --workers 2 --interval 1 --out runs/reunioes.jsonl
```

Real mode sends data and consumes credits. Running the same command resumes saved results, including errors. A drop between the response and the write step can still repeat consumption; there’s no guarantee of a single charge. Do not modify the batch or template to reuse the same checkpoint.

The interval controls when queries start, not each internal retry. Compare concurrency and equivalent conditions when evaluating speed. A fast batch doesn’t prove quality, calibration, or universal gain.

## 5. Deliver the pilot

Define, with independent human reference:

- Questions and alternatives, including insufficiency.
- Minimal data and sending authorization.
- Expected labels per question, without copying the model’s prediction.
- Quality metrics, coverage, full cost, and latency.
- Review of false negatives among discarded items.
- Criterion to adopt, collect more evidence, or not automate.

For Codex and Claude Code, the skill `jev-decidir` queries the client as a tool. In OpenPCBot v3, `/jev observar` uses its own gateway and only compares suggestions; `/ajuda jev` explains the feature. The notes and meetings packages are still not new native bot commands.

[Complete integration instructions and reference format](https://github.com/inematds/jev/blob/main/docs/11-fluxos-praticos.md) · [Packages](https://github.com/inematds/jev/tree/main/pacotes) · [Back to course](../README.md).
