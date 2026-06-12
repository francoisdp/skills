# Worked example: configuration for one user

This is the Configuration table from `SKILL.md`, filled in for the author's own setup. Copy the
shape and replace each value with your own.

| Setting | Value |
|---|---|
| Skills source | `~/.claude/skills/`, then the vault's `.claude/skills/` |
| Staging folder | `4_Resources/Skills - Claude/` inside an Obsidian vault, kept as a local copy of each package |
| Skills repository | `francoisdp/skills` (public) |
| Author | Francois du Plessis |
| Writing standard | the `anti-ai-writing` skill, applied at full strength |

Notes on this setup:

- The staging folder doubles as a browsable archive, so every deployed skill keeps a copy in the
  vault beside the published version in the repository.
- The writing standard is the full `anti-ai-writing` rule set rather than the short default scan
  list, so the gate in step 8 runs the complete review rather than the five quick scans.
- The author publishes everything in one repository, `francoisdp/skills`, with a folder per skill,
  so `anti-ai-writing`, `model-router`, `youtube2article`, `marp-deck`, `study-note` and
  `deploy-skill` all sit side by side at the repository root.
