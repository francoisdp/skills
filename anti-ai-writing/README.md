# anti-ai-writing

A set of writing-quality rules that strip the patterns which mark text as machine-generated, applied passively to every output and as an active review pass on request. The skill shapes generation from the first word so that the prose reads as something a person wrote, so that when you ask for it explicitly the same rules run as an audit that finds violations in an existing draft and rewrites them. The rules cover hedging, inflated significance, formulaic transitions, copula avoidance, structural monotony and a catalogue of vocabulary and punctuation tells, each one a statistical fingerprint of generated text that the rules are built to remove.

## What it does

The skill runs in two modes. In passive mode it is always active, shaping output as it is generated rather than cleaning it up afterwards, so the AI patterns never enter the text in the first place. In active review mode you invoke it on an existing draft, where it returns a structured audit that quotes each violation, names the rule it breaks, rewrites the passage and then re-reads its own rewrite for surviving patterns. The scope is everything you produce in writing, which means prose, reports, proposals, emails and messages, code comments, documentation, web copy and creative writing, each with its own profile of which rules apply at full strength and which relax.

## Installation

The skill is a folder that contains a `SKILL.md` file plus a `references` directory, which most tools discover automatically once the folder sits in the right place. One detail matters across every platform, which is that the installed folder must be named `anti-ai-writing` rather than `anti-ai-writing-skill` so that the folder name matches the skill name declared in the `SKILL.md` frontmatter. Copy the inner contents into a folder called `anti-ai-writing` when you install.

For **Claude Code**, copy the skill folder into your skills directory. For a user-level install that applies across all your projects, place it at:

```
~/.claude/skills/anti-ai-writing/
```

For a project-level install that applies only inside one project, place it at `.claude/skills/anti-ai-writing/` within that project. Claude Code discovers the skill automatically from its frontmatter `name` and `description`, so there is nothing further to configure once the folder is in place.

For **Claude Desktop and claude.ai**, skills are added through the application settings rather than the filesystem, where you upload or reference the `SKILL.md`. The exact location of the setting changes from time to time as the interface evolves, so look under settings for an entry named "Skills" or "Capabilities" and add the skill from there.

For **Copilot CLI**, skills are auto-discovered from installed plugins, so the same `SKILL.md` works through the `skill` tool once the plugin that carries it is installed. No separate registration step is needed beyond installing the plugin.

For **Gemini CLI**, skills activate through the `activate_skill` mechanism, with the `SKILL.md` frontmatter loaded at session start, so the rules are available from the beginning of the session once the skill is installed where Gemini CLI looks for it.

For **any other LLM tool**, the rules are plain Markdown with no tool-specific syntax, so you can paste them into a system prompt or into a project instruction file for tools that do not support skills natively. The common instruction files are `CLAUDE.md`, `AGENTS.md` and `GEMINI.md`, so dropping the rule text into whichever file your tool reads gives you the passive shaping without any skill mechanism at all.

## Usage

Passive mode needs no command. Once the skill is installed it shapes every output automatically, so the prose comes out already free of the patterns the rules target, with nothing to invoke to get this behaviour.

Active review mode is invoked with a phrase. The trigger phrases are "review for AI writing", "clean up AI patterns", "audit this draft", "make this sound human", "anti-AI check" and "does this sound like AI", so any of them on a piece of text starts the audit. The review returns four sections in a fixed order, which are the violations found (each one quoted, with the rule it breaks and the reason), the rewritten version with every violation fixed, a change summary grouped by rule, then a second-pass audit that re-reads the rewrite and flags anything that survived. The full audit procedure, including the surface-scan checks and the severity levels, lives in `references/review-checklist.md`.

## Rationale

The rules exist because machine-generated text fails in recognisable ways, with each rule countering a specific failure rather than imposing taste for its own sake. Grouping the rules by the pattern they target makes the reasoning easier to follow than stepping through all 31 in sequence.

The first group is about conviction and leading with the point, which Rules 1 and 2 cover, because hedging and throat-clearing are the clearest tells of all. A model trained to be agreeable reaches for "it could be argued" and "it is important to note that" and an opening paragraph that circles the subject before naming it, so stripping the hedges and putting the conclusion in the first sentence does more to make text read as human-written than any other single change.

The second group is about earning words and cutting inflation, which Rules 3, 9 and 13 cover, because generated prose pads. It fills sentences with adjectives that carry no information, it amplifies ordinary events into watershed moments and paradigm shifts, then it attributes claims to "experts" and "studies" that it never names, so the cure in each case is specificity, which means deleting the empty adjective, describing what actually happened rather than labelling it significant, then naming the source or cutting the claim.

The third group is about structure and rhythm, which Rules 4, 5, 16 and 17 cover, because a model defaults to a small set of templates. It writes the same paragraph shape three times in a row, it reaches for a bullet list whenever the content could be enumerated, it groups ideas into threes whether the content has three parts or not, then it falls into a metronomic short-long-short cadence, so the rules push toward varied paragraph lengths, prose by default, deliberate counts other than three, then irregular rhythm achieved through connected sentences rather than staccato fragments.

The fourth group is about vocabulary and constructions, which Rules 6, 8, 10, 11 and 20 cover, because particular words and sentence shapes are statistical fingerprints. Words such as "delve", "leverage" and "facilitate", copula-avoiding constructions such as "serves as" and "boasts", formulaic openers such as "Moreover" and "Furthermore", the cycling through synonyms to avoid a repeat, together with the "It's not X, it's Y" mirror are all far more frequent in generated text than in writing produced quickly by a person in their own voice, so the rules name them and supply the plainer alternative.

The fifth group is about punctuation tells, which Rules 7, 24 and 30 cover, because three marks carry signal about who wrote the text. The spaced em dash is one of the highest-frequency AI tells across all models and is banned outright, which is a strong universal default. The semicolon ban and the dropped Oxford comma are different in kind, because they are personal-style choices that identify a particular writer rather than universal anti-AI improvements, so an adopter who writes with semicolons or keeps the serial comma should treat those two as preferences to adjust rather than rules to keep.

The sixth group is about voice and register, which Rules 18, 21, 22, 27 and 31 cover, because matching a real writer's voice is what separates acceptable output from output the writer would actually sign. The rules anchor generation to a voice profile, keep sentences flowing rather than blunt, hold the prose at a register a reader from a neighbouring discipline can follow, then govern tone so that the output reads as a plain professional adviser rather than a performing chatbot.

The seventh group is about technical-writing discipline, which Rules 25 and 28 cover, because technical prose has failure modes of its own. A reader must be led into a term, an acronym, a table or a figure before it is used, so that someone landing mid-document still understands what they are looking at, while mathematical content must be written in LaTeX rather than improvised with Unicode symbols, so that equations render correctly and read consistently.

The eighth group is about web-publishing tells, which Rule 26 covers, because content tools optimising for volume leave a particular hand on the page. The same heading skeleton repeats from post to post, claims appear with no citation, the meta description copies the first sentence, then a product with a name gets called "the platform", so the rule pushes toward varied headings, sourced claims, a written meta description and the product named directly.

The ninth group is about artefacts and fakery, which Rules 12, 14 and 15 cover, because generated text reaches for pleasantries and emotion and tidy endings that a person writing for a specific reader would not. The chatbot openers and closers, the asserted feelings that were never felt, together with the generic "the future looks bright" conclusion are all filler, so the rules strip them and end instead on the most important remaining fact or a concrete next step.

Read together, these groups explain why machine-generated text reads the way it does, which is that a model trained to be agreeable, fluent and safe converges on hedging, inflation, template structure, a narrow vocabulary, a few punctuation habits, a flattened voice and reflexive pleasantries, so the rules counter each pattern in turn and the output that results reads as something a person wrote with care.

## Universal rules versus personal-style rules

Before you adopt the skill it helps to know which rules are safe to take unchanged and which encode one writer's taste, because that question decides what you keep and what you adjust. The table below classifies all 31 rules, marking each as Universal or Personal-style. The eight personal-style rules are 7, 21, 22, 23, 24, 28, 30 and 31, so everything else is universal. For Rule 30 the classification splits, because dropping the Oxford comma is personal while barring the "And" or "But" sentence opener is a universal anti-AI improvement.

| Rule | Type | How to relax it, or why keep it |
|---|---|---|
| 1 Write with conviction | Universal | Keep. Hedging is the clearest AI tell. |
| 2 Lead with the point | Universal | Keep. Throat-clearing marks generated text. |
| 3 Earn every adjective | Universal | Keep. Empty adjectives are filler. |
| 4 No structural monotony | Universal | Keep. Template repetition is a tell. |
| 5 Lists require justification | Universal | Keep. Reflexive bulleting is a tell. |
| 6 Vocabulary discipline | Universal | Keep. The blacklist words are statistical fingerprints. |
| 7 No em-dash, ever | Personal-style | The spaced em dash is a strong universal default to ban, though a writer who uses it deliberately may allow it sparingly. |
| 8 No formulaic transitions | Universal | Keep. "Moreover" and "Furthermore" are tells. |
| 9 No significance inflation | Universal | Keep. Watershed-moment language is a tell. |
| 10 No copula avoidance | Universal | Keep. "Serves as" for "is" is a tell. |
| 11 No synonym cycling | Universal | Keep. Synonym cycling is a tell. |
| 12 Kill chatbot artifacts | Universal | Keep. Pleasantries mark a chatbot. |
| 13 Specific over vague | Universal | Keep. Vague attribution is a tell. |
| 14 No emotional fakery | Universal | Keep. Asserted feelings read as fake. |
| 15 No generic conclusions | Universal | Keep. "The future looks bright" is filler. |
| 16 Rhythm and variety | Universal | Keep. Metronomic rhythm is a tell. |
| 17 Context-aware formatting | Universal | Keep. Matching format to content is sound. |
| 18 Voice calibration | Universal | Keep the mechanism. Point it at your own profile. |
| 19 The "read aloud" test | Universal | Keep. A good general check. |
| 20 No parallel negative constructions | Universal | Keep. "It's not X, it's Y" is a tell. |
| 21 Flowing sentences, never blunt | Personal-style | The flowing preference is a voice choice. A writer who wants a terser rhythm may relax it. |
| 22 Write in the user's inherent voice | Personal-style | The specific voice is personal. Anchor to your own profile in references/voice-calibration.md. |
| 23 Total ban on "honest" | Personal-style | The absolute ban is a personal preference. Downgrade it to a Tier 2 flag or remove it if you use the word naturally. |
| 24 No semicolons | Personal-style | A personal preference. Remove this rule if you write with semicolons. |
| 25 Lead the reader into a concept | Universal | Keep. Undefined terminology fails any reader. |
| 26 Web-publishing discipline | Universal | Keep where you publish to the web. |
| 27 Accessible intellectual register | Universal | Keep. Pretentious vocabulary helps no one. |
| 28 LaTeX notation for mathematics | Personal-style | Applies only to writers who produce mathematical or technical documents, irrelevant otherwise. |
| 29 No idioms or figurative expressions | Universal | Keep. Stock idioms gesture at meaning instead of stating it. |
| 30 No comma before "and", no And/But openers | Personal-style and Universal | The no-Oxford-comma part is personal and adopters may keep the serial comma. The no-And/But-opener part is a universal anti-AI improvement most writers will want to keep. |
| 31 Formal register, plain English, assistant tone | Personal-style | Encodes the author's South African second-language English preference and an advising stance. Adjust to your own register and audience. |

The conclusion follows from the split. Adopt the universal set as it stands, because those rules improve almost anyone's text and removing them would weaken the anti-AI effect, then decide rule by rule on the personal set, keeping the ones that match your taste, softening the ones that are close but not quite yours and removing the ones that do not fit how you write at all.

## Extension guide

The skill is plain Markdown, so customising it means editing files, with five things you will most often want to do.

The first is to write your own voice profile, which the skill reads through Rule 18 and Rule 22. Copy `examples/voice-calibration-francois.md` to `references/voice-calibration.md` and edit it until it describes you, or fill in the blank template that already sits at `references/voice-calibration.md`. You capture your voice by pasting samples of your own writing into each trait, by adding an AI-sounding counter-example beside each sample so the skill learns the contrast, then by listing your word preferences together with the words you never use, the more concrete the better.

The second is to relax or remove a personal-style rule, which you do by editing `SKILL.md`, finding the rule by its number and either deleting it, softening its wording or downgrading a hard ban into a review-time flag. The ban on "honest" in Rule 23 and the semicolon ban in Rule 24 are the two an adopter most often removes, so if either word is part of how you naturally write, delete the rule or move the word down to a Tier 2 flag in `references/vocabulary-flags.md`.

The third is to add your own rule, which you do by appending a new numbered rule that follows the existing pattern, meaning a heading, the rule stated plainly and a Violated-by and Fixed pair of examples, after which you add the new rule to the "Application by Output Type" matrix at the bottom of `SKILL.md` so the audit knows where it applies.

The fourth is to add vocabulary to the blacklist, which you do by editing `references/vocabulary-flags.md` and placing each new word in the right tier, which is Tier 1 for words to replace on sight, Tier 2 for words to flag during review, then Tier 3 for common words that only become tells when several cluster in one paragraph.

The fifth is to keep the review checklist in step with your changes, because the active audit is driven by `references/review-checklist.md`, so whenever you add or remove a rule you update the checklist to match, which keeps the audit covering exactly the rules the skill actually enforces.

## Repository layout

```
anti-ai-writing-skill/
├── SKILL.md                          the 31 rules, the output-type matrix and the active-review section
├── README.md                         this file
├── LICENSE                           MIT licence
├── references/
│   ├── vocabulary-flags.md           the tiered word blacklist and the sentence-level pattern bans
│   ├── voice-calibration.md          the blank voice-profile template you fill in
│   └── review-checklist.md           the structured audit procedure for active review
└── examples/
    └── voice-calibration-francois.md a fully worked voice profile, kept as a model
```

## Licence

This package is released under the MIT licence, with the full text in the `LICENSE` file.

## Credit

The skill was developed by Francois du Plessis. Contributions and forks are welcome.
