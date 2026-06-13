# model-router

[![Tested with NVIDIA SkillSpector](https://img.shields.io/badge/Tested%20with-NVIDIA%20SkillSpector-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/SkillSpector)

> **Security:** This skill was scanned with [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), a security scanner for AI agent skills. The skill contains no executable code. Every pattern the scanner flagged was reviewed manually and assessed as a false positive against the skill's documentation and templates. For your own safety, read the skill source and re-scan it before installing if you have any doubt. The full scan report sits in this folder as `skillspector-report.md`.

A Claude Code skill that routes each work task to the cheapest model tier that can handle it, then verifies the result with a higher-tier supervisor that patches the output in place.

## What it does

When you invoke this skill, it:

1. Classifies the prompt into one of three tiers: **Haiku** (mechanical, cheap), **Sonnet** (standard engineering work), or **Opus** (deep reasoning, ambiguous spec).
2. Dispatches a worker subagent at that tier via the Claude Code `Agent` tool.
3. Dispatches a supervisor one tier higher that checks the output on four axes: correctness, style, completeness, and depth of solution.
4. The supervisor patches the worker's output in place if any axis falls short.
5. Reports back with a two-block `Result` and `Observed` summary.

The pattern roughly doubles token cost per prompt, so it biases hard toward cheap tiers and skips entirely on conversational replies.

## Installation

### Claude Code (CLI / Desktop / IDE extension)

1. Create the directory `~/.claude/skills/model-router/`.
2. Copy `SKILL.md` into that directory.
3. The skill is now available in any Claude Code session as `model-router` in the skills list.

To invoke it manually, use the `Skill` tool:

```
Skill({ skill: "model-router" })
```

To activate it automatically on every actionable prompt, add the following instruction to your `~/.claude/CLAUDE.md`:

```
## Model Routing

Before responding to any prompt that asks for real content production (code, file edits,
reports, multi-step research, drafts, refactors, debugging, design), invoke the
`model-router` skill via the Skill tool before any other tool call.

Skip on greetings, chit-chat, simple lookups, and clarifying questions back to the user.

Skill: `~/.claude/skills/model-router/SKILL.md`
```

### Verification

After installation, start a new Claude Code session and ask it to write any piece of code. The first line of its response should read:

```
Routing this to **Sonnet**. **Opus** will supervise.
```

(The exact tier depends on the task, but the routing announcement should always appear.)

## File layout

```
model-router/
├── SKILL.md    — the skill definition loaded by the Skill tool
└── README.md   — this file
```

## Tier guide

| Tier | When to use |
|------|-------------|
| Haiku | Mechanical edits, format conversion, simple lookups |
| Sonnet | Feature implementation, debugging, documentation, code review |
| Opus | Architecture, security-critical code, cross-cutting refactors, ambiguous specs |

## Supervisor rubric

The supervisor checks four axes on every pass:

1. **Correctness** — does the output do what was asked, with no bugs or hallucinated APIs?
2. **Style** — does it match project conventions and any voice rules in CLAUDE.md?
3. **Completeness** — are all parts of the request addressed, including edge cases?
4. **Depth** — did the worker find the best approach, or stop at the first plausible one?

## License

MIT. Use freely.
