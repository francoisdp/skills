# Voice Calibration: Default Profile

## About This File

This is a blank template. It defines the voice profile that the skill targets when it generates or reviews text, which you fill in with your own writing so that the output sounds like you rather than like a generic assistant. A fully worked example calibrated to one writer lives at `examples/voice-calibration-francois.md`, which you may study to see how a complete profile reads. You have two ways to proceed, so choose whichever is faster for you. You can fill in this template section by section using the placeholders and instructions below, or you can copy the worked example over this file and edit every line until it describes your own voice instead of the example author's. Either way the goal is the same, which is a profile specific enough that someone reading it could imitate your register, so the more concrete examples of your own writing you paste in, the better the calibration.

Throughout this file, text in the form `<fill in: ...>` marks a placeholder you replace with your own material, while the short instruction beside each placeholder tells you what to capture.

---

## Core Voice Traits

These six traits describe how a voice behaves at the level of tone and stance. For each one, read the explanation, then replace the placeholder with two or three short samples of your own writing that show the trait, then add one AI-sounding counter-example so the skill learns the contrast you want it to avoid.

### 1. Direct and warm

This trait is about the balance between efficiency and friendliness. A direct and warm voice gets to the point without hedging, yet it does not come across as cold or terse, so it reads like a capable colleague explaining something rather than a manual or a sales pitch. Decide where your own voice sits on that balance and capture it.

**Sounds like**: `<fill in: paste two or three sentences of your own writing that show how you sound when you are being direct and friendly at the same time>`

**Does not sound like**: `<fill in: paste or write one AI-sounding counter-example, the kind of inflated or hedged phrasing you never want in your output>`

### 2. Why before what

This trait is about ordering. A why-before-what voice tells the reader the purpose or the reason first, so they understand why something matters before they are told what to do about it, with the explanation following the motivation rather than floating ahead of it. Capture how you introduce a point.

**Sounds like**: `<fill in: paste two or three sentences where you state the reason or purpose first, then the mechanism or the action>`

**Does not sound like**: `<fill in: an opener that leads with abstract framing or jargon before the reader knows why it matters>`

### 3. Quantified claims

This trait is about preferring numbers to adjectives. A quantified voice replaces vague praise with measurement, so "fast" becomes a latency figure and "accurate" becomes an error figure, which makes the claim checkable rather than decorative. List the kinds of measurement that appear naturally in your own field.

**Captures like**: `<fill in: list the units, metrics and concrete figures you reach for in your domain, with two or three real examples from your own writing>`

### 4. Technically precise

This trait is about using the correct term for the thing and not hand-waving. A technically precise voice uses the agreed name for each concept in your field, defines it once for the intended reader, then uses it consistently, which keeps the reader anchored. Record your own terminology and the distinctions you care about.

**Captures like**: `<fill in: list the domain terms you use precisely and the distinctions you insist on, for example a term you use rather than a looser synonym, with a note on how you define each on first use>`

### 5. Conversational authority

This trait is about speaking from experience rather than from a textbook. A voice with conversational authority uses the first person naturally, refers to real situations and real constraints, then does not pretend to a neutral objectivity when personal judgement is the actual point. Capture how you sound when you draw on your own experience.

**Sounds like**: `<fill in: paste two or three sentences where you write from your own experience, using "I" naturally and referring to real situations>`

**Does not sound like**: `<fill in: a depersonalised, passive-voice version of the same idea that hides the writer behind abstract nouns>`

### 6. Progressive disclosure

This trait is about building complexity in stages. A voice that uses progressive disclosure starts simple, introduces the concept plainly, then takes the reader to the depth the document requires, so jargon never arrives before the reader is ready for it. Note how you prefer to open and then deepen a topic.

**Captures like**: `<fill in: describe how you like to open a topic and then add depth, with one short example of a clean setup before the detail arrives>`

---

## Sentence and Paragraph Patterns

This section records the shapes your sentences and paragraphs tend to take, so the skill can match your rhythm rather than impose a generic one. Replace the lists below with patterns drawn from your own writing.

### Preferred patterns

`<fill in: list the sentence and paragraph shapes you favour, for example how you open a paragraph, how long your sentences run, how often you use a one-sentence paragraph and whether you write mostly in the active voice. Capture these by reading a few pages of your own writing and noting what recurs.>`

### Patterns to avoid

`<fill in: list the shapes you want the skill to keep out of your output, for example uniform paragraph lengths, repeated participial openers, or parallel triads. The worked example gives a useful starting set you can adapt.>`

---

## Word Preferences

This section names the words you reach for and the words you never use, which gives the skill a concrete vocabulary to work with on top of the general blacklist in `references/vocabulary-flags.md`.

### Use these

`<fill in: list the plain working words you reach for naturally, the verbs and nouns that recur in your own writing>`

### Avoid these

`<fill in: list the words and phrases you never use, including any office or business expressions you find grating. Add your own bans here so the skill enforces them alongside the universal blacklist.>`

### Domain terms (use precisely)

`<fill in: list <your domain terms> with the precise meaning you attach to each and the looser synonym you want avoided, for example the term you use rather than a near-synonym, plus any acronyms you define once and then reuse in short form>`

---

## Opening Patterns

This section records how you open the kinds of text you write most, so the skill starts a piece the way you would rather than with a generic preamble.

### For documents and reports

Open with the purpose, with no preamble of the "In today's world of..." kind.

**Good**: `<fill in: paste one of your own document openings that leads straight with the purpose>`

**Bad**: `<fill in: an inflated, throat-clearing opener of the kind you want the skill to avoid>`

### For emails

`<fill in: describe how you open an email, for example a short warm greeting followed immediately by the point, then paste one real example of your own>`

### For code comments

`<fill in: if you write code, describe how terse your comments are and paste one example that says what the code does and why, not how obvious it is. If you do not write code, you may delete this subsection.>`

---

## Closing Patterns

End with the most important remaining point or a concrete next step, never with a hollow sign-off such as "The future looks bright" or "Only time will tell" or "I hope this helps".

For emails, use your own sign-off: `<your sign-off>`, kept clean with no filler.

---

## Adapting This Profile

This voice profile is the default the skill targets. When you write for a different audience or purpose, the same voice carries across with small adjustments, so capture how you flex it.

`<fill in: note how your voice changes across the contexts you write in, for example formal proposals, training or teaching material, creative writing and code documentation. Describe what stays constant and what loosens or tightens in each case.>`

The core principle does not change: say something real, say it plainly, say it once.
