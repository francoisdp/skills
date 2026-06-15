#!/usr/bin/env python3
"""Generate a PDF index note for a folder.

Scans the given folder and every subfolder for PDF files, sorts them by
modification time with the most recently generated file at the top, and writes
an Obsidian note named "PDF list.md" at the root of that folder. Each entry is a
wiki link to the PDF followed by its modification date and time.

Usage:
    folder_docs.py "<folder path>"

Wiki links are resolved relative to the Obsidian vault root, found by walking up
the directory tree until a ".obsidian" folder is located. When no vault root is
found the links fall back to the bare file name.
"""

import os
import sys
from datetime import datetime

OUTPUT_NAME = "PDF list.md"

# Directories that never hold real study material and must be skipped.
SKIP_DIRS = {".git", ".obsidian", ".trash", ".smart-env", "node_modules"}


def find_vault_root(start):
    """Walk upward from start until a directory containing .obsidian is found."""
    current = os.path.abspath(start)
    while True:
        if os.path.isdir(os.path.join(current, ".obsidian")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return None
        current = parent


def collect_pdfs(folder):
    """Return a list of (absolute_path, mtime) for every PDF under folder."""
    found = []
    for root, dirs, files in os.walk(folder):
        # Prune skip directories in place so os.walk does not descend into them.
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name.lower().endswith(".pdf"):
                path = os.path.join(root, name)
                try:
                    mtime = os.path.getmtime(path)
                except OSError:
                    continue
                found.append((path, mtime))
    return found


def wiki_target(path, vault_root):
    """Vault-relative path with forward slashes, or bare name when no vault."""
    if vault_root:
        rel = os.path.relpath(path, vault_root)
        return rel.replace(os.sep, "/")
    return os.path.basename(path)


def build_note(folder, pdfs, vault_root):
    lines = ["# PDF list", "", "Most recently generated at the top.", ""]
    if not pdfs:
        lines.append("No PDF files were found in this folder.")
        lines.append("")
        return "\n".join(lines)
    for path, mtime in pdfs:
        target = wiki_target(path, vault_root)
        display = os.path.basename(path)
        stamp = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
        lines.append(f"- [[{target}|{display}]] — {stamp}")
    lines.append("")
    return "\n".join(lines)


def main(argv):
    if len(argv) != 2:
        print('Usage: folder_docs.py "<folder path>"', file=sys.stderr)
        return 2

    folder = os.path.abspath(os.path.expanduser(argv[1]))
    if not os.path.isdir(folder):
        print(f"Not a directory: {folder}", file=sys.stderr)
        return 1

    vault_root = find_vault_root(folder)
    pdfs = collect_pdfs(folder)
    # Newest modification time first.
    pdfs.sort(key=lambda item: item[1], reverse=True)

    note = build_note(folder, pdfs, vault_root)
    output_path = os.path.join(folder, OUTPUT_NAME)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(note)

    print(f"Wrote {output_path}")
    print(f"Indexed {len(pdfs)} PDF file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
