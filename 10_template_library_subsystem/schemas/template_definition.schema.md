# SCHEMA 10: TEMPLATE DEFINITION SCHEMA (`template_definition.schema.md`)

This schema establishes the strict JSON contract for defining any production template within the Autonomous Studio System.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ProductionTemplateDefinition",
  "type": "object",
  "required": [
    "template_id",
    "template_name",
    "format_classification",
    "temporal_specifications",
    "shot_density_specifications",
    "script_page_budget",
    "creative_master_specifications",
    "technical_master_specifications",
    "hierarchical_directory_specifications"
  ],
  "properties": {
    "template_id": {
      "type": "string",
      "pattern": "^T[0-9]{2}_[A-Z0-9_]+$",
      "example": "T01_SHORT_EPISODE_6_7MIN"
    },
    "template_name": {
      "type": "string",
      "example": "Short Episode Film (6-7 Minutes)"
    },
    "format_classification": {
      "type": "string",
      "enum": ["short_film", "social_micro", "episodic_series", "feature_film", "hybrid"]
    },
    "temporal_specifications": {
      "type": "object",
      "required": ["min_duration_seconds", "max_duration_seconds", "target_duration_seconds"],
      "properties": {
        "min_duration_seconds": { "type": "number", "example": 360 },
        "max_duration_seconds": { "type": "number", "example": 420 },
        "target_duration_seconds": { "type": "number", "example": 390 }
      }
    },
    "shot_density_specifications": {
      "type": "object",
      "required": ["min_cuts_per_minute", "max_cuts_per_minute", "target_average_shot_length_seconds", "expected_total_shots_range"],
      "properties": {
        "min_cuts_per_minute": { "type": "number", "example": 25 },
        "max_cuts_per_minute": { "type": "number", "example": 27 },
        "target_average_shot_length_seconds": { "type": "number", "example": 2.8 },
        "expected_total_shots_range": {
          "type": "object",
          "properties": {
            "min_shots": { "type": "integer", "example": 150 },
            "max_shots": { "type": "integer", "example": 189 }
          }
        }
      }
    },
    "script_page_budget": {
      "type": "object",
      "required": ["target_page_count_min", "target_page_count_max", "page_to_minute_ratio"],
      "properties": {
        "target_page_count_min": { "type": "integer", "example": 6 },
        "target_page_count_max": { "type": "integer", "example": 7 },
        "page_to_minute_ratio": { "type": "string", "example": "1 page = 1.0 minute standard screen time" }
      }
    },
    "creative_master_specifications": {
      "type": "object",
      "required": ["script_mode", "shot_breakdown_mode", "voiceover_mode", "exclude_technical_blocks"],
      "properties": {
        "script_mode": { "type": "string", "example": "Pure dramatic dialogue and visual action without technical metadata" },
        "shot_breakdown_mode": { "type": "string", "example": "10-Column Master Production Table ONLY, zero technical JSON blocks" },
        "voiceover_mode": { "type": "string", "example": "Plain prose voiceover script without DSP signal chains or frequency tables" },
        "exclude_technical_blocks": { "type": "boolean", "example": true }
      }
    },
    "technical_master_specifications": {
      "type": "object",
      "required": ["enable_full_optical_decompilation", "enable_facs_action_units", "enable_aces_color_trees", "enable_atmos_panning_stems"],
      "properties": {
        "enable_full_optical_decompilation": { "type": "boolean", "example": true },
        "enable_facs_action_units": { "type": "boolean", "example": true },
        "enable_aces_color_trees": { "type": "boolean", "example": true },
        "enable_atmos_panning_stems": { "type": "boolean", "example": true }
      }
    },
    "hierarchical_directory_specifications": {
      "type": "object",
      "required": ["base_project_directory", "creative_suite_path", "technical_suite_path", "canonical_state_path", "audit_log_path"],
      "properties": {
        "base_project_directory": { "type": "string", "example": "workspace/projects/{PROJECT_SCRIPT_TITLE}/" },
        "creative_suite_path": { "type": "string", "example": "workspace/projects/{PROJECT_SCRIPT_TITLE}/01_Creative_Master_Suite/" },
        "technical_suite_path": { "type": "string", "example": "workspace/projects/{PROJECT_SCRIPT_TITLE}/02_Technical_Master_Suite/" },
        "canonical_state_path": { "type": "string", "example": "workspace/projects/{PROJECT_SCRIPT_TITLE}/00_Project_Bible_and_Canonical_State/" },
        "audit_log_path": { "type": "string", "example": "workspace/projects/{PROJECT_SCRIPT_TITLE}/03_Production_Logs_and_Audits/" }
      }
    }
  }
}
```
