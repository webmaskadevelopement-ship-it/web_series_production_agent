# TEMPLATE 03: EPISODIC TV DRAMA (30 MINUTES) — MANIFEST (`manifest.md`)

```json
{
  "template_id": "T03_EPISODIC_TV_30MIN",
  "template_name": "Episodic TV Drama (26-30 Minutes)",
  "format_classification": "episodic_series",
  "target_duration": {
    "min_minutes": 26.0,
    "max_minutes": 30.0,
    "target_minutes": 28.0,
    "total_seconds": 1680
  },
  "shot_density": {
    "cuts_per_minute_min": 14,
    "cuts_per_minute_max": 18,
    "average_shot_length_seconds": 3.8,
    "total_shots_budget": {
      "min_shots": 380,
      "max_shots": 540,
      "target_nominal_shots": 450
    }
  },
  "script_budget": {
    "target_pages": "26 to 30 pages",
    "page_timing_standard": "Industry 1 page = 1 minute standard; 3 to 4 Act TV act breaks"
  },
  "sub_asks_support": {
    "creative_master_edition": {
      "enabled": true,
      "script_format": "Full episodic screenplay with commercial act breaks",
      "shot_breakdown_format": "10-Column Master Production Table ONLY",
      "voiceover_format": "Episodic narrative prose VO"
    },
    "technical_master_edition": {
      "enabled": true,
      "full_drop_down_options": [
        "Episodic_A_B_C_storyline_intercut_matrices",
        "Broadcast_safe_color_and_loudness_standards",
        "Full_7_1_4_atmos_broadcast_deliverables"
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
