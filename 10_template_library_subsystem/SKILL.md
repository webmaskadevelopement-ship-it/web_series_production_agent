---
name: template-library-and-pacing-subsystem
version: 1.0.0
description: >
  Master Template Library & Pacing Engine governing project formats, temporal constraints,
  shot density benchmarks (e.g., 25-27 shots/min, ~3s average), and dual-mode rendering
  (Creative Master vs Technical File Master).
---

# SUB-SYSTEM 10: PRODUCTION TEMPLATE LIBRARY & PACING SUBSYSTEM (`SKILL.md`)

## 1. MISSION & SCOPE
The Template Library Subsystem provides standardized, calibrated production templates that define the temporal geometry, shot density, script page budgeting, and deliverable rendering modes for any film project.

It answers the critical physical production question:
**"What kind of film format are we making, what is its shot frequency, and how should deliverables be packaged for stakeholders?"**

---

## 2. CORE RESPONSIBILITIES
1. **Format Calibration:** Enforce duration limits (e.g., 6–7 minutes, 60 seconds, 30 minutes).
2. **Shot Density & Pacing Control:** Calculate and enforce shot velocity:
   - For Template 1 (Short Episode Film): **25–27 cuts per minute**, with an average duration of **~2.2 to 3.5 seconds per shot** ($\approx$ 150–189 total discrete shots for a 6–7 min episode).
3. **Dual-Mode Deliverable Packaging (Creative vs. Technical):**
   - **Technical File Master:** Full engineering dropdown across all 9 departments (Cooke/ARRI optical tables, FACS units, ACES nodes, 7.1.4 Atmos).
   - **Creative Master (Executive/Client Shareable Edition):**
     - Script budgeted to exact target pages without technical jargon.
     - Shot Breakdown with **10-column master tables ONLY** (zero technical JSON blocks).
     - Clean, performable **Plain Prose Voiceover Script** without DSP signal chains or frequency tables.
4. **Project Directory Routing:** Directs output generation into structured hierarchical folders under `workspace/projects/{PROJECT_SCRIPT_TITLE}/`.

---

## 3. SUBSYSTEM ARCHITECTURE
```
10_template_library_subsystem/
├── SKILL.md                                               # This Orchestrator
├── template_registry.md                                   # Global catalog of all available production templates
├── schemas/
│   └── template_definition.schema.md                     # Data contract governing template parameters
└── templates/
    ├── template_01_short_episode_film_6_7min/             # Master 6-7 min Short Episode Film
    │   ├── manifest.md                                    # Core parameters & duration boundaries
    │   ├── pacing_and_density_rules.md                    # 25-27 shots/min, 3s shot math, beat timing
    │   ├── creative_master_spec.md                        # Script page budgeting, 10-col tables, prose VO
    │   └── technical_master_spec.md                       # Full technical engineering drop-down
    ├── template_02_social_micro_short_60s/                # 60s Social Micro-Short
    │   └── manifest.md                                    # 30-40 shots, 1.5-2s cuts, mobile-first
    └── template_03_episodic_tv_30min/                     # 30 min TV/Streaming Episode
        └── manifest.md                                    # 400-500 shots, 3-act broadcast structure
```

---

## 4. TEMPLATE EXECUTION PIPELINE
1. **User Gate Ingestion:** After Sub-System 00 parses the canonical story bible, the user selects a Template (`T1`, `T2`, `T3`, or `T0`).
2. **Constraint Propagation:** The selected template's pacing rules and density formulas are passed into `00_story_ingestion_subsystem/technical_brain/01_shot_granularity_estimator_algorithm.md` to establish the exact shot index.
3. **Dual-Mode Filtration:** When the user selects Creative Master (`M1`) or Technical Master (`M2`), the rendering engines format and route deliverables accordingly.
