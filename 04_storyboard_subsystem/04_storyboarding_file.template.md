# STORYBOARDING FILE TEMPLATE (`04_storyboarding_file.template.md`)

This template governs the appending of storyboard panels into `workspace/exports/04_Storyboarding_File.md`:

```markdown
<!-- PANEL START: {{PANEL_INDEX}} -->
### {{PANEL_INDEX}} | Shot: {{SHOT_UID}} ({{SHOT_NO}})

> **Hierarchy:** Act: {{ACT_NO}} | Scene: {{SCENE_NO}} | Duration: {{DURATION_SEC}}  
> **Camera Badge:** {{SHOT_SIZE_AND_ANGLE}} | {{LENS_AND_TSTOP}} | {{CAMERA_MOVEMENT_RIG}}  

#### STRICT 2-LINER VISUAL STORYBOARD
- **Line 01 (Composition & Staging):** {{LINE_01_COMPOSITION}}
- **Line 02 (Kinetic Action & Focus):** {{LINE_02_ACTION}}

#### SPATIAL DEPTH PLANES & MOTION VECTORS
- **Foreground (FG):** {{FG_DEPTH_DESC}}
- **Midground (MG):** {{MG_DEPTH_DESC}}
- **Background (BG):** {{BG_DEPTH_DESC}}
- **Motion Vectors:** `{{MOTION_VECTORS_NOTATION}}`
- **Tonal Map:** Shadow: {{SHADOW_PCT}}% | Midtone: {{MIDTONE_PCT}}% | Highlight: {{HIGHLIGHT_PCT}}%

#### CONCEPT SKETCH GENERATION PROMPT
```text
{{STORYBOARD_SKETCH_PROMPT}}
```

#### MACHINE-READABLE PANEL DATA BLOCK
```json
{{COMPILED_STORYBOARD_PANEL_CARD_JSON}}
```
<!-- PANEL END: {{PANEL_INDEX}} -->
```
