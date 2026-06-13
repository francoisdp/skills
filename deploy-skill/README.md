# deploy-skill

[![Tested with NVIDIA SkillSpector](https://img.shields.io/badge/Tested%20with-NVIDIA%20SkillSpector-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/SkillSpector)

> **Security:** This skill was scanned with [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector), a security scanner for AI agent skills. The skill contains no executable code. Every pattern the scanner flagged was reviewed manually and assessed as a false positive against the skill's documentation and templates. For your own safety, read the skill source and re-scan it before installing if you have any doubt. The full scan report sits in this folder as `skillspector-report.md`.

A skill that packages one of your own Claude skills and publishes it to your GitHub repository as a clean, well-documented public folder. It is the engine the rest of these skills were shipped with, since it takes a private skill, genericises the parts that are personal to you, writes a full README covering installation, usage, rationale and an extension guide, adds a licence, then pushes the result to a repository you configure. You invoke it as `/deploy-skill <skillname>`.

## What it does

Point the skill at the name of a skill you authored and it runs a ten-step workflow. It resolves where the source skill lives, reads it in full, stages a package folder, bundles any files the skill depends on from outside its own folder, replaces the content that is personal to you with placeholders while preserving your filled-in version as a worked example, writes the README and the licence, checks its own prose against your writing standard, then clones your skills repository, adds the new folder and pushes. The result is a folder anyone can install, documented well enough that they understand not only how to use the skill but why it works the way it does.

## Installation

The skill is a folder containing `SKILL.md` and an `examples/` folder. The folder must be named `deploy-skill` so it matches the skill name in the frontmatter.

For **Claude Code**, copy the folder into `~/.claude/skills/deploy-skill/` for a user-level install, or `.claude/skills/deploy-skill/` inside a project. Claude Code discovers the skill from its frontmatter.

For **Claude Desktop and claude.ai**, add the skill through the Skills or Capabilities setting in the application.

For **Copilot CLI**, the skill is auto-discovered from installed plugins through the `skill` tool.

For **Gemini CLI**, the skill activates through `activate_skill`, with the frontmatter loaded at session start.

For **any other tool**, the steps are plain Markdown you can paste into a system prompt or an instruction file such as `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`.

The publish step uses the GitHub command-line tool `gh` and `git`, so install both and authenticate `gh` once with `gh auth status` to confirm. Publishing pushes to a repository, so the account you authenticate must have write access to the repository you configure.

## Usage

Before the first run, set the five configuration values in the Configuration section of `SKILL.md`. These tell the engine where your authored skills live, where to stage the package, which GitHub repository to publish to, what name to put on the licence and which writing standard to hold the README to. A worked example filled in for one user sits at `examples/config-francois.md`, which you can copy and edit.

Once configured, trigger the skill with `/deploy-skill <skillname>`, where `<skillname>` is the folder name of a skill you wrote. The engine runs the workflow and reports the staged path, the published folder URL inside your repository, a note of what it genericised and the result of the writing-gate checks. It stops and asks rather than guessing whenever the source is ambiguous. It also refuses to publish a skill that carries another person's author metadata or licence, so you do not ship someone else's work by accident.

## Rationale

A skill that works for you is not the same as a skill someone else can install. Your version is full of things that only make sense in your setup, which is absolute paths to your machine, the name of your business, your brand assets, your folder structure and the writing habits that are yours rather than universal. The engine exists to cross that gap in a repeatable way, so that publishing the tenth skill is as disciplined as publishing the first, rather than a fresh round of manual copying and editing that quietly forgets a step.

Each step earns its place by closing a specific failure. The author-and-licence check at the start stops you from republishing a downloaded skill under your own name, which is both a courtesy and a legal point. The dependency-bundling step exists because a skill that reads templates or scripts from a fixed path will install cleanly yet fail on first use, since the adopter never had those files, so the engine copies a generic version of them into the package. The genericising step replaces what is personal with placeholders while preserving your filled-in original as a worked example, so the deployed default is clean without throwing away the concrete version that shows an adopter what good looks like. The writing gate treats the README as a release artifact rather than an afterthought, because a sloppy README is the first thing a reader judges. The publish step works through a temporary clone and adds only the new folder, so a deploy never force-pushes over the skills already in the repository.

The configuration block is what makes the engine portable. Everything personal is named once at the top, which is your skills source, your staging folder, your repository, your name and your writing standard, then every step reads those values rather than hardcoding them. That is the same discipline the engine applies to the skills it ships, turned back on itself, so the engine that genericises other skills is itself genericised.

## Extension guide

The skill is plain Markdown, so customising it means editing `SKILL.md`.

Start with the Configuration table, where you set the five values for your own setup. The most consequential is the writing standard in step 8. The default is a short set of anti-AI-writing scans that encode one writer's preferences, which include dropping the Oxford comma and banning the em-dash, the semicolon and a few specific words. If those are not your preferences, edit the scan list in step 8, or point the gate at your own standard. The full rule set behind the default scans is the `anti-ai-writing` skill in the same repository, which you can adopt wholesale as your standard.

To change what counts as personal content, edit the list in step 5, adding the kinds of names, paths or assets that appear in your own skills. To change the README structure, edit the README requirements section, which sets the order and content of the sections the engine writes. To change where packages are staged or which repository they publish to, edit the Configuration table rather than the steps, since the steps read from it. To delegate the README writing to a worker-and-reviewer pass, see the note on delegation at the end of `SKILL.md`.

## Repository layout

```
deploy-skill/
├── SKILL.md     the engine: configuration, the ten-step workflow, README requirements and notes
├── README.md    this file
├── LICENSE      MIT licence
└── examples/
    └── config-francois.md   a worked configuration filled in for one user
```

## Licence

This package is released under the MIT licence, with the full text in the `LICENSE` file.

## Credit

The skill was developed by Francois du Plessis. Contributions and forks are welcome.
