# deep-research

[![Tested with NVIDIA SkillSpector](https://img.shields.io/badge/Tested%20with-NVIDIA%20SkillSpector-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/SkillSpector)

> **Security:** This skill was scanned with [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), a security scanner for AI agent skills. The skill contains no executable code. Every pattern the scanner flagged was reviewed manually and assessed as a false positive against the skill's documentation and templates. For your own safety, read the skill source and re-scan it before installing if you have any doubt. The full scan report sits in this folder as `skillspector-report.md`.

A skill that runs comprehensive research as a delegated task rather than as inline web searches, so the main conversation stays clear while a specialist agent does the digging. It hands a self-contained research brief to a `deep-research-agent` subagent, which plans the investigation, searches and cross-checks sources, then returns a structured report with citations and confidence levels. For a question with several independent facets, the skill dispatches several agents in parallel and synthesises their results.

## What it does

The skill is the dispatcher and the bundled agent is the engine. When you ask a research question, the skill decides whether it warrants delegation, writes a bounded brief with an explicit scope, source requirements and output format, then dispatches one `deep-research-agent` for a single focused question or several in parallel for a multi-angle one. Each agent works in its own context, which keeps the main window free, then returns an executive summary, key findings with inline citations, a synthesis and an explicit confidence statement. The skill then writes a unified answer for you, preserving the citations and flagging any contradictions between agents.

## Installation

This skill has two parts that install in two places: the skill itself and the agent it dispatches. Install both, since the skill does nothing without the agent.

For **Claude Code**, copy the skill folder into `~/.claude/skills/deep-research/` for a user-level install, or `.claude/skills/deep-research/` inside a project, with the folder named `deep-research` to match the frontmatter. Then copy the bundled agent from `agent/deep-research-agent.md` into your agents directory at `~/.claude/agents/deep-research-agent.md`, since the skill dispatches an agent of type `deep-research-agent` and Claude Code resolves that name from the agents directory. Once both are in place the skill activates on research requests with nothing further to configure.

For **Claude Desktop and claude.ai**, add the skill through the Skills or Capabilities setting. The subagent dispatch is a Claude Code feature, so on a platform without subagents the skill cannot delegate. In that case use the agent file as a system prompt or a project instruction instead, which gives you the same research methodology run inline rather than in a separate context.

For **Copilot CLI** and **Gemini CLI**, the skill is discovered the same way as any other skill in those tools, though the parallel-subagent dispatch depends on the host supporting subagents. Where it does not, fall back to using the agent's methodology as an instruction file.

For **any other tool**, the agent file is a complete research methodology in plain Markdown, so you can paste it into a system prompt and ask the model to follow it, which works without any skill or subagent mechanism.

## Usage

Trigger the skill with a research request. Phrases it recognises include "research X", "investigate", "look into", "deep dive on", "survey the field" and "do a literature review". The skill delegates when the question needs multi-source synthesis, a comparison across several dimensions, a survey of a field or a trace of causes and consequences. It answers inline without delegating when the question is a single fact lookup, when the answer is already in the conversation or when the question is about your own files rather than the web.

For a multi-angle question the skill decomposes the work along a sensible axis, for example one agent per company, one per time period or one per comparison dimension, dispatches them in parallel, then synthesises. The result you receive is the synthesis, with citations and confidence preserved, rather than the raw agent reports. A rendered example of what one agent returns is in `examples/example-report.pdf`.

## Rationale

Research done inline in the main conversation has two problems, which this skill is built to solve. The first is context, since a thorough investigation reads many sources and fills the window with material that crowds out the actual task, so the skill moves the reading into a subagent whose context is separate and disposable, so only the distilled report comes back. The second is rigour, since an inline answer tends toward a few quick searches and a confident summary, while the bundled agent follows a deliberate method of planning, multi-hop reasoning, self-reflection and source cross-checking, which produces an answer that states its confidence and shows its evidence rather than asserting.

The parallel dispatch exists because many research questions are really several independent questions wearing one coat, for example a question about who leads a field, what the hurdles are and when commercialisation is realistic. Those facets do not depend on each other, so running them at once is both faster and cleaner than one agent trying to hold all three. The synthesis step is where the separate findings are reconciled and any contradictions surfaced.

The brief structure matters because a subagent works in isolation with no view of the conversation, so a vague prompt yields a vague report. A good brief names the question in one sentence, fixes the scope with an include-list and an exclude-list, states the acceptable sources and the recency window, sets the output format and asks for an explicit confidence level, which is what turns a delegated search into a usable research report.

## Extension guide

The skill and the agent are plain Markdown, so customising them means editing two files.

To change when the skill delegates rather than answering inline, edit the "When to dispatch" and "When NOT to dispatch" lists in `SKILL.md`. To change how multi-angle questions are split, edit the decomposition axes in the same file. To change the research methodology itself, which is the planning strategies, the reasoning patterns, the quality standards and the report structure, edit `agent/deep-research-agent.md`, since that file is what governs how the investigation runs and how the report is shaped. To change the required shape of the brief that every dispatch carries, edit the brief-structure section of `SKILL.md`, then make sure the report-structure section of the agent matches what the brief asks for, so the two stay in step.

## Repository layout

```
deep-research/
├── SKILL.md                          the dispatcher: when to delegate and how to brief
├── README.md                         this file
├── LICENSE                           MIT licence
├── agent/
│   └── deep-research-agent.md        the research engine, install into ~/.claude/agents/
└── examples/
    ├── example-report.md             an illustrative research report showing the output format
    └── example-report.pdf            the example rendered, so you see the output first
```

## Licence

This package is released under the MIT licence, with the full text in the `LICENSE` file.

## Credit

The skill was developed by Francois du Plessis. Contributions and forks are welcome.
