# SHOT GRANULARITY ESTIMATOR ALGORITHM (`technical_brain/01_shot_granularity_estimator_algorithm.md`)

## 1. MATHEMATICAL FORMULATION
In cinematic editing and shot coverage, a scene cannot be covered by a single continuous angle unless specifically engineered as an auteur *plan-séquence* (oner). The Ingestor must mathematically calculate the **minimum required shot granularity** for every scene during the ingestion phase so downstream departments never default to generic single-shot coverage.

---

## 2. SHOT COUNT ESTIMATOR EQUATION

The estimated shot count $S_{\text{count}}$ for any scene is calculated as:

$$S_{\text{count}} = S_{\text{base}} + (B_{\text{action}} \times M_{\text{action}}) + (D_{\text{turns}} \times M_{\text{dialogue}}) + P_{\text{thehraav}} + I_{\text{props}}$$

Where:
- $S_{\text{base}} = 2$: Mandatory Scene Master Establishing Shot (EWS/WS) + Final Scene Out-Point / Resolving Cut.
- $B_{\text{action}}$: Total number of physical blocking maneuvers or room threshold transitions.
- $M_{\text{action}} = 2.0$: Each physical maneuver requires coverage (Wide tracking + Close-up of body movement/footfall).
- $D_{\text{turns}}$: Total number of speaker turns in the dialogue stream.
- $M_{\text{dialogue}}$: Dialogue coverage multiplier:
  - Intimate 2-person dramatic scene: $M = 1.25$ (alternating OTS, profile, and reaction cuts).
  - High-conflict 2-person argument: $M = 1.80$ (punchy cuts to close-ups and reaction inserts).
  - Multi-person scene (3+ characters): $M = 2.20$.
- $P_{\text{thehraav}}$: Total number of loaded silence pauses $>1.0\text{s}$ (each generates a dedicated reaction shot or environment cutaway).
- $I_{\text{props}}$: Total number of hero prop interactions (e.g., opening a paan-daan, signing a deed, picking up tea glass). Each requires a dedicated Macro/ECU insert.

---

## 3. WORKED CALCULATION EXAMPLE (SCENE 01)
- $S_{\text{base}} = 2$ (EWS Master + Out-Point Cut)
- $B_{\text{action}} = 2$ (Raghav arrives at threshold; Savitri shifts on chauki) $\rightarrow 2 \times 2 = 4$
- $D_{\text{turns}} = 4$ (4 dialogue exchanges / subtextual vocalizations) $\rightarrow 4 \times 1.25 = 5$
- $P_{\text{thehraav}} = 3$ (Three 1.5s loaded silences with rain drops) $\rightarrow 3$
- $I_{\text{props}} = 4$ (Umbrella tip drip insert, brass thali insert, garlic clove peel ECU, father's photograph cutaway) $\rightarrow 4$

$$\text{Total Pre-Calculated Shots} = 2 + 4 + 5 + 3 + 4 = 18\text{ Shots}$$

This mathematically mandates that `SCN_01` must be broken down into exactly 18 distinct shots (`SHT_01A` through `SHT_01R`) in the downstream Shot Breakdown and Storyboarding files.

---

## 4. INGESTION ENFORCEMENT
If the downstream `02_shot_breakdown_subsystem` submits a scene with fewer shots than the calculated $S_{\text{count}}$, the completeness audit automatically rejects the batch.
