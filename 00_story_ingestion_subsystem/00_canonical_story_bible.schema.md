# SCHEMA 00: CANONICAL STORY BIBLE DATA CONTRACT (`00_canonical_story_bible.schema.md`)

The locked canonical state written to `workspace/state/00_canonical_story_bible.md` MUST conform to this strict schema:

```json
{
  "canonical_story_bible": {
    "project_metadata": {
      "title_devanagari": "कहानी का मूल शीर्षक (Original Hindi Title)",
      "title_english": "English Working / Production Title",
      "author_and_source_text": "Original author, publication source, or adaptation credit",
      "genre_and_subgenre": "e.g., Psychological Domestic Drama / Neo-Realist Tragedy",
      "target_format": "Feature Film / Limited Web Series Episodic",
      "estimated_runtime_minutes": 84,
      "state_version": "1.0.0-LOCKED"
    },
    "act_architecture": [
      {
        "act_id": "ACT_01",
        "act_title": "The Threshold of Return",
        "narrative_span": "Arrival of protagonist in ancestral space through realization of entrapment",
        "thematic_polarity_shift": "+/- Formal Politeness to -- Suppressed Bitterness",
        "target_screen_time_seconds": 1260
      }
    ],
    "master_scene_registry": [
      {
        "scene_id": "SCN_01",
        "act_id": "ACT_01",
        "scene_sequence_index": 1,
        "slugline": "INT. SHARMA ANCESTRAL HAVELI - CENTRAL COURTYARD (VARANASI) - DUSK",
        "location_uuid": "LOC_01",
        "time_of_day_state": "BLUE_HOUR_TWILIGHT (18:15 IST)",
        "weather_state": "POST-MONSOON DRIZZLE / 88% HUMIDITY",
        "dominant_rasa": "Karuna (Pathos / Smoldering Grief)",
        "sthayi_bhava": "Shoka (Unspoken betrayal)",
        "dramatic_objective": "Establish moral gulf between modern legal expediency and ancestral permanence",
        "pre_calculated_shot_count": 18,
        "characters_present": ["CHAR_01", "CHAR_02"],
        "hero_props_present": ["PROP_01", "PROP_02", "PROP_04"]
      }
    ],
    "master_shot_index": [
      {
        "shot_uid": "ACT1_SCN01_SHT01A",
        "scene_id": "SCN_01",
        "shot_number": "01A",
        "framing_type": "EWS (Extreme Wide Master)",
        "camera_movement": "Precision Dolly Push-In",
        "focal_length": "50mm Anamorphic",
        "estimated_duration_sec": 6.5
      }
    ],
    "entity_registry": {
      "characters": [
        {
          "character_uuid": "CHAR_01",
          "name_devanagari": "राघव शर्मा",
          "name_roman": "Raghav Sharma",
          "tier": "Protagonist",
          "archetype": "The Prodigal Son / Corporate Advocate",
          "core_wound": "Abandonment of father during final illness"
        }
      ],
      "props": [
        {
          "prop_uuid": "PROP_01",
          "name_bilingual": "पितृ-स्मृति पीतल का पानदान (Father's Ancestral Brass Paan-Daan)",
          "classification": "Hero Action Prop",
          "narrative_symbolism": "Father's preserved dignity and uncashed money orders"
        }
      ],
      "locations": [
        {
          "location_uuid": "LOC_01",
          "name_bilingual": "शर्मा पुश्तैनी हवेली (Sharma Ancestral Haveli - Varanasi)",
          "typology": "Traditional merchant courtyard haveli, late 19th-century Chunar sandstone"
        }
      ]
    }
  }
}
```
