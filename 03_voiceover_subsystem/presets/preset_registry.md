# DOCUMENTARY KATHAVACHAK NARRATION PRESET REGISTRY

**Purpose:** Reusable voiceover presets for 6–7 minute Hindi documentary episodes with investigative, police-procedural, civic, or historical subject matter.

**Source style analyzed:** User-supplied reference narration in `pasted_content.txt`.

## Reference Style Fingerprint

- **Narrative stance:** First-person retrospective field witness; the narrator has direct operational knowledge and speaks as a former or current officer.
- **Opening architecture:** Philosophical aphorism or moral paradox, followed by a precise place/date anchor and an atmospheric warning.
- **Dramatic sequence:** Moral hook → location/time → antagonist dossier → operational setup → tactical encounter → decisive action → civic/moral afterglow.
- **Language:** Hindi as the emotional base with selective English institutional and operational nouns: Police, Deputy SP, Crime Branch, Electronic Surveillance, Gunner, Driver, Table, Toilet, Photo, Meter.
- **Sentence rhythm:** Short factual sentences during action; longer sensory clauses while building threat; one-line verdicts after violence or revelation.
- **Suspense method:** Delay the reveal, repeat the distance/location, foreground the narrator’s observation, then compress action into a few decisive verbs.
- **Paralinguistic surface:** Inline cues such as `[thoughtful]`, `[serious]`, `[whispers]`, `[short pause]`, `[long pause]`, `[exhales sharply]`, `[chuckles]`, and `[gunshot]`.
- **Silence design:** Ellipses and explicit pauses are used as controlled suspense, not as filler. Use 5–9 timed pauses in a 6.5-minute script.
- **Emotional register:** Restrained authority. Avoid constant shouting; let the narrator sound certain because the facts are strong.
- **Moral landing:** End with a civic principle that widens the incident beyond one arrest or operation.

## Preset Selection

| Preset | Choose when | Primary register | Target pace |
|---|---|---|---:|
| `01_civic_noir_field_witness.md` | The episode needs atmosphere, danger, and a memorable moral close | Dark, reflective, tactical | 82–88 WPM |
| `02_grounded_police_procedural.md` | The episode needs clarity, evidence, process, and audience trust | Direct, factual, controlled | 88–96 WPM |
| `03_accessible_public_memory.md` | The episode must be easy for a broad audience while retaining documentary weight | Simple, warm, suspenseful | 86–92 WPM |

## Runtime Rule for a 6.5-Minute Episode

Target one of two mathematically grounded timing profiles:

- **Slow intimate profile:** approximately **560–575 spoken words at 86–88 WPM**, with pauses calculated separately.
- **Base Style long-form profile:** approximately **650–720 spoken words at 100–110 WPM**, with pauses calculated separately. This profile gives the tactical memoir enough scene oxygen without falsely claiming 6:30 at 86 WPM.

Do not pad with repeated explanation. Add time through intentional breath, scene transition, and silence cues only where the visual edit supports them.

## Mandatory Output Shape

Write the final Creative Master as continuous prose paragraphs, not numbered pointer lines. Preserve paragraph breaks at story turns. Add bracketed delivery cues only when they change performance: `[thoughtful]`, `[serious]`, `[measured]`, `[quietly]`, `[whispers]`, `[short pause]`, `[long pause]`, `[exhales sharply]`, or a specific diegetic event such as `[gunshot]`.

## Mandatory Draft Differentiation

When multiple drafts are requested, generate each draft as a separate creative pass, not as a header change or tag-only transformation. Declare `draft_id`, `primary_preset`, `secondary_influence`, and `textual_transformation` in the output metadata. Compare normalized prose against sibling drafts before PDF export: identical prose is a hard failure, and similarity of `0.82` or higher requires a rewrite unless the user explicitly requested a formatting-only edition. A tagging pass over unchanged prose must be labeled an edition, not a new draft.

## Mandatory Base-Style Gates

- Lock POV to first-person insider (`मैं`, `हम`, `मेरी नज़र`, `हमारी टीम`) when the Canonical Story Bible supports direct operational knowledge; otherwise record why intimate third person is required.
- Build each major beat through hook → forensic place/time anchor → sensory and spatial micro-blocking → cause-and-effect action → consequence/accountability.
- Build and retain a fact inventory before rewriting: named people, locations, numbers, durations, props, ranks, departments, and distinctive descriptors. Do not replace `Arun Shukla`, `Brijesh`, `36 Districts`, `90 Minutes`, or similar anchors with vague substitutes such as `अपराधी`, `कई जिले`, or `कुछ देर`.
- Include exact source-supported distances, times, ranks, objects, posture, and behavior. Never invent a number or prop to imitate texture.
- Keep narrative Hindi in Devanagari but retain source-supported Roman English for ranks, departments, locations, technical terms, modern props, and units when using a Hinglish TTS preset.
- Reject three consecutive sentences of four words or fewer. Noun-list montage is not scene writing.
- Place at least half of all paralinguistic cues inside paragraphs. Never place `[whispers]` immediately before `[gunshot]`; the vocal energy must change before kinetic action.
- For Civic Noir, require approximately 8–12 ellipsis groups and a minimum of 560–575 spoken words for a 6.5-minute script at 86–88 WPM. Count spoken words before printing any duration claim.

Run `presets/draft_integrity_and_style_gate.md` and `scripts/validate_voiceover_draft.py` before compiling a PDF. Rewrite and rerun any failing gate.

## Safety and Accuracy Guardrails

- Preserve source facts, dates, names, ranks, distances, and operational sequence.
- Do not invent a first-person claim unless the canonical story assigns the narrator direct knowledge.
- Keep English code-switching purposeful and intelligible; do not scatter English words for decoration.
- Depict violence briefly and factually. Do not glorify cruelty or turn a death into a punchline.
- End with consequence, accountability, or public meaning rather than a generic motivational slogan.
