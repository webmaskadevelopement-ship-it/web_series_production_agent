# TEMPLATE 01: SHORT EPISODE FILM (6–7 MINUTES) — MANIFEST (`manifest.md`)

```json
{
  "template_id": "T01_SHORT_EPISODE_6_7MIN",
  "template_name": "Short Episode Film (6-7 Minutes)",
  "format_classification": "short_film",
  "target_duration": {
    "min_minutes": 6.0,
    "max_minutes": 7.0,
    "target_minutes": 6.5,
    "total_seconds": 390
  },
  "shot_density": {
    "cuts_per_minute_min": 25,
    "cuts_per_minute_max": 27,
    "average_shot_length_seconds": 2.8,
    "total_shots_budget": {
      "min_shots": 150,
      "max_shots": 189,
      "target_nominal_shots": 168
    }
  },
  "script_budget": {
    "target_pages": "6 to 7 pages",
    "page_timing_standard": "1 page = ~55-60 seconds of screen action",
    "devanagari_density": "Industry standard 55-character line margins"
  },
  "sub_asks_support": {
    "creative_master_edition": {
      "enabled": true,
      "script_format": "Clean prose screenplay without camera metadata",
      "shot_breakdown_format": "10-Column Master Production Table ONLY (zero technical JSON)",
      "voiceover_format": "Plain prose voiceover script without DSP signal chains"
    },
    "technical_master_edition": {
      "enabled": true,
      "full_drop_down_options": [
        "Cooke_i_lens_optical_aberration_blocks",
        "IRE_exposure_and_photometric_tables",
        "FACS_action_unit_muscular_matrices",
        "Laban_movement_effort_descriptors",
        "ACES_12_node_resolve_color_trees",
        "Dolby_Atmos_7_1_4_stem_routing",
        "PBR_patina_chemistry_physics"
      ]
    }
  },
  "workspace_paths": {
    "canonical_bible": "workspace/projects/{PROJECT_SCRIPT_TITLE}/00_Project_Bible_and_Canonical_State/00_canonical_story_bible.md",
    "creative_suite": "workspace/projects/{PROJECT_SCRIPT_TITLE}/01_Creative_Master_Suite/",
    "technical_suite": "workspace/projects/{PROJECT_SCRIPT_TITLE}/02_Technical_Master_Suite/",
    "audits": "workspace/projects/{PROJECT_SCRIPT_TITLE}/03_Production_Logs_and_Audits/"
  }
}
```

---

## SPECIFICATION SUMMARY
- **Format:** High-velocity narrative short episode (e.g., anthology segment, premium web series episode, tight festival drama).
- **Duration:** 6 minutes 00 seconds to 7 minutes 00 seconds.
- **Cutting Cadence:** 25 to 27 shots per minute.
- **Shot Duration Math:** Every shot averages between 2.2 and 3.5 seconds, creating an energetic cinematic cadence that balances visual dynamism with emotional *Thehraav* (deliberate dramatic beats).
- **Total Discrete Shots:** Exactly 150 to 189 shots, pre-indexed in `00_canonical_story_bible.md`.
