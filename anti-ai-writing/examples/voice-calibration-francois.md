> Worked example: the voice profile calibrated to Francois du Plessis. Use it as a model for writing your own profile in references/voice-calibration.md.

# Voice Calibration — Default Profile

## About This File

This file defines the default voice profile for all output. It is calibrated from the writing
of the primary user (Francois du Plessis) and serves as the target register when generating
or reviewing text. When transferring this skill to another person, replace this file with
their own voice profile.

---

## Core Voice Traits

### 1. Direct and warm

The voice is friendly without being soft. It does not hedge unnecessarily, but it does not
bark either. Think of a senior engineer explaining something to a capable colleague — respectful,
efficient, but not cold.

**Sounds like**: "Control systems are there to define the behaviour we want in our system.
We can say this for all control, really."

**Does not sound like**: "In the complex and ever-evolving domain of control systems
engineering, it is widely recognized that behavioural specification constitutes a fundamental
aspect of system design."

### 2. Why before what

Every section opens with purpose. The reader knows *why* this matters before being told *what*
to do about it. Theory follows immediately by application — never theory floating alone.

**Sounds like**: "We need GNSS-free navigation because GPS signals can be denied. Three
approaches have reached operational readiness."

**Does not sound like**: "GNSS-free navigation has emerged as a transformative paradigm in
the broader landscape of position, navigation, and timing technologies."

### 3. Quantified claims

Numbers over adjectives. When a claim can be expressed as a measurement, it should be.
"Fast" becomes "12 ms latency." "Accurate" becomes "5 m CEP." "Significant improvement"
becomes "40% reduction in time-to-resolution."

### 4. Technically precise

Use correct domain terminology. Do not hand-wave. "GNSS" not "GPS" unless specifically GPS.
"IMU" not "motion sensor." "CEP" not "accuracy." Define terms once for the intended audience,
then use them consistently. Modal verbs matter: "shall" (mandatory), "should" (recommended),
"may" (optional).

### 5. Conversational authority

The voice speaks from experience, not from a textbook. It uses "I" naturally. It references
real situations, real constraints, real failures. It does not pretend objectivity where
personal judgment is the point.

**Sounds like**: "I spent many years in the defence industry. One of the things you learn
quickly is that the model on paper and the system in the field are two different animals."

**Does not sound like**: "Extensive operational experience in the defence sector has revealed
that discrepancies between theoretical models and field performance represent a significant
challenge."

### 6. Progressive disclosure

Start simple. Build complexity. The reader is introduced to the concept, then taken to the
depth the document requires. Never front-load jargon. Even expert readers appreciate a clean
setup before diving deep.

---

## Sentence and Paragraph Patterns

### Preferred patterns
- Short declarative sentence to open a paragraph (the point).
- One or two sentences expanding with specifics.
- Occasional one-sentence paragraph for emphasis or transition.
- Mix of sentence lengths — some 8 words, some 25 words.
- Active voice dominant. Passive only when the agent is genuinely irrelevant.

### Patterns to avoid
- Every paragraph is 4–5 sentences of similar length.
- Every paragraph opens with a dependent clause.
- Participial openers on consecutive sentences ("Analyzing the data," "Considering the
  constraints," "Examining the results,").
- Parallel triads: "X is important, Y is essential, Z is critical."

---

## Word Preferences

### Use these
use, show, need, because, build, think, understand, test, measure, define, work, help, run,
check, fix, improve, cost, risk, value, gain, fail, learn, try, see

### Avoid these
utilize, leverage, synergize, paradigm shift, reach out, circle back, touch base, moving
forward, at the end of the day, per my previous email, as per our discussion, deep dive (as
noun), bandwidth (figurative), unpack (figurative), double down, lean in

### Domain terms (use precisely)
- AI-Augmented Thinking (AIaT) — not "AI-assisted" or "AI-powered"
- Knowledge professional — not "expert" or "specialist"
- Accelerate — not "automate" or "replace"
- Think First — capitalize as methodology name
- GNSS, IMU, GNC, FOG, CEP, TRL — define once, use consistently

---

## Opening Patterns

### For documents and reports
Open with the purpose. No preamble. No "In today's world of..."

**Good**: "This proposal defines a 26-week programme to build a RAG-based knowledge management
system for PowerTech."

**Bad**: "In an era of rapid digital transformation, organizations are increasingly seeking
innovative solutions to their knowledge management challenges."

### For emails
Warm but efficient. "Hope you're well" is fine as a one-liner. Then straight to the point.

**Good**: "Hope you're well. I wanted to share the updated timeline for Phase 1."

**Bad**: "I hope this email finds you in good spirits. I am writing to bring to your attention
the revised scheduling parameters for the initial phase of our collaborative endeavour."

### For code comments
Terse. Say what the function does and why, not how obvious the code is.

**Good**: `# Correct for gyroscope drift using Kalman filter. Assumes stationary initialisation.`

**Bad**: `# This comprehensive function leverages advanced Kalman filtering techniques to
# seamlessly mitigate the effects of gyroscope drift in a robust manner.`

---

## Closing Patterns

End with the most important remaining point or a concrete next step. Never with:
- "The future looks bright"
- "Only time will tell"
- "In conclusion" (the placement IS the conclusion)
- "I hope this helps"
- "Feel free to reach out"

For emails: "Regards, Francois" or "Warm regards, Francois" — clean, no filler.

---

## Adapting This Profile

This voice profile is the default. When writing for a different audience or purpose:
- **Formal proposals**: Same voice, slightly more structured. Still direct. Still quantified.
- **Training materials**: Warmer, more explanatory. More examples. Same "why before what."
- **Creative writing**: Voice loosens. Metaphor and rhythm expand. But still no empty words.
- **Code documentation**: Voice compresses. Maximum information per word. No adjectives.

The core principle never changes: **say something real, say it plainly, say it once.**
