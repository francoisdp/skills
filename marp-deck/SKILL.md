---
name: marp-deck
description: Convert a vault note into a portable Marp presentation (markdown + PDF). USE WHEN user says "make a deck from", "convert this note to a presentation", "create a Marp deck", or provides a note path and asks for slides.
---

# Marp Deck Skill

Convert any vault markdown note into a standalone Marp presentation. The source note is preserved as the knowledge source; the deck is a self-contained distribution artifact (images copied, wiki-links flattened, PDF exported) that can be emailed or opened outside Obsidian.

## Quick Commands

| Say | Does |
|-----|------|
| "Make a deck from `<path>`" | Full pipeline with default template |
| "Make a deck from `<path>` using `<template>`" | Uses named template from `Marp_template/` |
| "Convert `<path>` to a presentation" | Same as above, asks for template if ambiguous |
| "Rebuild the deck for `<path>`" | Regenerates deck from source, overwrites existing output |

## Inputs

- **Required:** path to a `.md` file in the vault
- **Optional:** template name (matches a file in `Marp_template/` without `.md` extension)
- **Optional:** summarization level — `aggressive` | `light` | `verbatim`

## Process

### Step 1 — Read the source note

Read the file at the provided path. Extract:
- Title (from H1 or filename)
- Frontmatter (if any — check for a `marp_template:` hint, but CLI/argument override wins)
- Body content
- List of image references (`![...](path)` and `![[image.png]]`)
- List of wiki-links to notes (`[[Note]]` and `[[Note|alias]]`)
- External links (`[text](url)`)

### Step 2 — Resolve the template

Resolution order:
1. If user passed `--template <name>` or "using `<name>`", use `Marp_template/<name>.md`
2. Otherwise use `Marp_template/default.md`

If the template file doesn't exist, list available templates and ask the user to pick one. Never silently fall back.

Read the template file — it contains Marp frontmatter, any `<style>` block, and structural scaffolding with `[TITLE]`, `[SECTION]`, `[POINT]` placeholders.

### Step 3 — Ask about summarization

Unless already specified by the user, prompt once:

> **How aggressively should I condense?**
> 1. **Aggressive** (default) — main points only, ~10–15 slides
> 2. **Light** — preserve all sections, tighten prose for slide readability
> 3. **Verbatim** — split the note as-is, one slide per major heading

Wait for the answer. Do not re-ask later.

### Step 4 — Create the deck folder

Folder layout:

```
<source-dir>/<source-basename>-deck/
├── deck.md
├── deck.pdf            (generated in Step 9)
└── images/             (copied attachments)
```

Where `<source-basename>` is the source filename without `.md`. If the folder already exists, confirm with the user before overwriting.

### Step 5 — Copy images

For every image reference in the source note:

1. Resolve the image path (check the note's folder, vault attachment folder, and common locations like `Excalidraw/` or `attachments/`)
2. Copy the file to `<deck-folder>/images/<original-name>`
3. In the deck content, rewrite the reference to `![alt](images/<original-name>)` (standard markdown syntax — Marp doesn't handle `![[...]]` embeds)
4. If an image can't be located, note it in the report and leave a TODO comment in the deck

### Step 6 — Flatten wiki-links to footnotes

For every `[[Note]]` or `[[Note|alias]]` in the body:

1. Replace the wiki-link with the display text plus a numbered footnote marker: `Text[^1]`
2. Collect each link into a footnote registry with:
   - The target note name
   - A one-line description (infer from the target note's H1 or first paragraph if readable; if the target note is not found, use the wiki-link target text as-is)
3. On the final slide, render a **"References"** section listing footnotes in order:
   ```
   [^1]: Target Note — short description
   [^2]: Another Note — short description
   ```

External markdown links `[text](url)` stay as plain markdown links — do not move them to footnotes.

### Step 7 — Generate slide content

Apply the chosen summarization level to the body:

- **Aggressive:** extract the 5–8 key ideas, build a narrative arc (Problem → Approach → Evidence → Implication → Next), target 10–15 slides. Use short bullet phrases, not paragraphs.
- **Light:** keep all H2-level sections. Per section, tighten prose to bullet points. One slide per H2; split long sections across 2 slides with a continuation marker.
- **Verbatim:** one slide per H1/H2 heading, preserve prose as-is. Accept that some slides may be dense.

Slide separator in Marp: `---` on its own line.

Replace template placeholders:
- `[TITLE]` → note title
- `[SUBTITLE]` → one-line summary of the note
- `[DATE]` → today's date
- `[AUTHOR]` → leave empty or use the configured git user name if the template expects it
- Structural placeholders (`[SECTION]`, `[POINT]`) are replaced by the generated slide content

### Step 8 — Write `deck.md`

Assemble:
1. Template frontmatter (preserve `marp: true`, `theme:`, `paginate:`, `size:`, any `<style>` block)
2. Title slide
3. Generated content slides (separated by `---`)
4. References slide (footnotes)

Write to `<deck-folder>/deck.md`.

### Step 9 — Export to PDF

Run Marp CLI via `npx` (no global install needed):

```bash
cd <deck-folder> && npx -y @marp-team/marp-cli@latest deck.md --pdf --allow-local-files
```

If the export fails (e.g. no Chrome/Chromium found), report the error with remediation guidance — don't silently continue. Common fix: set `CHROME_PATH` env var or install Chrome.

### Step 10 — Report

Present a summary to the user:

```
Deck created: <deck-folder>/deck.md
PDF exported: <deck-folder>/deck.pdf
Template: <template-name>
Summarization: <level>
Slides: <count>
Images copied: <count>
Wiki-links footnoted: <count>
Source note: unchanged at <source-path>

[Warnings, if any — missing images, failed exports, etc.]
```

Ask: "Open the PDF, or want me to adjust anything?"

## Templates

Templates live in a `Marp_template/` folder at the vault root, where each is a self-contained `.md` file with Marp frontmatter, optional inline `<style>` and placeholder scaffolding. This skill package bundles five starter templates in its own `templates/` folder, so on first use copy them into `Marp_template/` at the vault root, or point Step 2 at the package `templates/` folder if you prefer to keep them with the skill.

Available out of the box:

| Template | Style | Use case |
|---|---|---|
| `default` | Clean, light, serif body | General-purpose decks |
| `dark` | Dark background, high contrast | Screen presentations, demos |
| `academic` | Serif, dense, paginated | Technical papers, research talks |
| `business` | Bold accent color, light | Client pitches, proposals |
| `aerospace` | Engineering-style, mono accents | Aerospace / technical briefings |

To add a new template: drop a `.md` file with Marp frontmatter into `Marp_template/`. The skill will pick it up automatically on next run.

## Implementation notes

- **Wiki-links in images:** `![[image.png]]` is Obsidian-specific; Marp needs `![alt](path)`. Always convert.
- **Excalidraw embeds:** `![[drawing.excalidraw]]` — these export to PNG on save. If a `.svg` or `.png` sibling exists, use it; otherwise flag as unsupported.
- **Dataview blocks:** Strip them with a note — `<!-- dataview block removed: not renderable in Marp -->`. These don't evaluate outside Obsidian.
- **Callouts (`> [!note]`):** Convert to standard blockquotes; the callout type becomes bold prefix (`**Note:** ...`).
- **Tasks (`- [ ]`):** Preserve — Marp renders them as checkboxes.
- **Source note stays untouched.** Never write back to the source note.

## When the user's request is ambiguous

If the path is missing, ask for it. If the template isn't specified, use `default` silently — don't re-ask (user preference: don't re-ask after approval). If summarization level isn't specified, ask once per run.
