---
name: deploy-skill
description: >
  Use when the user wants to package one of their authored Claude skills and publish it to their
  own GitHub skills repository, or types "/deploy-skill <skillname>", "deploy the <name> skill",
  "publish <name> skill", or "push <name> skill to github". This is the engine for turning a
  private authored skill into a shareable, well-documented public skill.
---

# Deploy Skill

## Overview

This skill packages an authored Claude skill as a deployable, publicly shareable skill, then
publishes it to a GitHub repository you configure, with full documentation. It is the engine that
turns a private skill into a clean public folder carrying installation instructions, usage
instructions, the rationale behind the skill and an extension guide. The user invokes it as
`/deploy-skill <skillname>`, where `<skillname>` is the folder name of a skill the user authored.

The README you produce is itself generated output, so it must meet your own writing standard before
it ships. A README that fell below the standard you hold for published work would undercut the
skill it documents, so treat the writing gate in step 8 as a release gate, not a finishing touch.

## Configuration

Set these five values once for your own setup, then the workflow reads them throughout. A worked
example, filled in for one user, sits at `examples/config-francois.md`.

| Setting | What it is | Suggested default |
|---|---|---|
| Skills source | The folders where your authored skills live | `~/.claude/skills/`, then a project's `.claude/skills/` |
| Staging folder | A working folder where the package is built and kept as a local copy | any folder you keep working files in |
| Skills repository | The public GitHub repository that holds your published skills, as `owner/repo` | `<your-github-user>/skills` |
| Author | Your name, for the licence and the credit line | `<your name>` |
| Writing standard | The writing-quality gate applied to the README before publishing | the scan set in step 8 |

The repository uses a folder-per-skill layout at its root, so each published skill sits in its own
`<skillname>/` directory beside the others. The staged folder name and the published folder name
must both equal the skill's frontmatter `name`, because a skill only loads when its folder name
matches that `name`.

## When to use

Use this when the user wants to share one of their own skills with other people. Do not use it for
third-party skills the user only installed, because those carry their own licence and author. If
the source skill carries author metadata for someone else, or a licence file pointing to another
owner, stop and tell the user rather than publishing someone else's work under their name.

## Workflow

1. **Resolve the source.** Look for `<skillname>` in your skills-source folders in order. If it is
   absent from all of them, stop and tell the user. If it exists in more than one, ask which one to
   publish before continuing.

2. **Read the whole skill.** Read `SKILL.md` and every file under `references/` and any other
   supporting files, so the package and the README describe what the skill actually does rather
   than what its name suggests.

3. **Stage the package.** Create a `<skillname>/` folder inside your staging folder and copy the
   source files into it, preserving the `references/` structure. This staged folder is the
   user-visible deliverable.

4. **Bundle external dependencies.** Check whether the skill reads files that live outside its own
   folder, for example templates, scripts, config, prompt files or assets at a fixed path. A skill
   that depends on such files will not run once installed elsewhere, because the adopter will not
   have them. For each external dependency, copy a generic version into the staged package under a
   sensible subfolder such as `templates/`, `scripts/` or `assets/`, leaving out any branded or
   personal variant. Then update the staged `SKILL.md` so it points at the bundled copy, or document
   in the README how the adopter installs the bundled files where the skill expects them. The test
   is whether a clean install carrying nothing but this package would run, so bundle whatever the
   skill needs to reach that.

5. **Genericise personal and branded content.** Find anything tied to one person, one machine or one
   business: a personal name, a brand name or logo, a colour palette, an absolute path bound to one
   machine or vault, client names, private endpoints, credentials or personal email addresses.
   Replace each with a clearly marked placeholder or a config value the adopter fills in. Preserve
   the original filled-in version as a worked example under `examples/`, named with an identifying
   suffix, so the value is kept while the deployed default stays generic. Where the skill carries
   personal-style rules or preferences, mark them inline so adopters can relax them.

6. **Write the README.** It must read in the author's voice and cover, in this order: a title and a
   one-paragraph summary, a short "what it does" section, installation, usage, rationale, an
   extension guide, the repository layout, the licence and a one-line credit. The four sections the
   user always wants are installation, usage, rationale and the extension guide, so never ship
   without all four. See the README requirements below.

7. **Add a licence.** Write an MIT `LICENSE` with `Copyright (c) <year> <your author name>`, unless
   the source skill already carries a different licence, in which case keep that one and credit the
   original terms.

8. **Run the writing gate.** Re-read the README and any prose you wrote, then check it against your
   writing standard and fix every issue before publishing. The default standard bundled with this
   engine is a set of anti-AI-writing scans, which encode one writer's preferences that you may
   adjust or replace:
   - `grep -nE ", and\b"` for the serial comma or a comma-joined "and" (drop this check if you keep
     the Oxford comma)
   - no em-dash character and no spaced em dash
   - no semicolon
   - no whole-word "honest", "honesty" or "honestly", except where the README names a rule as a
     meta-reference
   - no sentence opening with "And" or "But"
   The full rule set behind these scans lives in the `anti-ai-writing` skill, which you can adopt as
   your standard or swap for your own. The verbatim source files are not your prose, so do not alter
   them to pass the scan.

9. **Build a populated example and ship a compiled output.** Every package must carry a worked
   example of the skill's output that a reader can see, since an abstract template or a description
   alone cannot be visualised. If the skill produces a compiled artifact, for example a PDF from a
   Quarto, LaTeX, Marp or Markdown source, ship a populated example that compiles on its own, not
   only a placeholder template, then actually run the compile and commit both the source and the
   rendered file, for example the `.qmd` or `.md` together with the `.pdf`. A real build is required
   here, because a static read misses compile-time failures, for example a style file ending with
   `\endinput` that terminates the document when the build tool inlines it, or a tool that reads a
   stray `.env` file from the working directory and stops. For a skill whose output is text rather
   than a compiled document, render a short representative sample of that output to a PDF so the
   reader can still see what a run produces. Fix any build failure in the bundled files before
   publishing.

10. **Publish to GitHub.** Clone your skills repository into a temporary directory, copy the staged
    `<skillname>/` folder into the clone as `<skillname>/`, commit with a clear message, push to the
    default branch, then remove the temporary clone. Pushing is irreversible and outward facing, so
    confirm the source is the user's own work before this step.

11. **Report.** Give the staged path, the published folder URL inside the repository, a note of what
    was genericised, the result of the writing-gate checks and the result of the example build.

## README requirements

Write the installation section for every platform the skill can run on, in short paragraphs rather
than a wall of bullets. Cover Claude Code (copy the folder into `~/.claude/skills/<skillname>/` for
a user-level install or `.claude/skills/<skillname>/` for a project-level install, with the folder
named to match the frontmatter), Claude Desktop and claude.ai (added through the Skills or
Capabilities setting), Copilot CLI (auto-discovered from installed plugins), Gemini CLI (activated
through `activate_skill`) and any other tool (paste the rules into a system prompt or an instruction
file such as `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`).

Write the usage section so it explains how the skill is triggered and what it returns, including any
slash-command form and any trigger phrases.

Write the rationale section so a reader understands why the skill works the way it does, grouped by
theme rather than walked through line by line. The reader should finish it understanding the problem
the skill solves and how each part of the skill addresses that problem.

Write the extension guide so an adopter has a concrete path to customise the skill: which file to
edit for each kind of change, how to supply their own config or voice profile where the skill uses
one and how to keep any companion files in step with their edits.

## Genericising notes

The test for whether something must be genericised is simple. Ask whether the content only makes
sense for one person, one machine or one business, or whether it would help anyone. Content that
helps anyone stays. Content that is personal becomes a placeholder, with the filled-in original
preserved under `examples/` so nothing of value is lost. When a skill embeds a brand, pull the brand
into a config the adopter replaces, so the method publishes without the brand assets.

## Common mistakes

- Publishing a third-party skill as the user's own. Check author metadata and licence first.
- A staged or published folder name that does not match the frontmatter `name`, so the skill never
  loads. Keep both names equal to `name`.
- An external file dependency left unbundled, so the skill installs but cannot run because the
  adopter lacks the templates, scripts, config or assets it reads from outside its folder. Bundle
  them into the package.
- A README that falls below your writing standard. Run the writing gate before pushing.
- Shipping a skill with no visible example of its output, so a reader cannot picture what it
  produces. Ship a compilable example and a rendered PDF, then build it before publishing, since a
  static read misses compile-time failures.
- Leaving brand assets or a personal voice profile in the deployed default. Genericise, then keep
  the original under `examples/`.
- Force-pushing or overwriting other skills in the repository. Add the new folder only, then push.

## Note on delegation

The README writing is real content production, so it may be delegated to a worker-and-reviewer pass,
where one agent drafts the package and a second reviews it for correctness, style, completeness and
depth before the push. A router skill such as `model-router` can manage that split, though the
choice is yours. Whether delegated or written directly, the README must pass the writing gate in
step 8 before the push in step 10.
