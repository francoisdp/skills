# branded-document-toolkit

A skill that turns input of three kinds into a branded PDF through one shared pipeline. It takes raw notes you want written up, a finished document you only want branded, or a raw transcript you want reorganised, then it produces a polished Quarto document carrying your brand, compiled to PDF and opened for you. The brand lives in a small config and a swappable template, so you publish the method and the adopter supplies their own colour, name, website and logo.

## What it does

The skill has three input modes that share one brand pipeline. In WRITE mode you give it raw notes, bullet points or an outline and it structures and writes the document from scratch, applying a writing standard to the prose. In WRAP mode you give it an already-structured `.md`, `.qmd` or `.tex` document and it applies the brand without rewriting, wrapping selected content in callout boxes and stripping anything the template already supplies. In RESTRUCTURE mode you give it a raw transcript and it reorganises the spoken text into sections and boxes without inventing content.

All three modes converge on the same pipeline. The skill asks once for the document title, infers the cover details from the content and the folder, computes the path to your logo files, assembles the document from `template/branded-proposal-template.qmd`, substitutes every placeholder and the body, writes a prefixed `.qmd`, runs `quarto render`, opens the PDF and reports both paths. The brand template loads `template/brand.sty`, which carries the accent colour, the five callout boxes, the section divider, the cover and closing pages and the page header and footer.

## Installation

The skill is a folder containing `SKILL.md`, a `template/` folder and an `examples/` folder. The folder must be named `branded-document-toolkit` so it matches the skill name in the frontmatter.

For **Claude Code**, copy the folder into `~/.claude/skills/branded-document-toolkit/` for a user-level install, or `.claude/skills/branded-document-toolkit/` inside a project. Claude Code discovers the skill from its frontmatter.

For **Claude Desktop and claude.ai**, add the skill through the Skills or Capabilities setting in the application.

For **Copilot CLI**, the skill is auto-discovered from installed plugins through the `skill` tool.

For **Gemini CLI**, the skill activates through `activate_skill`, with the frontmatter loaded at session start.

For **any other tool**, the steps are plain Markdown you can paste into a system prompt or an instruction file such as `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`.

The compile step needs three things on the machine. The first is **Quarto**, the document system that drives the render. The second is a **LaTeX distribution** that Quarto can use, such as TeX Live or TinyTeX. TinyTeX installs through `quarto install tinytex` and is the lighter option. The third is that **`quarto render` must work** on a `.qmd` file before you run the skill. The template compiles with `xelatex`, so the distribution must provide it, which both TeX Live and TinyTeX do. Confirm the toolchain with `quarto render` on any small `.qmd` file before first use, so a failure during the skill is a content problem and not a missing dependency.

## Usage

Trigger the skill with input and a phrase it recognises. Say "Turn these notes into a branded PDF" with raw material for WRITE mode, "Brand this document" with a path to a finished `.md`, `.qmd` or `.tex` file for WRAP mode, or "Polish this transcript into a branded PDF" with a raw transcript for RESTRUCTURE mode. The skill picks the mode from the input, asks once for the document title, then runs the full pipeline. It returns the path to the generated `.qmd`, the path to the compiled PDF and a note of any cover details it inferred so you can correct them. It asks before overwriting an existing output file.

## Rationale

The brand and the method are separated so the valuable part can be published without giving away the brand assets. The method is the three modes, the callout boxes, the cover and closing pages and the compile pipeline. The brand is one accent colour, an organisation name, a website and two logo files. By holding the brand in a config block in `template/brand.sty` and an `assets/` folder the adopter fills, the same skill serves any organisation, while the author's own logo files never need to ship in the package.

Three modes share one pipeline because the only real difference between them is how the document body is produced. Once you have a structured body, branding it, compiling it and opening it are identical work regardless of whether the body was written from notes, lifted from a finished document or reorganised from a transcript. Folding the three into one skill removes duplicated pipeline steps that previously drifted apart across three separate skills.

The callout boxes exist to give a document visual structure that plain headings cannot. A `propbox` marks a recommendation, an `insightbox` carries a principle in italics with a coloured rule, a `riskbox` flags a caution, a `conceptbox` holds a definition and a `teambox` introduces people. Each box reads as a distinct kind of content at a glance, which makes a long proposal easier to scan. The boxes use raw-LaTeX `tcolorbox` environments rather than Quarto callouts because the template does not load the Quarto callout package, so the boxes must be fenced in `{=latex}` blocks to pass through Pandoc untouched.

The titlesec fix exists because Quarto and Pandoc wrap `\paragraph` with `\mbox{}`. The `titlesec` package then fails with `Argument of \paragraph has an extra }`. That error stops the build. Resetting `\paragraph` and `\subparagraph` before loading `titlesec` avoids the clash. The fix lives in `brand.sty` and must not be removed, since without it no document compiles.

## Make it your brand

This is the part you do once. Three small edits turn the toolkit from a neutral template into your organisation's brand.

**1. Set your accent colour, name and website in `template/brand.sty`.**

Open `template/brand.sty` and edit only the CONFIG block at the very top. Nothing below that block needs touching. Set the accent colour as an HTML hex value, six digits with no leading hash:

```latex
\definecolor{brandAccent}{HTML}{1C6EA4}
```

If you prefer an RGB triple, comment out the HTML line and use the RGB form shown directly beneath it. Then set your organisation identity:

```latex
\newcommand{\brandOrgName}{Your Organisation}
\newcommand{\brandStrapline}{Your strapline here}
\newcommand{\brandWebsite}{www.example.com}
```

The accent colour drives the headings, the bold text, the rules, the box accents and the links, so changing that one value reskins the whole document.

**2. Drop your logo into `template/assets/`.**

Place two image files in `template/assets/`. Name them `logo.png` for a logo that reads on a light page header and `logo-inverted.png` for a logo that reads on the dark cover and closing pages. If you would rather keep your own filenames, set them in the CONFIG block:

```latex
\newcommand{\brandLogo}{your-logo.png}
\newcommand{\brandLogoInverted}{your-logo-inverted.png}
```

The names in the macros and the names of the files in `assets/` must match. Until both files exist the template still compiles, with the cover and closing pages falling back to a text wordmark built from your organisation name and the header omitting the logo. Add the files and the images appear on the next render.

**3. Set your filename prefix and writing standard.**

Pick a short prefix for generated files, for example `AB-` for a firm called Acme Brand. The default is `Doc-`. The prefix is named in `SKILL.md` under Configuration. For WRITE mode, the skill applies a writing standard to the prose. The toolkit author uses the `anti-ai-writing` skill. Swap in your own writing standard if you prefer, then adjust the WRITE-mode note in `SKILL.md` to point at it.

A complete worked example of every value above, filled in for a real brand, is in `examples/config-grey-matter.md`. Read it alongside the empty CONFIG block to see how each field maps.

## Extension guide

The skill is plain Markdown, one Quarto template and one LaTeX style file, so customising it means editing those files.

To change the look of the document beyond the accent colour, edit the mechanics below the CONFIG block in `template/brand.sty`. The section heading style, the list bullets, the box geometry and the cover and closing layouts all live there. To add a new callout box, copy one of the five `\newtcolorbox` definitions, rename it and adjust its colours, then use it in a `{=latex}` fence in your body. To change the cover or closing layout, edit the `\brandcover` and `\brandclose` commands.

To change the document body rules, edit `SKILL.md`. The mode sections control how each input kind becomes a body, while the shared pipeline controls placeholder inference, the filename prefix and the compile and open steps. To change which document types the cover label can take, edit the `__COVER_LABEL__` row in the shared pipeline.

## Repository layout

```
branded-document-toolkit/
├── SKILL.md                          the three modes and the shared brand pipeline
├── README.md                         this file
├── LICENSE                           MIT licence
├── template/
│   ├── branded-proposal-template.qmd the Quarto template with placeholder tokens
│   ├── brand.sty                     the LaTeX style with the CONFIG block to edit
│   └── assets/
│       └── README.md                 where to drop logo.png and logo-inverted.png
└── examples/
    └── config-grey-matter.md         a real brand config, filled in, no logo binaries
```

## Licence

This package is released under the MIT licence, with the full text in the `LICENSE` file.

## Credit

The skill was developed by Francois du Plessis. Contributions and forks are welcome.
