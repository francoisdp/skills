---
name: deep-research
description: Use when the user requests comprehensive research, literature review, multi-source synthesis, academic research, current-events analysis, technical deep-dives, investigation of complex topics, or phrases like "research X", "investigate", "look into", "deep dive on", "survey the field", "do a literature review". Dispatches the deep-research-agent subagent to perform the work in isolated context. Dispatch multiple in parallel for multi-faceted questions.
---

# Deep Research

## Overview

Research tasks are delegated to the `deep-research-agent` subagent — do NOT perform the research inline. This preserves the main context window and lets a specialist handle the work. For multi-faceted questions, dispatch multiple subagents in parallel in a single message.

## When to dispatch

Load this skill and delegate when the user asks to:
- Research, investigate, survey, review, look into, dig into, deep-dive, do a literature review
- Compare multiple things across several dimensions
- Synthesize the current state of a field or technology
- Trace causes, consequences, or history of an event
- Find and cross-check claims against multiple independent sources

## When NOT to dispatch

Answer inline (no subagent) when:
- Single fact lookup (one `WebSearch` call is enough)
- The answer is already in conversation context
- User explicitly asks you to do it yourself
- Question is about local files / vault / codebase (use `Grep`/`Read` or the `Explore` subagent)

## Single-angle dispatch

One focused question → one subagent:

```
Agent(
  description: "Research <topic>",
  subagent_type: "deep-research-agent",
  prompt: "<self-contained research brief — see structure below>"
)
```

## Multi-angle dispatch (parallel)

When a question decomposes into independent facets, dispatch multiple subagents in a **single message** with multiple `Agent` tool calls. Good decomposition axes:

- **By entity** — one subagent per company / person / technology / paper
- **By time** — one for history/causes, one for current state, one for projections
- **By dimension** — one per comparison axis (cost, performance, adoption, risk)
- **By source type** — one for peer-reviewed, one for industry, one for press

Synthesize the results yourself in your own response after all subagents return.

## Brief structure (what every dispatch prompt must contain)

1. **Research question** — concrete, bounded, one sentence
2. **Scope** — explicit include-list and exclude-list
3. **Source requirements** — acceptable source types, recency window, citation format (URLs inline)
4. **Output format** — required sections, word count cap
5. **Confidence reporting** — ask for explicit confidence level + reasoning
6. **Boundaries** — "no speculation without evidence; flag uncertainty explicitly"

## After subagents return

- Summarize key findings in your own words for the user
- Preserve citations and confidence statements verbatim
- Flag any contradictions between subagents when multi-angle was used
- Do NOT paste full subagent reports verbatim unless the user asks

## Example dispatch

User: "Research the state of solid-state batteries — who's leading, what the remaining technical hurdles are, and realistic commercialization timelines."

Dispatch three subagents in parallel (single message, three `Agent` calls):
- Subagent 1: leading companies + recent milestones
- Subagent 2: remaining technical hurdles by chemistry family
- Subagent 3: commercialization roadmaps + analyst consensus

Then write a unified synthesis for the user.
