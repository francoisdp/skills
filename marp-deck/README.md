# marp-deck

[![Tested with NVIDIA SkillSpector](https://img.shields.io/badge/Tested%20with-NVIDIA%20SkillSpector-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/SkillSpector)

> **Security:** This skill was scanned with [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), a security scanner for AI agent skills. The skill contains no executable code. Every pattern the scanner flagged was reviewed manually and assessed as a false positive against the skill's documentation and templates. For your own safety, read the skill source and re-scan it before installing if you have any doubt. The full scan report sits in this folder as `skillspector-report.md`.

A skill that turns a Markdown note into a self-contained Marp presentation, exported to PDF, that opens and travels on its own outside the vault it came from. The source note stays untouched as the knowledge record, while the deck is a distribution copy with its images bundled, its wiki-links turned into footnote references and its slides built to a chosen template, so you can email the result or present it without needing Obsidian or the original note.

## What it does

Point the skill at a note and pick how aggressively to condense it, then it reads the note, resolves a template, copies every referenced image into the deck folder, rewrites the image references to plain Markdown that Marp understands, turns wiki-links into numbered footnotes collected on a References slide, builds the slides at the level you chose, writes a `deck.md` and exports a `deck.pdf` through the Marp command-line tool. The condensing has three levels, from an aggressive cut to roughly ten or fifteen slides, through a lighter pass that keeps every section, to a verbatim split that puts one slide per heading. The source note is never written back to, so the deck is always a copy.

## Installation

The skill is a folder containing `SKILL.md` and a `templates/` folder of starter templates. The folder must be named `marp-deck` so it matches the skill name in the frontmatter.

For **Claude Code**, copy the folder into `~/.claude/skills/marp-deck/` for a user-level install, or `.claude/skills/marp-deck/` inside a project. Claude Code discovers the skill from its frontmatter.

For **Claude Desktop and claude.ai**, add the skill through the Skills or Capabilities setting in the application.

For **Copilot CLI**, the skill is auto-discovered from installed plugins through the `skill` tool.

For **Gemini CLI**, the skill activates through `activate_skill`, with the frontmatter loaded at session start.

For **any other tool**, the steps are plain Markdown you can paste into a system prompt or an instruction file such as `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`.

The PDF export runs the Marp command-line tool through `npx`, so you need Node.js installed, which provides `npx`. The export step renders through headless Chrome or Chromium, so you need one of those available. If the tool cannot find it, you set the `CHROME_PATH` environment variable to point at your browser. No global Marp install is needed, since `npx -y @marp-team/marp-cli@latest` fetches it on demand.

The skill reads templates from a `Marp_template/` folder at the vault root. On first use, copy the five bundled templates from this package's `templates/` folder into `Marp_template/`, or edit Step 2 of `SKILL.md` to point at the package `templates/` folder if you would rather keep the templates beside the skill.

## Usage

Trigger the skill with a note path and one of the phrases it recognises. Say "Make a deck from `<path>`" for the default template, "Make a deck from `<path>` using `<template>`" to choose one of the bundled templates by name, or "Rebuild the deck for `<path>`" to regenerate over an existing output. The skill asks once how aggressively to condense, unless you state the level yourself, then it runs the full pipeline and reports the deck path, the PDF path, the template used, the slide count, the images copied and the wiki-links footnoted. It asks before overwriting an existing deck folder, so a rebuild never destroys output without your word.

The five bundled templates are `default` for general decks, `dark` for screen presentations, `academic` for dense paginated technical talks, `business` for a bold accent suited to proposals and `aerospace` for an engineering-style technical briefing. To add your own, drop a `.md` file with Marp frontmatter into `Marp_template/` and the skill picks it up on the next run.

## Rationale

A note and a presentation answer different needs. The note is where the thinking lives, linked into the rest of your knowledge through wiki-links and embedded images, while a presentation has to stand alone in front of an audience or in someone's inbox, with no access to the vault that gave the note its context. The skill exists to cross that gap without damaging the note, which is why it always works on a copy and never writes back to the source.

Most of the steps exist because Obsidian Markdown and Marp Markdown are not the same dialect. Obsidian embeds images with `![[image.png]]` and links notes with `[[Note]]`, neither of which Marp renders, so the skill rewrites image embeds into the standard `![alt](path)` form that Marp understands, copies the image files into the deck folder so the deck is portable, then turns each wiki-link into a numbered footnote on a References slide rather than dropping the link entirely, which keeps the provenance of each claim visible to the audience. Dataview blocks are stripped with a comment, because they only evaluate inside Obsidian, while callouts become blockquotes and tasks stay as checkboxes, since Marp renders those natively. The condensing levels exist because the same note serves different talks, where a conference slot needs the aggressive cut to a tight arc while a teaching session may want every section kept, so the skill asks once rather than guessing. The PDF export through `npx` avoids a global install, which keeps the skill self-contained and easy to run on a fresh machine.

## Extension guide

The skill is plain Markdown plus a folder of templates, so customising it means editing `SKILL.md` or adding template files.

To change the look of a deck, edit a template in `templates/` or add a new one. A template is a self-contained Marp file carrying the frontmatter that sets `theme`, `paginate` and `size`, an optional inline `<style>` block and the placeholder scaffolding the skill fills in, which is `[TITLE]`, `[SUBTITLE]`, `[DATE]`, `[AUTHOR]`, `[SECTION]` and `[POINT]`. Drop the new file into `Marp_template/` at the vault root and call it by name.

To change how the note is condensed, edit the summarization rules in Step 7, where the slide targets and the bullet style for each level are stated. To change the deck folder layout or the image-handling, edit Steps 4 and 5. To change how wiki-links are rendered, edit Step 6, where the footnote format lives. To set a default author name on the title slide, fill the `[AUTHOR]` placeholder in your chosen template rather than leaving it empty.

The skill assumes an Obsidian-style vault for its wiki-link, Excalidraw, Dataview and callout handling, so a plain-Markdown user can ignore those steps, since a note without wiki-links or embeds simply skips them and the core note-to-deck-to-PDF pipeline still runs.

## Repository layout

```
marp-deck/
├── SKILL.md             the full pipeline: read, template, condense, images, links, export
├── README.md            this file
├── LICENSE              MIT licence
└── templates/           five starter Marp templates
    ├── default.md
    ├── dark.md
    ├── academic.md
    ├── business.md
    └── aerospace.md
```

## Licence

This package is released under the MIT licence, with the full text in the `LICENSE` file.

## Credit

The skill was developed by Francois du Plessis. Contributions and forks are welcome.
