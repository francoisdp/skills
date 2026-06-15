# folder-docs

[![Tested with NVIDIA SkillSpector](https://img.shields.io/badge/Tested%20with-NVIDIA%20SkillSpector-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/SkillSpector)

> This skill was scanned with NVIDIA SkillSpector and returned a SAFE recommendation. It ships one small Python script, `scripts/folder_docs.py`, which only reads the modification timestamps of PDF files and writes a single Markdown index file. It makes no network calls and runs no other process. The scanner raised one MEDIUM note, that the skill performs file reads and writes without a declared permissions field. That note is an accurate description of the skill's purpose rather than a vulnerability, so it was reviewed and accepted. The full scan is bundled as `skillspector-report.md`. If you are in any doubt, read the source and re-scan before you install.

A Claude skill that builds an index of every PDF in a folder, sorted so the most recently generated file sits at the top. It writes the index as an Obsidian note named `PDF list.md` at the root of the folder you give it, with each entry a clickable wiki link. You open the note and the work you produced most recently is the first line.

## What it does

Point the skill at a folder. It finds every PDF in that folder and all of its subfolders, sorts them by modification time with the newest first and writes a note called `PDF list.md` at the root of the folder. Each line is a wiki link to the PDF followed by the date and time the file was last written. The note is overwritten on each run, so it always shows the current state.

The skill was built to answer a recurring question. When you produce a series of documents over weeks, for example study reports or proposals compiled to PDF, you lose track of which one you generated last. A list ordered by modification time, newest first, answers that at a glance and lets you click straight through to the file.

## Installation

The skill is one folder containing `SKILL.md` and a `scripts/` directory. Install it by placing that folder where your tool looks for skills, keeping the folder name `folder-docs` so it matches the `name` in the frontmatter.

**Claude Code.** Copy the `folder-docs/` folder into `~/.claude/skills/folder-docs/` for a user-level install that is available in every project, or into `.claude/skills/folder-docs/` inside a project for a project-level install. The skill then loads when you type `/folder-docs` or describe the task.

**Claude Desktop and claude.ai.** Add the skill through the Skills or Capabilities setting and upload the folder. The script runs in environments that provide a Python runtime.

**Copilot CLI.** The skill is auto-discovered from installed plugins once the folder is placed in the plugin skills location.

**Gemini CLI.** The skill is activated through `activate_skill` once Gemini has loaded its metadata at session start.

**Any other tool.** The logic lives in `scripts/folder_docs.py`. You can run that script directly with `python3 scripts/folder_docs.py "<folder path>"`, or paste the process from `SKILL.md` into a system prompt or an instruction file such as `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`.

The script needs Python 3 and uses only the standard library, so there is nothing to install beyond Python itself.

## Usage

Trigger the skill with a folder path. Any of these work:

- `/folder-docs <folder>`
- `/folder docs <folder>`
- "Index the PDFs in `<folder>`"
- "List the latest documents in `<folder>`"

The folder can be a path relative to your vault root or an absolute path. Quote it if it contains spaces. The skill runs the script, which writes `PDF list.md` at the root of the folder and reports the path it wrote and the number of PDFs it indexed. Open the note in Obsidian and the newest document is at the top.

A generated line looks like this:

```markdown
- [[Resources/Research/Study on X.pdf|Study on X.pdf]] — 2026-06-14 14:32
```

The link target is the path relative to the Obsidian vault root, so the link resolves even when two PDFs in different subfolders share a name. The visible text is the file name. The timestamp shows when the file was last written.

## Rationale

**Why modification time, newest first.** The question the skill answers is "which document did I produce most recently". For a file compiled from source, the modification time is effectively the time it was generated, so sorting by modification time with the newest first puts the most recent work where you look first. The date and time are shown on every line so the ordering is visible rather than implied.

**Why a script rather than prose instructions.** Listing files, sorting them by timestamp and building correct link paths is deterministic work. A script does it the same way every time, so the result does not drift with the model's mood or the length of the folder. The skill is a thin wrapper that hands the folder to the script and reports the outcome.

**Why vault-relative link paths.** An Obsidian wiki link resolves from the vault root. If two PDFs in different subfolders share a file name, a bare name is ambiguous and may open the wrong file. The script writes the full vault-relative path as the link target and shows the file name as the visible text, so the link is unambiguous and still reads cleanly. It finds the vault root by walking up the directory tree to the nearest `.obsidian` folder. When no vault is found, it falls back to the bare file name.

**Why recursive.** Documents are often kept in subfolders by topic or date. Indexing only the top level would miss most of them, so the skill walks the whole tree under the folder you give it and lists everything in one note. It skips system folders such as `.git`, `.obsidian` and `.trash`.

## Extension guide

The behaviour lives in `scripts/folder_docs.py`. The constants at the top of that file are the parts you are most likely to change.

- **Output file name.** Change `OUTPUT_NAME` to rename the index note from `PDF list.md` to anything you prefer.
- **File type.** The script matches files ending in `.pdf`. Change the suffix test in `collect_pdfs` to index other types, for example `.docx` or `.md`, or extend it to match several types.
- **Skipped folders.** Add or remove entries in `SKIP_DIRS` to control which subfolders the walk ignores.
- **Sort order.** The script sorts by modification time, newest first. Change the `sort` call in `main` to sort by name, or by creation time where your platform exposes it, or to put the oldest first.
- **Line format.** Change `build_note` to alter how each entry reads, for example to drop the timestamp, to show a relative date or to embed the PDF with `![[...]]` rather than link to it.

If you change the output file name in the script, update the `SKILL.md` text so the skill reports the right name. The `SKILL.md` describes the process and triggers, so keep it in step with any change to the script's behaviour.

## Repository layout

```
folder-docs/
├── README.md                 # This file
├── LICENSE                   # MIT
├── SKILL.md                  # The skill definition and process
├── skillspector-report.md    # Bundled security scan
└── scripts/
    └── folder_docs.py        # The script that builds the index
```

## Licence

MIT. See `LICENSE`.

## Credit

Created by Francois du Plessis.
