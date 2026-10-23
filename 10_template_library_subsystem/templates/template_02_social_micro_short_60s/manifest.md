# TEMPLATE 02: SOCIAL MICRO-SHORT (60 SECONDS) — MANIFEST (`manifest.md`)

```json
{
  "template_id": "T02_SOCIAL_MICRO_SHORT_60S",
  "template_name": "Social Micro-Short (60 Seconds)",
  "format_classification": "social_micro",
  "target_duration": {
    "min_minutes": 1.0,
    "max_minutes": 1.25,
    "target_minutes": 1.0,
    "total_seconds": 60
  },
  "shot_density": {
    "cuts_per_minute_min": 30,
    "cuts_per_minute_max": 40,
    "average_shot_length_seconds": 1.6,
    "total_shots_budget": {
      "min_shots": 30,
      "max_shots": 45,
      "target_nominal_shots": 36
    }
  },
  "script_budget": {
    "target_pages": "1 to 1.5 pages",
    "page_timing_standard": "Rapid visual delivery; 9:16 vertical priority"
  },
  "sub_asks_support": {
    "creative_master_edition": {
      "enabled": true,
      "script_format": "Punchy vertical micro-script",
      "shot_breakdown_format": "10-Column Master Production Table ONLY",
      "voiceover_format": "Rapid hook-driven prose VO"
    },
    "technical_master_edition": {
      "enabled": true,
      "full_drop_down_options": [
        "Vertical_9_16_sensor_reframe_matrices",
        "Fast_shutter_180_degree_clarity_specs",
        "High_clarity_vocal_presence_DSP"
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
