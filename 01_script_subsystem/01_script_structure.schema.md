# SCHEMA 01: MASTER SCREENPLAY & BILINGUAL SCRIPT (`01_script_structure.schema.md`)

Every scene in `01_Script.md` (and compiled `01_Script.pdf`) MUST contain both the **Creative Dramaturgy Header** and the **Formatted Screenplay Block** adhering to the structure below:

```json
{
  "script_scene_unit": {
    "hierarchy": {
      "act_id": "ACT_01 | ACT_02 | ACT_03",
      "sequence_id": "SEQ_01 (Narrative grouping of 2-4 scenes)",
      "scene_id": "SCN_01",
      "page_span_estimate": "e.g., 2.375 pages (2 pages and 3/8ths — standard 8-eighths AD breakdown)",
      "estimated_screen_time_seconds": 142
    },
    "slugline_architecture": {
      "environment_prefix": "INT. | EXT. | INT./EXT. (I/E.)",
      "master_location_name": "SHARMA ANCESTRAL HAVELI",
      "sub_location_zone": "CENTRAL COURTYARD (AANGAN) & NORTHERN VERANDA",
      "location_uuid": "LOC_01",
      "time_and_solar_state": "DUSK (BLUE HOUR TRANSITIONING TO ASTRONOMICAL NIGHT — 18:15 IST)",
      "weather_and_atmospheric_tag": "POST-MONSOON DRIZZLE / 88% HUMIDITY / STILL AIR"
    },
    "creative_dramaturgy_pass": {
      "dominant_rasa": "Karuna (Pathos / Smoldering Grief) shifting to Raudra (Suppressed Fury)",
      "sthayi_bhava": "Shoka (Sorrow anchored in unspoken betrayal)",
      "scene_polarities": {
        "opening_value": "+/- Guarded Formal Politeness",
        "turning_point_beat": "Mother slides the uncashed money orders across the wet stone floor",
        "closing_value": "-- Irreversible Emotional Rupture"
      },
      "thehraav_silence_architecture": "3 distinct loaded silences totaling 19 seconds where environmental Foley replaces spoken dialogue."
    },
    "scene_beats_and_dialogue_stream": [
      {
        "beat_id": "SCN01_BT01",
        "linked_shot_ids": ["ACT1_SCN01_SHT01A", "ACT1_SCN01_SHT01B"],
        "element_type": "ACTION_KINAESTHETIC | DIALOGUE_BLOCK | THEHRAAV_PAUSE | TRANSITION",
        "action_prose": "Strict present-tense visual behavior. Zero internal monologue. Includes exact prop UUIDs [PROP_01] and character blocking coordinates.",
        "character_cue": {
          "character_uuid": "CHAR_02",
          "display_name": "SAVITRI (MAA)",
          "vocal_extension": "NONE | (O.S.) | (V.O.) | (CONT'D) | (OVERLAPPING)",
          "dialect_register": "Purvanchali-inflected Hindi; drops formal pronouns, uses archaic household nouns"
        },
        "parenthetical_micro_direction": "(without looking up; thumb splitting a damp garlic pod; voice flat at -6 dB below room tone)",
        "dialogue_layers": {
          "hindi_devanagari": "छत टपकती थी तो तुम्हारे बाबूजी ने तसला रख दिया था... तुम तो पूरा आँगन ही बेचने का काग़ज़ ले आए।",
          "roman_phonetic_transliteration": "Chhat tapakti thi toh tumhare Babuji ne tasla rakh diya tha... [PAUSE: 1.4s] tum toh poora aangan hi bechne ka kaagaz le aaye.",
          "english_literal_and_subtext": "Literal: 'When the roof leaked, your father placed a basin underneath... you have brought papers to sell the entire courtyard.' | Subtext: 'Your father endured decay to preserve our shelter; you erase us for convenience.'"
        }
      }
    ]
  }
}
```
