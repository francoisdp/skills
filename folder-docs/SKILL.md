---
name: folder-docs
description: Generate an index note of every PDF in a folder, newest first, as Obsidian wiki links. USE WHEN the user types "/folder docs <folder>", "/folder-docs <folder>", or asks to list, index, or catalogue the PDFs in a folder so they can see which document was generated most recently.
---

# Folder Docs Skill

Build a single index note that lists every PDF in a folder and all of its
subfolders, sorted by modification time with the most recently generated file at
the top. The note is written to `PDF list.md` at the root of the folder, so the
user can open it and click through to any document, with the latest work always
at the top of the list.

## Quick Commands

| Say | Does |
|-----|------|
| `/folder docs <folder>` | Builds `PDF list.md` for that folder |
| `/folder-docs <folder>` | Same as above |
| "Index the PDFs in <folder>" | Same as above |
| "List the latest documents in <folder>" | Same as above |

## Process

### Step 1: Identify the folder

Take the folder path from the user's message. It may be:
- A path relative to the vault root, for example `Resources/Research`
- An absolute path
- A folder the user refers to in context

If no folder is given, ask which folder to index. Do not guess.

### Step 2: Run the script

Run the bundled script with the folder path as the single argument. Quote the
path because folders often contain spaces. The script lives in the skill's own
folder, so call it through the skill base directory that the harness reports when
this skill loads.

```bash
python3 "<skill base directory>/scripts/folder_docs.py" "<folder path>"
```

The script does all of the work deterministically:
- Finds every `.pdf` file in the folder and every subfolder, recursively.
- Sorts them by modification time, most recent first.
- Locates the Obsidian vault root by walking up to the nearest `.obsidian`
  folder, so the wiki links resolve correctly from anywhere in the vault.
- Writes `PDF list.md` at the root of the folder, overwriting any previous
  version so the index always reflects the current state.
- Skips system folders such as `.git`, `.obsidian`, and `.trash`.

Each line in the note has this form:

```markdown
- [[Resources/Research/Study on X.pdf|Study on X.pdf]] — 2026-06-14 14:32
```

The link target is the vault-relative path, so it always resolves. The visible
text is the file name, and the date and time show when the file was last
generated.

### Step 3: Report

Tell the user the path of the note that was written and how many PDFs were
indexed. The script prints both. Confirm that the newest document is at the top.

## Notes

- "Most recently generated" means the file modification time. For a compiled
  document, that is effectively the time it was produced.
- The note is overwritten on every run, so the user can re-run the skill at any
  time to refresh the list.
- If the folder sits outside any Obsidian vault, the links fall back to the bare
  file name rather than a vault-relative path.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Not quoting the folder path | Folder paths contain spaces; always wrap the argument in quotes. |
| Expecting only the top-level folder | The skill is recursive by design; it includes every subfolder. |
| Re-implementing the listing by hand | Always run the script; it guarantees correct sorting and link paths. |
