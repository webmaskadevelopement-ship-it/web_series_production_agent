# SCHEMA 08: PROP LIST, PBR MATERIAL PHYSICS & CONTINUITY SYSTEM (`08_prop_continuity.schema.md`)

Every Prop in `08_Prop_List_System.md` MUST be cataloged with its **Physical/PBR Properties**, **Acoustic Foley Signature**, **Cultural Backstory**, and **Shot-by-Shot Continuity Ledger**:

```json
{
  "prop_master_entry": {
    "prop_uuid": "PROP_01",
    "prop_name_bilingual": "पितृ-स्मृति पीतल का पानदान (Father's Ancestral Moradabad Brass Paan-Daan)",
    "classification": "Hero Action Prop (Category A — Requires 3 identical production duplicates: 1 Hero Macro, 1 Stunt/Drop, 1 Clean Flashback)",
    "linked_characters": ["CHAR_02 (Primary custodian)", "CHAR_01 (Inheritor in Act 3)"],
    "physical_and_pbr_specifications": {
      "geometry_and_dimensions": "Octagonal domed casket: 185mm diameter x 92mm height; wall thickness 1.8mm; internal 5-compartment removable tray",
      "mass_grams": 680,
      "primary_material": "65/35 CuZn yellow Moradabad hand-engraved brass (`Chikan` floral relief)",
      "pbr_shader_parameters": {
        "base_color_hex": "#B58938 (Polished high-points) / #3B4D3E (Recessed verdigris crevices)",
        "metallic": 0.88,
        "specular_roughness": "0.32 on worn thumb-latch; 0.78 inside oxidized floral grooves",
        "index_of_refraction_ior": "2.45 (Tarnished brass oxide film)"
      },
      "patina_and_aging_chemistry": "40 years of continuous domestic handling: red slaked-lime (`Katha/Chuna`) stain crust inside hinge; green copper carbonate verdigris inside recessed floral etchings; mirror-burnished wear patch on the top lid knob from thousands of thumb presses."
    },
    "acoustic_foley_profile": {
      "latch_release_transient": "Sharp metallic brass hasp 'clink' peaking at 3.8 kHz with a 180ms hollow dome resonance at 620 Hz.",
      "surface_contact_sound": "Heavy gritty scrape when slid across unpolished Chunar sandstone (`800 Hz – 2.1 kHz`)."
    },
    "narrative_dramaturgy": "Represents the late father's daily ritual; Savitri keeps the uncashed postal money orders folded inside its bottom compartment instead of betel leaves.",
    "act_scene_shot_continuity_matrix": [
      {
        "scene_id": "SCN_01",
        "shots_visible": ["01A", "01D", "01G"],
        "spatial_coordinates": "Sitting closed in the sandstone wall niche (`Taak`) 40cm behind Savitri's right shoulder (`X:+1.6m, Y:+0.45m, Z:4.5m`).",
        "physical_state": "Latch closed; dry; thin film of lime-plaster dust on upper dome; lit by 2200K diya edge-light."
      },
      {
        "scene_id": "SCN_04",
        "shots_visible": ["04B", "04C (100mm Macro ECU)", "04F"],
        "spatial_coordinates": "Placed on the wet courtyard stone between Savitri and Raghav (`X:0.0m, Y:0.0m, Z:2.1m`).",
        "physical_state": "Lid flipped open 110° to the left; top tray removed and resting at 4 o'clock; 14 yellowed Indian Post Money Order receipts visible inside base."
      }
    ]
  }
}
```
