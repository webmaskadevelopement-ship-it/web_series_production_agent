# LAW 01: ANTI-TRUNCATION & ZERO GROUPING LAW (`01_anti_truncation_and_zero_grouping_law.md`)

## 1. CORE MANDATE
AI language models naturally default to summarization and grouping after generating large volumes of text. This behavior is fundamentally incompatible with professional cinematic production. In film production, an omission or summarization in a script, shot breakdown, sound cue sheet, or color grade results in production halts, wasted crew hours, and continuity collapse.

Therefore, this law enforces **ABSOLUTE ZERO-TRUNCATION** and **ZERO SHOT GROUPING** across all sub-systems and output files.

---

## 2. STRICTLY PROHIBITED PATTERNS

### A. Grouped Shot Identifiers
The agent is strictly forbidden from compressing multiple cinematic cuts into a single entry or table row.
- **FORBIDDEN:** `"Shots 01A–01D: Coverage of Raghav and Savitri speaking"`
- **FORBIDDEN:** `"SHT_04 to SHT_08: Alternating over-the-shoulder reverse shots"`
- **MANDATORY:** Every single cut, camera angle change, focal length change, or subject reversal MUST receive its own independent, discrete shot record (`SHT_01A`, `SHT_01B`, `SHT_01C`, etc.) with full optical, lighting, blocking, audio, and editorial parameters.

### B. Ellipses and Continuation Placeholders
The agent must never use placeholder indicators that imply continuation without explicit detail.
- **FORBIDDEN:** `"The conversation continues in similar fashion..."`
- **FORBIDDEN:** `"[...Remaining 12 lines of dialogue follow the same tone...]"`
- **FORBIDDEN:** `"Lighting remains consistent with previous shot"`
- **MANDATORY:** Every dialogue line, audio cue, and lighting state must be rendered in full, unabridged text.

### C. Scene Collapsing
A scene described in a narrative prose document cannot be abridged or summarized into a high-level overview.
- **FORBIDDEN:** `"Scene 03: Raghav explores the haveli and reminisces about his childhood."`
- **MANDATORY:** Every action, doorway threshold crossed, tactile contact with walls or props, pause (*Thehraav*), and glance must be broken down beat-by-beat into filmable present-tense actions.

---

## 3. GRANULARITY STANDARDS BY DEPARTMENT

1. **Screenplay (`01_script_subsystem`):**
   - 1 page of screenplay equals approximately 60 seconds of screen time.
   - Every pause of significance (>0.5s) must be explicitly coded as a `THEHRAAV_PAUSE` beat.
   - No unfilmable prose: internal psychological states must be converted into visible, physical behavior and micro-expressions.

2. **Shot Breakdown (`02_shot_breakdown_subsystem`):**
   - Every dramatic beat requires at least 1-3 distinct camera set-ups (Master, Close-Up, Insert, Reaction).
   - A standard 2-minute dramatic scene requires between 12 and 24 individual shots. Any scene breakdown with fewer than 8 shots must be validated against the dramatic pacing law.
   - Every single shot must define all 7 Technical Pillars: Framing/Lens, Sensor/Exposure, Movement, Lighting/Color Temp, Action/Blocking/Micro-expressions, Audio/Foley/Score, and Edit Transition/Pacing.

3. **Voiceover (`03_voiceover_subsystem`):**
   - Every spoken phrase must be logged with millisecond-level timecode spans, words-per-minute (WPM), pitch contour in Hz, and exact respiratory markers (inhale, swallow, glottal pause, vocal fry).

4. **Storyboarding (`04_storyboard_subsystem`):**
   - Exact 1:1 shot parity with the Shot Breakdown. If the Shot Breakdown has 18 shots in Scene 1, the Storyboard file must contain exactly 18 storyboard panel cards (`PANEL_001` through `PANEL_018`).

5. **Color Grading (`05_color_grading_subsystem`):**
   - Master Look specification per scene, followed by per-shot CDL trim offsets for every key shot. Never assume a global LUT without specifying per-shot exposure and balance adjustments.

6. **Audio & Sound Design (`06_sound_design_subsystem`):**
   - Every shot must contain separate stems: Foley handling, cloth rustle, hard diegetic SFX, ambient beds, and musical raga score cues with 3D Atmos Cartesian coordinates (X, Y, Z).

7. **Art Department (`07_character`, `08_prop`, `09_location`):**
   - Every character must have complete psychological, FACS facial unit, Laban effort, and wardrobe textile breakdowns.
   - Every prop must have physical dimensions, PBR shader values, patina chemistry, and a scene-by-scene continuity state ledger.
   - Every location must specify architectural dimensions, surface albedos, practical light fixture coordinates, and RT60 acoustic reverb calculations.

---

## 4. SELF-AUDIT & REJECTION PROTOCOL
Before writing any file to disk, the active Sub-System must run its internal `.audit.md` check:
- If any grouped range (e.g., `01A-01D`) is detected, execution must halt immediately.
- The block must be decompiled into individual constituent records and regenerated in full.
