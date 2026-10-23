# CHARACTER SHEET SYSTEM TEMPLATE (`07_character_sheet_system.template.md`)

This template governs the appending of character dossiers into `workspace/exports/07_Character_Sheet_System.md`:

```markdown
<!-- CHARACTER DOSSIER START: {{CHARACTER_UUID}} -->
# {{CHARACTER_UUID}}: {{CHARACTER_NAME_ROMAN}} ({{CHARACTER_NAME_DEVANAGARI}})
> **Narrative Tier:** {{NARRATIVE_TIER}} | Kinship Terms: {{KINSHIP_TERMS}}  
> **Appears In Scenes:** {{SCENES_APPEARING_LIST}}  

---

## 1. PSYCHOLOGICAL ARCHITECTURE & ENNEAGRAM
- **Core Wound (*The Ghost*):** {{CORE_WOUND}}
- **Internal Lie:** {{INTERNAL_LIE}}
- **Conscious Outer Want:** {{CONSCIOUS_WANT}}
- **Unconscious Inner Need:** {{UNCONSCIOUS_NEED}}
- **Archetype & Enneagram:** {{ENNEAGRAM_AND_JUNGIAN_PROFILE}}
- **Defense Mechanisms:** {{DEFENSE_MECHANISMS}}

---

## 2. SOCIOCULTURAL HABITUS & DIALECT IDIOLECT
- **Class, Caste & Migration Trajectory:** {{SOCIOCULTURAL_TRAJECTORY}}
- **Baseline Speech Register:** {{BASELINE_SPEECH_REGISTER}}
- **Stress-Induced Regression Cadence:** {{STRESS_REGRESSION_CADENCE}}

---

## 3. PHYSICAL ANTHROPOMETRY & DERMATOLOGY
- **Chronological / Biological Age:** {{CHRONOLOGICAL_AGE}} / {{BIOLOGICAL_APPARENT_AGE}} years
- **Height, Mass & Somatotype:** {{HEIGHT_MASS_SOMATOTYPE}}
- **Craniofacial Geometry:** {{CRANIOFACIAL_GEOMETRY}}
- **Fitzpatrick Skin Classification:** {{FITZPATRICK_SCALE_TYPE}} (Base Hex: `{{BASE_SKIN_HEX}}`)
- **Hair & Stubble:** {{HAIR_AND_STUBBLE_PROFILE}}
- **Ocular Metrics:** {{OCULAR_PROFILE}} (Resting Blink: {{RESTING_BLINK_RATE}} bpm)

---

## 4. PAUL EKMAN FACS MICRO-EXPRESSION LEXICON
- **Baseline Resting Mask:** `{{BASELINE_FACS_RESTING}}`
- **Suppressed Guilt Trigger:** `{{SUPPRESSED_GUILT_FACS}}`
- **Defensive Irritation / Rage Trigger:** `{{DEFENSIVE_RAGE_FACS}}`

---

## 5. RUDOLF LABAN BESS MOVEMENT & BLOCKING PROFILE
- **Body Initiation:** {{BODY_INITIATION_ZONE}}
- **Dominant Effort Drive:** {{DOMINANT_EFFORT_DRIVE}}
- **Kinesphere & Proxemic Habits:** {{KINESPHERE_AND_PROXEMICS}}
- **Gait & Footfall:** {{GAIT_AND_FOOTFALL}}

---

## 6. WARDROBE, COSTUME & TEXTILE SPECIFICATION
- **Garment 01 (Torso):** {{GARMENT_01_SPEC}}
- **Garment 02 (Lower):** {{GARMENT_02_SPEC}}
- **Footwear & Accessories:** {{FOOTWEAR_ACCESSORIES_SPEC}}
- **Costume Palette Hex:** `{{COSTUME_PALETTE_HEX_LIST}}`

---

## 7. MULTI-ANGLE AI CONSISTENCY PROMPTS & MACHINE JSON
```text
{{AI_CHARACTER_CONSISTENCY_ANCHOR_PROMPT}}
```

```json
{{COMPILED_CHARACTER_MASTER_DOSSIER_JSON}}
```
<!-- CHARACTER DOSSIER END: {{CHARACTER_UUID}} -->
```
