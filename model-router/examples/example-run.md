---
title: "Model Router: Example Run"
---

# Model Router: Example Run

This skill produces no document of its own, since its output is a routing decision and a short report. This sample shows what that output looks like on a real task, so you can picture a run before you use it. The task was "Refactor the granola skill to handle the new transcript schema and add tests."

## The routing line

The skill announces the decision in one line before it dispatches:

> Routing this to **Sonnet**. **Opus** will supervise.

## What happened

The skill classified the task as Sonnet tier, since it is a multi-file change with a clear goal and a moderate surface. It dispatched a Sonnet worker that refactored the skill and wrote the tests, then dispatched an Opus supervisor that checked the four axes of correctness, style, completeness and depth, then patched two missed cases in place.

## The final report

The run closes with a two-block report:

> **Result:** Refactored `granola/SKILL.md` and added `granola/tests/test_schema.py` with six cases covering the old and new transcript shapes. The tests pass.
>
> **Observed:** Sonnet ran the work. The Opus supervisor found two unhandled fields in the new schema and a missing null check, patched all three in place, then confirmed the tests still pass.
