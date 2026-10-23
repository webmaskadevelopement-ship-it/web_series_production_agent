# CANONICAL STORY BIBLE STATE TEMPLATE (`00_story_bible_state.template.md`)

This template dictates how `workspace/state/00_canonical_story_bible.md` must be formatted upon completion of Sub-System 00 execution:

```markdown
# CANONICAL STORY BIBLE: {{PROJECT_TITLE_ENGLISH}} ({{PROJECT_TITLE_HINDI}})

> **Status:** LOCKED SINGLE SOURCE OF TRUTH (VERSION 1.0.0)  
> **Adaptation:** {{AUTHOR_AND_SOURCE}}  
> **Format:** {{TARGET_FORMAT}} | Runtime: {{TOTAL_RUNTIME_MINUTES}} mins | Total Cuts: {{TOTAL_SHOT_COUNT}}  

---

## 1. EXECUTIVE NARRATIVE OVERVIEW
{{EXECUTIVE_LOGLINE_AND_THEMATIC_SUMMARY}}

---

## 2. ACT STRUCTURAL ARCHITECTURE
| Act ID | Title | Narrative Span | Rasa Progression | Estimated Runtime |
| :--- | :--- | :--- | :--- | :--- |
| `ACT_01` | {{ACT_01_TITLE}} | {{ACT_01_SPAN}} | {{ACT_01_RASA}} | {{ACT_01_MINS}} mins |
| `ACT_02` | {{ACT_02_TITLE}} | {{ACT_02_SPAN}} | {{ACT_02_RASA}} | {{ACT_02_MINS}} mins |
| `ACT_03` | {{ACT_03_TITLE}} | {{ACT_03_SPAN}} | {{ACT_03_RASA}} | {{ACT_03_MINS}} mins |

---

## 3. MASTER SCENE REGISTRY
| Scene ID | Act | Slugline | Solar / Lighting Clock | Rasa & Sthayi Bhava | Shot Count | Characters | Props |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `SCN_01` | `ACT_01` | {{SCN01_SLUGLINE}} | {{SCN01_SOLAR}} | {{SCN01_RASA}} | {{SCN01_SHOTS}} | `CHAR_01`, `CHAR_02` | `PROP_01`, `PROP_02` |

---

## 4. ENTITY REGISTRY (IMMUTABLE UUIDS)

### Characters (`CHAR_XX`)
- **`CHAR_01`**: {{CHAR_01_NAME}} | {{CHAR_01_TIER}} | Core Wound: {{CHAR_01_WOUND}}
- **`CHAR_02`**: {{CHAR_02_NAME}} | {{CHAR_02_TIER}} | Core Wound: {{CHAR_02_WOUND}}

### Props (`PROP_XX`)
- **`PROP_01`**: {{PROP_01_NAME}} | {{PROP_01_CLASS}} | Material: {{PROP_01_MATERIAL}}
- **`PROP_02`**: {{PROP_02_NAME}} | {{PROP_02_CLASS}} | Material: {{PROP_02_MATERIAL}}

### Locations (`LOC_XX`)
- **`LOC_01`**: {{LOC_01_NAME}} | {{LOC_01_TYPOLOGY}} | Acoustic RT60: {{LOC_01_RT60}}

---

## 5. COMPLETE MACHINE-READABLE CANONICAL JSON STATE
```json
{{COMPILED_CANONICAL_STORY_BIBLE_JSON}}
```
```
