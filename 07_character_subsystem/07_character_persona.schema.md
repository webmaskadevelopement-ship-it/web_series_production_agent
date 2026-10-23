# SCHEMA 07: CHARACTER SHEET & PERSONA SYSTEM (`07_character_persona.schema.md`)

*(Integrates Jungian psychology, Paul Ekman’s FACS Action Units, Rudolf Laban’s BESS Movement Analysis, Fitzpatrick dermatology, and Costume Textile Science)*

Every Character in `07_Character_Sheet_System.md` MUST be decompiled across 7 exhaustive modules:

```json
{
  "character_master_dossier": {
    "identity_metadata": {
      "character_uuid": "CHAR_01",
      "full_name_devanagari": "राघव शर्मा (Raghav Sharma)",
      "nicknames_and_kinship_terms": "Called 'Babu' by old haveli caretaker; addressed without a name (using indirect 'तुम') by his mother Savitri",
      "narrative_tier": "Primary Protagonist / Antagonistic Catalyst in Act 1",
      "scenes_appearing": ["SCN_01", "SCN_02", "SCN_04", "SCN_05", "SCN_07", "SCN_09", "SCN_10"]
    },
    "psychological_architecture": {
      "core_wound_the_ghost": "Six years ago, during the monsoon floods, he refused to return from Delhi for his father's final week of paralysis because of a Senior High Court elevation interview.",
      "the_internal_lie": "Believes that financial settlement and moving his mother to a modern Noida apartment can erase moral abandonment.",
      "conscious_outer_want": "Obtain Savitri's thumbprint/signature on the Partition & Sale Deed before the Monday morning train.",
      "unconscious_inner_need": "To drop his legal armor, weep at his father's empty cot, and accept his mother's judgment.",
      "enneagram_and_jungian_profile": "Enneagram Type 3w4 (The Professional / Achiever disintegrating to Type 9 paralysis under guilt) | Jungian Persona: The Rational Advocate | Shadow: The Cowardly Son.",
      "cognitive_defense_mechanisms": "Intellectualization, switching to formal Sanskritized/English legal vocabulary whenever emotional intimacy threatens him, obsessive checking of his wristwatch."
    },
    "indian_sociocultural_habitus": {
      "caste_class_and_migration_trajectory": "First-generation metropolitan migrant from a declining Varanasi Brahmin scholarly family; caught between Lutyens' Delhi corporate polish and Purvanchali domestic orthodoxy.",
      "linguistic_idiolect": {
        "baseline_speech": "Crisp Delhi-standard Khari Boli Hindi mixed with English legal nouns ('mutation', 'registry', 'valuation').",
        "stress_regression": "Under emotional breakdown in Act 3, his syntax fractures back into childhood Banarasi/Awadhi cadence ('हमसे नाही हो पाई अम्मा')."
      }
    },
    "physical_anthropometry_and_biology": {
      "chronological_age": 34,
      "biological_apparent_age": "38 (prematurely aged by chronic cortisol, 4 hours/night sleep, and metropolitan smog)",
      "height_mass_and_somatotype": "178 cm (5'10\"), 68 kg, lean ectomorph with slight cervical forward-head posture (12° kyphotic tilt from years over case files)",
      "craniofacial_geometry": "Dolichocephalic (long, narrow face), prominent zygomatic arches, slightly asymmetrical nasal bridge, deep infraorbital tear troughs",
      "dermatology_and_fitzpatrick_scale": "Fitzpatrick Type IV — Warm olive-wheatish undertone (#C68B59 base, #8C583A shadow contour); visible pores on nasal bridge; high specular sweat sheen in 85% humidity",
      "hair_and_facial_hair": "Jet-black wavy hair with 10% premature silver temples, parted on left, flattened at crown by monsoon dampness; 4-day uneven stubble (0.8mm length)",
      "ocular_profile": "Deep-set dark brown irises (#2A1B12); scleral micro-capillaries slightly reddened from overnight train travel; resting blink rate: 22 blinks/min (spikes to 38 blinks/min when lying)"
    },
    "facs_micro_expression_lexicon": {
      "baseline_resting_mask": "AU12 (Lip Corner Puller - unilateral left trace, polite lawyer facade) + AU24 (Lip Pressor - Intensity B)",
      "suppressed_guilt_trigger": "AU1+AU4 (Inner Brow Raiser + Brow Lowerer oblique grief triangle) + AU15 (Lip Corner Depressor) + AU54 (Head Down 8°) + gaze aversion down-left (AU61+AU64)",
      "defensive_irritation_trigger": "AU4 (Brow Lowerer - Intensity C) + AU7 (Lid Tightener) + AU23 (Lip Tightener) + masseter jaw clench (AU31)"
    },
    "laban_bess_movement_and_blocking_profile": {
      "body_initiation": "Moves from upper sternum and fingertips; pelvis and lower spine remain rigid and locked.",
      "dominant_effort_drive": "Press (Direct Space + Sustained Time + Heavy Weight + Bound Flow) when speaking to subordinates; shifts to Wring (Indirect Space + Sustained Time + Heavy Weight + Bound Flow) inside the haveli.",
      "kinesphere_and_proxemics": "Narrow Near-Reach Kinesphere (keeps elbows within 15cm of ribcage); maintains >2.5m Social-Consultative distance from his mother in Act 1.",
      "gait_and_footfall": "Heel-strike dominant urban stride (112 steps/min) that falters into tentative toe-testing steps on wet mossy courtyard stones."
    },
    "wardrobe_costume_and_textile_system": {
      "act_01_costume_spec": {
        "garment_01_shirt": "Off-white 100% linen button-down shirt (145 GSM plain weave, semi-translucent where rain-soaked across clavicles and shoulder blades; sleeves rolled unevenly to mid-forearm).",
        "garment_02_trousers": "Charcoal grey merino-poly blend tailored trousers (240 GSM twill weave; bottom 8cm of cuffs darkened by capillary absorption of wet Varanasi alley mud).",
        "footwear_and_accessories": "Black Goodyear-welted Oxford leather shoes (left outside threshold in SCN_01, exposing damp grey ribbed cotton socks); Father's vintage 1984 silver HMT Janata mechanical watch on left wrist (strap leather cracked at third hole)."
      },
      "costume_color_palette_hex": ["#EAE6DF", "#2B2D2F", "#4A433B", "#8C9296"],
      "ai_character_consistency_anchor": "34-year-old lean Indian man named Raghav, 178cm, narrow angular face, deep dark circles under dark brown eyes, 4-day patchy black-and-silver stubble, damp black hair parted on left, wearing rain-dampened off-white linen shirt with rolled sleeves and dark charcoal trousers with muddy hems, vintage silver HMT wristwatch on left wrist, photorealistic 35mm cinema portrait"
    }
  }
}
```
