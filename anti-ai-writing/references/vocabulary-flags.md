# Vocabulary Flags: Soft Blacklist

## How to Use This List

- **Tier 1: Always flag**: These words have no legitimate use in the output contexts covered
  by this skill. Replace on sight.
- **Tier 2: Flag during review**: These words are overused by AI but occasionally appropriate.
  Flag them and replace unless the word is genuinely the most precise term for the context.
  One Tier 2 word per 500 words of output is acceptable. More than that is a pattern.
- **Tier 3: Flag when clustered**: These are common words that only become tells when two or
  more appear within the same paragraph. One alone is fine. Two in a paragraph is suspicious.
  Three is a pattern; rewrite.

---

## Tier 1: Always Replace

| AI word/phrase | Plain alternative |
|---|---|
| em dash: — or " — " (spaced) | comma, colon, semicolon, parentheses, or restructure |
| delve / delve into | examine, look at, explore (if genuinely exploring) |
| utilize | use |
| leverage (verb) | use, apply |
| harness | use, apply, capture |
| facilitate | help, enable, allow |
| commence | start, begin |
| endeavor(s) | effort(s), work, attempt |
| aforementioned | (name the thing again, or use "this") |
| myriad | many, several, a range of |
| plethora | many, a lot of |
| paradigm (outside philosophy of science) | model, approach, framework |
| synergy / synergize | (delete or describe the specific benefit) |
| bolster | support, strengthen |
| pivotal | important, key (or delete; let importance show) |
| embark on | start, begin |
| underscore (figurative) | show, highlight, make clear |
| elucidate | explain, clarify |
| multifaceted | complex, varied (or describe the actual facets) |
| nuanced (as empty praise) | (describe the actual nuance) |
| navigating (figurative) | managing, handling, working through |
| streamline | simplify, speed up |
| empower | enable, equip, help |
| spearhead | lead |
| foster | support, encourage, build |
| illuminate | show, reveal, explain |
| ascertain | find out, determine |
| optimize (when vague) | improve (or specify what metric improves) |
| revolutionize | (describe the specific change) |
| groundbreaking | (describe what's actually new) |
| cutting-edge | current, latest, recent |
| state-of-the-art | current, latest (or name the specific tech) |
| best-in-class | (name the actual benchmark or delete) |
| game-changer | (describe the specific impact) |
| disrupt / disruptive | (describe what changes and for whom) |
| crafts / crafting (figurative) | makes, creates, writes, designs |
| cultivate / cultivates (figurative) | build, grow, develop |
| symbolic of / symbolises / symbolizes (figurative) | (describe what it actually shows or delete) |
| reflects (figurative meaning-making) | shows, indicates (or describe what is shown) |
| emblematic of | (describe what it shows or delete) |
| unsung hero | (name the actual contribution) |
| secret weapon | (name the actual advantage) |
| "this is gold" | (describe what is valuable about it) |
| fluff (as filler dismissal) | (delete the meta-comment, or describe what is actually being removed) |

---

## Tier 2: Flag During Review

These are acceptable in limited use. Flag if more than one appears per 500 words.

| Word/phrase | When it's OK | When it's an AI tell |
|---|---|---|
| robust | Describing tested, fault-tolerant systems | Vague praise: "a robust solution" |
| seamless | Describing genuinely zero-friction integration | Generic praise: "seamless experience" |
| comprehensive | Describing documented coverage scope | Filler: "a comprehensive overview" |
| innovative | Describing a specific technical novelty | Empty praise without specifics |
| landscape | In geography or literal terrain | Figurative: "the AI landscape" |
| ecosystem | In biology or platform architecture | Vague: "the tech ecosystem" |
| tapestry | In textiles or art discussion | Figurative: "a rich tapestry of ideas" |
| realm | In specific domain reference | Vague: "in the realm of possibilities" |
| beacon | In navigation or lighting | Figurative: "a beacon of hope" |
| fabric | In textiles or material science | Figurative: "the fabric of society" |
| vibrant | Describing measured colour or activity | Empty praise: "a vibrant community" |
| thriving | With specific growth metrics | Vague: "a thriving ecosystem" |
| nestled | In literal geographic description | Promotional: "nestled in the heart of" |
| dynamic | Describing runtime behaviour | Vague praise: "a dynamic approach" |
| holistic | In systems engineering (justified) | Buzzword: "a holistic solution" |
| leverage (noun) | In finance (mechanical advantage) | Buzzword anywhere else |
| impactful | (prefer "effective" or describe the impact) | Almost always an AI tell |
| resonate | In acoustics or signal processing | Figurative: "this resonates with..." |
| compelling | With specific evidence cited | Empty: "a compelling argument" |
| insightful | (describe the insight instead) | Almost always empty praise |
| quiet (figurative) | Literal sound description | Marketing copy: "quiet luxury", "quiet revolution", "quiet quitting", "the quiet shift in..." |
| execute (figurative) | Running code, executing a trade, executing a program in the literal sense | Corporate-speak: "execute on our vision", "execute the strategy", "execute the plan" (replace with "do", "carry out", or describe the actual step) |

---

## Tier 3: Flag When Clustered

These are normal words individually. They become AI tells when two or more co-occur in the
same paragraph.

- crucial + significant + essential
- enhance + improve + elevate
- key + vital + critical
- notable + remarkable + noteworthy
- ensure + maintain + sustain
- transform + evolve + shift
- integrate + incorporate + embed
- address + tackle + mitigate
- offer + provide + deliver
- drive + fuel + propel
- highlight + emphasize + underscore
- ultimately + fundamentally + inherently
- increasingly + continuously + consistently
- effectively + efficiently + strategically

**The cluster test**: Read the paragraph aloud. If it sounds like a press release or a
management consultant's slide deck, it has too many Tier 3 words. Replace the weakest ones
with plainer language or delete them entirely.

---

## Model-Specific Tells (2025–2026)

These patterns are associated with specific models and have become recognizable:

### ChatGPT-associated
- "delve" (dropping off in 2025 but still a tell)
- Em-dash usage in any form (now Tier 1 banned globally)
- "It's not X, it's Y" constructions
- "But here's the thing"
- Emoji-headed bullet lists

### Claude-associated
- "I appreciate you sharing that"
- "That said," as transition
- "I should note that"
- "Let me be direct" / "Let me be straightforward"
- Starting responses with "Great question" or restating the question
- Reflexive both-sides-ing on any remotely contested topic

### Gemini-associated
- "emphasizing" / "highlighting" / "showcasing" (post mid-2025)
- Heavy attribution to media coverage for notability claims
- "enhance" as universal improvement verb

### General (all models)
- "Certainly!" / "Absolutely!" as openers
- "I hope this helps!"
- "Here's a comprehensive..."
- Curly quotes in contexts where straight quotes are standard
- Skipping heading levels (jumping from H1 to H3)

---

## Sentence-Level Patterns (Tier 1, hard ban)

These are multi-word constructions, not single vocabulary items. They are banned outright in
every output type, including informal emails. See SKILL.md Rule 23 for the rationale.

### "Honest", "honesty", "honestly" in any usage

**Absolute Tier 1 ban on the words "honest", "honesty", and "honestly" anywhere, in any
grammatical role.** This is not a context-dependent ban. The word never appears in the user's
professional writing. If it shows up in a draft, strip it and rewrite the surrounding clause
with a word that actually carries the intended meaning.

| Banned pattern | Fix |
|---|---|
| `Two honest gaps to carry forward` | `Two important aspects to take into account` |
| `Three honest observations` | `Three observations` |
| `An honest assessment` | `An assessment` |
| `The honest reality is...` | State the reality directly, without the preamble |
| `honest limitations` | `key limitations` or `limitations` |
| `the honest description of X` | `the best description of X` or `the most accurate description of X` |
| `the honest answer is X` | State X directly. Delete the preamble. |
| `an honest account of Y` | `an accurate account of Y` or `a direct account of Y` |
| `honest numbers` / `honest data` | `accurate numbers`, `verified data`, `the actual numbers` |
| `to anonymise honestly` | `to anonymise accurately` |
| `to handle this honestly` | `to handle this directly` or `to handle this without dressing it up` |
| `an honest broker` (idiom) | `an impartial broker` or restructure |
| `the honest verdict` | `the verdict`, `the right call` |
| `the honest path forward` | `the right path forward`, `the path forward` |

The underlying principle: the word "honest" performs candour rather than conveying meaning.
The user writes with specifics and direct claims, not with signals of sincerity. When the
intended sense is "true" or "accurate", say so. When the intended sense is "candid" or
"unvarnished", say that, or rewrite so the directness comes from the noun-and-verb choice
rather than from an adjective layered on top.

**User-supplied example of the trap**:

| Banned | Fix |
|---|---|
| `the system reasons about the reachable set, which is the honest description of the vehicle's possible whereabouts given only what is known` | `the system reasons about the reachable set, which is the best description of the vehicle's possible whereabouts given only what is known` (or `the most accurate description`, or `the tightest characterisation`) |

---

### Confessional interjections

Strip on sight, in every position (mid-sentence, sentence-opening, parenthetical aside).
Replace with the direct claim alone, or rewrite to add specificity instead of theatrical
sincerity.

| Banned phrase / pattern | Why it fails | Fix |
|---|---|---|
| `, I have to be honest with you,` (mid-sentence) | Fakes candour mid-flow; AI tell | Delete the interjection; state the claim directly |
| `I have to be honest with you, ...` (sentence-opener) | Same; theatrical sincerity | Delete; lead with the claim |
| `, to be honest,` (any position) | Hollow disclaimer | Delete |
| `, honestly,` (any position) | Hollow intensifier | Delete or replace with specifics |
| `, to be frank,` | Same | Delete |
| `, I'll be honest,` / `, let me be honest,` | Same | Delete |
| `, in all honesty,` / `, truth be told,` | Same | Delete |
| `, I will not lie,` / `, not gonna lie,` | Same | Delete |
| `If I'm being honest, ...` / `If I'm honest, ...` | Conditional confessional opener | Delete; lead with the claim |
| `Look, ...` (sentence-opener, performative) | AI-style faux candour | Delete |

The principle: if the writer needs to flag honesty, the surrounding prose has already failed
to be specific. Add a concrete fact instead of a confessional preamble.

---

### Idioms and figurative expressions (Rule 29, hard ban)

Idiomatic and figurative phrases read as cheap and unprofessional in the user's voice. Every
hit is a violation. Replace with the literal claim the figure was reaching for. The catalogue
below is not exhaustive. Any other idiom or figurative phrase is also banned.

**Business and office idioms**:

| Banned | Fix |
|---|---|
| `on the table` / `off the table` | `available` / `not possible`, `not realistic`, `ruled out` |
| `boil the ocean` | `solve every variable at once` (state why that is not feasible) |
| `move the needle` | quantify the actual effect, e.g. `cut response time by 23%` |
| `low-hanging fruit` | name the specific cheap intervention |
| `kick the can down the road` | `defer the decision`, `postpone without resolving` |
| `circle back` | `return to this on [date]` or `revisit once X is known` |
| `touch base` | `meet briefly`, `confirm by email`, or state the actual action |
| `park that for now` | `defer that for now`, `set that aside until X` |
| `in the weeds` | `caught up in detail at the expense of the main question` |
| `drinking from a firehose` | `processing more input than is comfortable`, or restructure |
| `raising the bar` / `moving the goalposts` | `increasing the criterion` / `changing the criterion after the fact` |
| `in the same boat` | `facing the same constraint`, name the constraint |
| `on the same page` | `aligned`, or state the specific point of agreement |
| `ducks in a row` | `prerequisites in place`, name them |
| `the elephant in the room` | Name the actual topic directly |
| `skin in the game` | `personal exposure to the outcome` |
| `at the end of the day` | Delete entirely |
| `when push comes to shove` | `when the trade-off is forced`, state the specific condition |
| `the rubber meets the road` | `in operation`, `under real conditions`, `at execution` |

**Body and combat metaphors**:

| Banned | Fix |
|---|---|
| `uphill battle` | `difficult`, `slow`, name the specific resistance |
| `fighting fires` | `responding to incidents as they arise` |
| `biting the bullet` | `accepting the cost` (name the cost) |
| `in the trenches` | `working directly on the implementation` |
| `shooting ourselves in the foot` | `damaging our own position by X` (name what) |
| `gunning for` | `pursuing aggressively`, restate the intent |
| `in the crosshairs` | `targeted by X` (name the actor) |

**Sports and game metaphors**:

| Banned | Fix |
|---|---|
| `ballpark figure` / `ballpark` | `rough estimate`, `approximately R110,000` |
| `hit it out of the park` | `delivered well above the target`, quantify |
| `game changer` | `displaces the previous approach because X`, or quantify |
| `level the playing field` | `equalise conditions`, name the conditions |
| `moving target` | `criterion that keeps changing`, state how |
| `endgame` | `final phase`, `final objective` |

**Travel and path metaphors**:

| Banned | Fix |
|---|---|
| `the road ahead` | `the next phase`, `the next twelve months` |
| `down the line` / `down the road` | `later`, `in [specific timeframe]` |
| `stay the course` | `continue with the current plan` |
| `off the beaten path` | `uncommon`, `rarely chosen`, name why |

**Water and weather metaphors**:

| Banned | Fix |
|---|---|
| `a sea change` | `a fundamental shift in X` (name the shift) |
| `weathering the storm` | `surviving the [specific] downturn` |
| `smooth sailing` | `straightforward`, `without obstacle` |
| `perfect storm` | `X, Y, and Z occurring together`, name the chain |
| `ride the wave` | `take advantage of the current X` |
| `in deep water` | `in serious difficulty with X`, name the difficulty |

**AI-prose metaphor sets** (these are the most common AI tells):

| Banned | Fix |
|---|---|
| `a tapestry of factors` | `several factors`, name them |
| `a landscape of options` | `the available options`, list them |
| `a journey through X` | `an account of X`, `working through X` |
| `a roadmap to Y` | `a plan for Y`, `the steps to reach Y` |
| `a window into X` | `a view of X`, `evidence about X` |
| `the dawn of a new era` | Delete the framing, state the specific change |
| `at the intersection of A and B` | `combining A and B`, restructure to state the combination |
| `weaving together threads` | `combining the points`, list the points |
| `the fabric of X` | `the structure of X`, `the composition of X` |

**Narrow exception**: a literal technical idiom that is the standard name of a concept in
its field stays, because the meaning is literal in that field. Examples: `bus`, `pipeline`,
`bottleneck`, `handshake`, `heartbeat`, `lock`, `fan-out`, `signal-to-noise ratio` when used
as the agreed technical term for a specific concept. The test is whether the term is the
established name of a specific concept, not whether it sounds technical. Using `bottleneck`
to mean "the slowest measured stage in a pipeline" is fine. Using `bottleneck` to mean
"anything slowing us down" is a figurative reach and is banned.

**User-supplied trap example**:

| Banned | Fix |
|---|---|
| `sealing the area is not on the table` | `sealing the area is not possible` or `sealing the area is not realistic` |

The principle: figurative language gestures at meaning instead of stating it. If a sentence
reaches for an idiom, the literal claim has not been worked out. Stop, write the literal
claim instead.

---

### "And" and "But" punctuation and syntax bans (Rule 30, hard ban)

Two coupled bans on how "and" and "but" appear in prose. Both apply at full strength in
every output type and every register.

**Ban 1: no comma directly before the word "and"**. This drops the Oxford (serial) comma in
lists and removes the comma that joins two independent clauses with "and" as a conjunction.
The `grep -nE ", and\b"` scan should return zero hits in any prose output.

| Banned (comma + and) | Fix |
|---|---|
| `LoRaWAN, Meshtastic, and MeshCore` | `LoRaWAN, Meshtastic and MeshCore` |
| `the system is resilient, robust, and inexpensive` | `the system is resilient, robust and inexpensive` |
| `we tested SF7, SF10, and SF12` | `we tested SF7, SF10 and SF12` |
| `she finished the report, and he reviewed it` | `she finished the report and he reviewed it`, or split into two sentences: `she finished the report. He reviewed it.` |
| `the variants vary in cost, in topology, in licence, and in support` | `the variants vary in cost, topology, licence and support` |

**Ban 2: no sentence opens with "And" or "But"** in any register. Reinforces and extends
Rule 22. The `grep -nE "(^|[.!?] )(And|But) "` scan should return zero hits.

| Banned (sentence opener) | Fix |
|---|---|
| `But the cost is prohibitive.` | `The cost is prohibitive though.`, or fold into prior sentence with `, though the cost is prohibitive` |
| `And the recommendation stands.` | `The recommendation stands.` |
| `But here's the catch.` | Restate the catch directly; the opener is hiding the content. |
| `And that is why we recommend Meshtastic.` | `That is why we recommend Meshtastic.`, or `We therefore recommend Meshtastic.` |
| `But what about the duty cycle?` | `The duty cycle is the next question.` |

**Interaction trap**: when a draft contains `X, and Y` as a compound sentence, the reflex is
to split into `X. And Y.` which trades a Ban 1 violation for a Ban 2 violation. Neither is
acceptable. The correct rewrite is one of:

- Drop the comma alone: `X and Y`.
- Split cleanly without a leading conjunction: `X. Y.`
- Use a different connective: `X, which Y`, `X because Y`, `X, though Y`.

The principle: "and" is a fluent connective inside a flowing sentence, not a punctuation
hinge between clauses and not a sentence opener. "But" is even more restricted: the user's
voice carries contrast through `though`, `yet`, `while`, or restructured phrasing, never
through a sentence-opening "But".

---

## The Replacement Principle

When replacing a flagged word, do not reach for another impressive synonym. Reach for the
**plainest accurate word**. The goal is not to find a clever substitute; it is to say the
thing simply.

"Leverage our robust infrastructure" → "Use our tested servers"
"Navigate the complex landscape" → "Handle the competing requirements"
"Foster meaningful collaboration" → "Help teams work together"
