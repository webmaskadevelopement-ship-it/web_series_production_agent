# MASTER SHOT BREAKDOWN TEMPLATE (`02_shot_breakdown_master_table.template.md`)

This template governs the appending of scene shot breakdowns into `workspace/exports/02_Shot_Breakdown.md`:

```markdown
<!-- ACT START: {{ACT_ID}} -->
# {{ACT_ID}}: {{ACT_TITLE}}
> **Visual Grammar:** {{ACT_VISUAL_GRAMMAR}}  

<!-- SCENE START: {{SCENE_ID}} -->
## {{SCENE_ID}}: {{SETTING_AND_LOCATION}}
> **Time:** {{TIME_OF_DAY}} | Total Duration: {{SCENE_DURATION_TOTAL}} | Total Shots: {{TOTAL_SHOTS_IN_SCENE}}  
> **Dramatic Purpose:** {{DRAMATIC_PURPOSE}}  
> **180° Axis of Action:** {{AXIS_OF_ACTION_180_LINE}}  

### 1. THE 10-COLUMN MASTER PRODUCTION TABLE (A3/A4 LANDSCAPE)

| Shot ID & Duration | Framing & Angle | Lens & Sensor | Movement & Rig | Focus & DoF | Lighting & Photometrics | Visual Action & Blocking | Audio: Dx, Foley & Music | Edit & Murch Justification | VFX & GenAI Prompt |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **{{SHOT_ID}}**<br>{{DURATION_SEC}}s<br>({{DURATION_FRAMES}} fr) | **{{SHOT_TYPE}}**<br>Pitch: {{PITCH}}<br>Roll: {{ROLL}}<br>Ht: {{HEIGHT}} | **{{FOCAL_LENGTH}}**<br>{{T_STOP}}<br>{{CAMERA_BODY}}<br>{{COLOR_SCIENCE}} | **{{RIG_TYPE}}**<br>{{MOVEMENT_AXIS}}<br>Vel: {{VELOCITY}}<br>Imp: {{IMPERFECTION}} | Near: {{NEAR_FOCUS}}<br>Far: {{FAR_FOCUS}}<br>Rack: {{RACK_FOCUS}} | Mood: {{LIGHTING_MOOD}}<br>Key: {{KEY_KELVIN}}<br>Fill: {{FILL_KELVIN}}<br>Ratio: {{RATIO}} | **Action:** {{ACTION_SUMMARY}}<br>**Blocking:** {{BLOCKING_COORDINATES}}<br>**FACS:** {{FACS_UNITS}} | **Dia:** {{DIALOGUE_OR_VO}}<br>**Foley:** {{FOLEY_CUES}}<br>**Room:** {{ROOM_TONE}}<br>**Score:** {{SCORE_CUE}} | **In:** {{IN_TRANSITION}}<br>**Out:** {{OUT_TRANSITION}}<br>**Eye-Trace:** {{EYE_TRACE_COORD}} | **VFX:** {{VFX_CUES}}<br>**Prompt:** `{{MIDJOURNEY_PROMPT}}` |

### 2. DEEP TECHNICAL DECOMPILATION BLOCKS (JSON DEEP DIVE)

```json
{{COMPILED_SCENE_SHOT_CONTAINER_JSON}}
```
<!-- SCENE END: {{SCENE_ID}} -->
```
