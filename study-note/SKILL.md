---
name: study-note
description: Process a markdown or text file into a standardised study note format. USE WHEN user wants to create a study note, process a document, or import content from Claude Desktop, NotebookLM, or other sources.
---

# Study Note Skill

Process any markdown, text, or Quarto file into a standardised study note and place it in the correct PARA location.

## Quick Commands

| Say | Does |
|-----|------|
| "Process this into a study note" | Converts content to study note format |
| "Create a study note on [topic]" | Creates a new study note from scratch |
| "Import this file as a study note" | Reads a file and converts it |

## Process

### Step 1: Identify the source

Determine the input — one of:
- **File path** — user provides a path to a `.md`, `.qmd`, or `.txt` file → read it
- **Pasted content** — user pastes text directly
- **Topic only** — user names a topic → create a blank study note

If a file is provided, read it and extract the content body (strip any existing frontmatter).

### Step 2: Determine placement

Ask the user where the note should be saved, offering the folders that fit your own structure. Replace the list below with your own destinations. The example list shows the shape, where each entry is a folder path with a short description of what belongs there:

> **Where does this study belong?**
> 1. `Areas/<topic-a>/`: first area of responsibility
> 2. `Areas/<topic-b>/`: second area of responsibility
> 3. `Resources/<reference-a>/`: first reference category
> 4. `Resources/<reference-b>/`: second reference category
> 5. `Projects/[name]/`: for a specific project
> 6. Other: specify

A worked version of this list, filled in for a PARA vault, is in `examples/placement-francois.md`, which you can copy and edit into the list above.

### Step 3: Extract or ask for metadata

From the content, try to extract:
- **title** — from the first heading or filename
- **date** — today's date if not specified
- **source** — infer from content or ask: `claude | notebooklm | manual | web | paper`
- **status** — default to `draft`
- **tags** — suggest based on content, ask user to confirm/edit

**Ask the user for any fields that could not be determined.** Present what you've inferred and let them confirm or correct:

```
I've extracted the following:
- Title: [extracted]
- Source: [inferred]
- Tags: [suggested]
- Placement: [determined]

Anything to change?
```

### Step 4: Format the study note

Convert the content into this standardised format:

```markdown
---
type: study
title: "[title]"
date: [YYYY-MM-DD]
source: [claude | notebooklm | manual | web | paper]
status: [draft | review | complete]
area: [PARA area name]
tags:
  - [tag1]
  - [tag2]
---

# [Title]

## Summary
[If the source content has no summary, generate 3-5 bullet points from the content]

## Detail
[Main content — preserve the original structure and formatting]
[Convert Quarto-specific syntax to standard markdown where needed:]
[- ::: callouts → > [!note] Obsidian callouts]
[- @references → inline links]
[- {{< >}} shortcodes → remove or convert]

## Sources
[Extract any URLs, references, or citations from the content]
[If none found, add placeholder: - [Add sources]]

## Connections
[Scan the vault for related notes and suggest wiki-links]
[Look in the target area folder and related areas]
[If no connections found: - [No connections identified yet]]
```

### Step 5: Write and confirm

1. Write the file to the determined location
2. Show the user:
   - File path created
   - Frontmatter summary
   - Any connections found in the vault
3. Ask: "Want me to adjust anything?"

## Quarto Conversion Notes

When processing `.qmd` files:
- Rename to `.md`
- Convert Quarto callouts (`::: {.callout-note}`) to Obsidian callouts (`> [!note]`)
- Remove code execution blocks (`{python}` → `python`) unless output is valuable
- Convert Quarto cross-references to standard markdown links
- Preserve all other markdown formatting

## Connection Scanning

After placing the note, scan for connections across your note folders (replace the folder list with your own):
```bash
# Find related notes by tags
grep -rl "[tag]" Areas/ Resources/ Projects/ --include="*.md" | head -10

# Find notes with similar titles/topics
grep -rl "[key topic word]" Areas/ Resources/ Projects/ --include="*.md" | head -10
```

Suggest wiki-links to add in the Connections section.
