---
name: branded-document-toolkit
description: Use when the user wants to turn raw notes or an outline into a branded PDF, when they hand over an already-structured .md/.qmd/.tex document and want your brand applied without rewriting it, or when they want a raw transcript reorganised and polished into a branded PDF. Also use on "/branded-document-toolkit". Input can be a file path, pasted text, or both. Output is a prefixed .qmd compiled to PDF and opened.
---

# branded-document-toolkit

One skill, three input modes, one shared pipeline. Each mode takes some form of input, turns it into a structured document body, then feeds that body into a common pipeline that applies your brand template, compiles the document to PDF and opens it.

The brand is separated from the method. The accent colour, organisation name, website and logo filenames live in `template/brand.sty`. The filename prefix and the writing standard are skill configuration. You publish the method and an adopter supplies their own brand. See the Configuration section at the end.

## Pick the mode first

Read the input and decide which of the three modes applies. The mode only changes how you produce the body. Everything after the body is shared.

| Mode | Input | What you do to the content |
|------|-------|----------------------------|
| WRITE | Raw notes, bullet points, an outline, a briefing, mixed text | You structure and write the document from scratch. Bullets become prose. An outline becomes sections. Apply your writing standard to the prose. |
| WRAP | An already-structured `.md`, `.qmd` or `.tex` document | You brand it without rewriting. Keep headings, ordering and prose as they are. You only wrap content in callout boxes and strip anything the template supplies. |
| RESTRUCTURE | A raw transcript or spoken-thoughts file, often named `*-raw.md` | You reorganise the text into sections and boxes without inventing content. Fix spoken-to-written grammar, never add claims, numbers or commitments not in the source. |

If the input is genuinely between modes, say which you picked and why in one sentence before continuing.

---

## Mode WRITE: raw material to a written document

You are writing a document, not just wrapping content.

> Apply a writing standard to all prose in this mode. The toolkit author uses the `anti-ai-writing` skill in the same repository as that standard. Invoke it through the Skill tool before you write a single sentence so the full rule set governs the prose, not a few remembered rules. This is the author's standard. An adopter may swap it for their own writing standard. See Configuration.

### Analyse the input

Before writing, identify:
- The core argument or purpose of the document.
- The natural sections. Three to six top-level sections is typical.
- Content that belongs in callout boxes. See the box guide below.
- Any data, figures or tables present in the raw material.

### Write the body

Write clean, flowing prose. Follow these rules:

**Structure**
- Use `#` for top-level sections, `##` for subsections, `###` for sub-subsections.
- Begin with an executive summary or introduction.
- End with a conclusion, next steps or call to action.
- Use `\clearpage` before major sections to control pagination.
- For longer documents with five or more sections, use `\gmsectiondivider{Part N}{Part Title}` for major part breaks.

**Prose**
- The writing standard governs all prose here. If you have not invoked it, invoke it now.
- Write in your brand voice: direct, warm, technically precise, why-before-what. This describes a register an adopter sets for their own organisation.
- Expand bullet points into sentences. Do not leave raw bullets in the body unless they are genuinely list-like.
- Earn every claim. Do not inflate significance.

**Tables**
- Use Markdown tables for comparisons and structured data.
- Wrap a table in a raw-LaTeX block if it needs `booktabs` formatting.

Then apply callout boxes (see the shared box guide) and continue to the shared pipeline.

---

## Mode WRAP: brand an existing document

Apply the brand to an existing document without rewriting it.

### Extract the body by file type

**`.md` input.** Read the file. Strip any YAML frontmatter block. The remainder is the body. Scan for content that maps to a callout box and wrap it. Do not restructure or rewrite. Group adjacent related items, apply boxes, leave the rest as it is.

**`.qmd` input.** Read the file. Strip the existing YAML frontmatter. Keep the body as it is. Do not alter headings, ordering or prose. If the body uses Quarto callout syntax (`::: {.callout-*}`), convert each to its nearest box: `.callout-note` and `.callout-tip` become `conceptbox`, `.callout-important`, `.callout-warning` and `.callout-caution` become `riskbox`.

**`.tex` input.** Read the file. Extract the content between `\begin{document}` and `\end{document}`. Remove any `\maketitle`, `\tableofcontents` and `abstract` blocks, since the template supplies all of these. Keep all other LaTeX markup. If there is no `\begin{document}`, take the whole file as the body and note this to the user.

Then continue to the shared pipeline.

---

## Mode RESTRUCTURE: transcript to a polished document

Reorganise a raw transcript into sections and boxes without inventing content.

Read the raw file. The content is typically a single block of spoken text. Restructure it into logical sections without adding or removing information.

**Heading discipline**
- Open with a brief `# Introduction` paragraph that frames what follows.
- Break the body into top-level `#` sections by major theme.
- Use `##` and `###` only when the source clearly has internal structure to surface.
- For natural narrative shifts, insert a part divider with `\gmsectiondivider{Part I}{Part Title}`.

**Voice and content rules**
- Restructure, do not rewrite the substance. Group related thoughts, fix grammar from spoken to written, never invent claims, numbers or commitments not in the source.
- Lead with the point. Each section opens with the core claim, then expands.
- Vary sentence rhythm. Do not open a sentence with "And", "But" or "So".
- Bold sparingly. The template renders `\textbf{}` in the accent colour, so only bold what you want to highlight.
- Numbered lists for principles or sequential steps. Bulleted lists for parallel items.
- If the transcript references images and an `images/` subfolder exists next to the output, include them with a caption and `{#fig-name width=100%}`. Otherwise skip.

Then apply callout boxes (see the shared box guide) and continue to the shared pipeline.

---

## Callout box selection guide (shared by all modes)

Wrap content in a raw-LaTeX fence so Pandoc passes it straight through:

````
```{=latex}
\begin{propbox}
Content here.
\end{propbox}
```
````

| Box | Use for |
|-----|---------|
| `propbox` | Proposed programs, engagement models, key recommendations, executive summaries |
| `conceptbox` | Explanations, definitions, capability descriptions, process descriptions, reference lists |
| `insightbox` | Principles, observations, brand-voice statements, key convictions. Rendered italic with a left accent rule |
| `riskbox` | Risk notes, cautions, constraints, warnings |
| `teambox` | Team profiles, people descriptions |

Rules for boxes:
- Use `\textbf{Label}` for bold labels inside boxes. Bold renders in the accent colour.
- Separate items inside a box with `\\[0.4em]`, not blank lines, which break tcolorbox.
- Never nest boxes.
- Do not put section headings inside boxes.
- No em-dash inside a box. A literal `---` or `—` renders wrong in the PDF. Use a comma, a colon, parentheses or rewrite the clause.
- Aim for at least one box per major section in documents over three pages. Fewer is fine for shorter documents.

---

# Shared pipeline

All three modes feed into this pipeline. The body is ready. Now brand it, compile it and open it.

## Step A: ask for the document title (one round)

Ask once, in plain text. Only ask what you cannot infer reliably:

> What is the document title? Everything else (document type, recipient, date, footer) I will infer from the content and folder.

Use the answer as both `__COVER_TITLE__` and the YAML `title`.

## Step B: infer the cover placeholders

Infer the rest without further prompting:

| Placeholder | Source |
|-------------|--------|
| `__COVER_LABEL__` | Document type inferred from content. Default `Report`. Options: `Proposal`, `Concept Note`, `Brief`, `Study`, `Specification`, `Analysis`. Rendered uppercase on the cover. |
| `__COVER_RECIPIENT__` | `A {Label} for {ClientName}`, where `ClientName` is the nearest meaningful parent folder or is inferred from the content. Skip generic folders such as `Resources`, `Areas`, `Projects`. |
| `__COVER_DATE__` | Current month and year, for example `June 2026`. |
| `__COVER_FOOTER_NAME__` | The same `ClientName`. |
| `__SUBTITLE__` | A short tagline, for example `A {Label} for {ClientName}`. |
| `__DATE__` | Same as `__COVER_DATE__`. |
| `__TITLE__` | The user's answer from Step A. |
| `__FOOTER_TAGLINE__` | Under 60 characters. Typically `{ClientName}`. |
| `__CLOSE_LINE_1__` | From the brand config. Typically an engagement question or a closing statement. See the worked example. |
| `__CLOSE_LINE_2__` | From the brand config. Typically the website. See the worked example. |

The two close lines and the website come from the brand config. See `examples/config-grey-matter.md` for a filled-in set of values. If any inference is genuinely ambiguous, surface your best guess in one sentence and confirm before writing.

## Step C: derive the output path

Derive the output filename from the title. Slugify the title, prepend the filename prefix (default `Doc-`) and use the `.qmd` extension. Example: title "Pilot Study" becomes `Doc-Pilot-Study.qmd`. The worked example shows an adopter setting a different prefix.

Output folder:
- If a source file was given, write the output in the same folder as the source.
- If only pasted text was given, ask the user for the output folder in Step A.

If `{prefix}{slug}.qmd` already exists in the folder, surface this and ask whether to overwrite before continuing.

## Step D: compute the graphicspath

The graphicspath is the relative path from the output `.qmd` folder to the folder that holds the logo files. Count the folder segments between the output file and that folder, then prepend that many `../` to the asset path. The trailing slash matters.

For the bundled toolkit the assets live in `template/assets/` inside the skill. When you deploy the skill into a vault or repository, point the graphicspath at wherever your logo files actually live. Substitute the result as `__GRAPHICSPATH__`.

A wrong depth produces `Unable to load picture or PDF file`. Verify before compiling.

## Step E: assemble the file

1. Read `template/branded-proposal-template.qmd` from inside the skill.
2. Substitute every `__PLACEHOLDER__` with the values from Steps A, B, C and D.
3. Replace `__BODY__` with the body your mode produced.
4. Sanity-check before writing:
   - No unresolved `__PLACEHOLDER__` markers remain. Grep for `__`.
   - No em-dash (`---` or `—`) anywhere in the body prose.
   - The template loads `brand.sty`, which carries the titlesec fix. Verify your substitutions did not remove the `include-in-header` `file: brand.sty` line.
   - `\graphicspath` has the correct `../` depth.
   - Every tcolorbox is inside a `{=latex}` raw-block fence.

## Step F: write the file

Write the assembled content to `{prefix}{slug}.qmd` in the output folder from Step C.

## Step G: compile

Run from the folder that resolves the graphicspath correctly, usually the repository or vault root:

```bash
quarto render "<relative path to the .qmd>"
```

Stream the output. Common errors and fixes:

| Error | Fix |
|-------|-----|
| `Argument of \paragraph has an extra }` | The titlesec fix was lost. Confirm `brand.sty` loads and that its `\makeatletter` block is intact. |
| `Unable to load picture` or `File '...logo...' not found` | The `\graphicspath` depth is wrong. Recount the folder segments and correct it. |
| `Undefined control sequence \begin{...box}` | A tcolorbox is missing its `{=latex}` raw-block fence. Wrap it. |
| `LaTeX Error: \begin{document} ended by \end{...}` | An unclosed tcolorbox. Check every `\begin` has a matching `\end`. |
| Visible em-dash or a box error mentioning an em-dash | A literal `---` or `—` slipped into a box. Replace it with a comma, a colon or rewritten text. |

Fix and re-render. Do not claim success without exit code 0 and a PDF on disk.

## Step H: open the PDF

```bash
open "<absolute path to the .pdf>"
```

Always run `open`. The user wants to see the PDF.

---

## Verification before finishing

1. `{prefix}{slug}.qmd` exists in the correct folder.
2. `quarto render` exited with code 0.
3. `{prefix}{slug}.pdf` exists.
4. `open` was run on the PDF.
5. Tell the user both output paths and note any inferences you made (cover label, recipient) so they can correct them.

---

## Configuration

What an adopter sets once, then reuses for every document:

- **The brand config in `template/brand.sty`.** Edit the CONFIG block at the top: the accent colour (`brandAccent`, as HTML hex or RGB), the organisation name, the strapline, the website and the two logo filename macros. Nothing below the CONFIG block needs editing to rebrand.
- **The logo files in `template/assets/`.** Drop in `logo.png` and `logo-inverted.png` (or the names you set in `brand.sty`). Until they exist, the cover and closing pages fall back to a text wordmark and the header omits the logo, so the template still compiles.
- **The filename prefix.** Default `Doc-`. Pick a short prefix for your organisation. The worked example shows an adopter setting their own.
- **The writing standard for WRITE mode.** The toolkit author uses the `anti-ai-writing` skill. Swap in your own writing standard if you prefer.

A worked, filled-in example of every brand-config value is in `examples/config-grey-matter.md`.
