# LAW 05: CROSS-DEPARTMENT UUID CONTINUITY LAW (`05_cross_department_uuid_continuity_law.md`)

## 1. THE PROBLEM OF DISCONNECTED SUB-SYSTEMS
When separate departments or sub-skills operate independently, hallucination and continuity drift inevitably occur:
- The Screenwriter describes a "blue kurta";
- The Character Sheet describes an "off-white linen shirt";
- The Shot Breakdown frames a "silver tea glass";
- The Prop Master catalogs a "brass paan-daan";
- The Colorist assumes a daylight exterior while the Sound Designer mixes night crickets.

To eliminate continuity errors across all 9 production departments, this law establishes **IMMUTABLE ENTITY UUIDs** locked in the Canonical Story Bible.

---

## 2. TAXONOMY OF PERSISTENT UUIDs

| UUID Prefix | Entity Category | Example UUID | Scope & Immutability |
| :--- | :--- | :--- | :--- |
| `ACT_` | Dramatic Act | `ACT_01` | Locked narrative phase (e.g., The Threshold of Return). |
| `SCN_` | Discrete Scene | `SCN_01` | Spatial/temporal unit locked to one primary location and time. |
| `SHT_` | Camera Shot / Cut | `ACT1_SCN01_SHT01A` | Precise visual framing unit; immutable across exports 02, 04, 05, 06. |
| `CHAR_` | Character Profile | `CHAR_01` | Biometric, psychological, and wardrobe anchor. |
| `PROP_` | Physical Object / Prop | `PROP_01` | Hero and set dressing objects with physical & patina continuity. |
| `LOC_` | Architectural Location | `LOC_01` | Physical geometry, acoustics, and lighting plot anchor. |
| `VO_` | Voiceover Cue | `VO_CUE_001` | Timecoded vocal cue linked to shot and narrator persona. |
| `CUE_` | Sound / Musical Cue | `MX_01A_01` | Audio stem or score event. |

---

## 3. CROSS-DEPARTMENT CONTINUITY ENFORCEMENT

1. **Single Source of Truth:**
   All sub-systems must read from `workspace/state/00_canonical_story_bible.md`. No sub-system is permitted to invent new characters or change the physical properties of existing entities.
2. **Prop Consistency Rule:**
   If `PROP_01` is defined as a *Hand-engraved Moradabad yellow brass paan-daan with verdigris patina* in `08_prop_subsystem`, it MUST:
   - Appear with the exact same material specs in `01_script_subsystem`.
   - Produce a metallic `3.8 kHz` clink in `06_sound_design_subsystem`.
   - Be illuminated by `2200K` warm practical light in `02_shot_breakdown_subsystem`.
   - Have its yellow/brass hues handled via the Yellow/Orange HSL vectors in `05_color_grading_subsystem`.
3. **Character Biometric Lock:**
   If `CHAR_01` (Raghav) has a 4-day salt-and-pepper stubble and a forward-head posture in `07_character_subsystem`, the Shot Breakdown action block and Storyboard 2-liner prompt must mirror these exact traits.
4. **Validation Check:**
   Any file containing an unregistered entity name (e.g., a character mentioned without a valid `CHAR_XX` tag) will be rejected by the departmental audit.
