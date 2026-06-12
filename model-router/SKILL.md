---
name: model-router
description: Use at the start of every actionable work prompt that produces real content (code, file edits, reports, multi-step research, drafts, refactors, debugging, design). Classifies the task into Haiku, Sonnet, or Opus, announces the choice up front, dispatches a worker subagent at that tier via the Agent tool, then dispatches a supervisor one tier higher (Opus self-reviews) that judges correctness, style, completeness, and depth, patching the worker's output in place when any of the four falls short. Skip on greetings, chit-chat, simple lookups, and clarifying questions back to the user.
---

# Model Router

Route each work task to the cheapest model that can plausibly handle it, then verify the result with a higher-tier supervisor that patches the worker's output in place when it falls short on correctness, style, completeness, or depth.

## When to invoke

Run this skill at the start of any prompt that asks for real content production: writing code, editing files, generating reports, doing multi-step research, drafting documents, refactoring, debugging, or designing systems.

Skip the skill on:

- Greetings, chit-chat, or one-line social replies.
- Pure clarifying questions you need to ask the user before doing anything.
- Trivial factual answers you already know and that need no tool calls.
- Single-file reads or lookups the user explicitly asked for with no follow-up work.

If you are not sure whether a prompt is actionable, run the skill anyway. The classification step is fast and cheap, and the supervisor pass only fires once a worker has produced output worth checking.

## Step 1: classify the task

Pick exactly one tier. Bias hard toward the cheapest tier that can plausibly do the job. The supervisor pass is the safety net, so undershooting on classification is preferred over overshooting.

### Haiku — fast, cheap, narrow

Mechanical or template-driven work where the spec is explicit and verification is local.

- Single-file edits with literal instructions like rename, remove, replace.
- Frontmatter extraction, format conversion, simple parsing.
- Boilerplate scaffolding from a known template.
- Listing, filtering, tabulating data the user already has.
- Short factual lookups that need a tool call but no judgment.

### Sonnet — default for real engineering work

Multi-step work that needs judgment but where the goal is clear and the surface area is moderate.

- Implementing a feature with a clear spec across a few files.
- Standard debugging where the symptom roughly points at the cause.
- Writing documentation, blog drafts, or reports with synthesis.
- Code review on moderate diffs.
- Most build-X or fix-Y requests.

### Opus — deep reasoning, broad surface, ambiguous spec

Work where getting it wrong is costly or the path is not obvious.

- Architectural or system design across many components.
- Cross-cutting refactors touching many files with non-trivial dependencies.
- Subtle bug investigation where the symptom is far from the cause.
- Algorithm design, security-sensitive code, correctness-critical logic.
- Long-horizon research with synthesis across many sources.
- Anything the user explicitly flags as hard, sensitive, or load-bearing.

When two tiers seem plausible, pick the lower one and let the supervisor catch any underperformance.

## Step 2: announce the routing decision

Before dispatching, tell the user in one short line what the routing decision is. Use this exact shape:

> Routing this to **\<tier\>**. **\<supervisor_tier\>** will supervise.

Supervisor mapping:

- Worker Haiku → Supervisor Sonnet.
- Worker Sonnet → Supervisor Opus.
- Worker Opus → Supervisor Opus, run as a self-review pass with explicit instruction to challenge the first answer rather than rubber-stamp it.

## Step 3: dispatch the worker

Use the `Agent` tool with the `model` parameter set to `haiku`, `sonnet`, or `opus` to match the chosen tier. Subagent type is usually `general-purpose` unless a more specific agent fits the task.

The worker prompt must be self-contained because the subagent has no view of this conversation. Include:

- The user's full original request, verbatim.
- The current working directory and any relevant file paths.
- Constraints from the active CLAUDE.md files, especially voice rules.
- A clear statement of whether the worker should write or edit files, or only return text.
- An instruction to report back the artefacts produced (paths, snippets) and the reasoning behind any non-obvious choices, so the supervisor has something concrete to judge.

Wait for the worker to finish before moving on.

## Step 4: dispatch the supervisor

Dispatch a second `Agent` call with `model` set one tier higher than the worker. For Opus workers, the supervisor is also Opus.

The supervisor prompt must include:

- The user's full original request.
- The worker's full output, including paths to any files the worker touched.
- The four-axis rubric (see below), spelled out.
- An explicit instruction to **patch and improve in place** rather than redo the work from scratch. The supervisor should edit the worker's existing files directly when patching, not write parallel files or duplicate work.
- Permission to leave the work untouched if the rubric is satisfied.

The supervisor returns one of two outcomes:

1. *No changes needed.* A short justification stating which axes were checked and why each passes. The worker's result stands.
2. *Patched.* A list of edits applied, the reason for each, and a one-line verdict on the patched result.

## Step 5: final report to the user

After the supervisor returns, give the user a tight two-block summary:

> **Result:** what was produced, with file paths or the key output inline.
>
> **Observed:** which tier ran the work, what the supervisor verdict was, and any patches the supervisor applied.

Keep this to a few lines. The routing should be visible without becoming noise.

## Supervisor rubric (the four axes)

Spell these out in the supervisor's prompt every time so the rubric stays consistent.

1. **Correctness.** Does the output do what the user asked? Are there bugs, broken references, off-by-one errors, wrong file paths, hallucinated APIs, fabricated facts, or invalid syntax?
2. **Style.** Does the output match project conventions, surrounding code or document style, the voice rules from CLAUDE.md, and the global anti-AI writing constraints? In particular: no em-dashes, no semicolons, no "And/But/So" sentence openers, no meta-honesty framings, warm flowing voice.
3. **Completeness.** Are all parts of the request addressed? Are edge cases handled? Are tests, documentation, follow-up tasks, or related files that should have been touched actually touched?
4. **Depth of solution.** Did the worker stop at the first plausible answer when a deeper one was warranted? Is the design too shallow for the problem? Did the worker miss a structural improvement, a better abstraction, or a more robust approach the higher-tier model would naturally see?

If any of the four falls short, the supervisor patches in place and explains the patch. If all four pass, the supervisor returns the no-changes verdict and the worker's output stands.

## Cost discipline

The worker plus supervisor pattern roughly doubles tokens on every actionable prompt. Keep the cost honest:

- Bias hard toward Haiku and Sonnet during classification.
- Skip the skill entirely on conversational replies and trivial lookups.
- Keep the supervisor's prompt focused on the four-axis rubric, not on rewriting from scratch.
- Trust the worker's output and patch only what fails the rubric.
- Never run a third pass. The supervisor is the final word.

## Example: a Haiku-tier prompt

User: "Add a frontmatter field `status: active` to every file in `Clients/` that does not already have one."

1. Classify: Haiku. Mechanical, scoped, verification is local.
2. Announce: Routing this to **Haiku**. **Sonnet** will supervise.
3. Worker (Haiku, general-purpose): edits the files, reports the list of paths touched.
4. Supervisor (Sonnet, general-purpose): checks correctness (only files missing the field were touched, no double-adds), style (frontmatter formatting matches the rest of the vault), completeness (all matching files touched, none skipped), depth (no obvious better approach). Patches in place if any axis fails.
5. Final report: Result lists files touched. Observed lists Haiku used, Sonnet verdict, any patches.

## Example: a Sonnet-tier prompt

User: "Refactor the `granola` skill so it handles the new transcript schema and add tests."

1. Classify: Sonnet. Multi-file change, clear goal, moderate surface area.
2. Announce: Routing this to **Sonnet**. **Opus** will supervise.
3. Worker (Sonnet): refactors the skill, writes tests, returns paths and a short rationale.
4. Supervisor (Opus): checks the four axes. Often catches missed edge cases or a shallower-than-warranted design and patches in place.
5. Final report: Result lists files and tests. Observed lists Sonnet used, Opus verdict, any patches.

## Example: an Opus-tier prompt

User: "Design the data model for the new cohort grading system across the report, study-note, and review skills."

1. Classify: Opus. Cross-cutting, ambiguous spec, design-heavy.
2. Announce: Routing this to **Opus**. **Opus** will self-review.
3. Worker (Opus): produces the design and any artefacts.
4. Supervisor (Opus, self-review): explicitly told to challenge the first pass rather than agree with it. Looks for missed integration points, weak abstractions, and depth gaps. Patches in place if any axis fails.
5. Final report: Result lists the design and any files. Observed lists Opus used, self-review verdict, any patches.
