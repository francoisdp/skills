# study-note

A skill that processes a Markdown, text or Quarto file into a single standardised study-note format, then places it where it belongs and links it to related notes. It takes a file path, pasted text or a bare topic, extracts or asks for the metadata, converts the body into a consistent structure of summary, detail, sources and connections, then writes the note and suggests wiki-links to related material already in your collection.

## What it does

Give the skill a source and it works out what you handed it, which is a file to read, pasted text to convert or a topic to start from scratch. It then asks where the note should live, infers the title, date, source and tags while asking you to confirm anything it could not determine, converts the content into the standard study-note shape, writes the file, then scans your note folders for related material and proposes connections. Quarto input is handled specially, with callouts, cross-references and shortcodes converted to their Markdown or Obsidian equivalents, so a `.qmd` export becomes a clean note rather than a file full of syntax that does not render.

## Installation

The skill is a folder containing `SKILL.md` and an `examples/` folder. The folder must be named `study-note` so it matches the skill name in the frontmatter.

For **Claude Code**, copy the folder into `~/.claude/skills/study-note/` for a user-level install, or `.claude/skills/study-note/` inside a project. Claude Code discovers the skill from its frontmatter.

For **Claude Desktop and claude.ai**, add the skill through the Skills or Capabilities setting in the application.

For **Copilot CLI**, the skill is auto-discovered from installed plugins through the `skill` tool.

For **Gemini CLI**, the skill activates through `activate_skill`, with the frontmatter loaded at session start.

For **any other tool**, the steps are plain Markdown you can paste into a system prompt or an instruction file such as `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`.

The skill has no command-line dependencies, so it works as soon as the folder is in place. It does assume a folder-based note collection for its placement and connection steps, which fits an Obsidian vault or any directory of Markdown files.

## Usage

Trigger the skill with one of the phrases it recognises. Say "Process this into a study note" to convert content you provide, "Create a study note on [topic]" to start a blank note on a subject, or "Import this file as a study note" to read and convert a file. The skill asks where the note belongs, presents the title, source, tags and placement it inferred for you to confirm or correct, then writes the note and shows you the path, the frontmatter summary and any connections it found. It closes by asking whether you want changes, so the first write is never the last word.

The note it produces carries a frontmatter block with `type`, `title`, `date`, `source`, `status`, `area` and `tags`, followed by four sections. The Summary holds three to five bullet points, generated from the content when the source has no summary of its own. The Detail preserves the original structure. The Sources section gathers any URLs or citations. The Connections section lists the wiki-links the skill suggested to related notes.

## Rationale

A collection of notes is only useful when the notes share a shape and connect to each other, since a pile of differently structured files is hard to scan, hard to search and hard to navigate. The skill exists to impose one consistent shape on whatever you feed it, so that every study note opens with a summary you can read in seconds, holds its detail in a predictable place, records where its claims came from, then points to the related notes around it. The fixed frontmatter serves the same end, because consistent fields let a notes app filter and group the collection rather than treating each note as a one-off.

The Quarto handling exists because research material often arrives as `.qmd` files from a writing or analysis tool, where callouts, cross-references and shortcodes are written in Quarto syntax that does not render in a plain notes app, so the skill converts each construct to its Markdown or Obsidian equivalent rather than leaving the reader to decode it. The connection scan exists because the value of a note grows when it is linked into what you already know, so the skill greps your note folders for shared tags and topic words, then suggests wiki-links rather than leaving every new note stranded on its own. The skill asks before guessing on placement and metadata, since the cost of one question is small next to the cost of a note filed in the wrong place with the wrong tags.

## Extension guide

The skill is plain Markdown, so customising it means editing `SKILL.md`.

The most useful change is the placement list. Step 2 ships with a generic list of example destinations, so replace it with the folders of your own collection, each with a short description of what belongs there. A worked version filled in for a PARA vault sits at `examples/placement-francois.md`, which you can copy into Step 2 and edit. When you change the placement folders, update the folder list in the Connection Scanning section so the connection scan greps the same folders you actually use.

To change the note shape, edit the format block in Step 4, where the frontmatter fields and the four sections are defined. The `type: study` and `area:` fields are conventions rather than anything the skill needs, so adjust or remove them to match how your notes app expects frontmatter. To change how Quarto input is converted, edit the Quarto Conversion Notes section, where each construct and its replacement are listed. To change the source categories the skill infers, edit the `source` field options in Step 3.

## Repository layout

```
study-note/
├── SKILL.md     the full process: identify, place, extract metadata, format, write, connect
├── README.md    this file
├── LICENSE      MIT licence
└── examples/
    └── placement-francois.md   a worked placement list for a PARA vault
```

## Licence

This package is released under the MIT licence, with the full text in the `LICENSE` file.

## Credit

The skill was developed by Francois du Plessis. Contributions and forks are welcome.
