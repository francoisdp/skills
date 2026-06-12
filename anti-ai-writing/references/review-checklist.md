# Review Checklist: Active Audit Procedure

## When to Use

Use this checklist when the user explicitly requests an anti-AI review. The passive rules
(in SKILL.md) shape generation automatically. This checklist structures the active audit of
existing text.

---

## Pass 1: Surface Scan

Read the full text once. Flag on sight:

### Vocabulary check
1. Scan for Tier 1 words (always replace). Count them.
2. Scan for Tier 2 words. Count them. Flag if more than 1 per 500 words.
3. Scan for Tier 3 clusters. Flag any paragraph with 2+ Tier 3 words from the same group.
4. Check for model-specific tells (see vocabulary-flags.md, "Model-Specific Tells").

### Structure check
5. Count consecutive paragraphs with identical structure. Flag runs of 3+.
6. Check for bullet lists in argumentative or analytical sections. Flag.
7. Check for any em dash (—) or spaced em dash ( — ). Every instance is a violation (hard ban, not a frequency limit).
8. Check heading levels: are any skipped (H1 to H3)?
9. Check for excessive bold. Flag if more than 2 bold phrases per page-equivalent.

### Transition check
10. List all paragraph-opening transitions. Flag banned openers (Rule 8).
11. Check for "Not only X, but also Y" constructions. Flag.
12. Check for "It's not X, it's Y" or "It's not X; it's Y" constructions. Flag if more than one in the piece.
13. Check for "But here's the thing" or similar conversational pivots.
13a. Check for ANY appearance of "honest", "honesty", or "honestly" (Rule 23). Run a case-insensitive whole-word scan (`grep -niwE "honest|honesty|honestly"` or equivalent). EVERY hit is a violation, regardless of grammatical role: confessional interjection, sentence opener, meta-honesty framing, structural-label adjective, plain descriptive adjective meaning "true"/"accurate" (e.g., "the honest description of X"), adverb ("anonymised honestly"), or idiom ("an honest broker"). Hard ban, no exceptions. Replace with the word that carries the actual meaning: `best`, `most accurate`, `accurate`, `correct`, `precise`, `direct`, `unvarnished`, or restructure so the noun stands without the modifier. Also flag the legacy specific phrases: `, to be frank,`, `, I'll be honest,`, `, in all honesty,`, `, truth be told,`, `If I'm being honest`, `If I'm honest`, `Look,` (as performative opener).
13b. Check for transition questions ("The catch?", "The kicker?", "The result?", "The twist?", "The takeaway?", or "Why does this matter?" as a standalone hinge). Hard ban, every instance is a violation (Rule 8).

### Content check
14. Flag any vague attribution ("experts believe," "studies show," "research indicates").
15. Flag any significance inflation ("watershed moment," "game-changer," "paradigm shift").
16. Flag any generic conclusion ("the future looks bright," "only time will tell").
17. Flag any chatbot artifacts ("Certainly!", "I hope this helps!", "Great question!").
18. Flag any emotional claims not backed by concrete detail.
19. Flag any copula avoidance ("serves as," "features," "boasts").
20. Flag any synonym cycling (same concept given 3+ different names in one section).

### Pattern check (added rules)
21. Flag rule-of-three pile-ups where most groupings are collapsed into threes regardless of natural count (Rule 4).
22. Flag uniform list lengths where every section or heading is followed by the same bullet count (Rule 4).
23. Flag "whether" appearing three or more times in the same passage, or "from X to Y" more than once (Rule 16).
24. Flag figurative meaning-making applied to ordinary events ("this represents", "this reflects", "symbolic of", "emblematic of") (Rule 9).
25. Flag fabricated illustrative personas ("Take Sarah Chen, a marketing manager at...", "Imagine Mark, a 35-year-old product lead...") (Rule 13).
26. Flag any statistic quoted without a date or source (Rule 13).
27. Flag "the ones who..." or similar vague subject groups without naming who is meant (Rule 13).
27a. Flag any idiom or figurative expression (Rule 29). Scan for stock business idioms ("on the table", "off the table", "boil the ocean", "move the needle", "low-hanging fruit", "kick the can down the road", "circle back", "touch base", "at the end of the day", "when push comes to shove", "the rubber meets the road", "the elephant in the room", "skin in the game", "ducks in a row", "on the same page", "in the weeds"), body and combat metaphors ("uphill battle", "fighting fires", "biting the bullet", "in the trenches", "in the crosshairs"), sports metaphors ("ballpark", "game changer", "level the playing field", "moving the goalposts", "hit it out of the park"), travel metaphors ("the road ahead", "down the line", "down the road", "stay the course", "off the beaten path"), water and weather metaphors ("a sea change", "weathering the storm", "smooth sailing", "perfect storm", "in deep water", "ride the wave"), and AI-prose metaphor sets ("a tapestry of", "a landscape of", "a journey through", "a roadmap to", "a window into", "the dawn of", "at the intersection of", "weaving together", "the fabric of"). Each hit is a violation. Replace with the literal claim. Test: ask "what would the sentence say if the figurative phrase were stripped?". If the literal claim is clearer, the figurative phrase was filler.
27b. Flag every comma directly before "and" (Rule 30, Ban 1). Run `grep -nE ", and\b"` against the prose. EVERY hit is a violation, including the Oxford (serial) comma in lists and the comma joining two independent clauses with "and". Fix by dropping the comma (`X, Y and Z`), by splitting the sentence (`X. Y.` without an "And" opener), or by using a different connective (`X, which Y`, `X because Y`, `X, though Y`).
27c. Flag every sentence that opens with "And" or "But" (Rule 30, Ban 2; reinforces Rule 22). Run `grep -nE "(^|[.!?] )(And|But) "` against the prose. EVERY hit is a violation, in every register including informal emails. Fix by folding the clause into the previous sentence with a connective ("though", "yet", "while", "because"), or by restating the second sentence so it stands on its own without a leading conjunction.

### Web-publishing check (only for blog posts, articles, and web copy)
28. Check whether H2 headings reuse the same skeleton across pieces in the same series, such as `What is X?`, `Why X matters`, `How to get started with X`, `Conclusion` (Rule 26).
29. Check whether claims, statistics, or expert opinions appear with no internal or external source link (Rule 26).
30. Check whether the meta description duplicates the first sentence of the body rather than framing why the reader should click (Rule 26).
31. Check whether a product is referenced generically ("the tool", "the platform", "the solution", "the software") when it has a brand name (Rule 26).

---

## Pass 1 Output

For each violation found, record:
- **The quoted text** (enough context to locate it)
- **Rule violated** (by number and name)
- **Why it's a violation** (one sentence)
- **Suggested fix** (the rewritten version)

---

## Pass 2: Rewrite

Apply all fixes from Pass 1. Produce the clean version. During rewriting:

- Do not introduce new AI patterns while fixing old ones. This is the most common failure
  mode. Replacing "leverage" with "harness" is not a fix; replace with "use."
- Do not over-correct into stiff, robotic prose. The goal is natural human writing, not
  stripped-down telegraph style.
- Preserve the original's intent, facts, and structure (unless the structure itself is the
  problem).
- Mark any passages where you changed meaning (not just style) with a note.

---

## Pass 3: Second-Pass Audit

Re-read the rewritten version as if encountering it fresh. Check specifically for:

1. **Surviving Tier 2 words**: did any slip through?
2. **New transitions**: did the rewrite introduce "Furthermore" or "Moreover"?
3. **Rhythm monotony**: read three consecutive paragraphs aloud. Same beat?
4. **Lingering copula avoidance**: any "serves as" that wasn't caught?
5. **Over-correction**: is the prose now so stripped that it reads like a telegram?
6. **Voice match**: does it sound like the person described in voice-calibration.md?

If any issues survive, fix them and note what survived and why.

---

## Output Structure

When returning results to the user, use exactly this structure:

```
## 1. Violations Found

[Table or grouped list of violations from Pass 1]

## 2. Rewritten Version

[Clean text with all fixes applied]

## 3. Change Summary

[Grouped by rule: what changed and why]

## 4. Second-Pass Audit

[Results of Pass 3: surviving patterns and fixes]
```

---

## Severity Levels

When reporting violations, assign severity:

- **High**: Chatbot artifacts, significance inflation, Tier 1 vocabulary, vague attributions
  without any source. These are immediate credibility risks.
- **High**: Em-dash usage in any form (Tier 1 ban). Chatbot artifacts, significance inflation, Tier 1 vocabulary, vague attributions without any source.
- **Medium**: Structural monotony, formulaic transitions, copula avoidance.
  These are pattern tells that accumulate.
- **Low**: Tier 3 clusters, mild rhythm monotony, occasional hedging. These are polish issues
  that matter in aggregate.

Focus the user's attention on High violations first. Medium violations should be fixed in any
professional output. Low violations are for final polish.

---

## Calibration Notes

This checklist is intentionally strict. Not every flagged item must be fixed; the user
decides. The skill's job is to surface the patterns so the user can make informed choices.
Some Tier 2 words genuinely are the best word for the job. Some lists genuinely serve the
content better than prose. The skill flags them; the human judges.
