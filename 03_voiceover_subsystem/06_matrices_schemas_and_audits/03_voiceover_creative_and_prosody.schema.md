# SCHEMA 03: MASTER VOICEOVER CREATIVE & PROSODY (`03_voiceover_creative_and_prosody.schema.md`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VoiceoverMasterProductionBible",
  "type": "object",
  "required": [
    "voiceover_master_production_bible"
  ],
  "properties": {
    "voiceover_master_production_bible": {
      "type": "object",
      "required": [
        "story_and_genre_routing",
        "narrator_psychological_persona",
        "studio_recording_and_dsp_chain",
        "shot_synced_voiceover_cues"
      ],
      "properties": {
        "story_and_genre_routing": {
          "type": "object",
          "required": [
            "primary_genre_playbook",
            "authorial_emulation_blend",
            "etymological_lexicon_distribution"
          ],
          "properties": {
            "primary_genre_playbook": { "type": "string" },
            "secondary_genre_inflection": { "type": "string" },
            "authorial_emulation_blend": { "type": "object" },
            "etymological_lexicon_distribution": { "type": "object" }
          }
        },
        "narrator_psychological_persona": {
          "type": "object",
          "required": [
            "narrator_id",
            "linked_character_uuid",
            "temporal_vantage_model",
            "reliability_index",
            "vocal_physiology_and_age"
          ]
        },
        "studio_recording_and_dsp_chain": {
          "type": "object",
          "required": [
            "acoustic_room_spec",
            "microphone_and_placement",
            "preamp_and_eq_compression_chain",
            "loudness_and_sidechain_spec"
          ]
        },
        "shot_synced_voiceover_cues": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "vo_cue_id",
              "linked_shot_uid",
              "timecode_in",
              "timecode_out",
              "duration_seconds",
              "creative_writing_decompilation",
              "script_and_phonetic_layers",
              "prosody_and_suprasegmental_math"
            ]
          }
        }
      }
    }
  }
}
```
