---
title: "Deploy Skill: Example Run"
---

# Deploy Skill: Example Run

This skill produces no document of its own, since its output is a published skill folder in a repository. This sample shows the report the engine emits on a deploy, so you can picture a run before you use it. The command was `/deploy-skill youtube2article`.

## What happened

The engine resolved the source skill, read it in full, staged the package, then checked for external dependencies and found none to bundle. It genericised the two vault path examples, wrote the README and the licence, ran the writing gate and built the bundled example, then published to the repository.

## The final report

The run closes with a report of what was produced:

> **Source:** Resolved to `youtube2article`, the user's own work, with no third-party licence.
>
> **Published:** the `youtube2article/` folder in the skills repository, beside the other skills.
>
> **Genericised:** two vault path examples replaced with neutral ones, the Obsidian conventions documented. No voice profile or brand asset to strip.
>
> **Writing gate:** zero hits for comma-before-and, em-dash, semicolon and banned words.
>
> **Example build:** the bundled example rendered to PDF, confirmed on disk.
