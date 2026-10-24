# DRAFT INTEGRITY & BASE-STYLE QUALITY GATE

Use this gate before compiling any 6–7 minute Creative Master voiceover PDF.

## 1. Distinct-Draft Contract

Every requested draft must declare a `draft_id`, `primary_preset`, `secondary_influence`, and `textual_transformation`. A title change, extra tags, or a header change does not count as a new creative draft.

- `Plain Hindi` must simplify vocabulary and syntax.
- `Polished Prose` must improve cadence, imagery, and paragraph transitions.
- `Preset Draft` must change voice architecture, POV, sensory geometry, and cue placement according to the selected preset.
- A technical/tagging pass over unchanged prose must be labeled an edition, not a new draft.

Reject a draft when normalized prose is identical to any sibling draft. Also reject when normalized character similarity is above `0.82` unless the request explicitly asks for a formatting-only edition. Record the similarity score in the audit report.

## 2. Runtime Gate

Do not print a duration header until the body has been counted. Use the declared spoken-word rate:

```text
target_words = target_minutes × target_wpm
allowed_words = target_words ± 4%
projected_seconds = spoken_word_count / target_wpm × 60 + pause_budget_seconds
```

For a 6 minute 30 second Hindi voiceover at 86–88 WPM, target approximately **560–575 spoken words**, then calculate pauses separately. For the longer Base Style / tactical-memoir profile requested in the critique, target **650–720 spoken words at a declared 100–110 WPM** and calculate pauses separately; do not claim 6:30 at 86 WPM with 650–720 words. Performance tags do not count as spoken words. A 375-word body must fail, regardless of the header claim.

## 3. POV and Immersion Gate

Default to first-person insider perspective (`मैं`, `हम`, `मेरी नज़र`, `हमारी टीम`) when the canonical story assigns direct operational knowledge. If the canon does not support first person, use intimate room-level third person and record the exception in metadata. Reject helicopter summaries that compress a major encounter into one or two factual sentences.

## 4. Five-Step Scene Geometry

Every major beat must contain, where the Canonical Story Bible supports it:

1. A philosophical or civic hook.

1. A hard place/time/weather anchor.

1. Two sensory or physical details.

1. Spatial micro-blocking: distance, direction, posture, object, or hand position.

1. A cause-and-effect action beat followed by consequence or accountability.

Never invent numbers, distances, props, ranks, or operational facts. Use exact source values in Arabic numerals with Roman English units when canonically available.

Before rewriting, create a `fact_inventory` from the Canonical Story Bible: named people, ranks, locations, dates, counts, distances, durations, props, departments, and distinctive descriptors. A creative rewrite may reorder or expand these facts, but may not silently replace them with vague substitutes such as `एक अपराधी`, `कई जिले`, or `कुछ देर`. If a fact is intentionally omitted, record the reason in the audit metadata.

## 5. Sentence Cadence Gate

Ban trailer-montage staccato. Do not chain three or more consecutive sentences of four words or fewer. Do not use noun lists as a substitute for scene writing. Prefer multi-clause sentences joined by commas, ellipses, or em dashes, then land on a short decisive sentence only at a true beat ending.

## 6. Hinglish TTS Hygiene

Keep narrative verbs, connectors, and emotional reflection in natural Devanagari Hindi. Keep canonical English ranks, departments, locations, technical terms, modern props, and measurement units in Roman script when that matches the selected preset. Examples: `SSP`, `DGP`, `CM`, `Crime Branch`, `Electronic Surveillance`, `Wireless`, `Jeep`, `Bonnet`, `Logbook`, `10 Meter`.

Do not transliterate operational English into robotic Devanagari forms such as `एसएसपी`, `डीजीपी`, `ई-सर्विलांस`, `जीप`, or `बोनट` in Hinglish presets.

## 7. Punctuation and Cue Gate

For Civic Noir, use approximately 8–12 ellipsis groups and occasional em dashes as breath architecture. Use exclamation marks only for kinetic violence or a genuine shock.

Use approved cues only: `[thoughtful]`, `[serious]`, `[annoyed]`, `[excited]`, `[measured]`, `[quietly]`, `[whispers]`, `[clears throat]`, `[inhales deeply]`, `[exhales sharply]`, `[chuckles]`, `[sighs]`, `[short pause]`, `[long pause]`, `[gunshot]`.

At least half of all cues must occur inside paragraphs, between clauses or sentences. Never put every mood tag at paragraph index zero. Do not place `[whispers]` immediately before `[gunshot]`; change energy before the shot. Cue psychology must match the beat.

Never place a mood or SFX cue after the final sentence of a paragraph as an afterthought. A cue must govern the words that follow it or mark the exact action at which it occurs. `[gunshot]` must appear at the firing beat, never after a completed philosophical sentence.

## 8. Pre-PDF Certification

Before PDF compilation, report:

- `draft_id`, preset, and transformation

- spoken word count and target WPM

- projected speech time and pause budget

- normalized similarity against sibling drafts

- POV result

- short-sentence streak result

- ellipsis count for noir presets

- Roman-English hygiene result

- mid-paragraph cue ratio

- scene-geometry coverage

- canonical fact-inventory retention and any approved omissions

- end-of-paragraph / retroactive cue scan

- PDF Unicode extraction scan when a PDF is delivered

If any hard gate fails, rewrite the failing paragraphs and rerun the audit. Do not deliver a PDF with a duration header that the body cannot support.
