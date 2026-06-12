---
marp: true
theme: default
paginate: true
size: 16:9
header: ''
footer: ''
---

<style>
section {
  font-family: "Helvetica Neue", "Inter", system-ui, sans-serif;
  font-size: 28px;
}
h1 { color: #1a1a1a; }
h2 { color: #2d3748; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.3em; }
code { background: #f4f4f5; padding: 0.1em 0.3em; border-radius: 3px; }
footer, header { color: #718096; }
</style>

# Edge AI for Remote Monitoring

A worked example deck, built by marp-deck from a vault note

June 2026

---

## Why it matters

- Inference runs on site, so latency drops to the device round-trip
- Only results travel upstream, so bandwidth cost falls
- Raw data stays on the device, which improves privacy

---

## Where it fits

- Remote monitoring of equipment, agriculture and infrastructure
- Sites far from reliable networks, where the cloud is not an option
- Limited on-device compute is the trade-off, which caps model size

---

## What to watch

- Model drift is the main risk, so plan a retraining loop
- Power budget constrains solar or battery sites
- A diagram of the data path sits in the source note

---

## References

The skill turns the note's wiki-links into a reference list:

- Bandwidth costs: the upstream data volume and its monthly cost
- Model drift: the slow loss of accuracy as field data shifts
