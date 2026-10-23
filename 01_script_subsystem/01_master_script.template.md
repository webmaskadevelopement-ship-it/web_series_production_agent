# MASTER SCREENPLAY TEMPLATE (`01_master_script.template.md`)

This template defines the layout for appending scenes into `workspace/exports/01_Script.md`:

```markdown
<!-- SCENE START: {{SCENE_ID}} -->
## {{SCENE_ID}}: {{SLUGLINE}}

> **Act:** {{ACT_ID}} | Sequence: {{SEQUENCE_ID}}  
> **Location:** {{LOCATION_NAME}} (`{{LOCATION_UUID}}`) | Time: {{TIME_OF_DAY}}  
> **Dramatic Objective:** {{DRAMATIC_OBJECTIVE}}  
> **Dominant Rasa:** {{DOMINANT_RASA}} (Sthayi Bhava: {{STHAYI_BHAVA}})  
> **Scene Pacing:** {{PAGE_SPAN_ESTIMATE}} (~{{ESTIMATED_SCREEN_TIME_SECONDS}} seconds)  

---

### ACTION & DIALOGUE STREAM

{{KINAESTHETIC_ACTION_BLOCK}}

{{CHARACTER_CUE}}
{{PARENTHETICAL}}
**{{HINDI_DEVANAGARI_LINE}}**  
*{{ROMAN_PHONETIC_LINE}}*  
> *Literal:* "{{ENGLISH_LITERAL}}"  
> *Subtext:* "{{ENGLISH_SUBTEXT}}"  

{{THEHRAAV_PAUSE_BLOCK}}

{{TRANSITION_DIRECTIVE}}

---
### MACHINE-READABLE SCENE DATA BLOCK
```json
{{COMPILED_SCRIPT_SCENE_UNIT_JSON}}
```
<!-- SCENE END: {{SCENE_ID}} -->
```
