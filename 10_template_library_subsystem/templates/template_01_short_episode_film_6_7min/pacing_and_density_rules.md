# TEMPLATE 01: PACING & SHOT DENSITY RULES (`pacing_and_density_rules.md`)

## 1. TEMPORAL DENSITY MATHEMATICS
For a 6–7 minute episode film, the cutting rhythm is strictly governed by the **25–27 Cuts / Minute** baseline:

$$\text{Episode Duration} = 390 \text{ seconds (nominal } 6.5 \text{ min)}$$
$$\text{Nominal Shot Budget} = 6.5 \text{ min} \times 26 \text{ cuts/min} = 169 \text{ discrete shots}$$
$$\text{Average Shot Length (ASL)} = \frac{390 \text{ seconds}}{169 \text{ shots}} \approx 2.31 \text{ seconds}$$

---

## 2. SHOT DURATION SPECTRUM & SPREAD
While the overall mathematical average is ~2.3–3.0 seconds, cuts are not mechanical metro-beats. They follow dynamic dramatic distribution:

| Shot Function / Category | Duration Range | Percentage of Total Shots | Dramatic Justification |
| :--- | :--- | :--- | :--- |
| **Micro-Cuts & Inserts (ECU / Reaction)** | **0.8s – 1.8s** | **35%** (~59 shots) | High-speed cognitive intake: ticking clock, trembling fingers, glancing eyes, knife edge, footstep. |
| **Standard Dialogue & Action (MCU / MS)** | **2.0s – 3.2s** | **45%** (~76 shots) | Standard conversational cadence, action execution, physical blocking across the room. |
| **Thematic Thehraav & Master Shots (WS / EWS)** | **3.5s – 5.5s** | **20%** (~34 shots) | Establishing spatial isolation, emotional weight, architectural environment, loaded silences. |

---

## 3. ACT-BY-ACT CUTTING VELOCITY BUDGET

### Act I: The Premise & Instigation (Minutes 0:00 – 1:45)
- **Duration:** 105 seconds (~1.75 min).
- **Cuts Allocation:** 42 – 46 shots.
- **Pacing Rhythm:** Accelerating from a wide, atmospheric 4-second opening establishing shot down to 2-second narrative exposition cuts.

### Act II: The Complication & Pressure Cooker (Minutes 1:45 – 5:00)
- **Duration:** 195 seconds (~3.25 min).
- **Cuts Allocation:** 82 – 90 shots.
- **Pacing Rhythm:** High-density cross-cutting between conflicting characters, 1.5-second reaction inserts, rapid dialogue exchanges alternating with sudden breathless holds.

### Act III: The Climax & Residue (Minutes 5:00 – 6:30 / 7:00)
- **Duration:** 90 – 120 seconds (~1.5 – 2.0 min).
- **Cuts Allocation:** 36 – 45 shots.
- **Pacing Rhythm:** Peak cutting velocity during the climax (1.0s – 1.5s per shot), decelerating dramatically into 4-to-5 second lingering residue shots as the final emotional truth settles.

---

## 4. INVIOLABLE SUB-SYSTEM 00 DERIVATION LAW
When this template is active:
1. `00_story_ingestion_subsystem/technical_brain/01_shot_granularity_estimator_algorithm.md` MUST partition the scenes such that the total sum of `SHT_XX` indices across all scenes falls strictly within **150 to 189 shots**.
2. Zero shots may be omitted or merged. Every shot gets its own discrete sequential identifier (`ACT1_SCN01_SHT01A` through `ACT3_SCN0X_SHTYYZ`).
