# SCHEMA 04: 2-LINER STORYBOARD & PRE-VISUALIZATION (`04_storyboard_frame.schema.md`)

Every shot in `04_Storyboarding_File.md` MUST maintain a **1:1 Shot ID parity** with `02_Shot_Breakdown.pdf` and strictly enforce the **2-Liner Visual Storyboard Rule** paired with spatial vectors and camera metadata:

```json
{
  "storyboard_panel_card": {
    "panel_index": "PANEL_001",
    "hierarchy": {
      "act_no": "ACT_01",
      "scene_no": "SCN_01",
      "shot_no": "01A",
      "shot_uid": "ACT1_SCN01_SHT01A",
      "duration_sec": "6.5s (156 frames)"
    },
    "camera_and_lens_badge": {
      "shot_size_and_angle": "EWS (Extreme Wide Master) | High Angle (-12.5°) | Frontal 0°",
      "lens_and_tstop": "50mm 2x Anamorphic Prime @ T2.8 | Aspect Ratio: 2.39:1",
      "camera_movement_rig": "Dolly Push-In (Z+ axis @ 8cm/s) | Rack Focus: 1.5m (FG) -> 4.2m (MG)"
    },
    "strict_two_liner_storyboard_description": {
      "line_01_spatial_composition_and_staging": "A central weathered sandstone pillar slices the 2.39:1 frame vertically in half—isolating Raghav frozen in the dark rain-streaked archway on the Left third (Z:6.1m) from Savitri seated on the floor in a warm pool of oil-lamp light on the Right third (Z:4.2m).",
      "line_02_kinetic_action_and_focal_shift": "As the camera creeps slowly forward along the wet courtyard axis, focus racks from the blurred foreground brass water pot to Savitri's unhurried hands peeling garlic while rainwater drips rhythmically from Raghav's umbrella tip."
    },
    "spatial_depth_planes_and_vectors": {
      "foreground_plane_fg": "0.8m–1.6m: Out-of-focus tarnished brass Kalash on stone ledge (Bottom-Left corner occlusion).",
      "midground_plane_mg": "4.2m–6.1m: Central dividing pillar; Savitri seated on chauki (Right); Raghav standing at threshold (Left).",
      "background_plane_bg": "8.5m–12.0m: Deep arched veranda corridor receding into 4 IRE shadow with a single flickering 2700K caged bulb.",
      "motion_vector_notation": "CAM: [Z+ PUSH 0.52m] | FOCUS: [RACK Z:1.5m -> Z:4.2m] | SUBJ_01: [STATIC] | SUBJ_02: [MICRO-HAND_MOTION] | ENV: [Y- DRIP_VECTOR Left Third]",
      "three_value_tonal_map": "Shadow (70% of frame: 4–15 IRE stone walls) | Midtone (22% of frame: 35–48 IRE twilight courtyard & faces) | Highlight (8% of frame: 85–94 IRE diya flame & wet stone speculars)"
    },
    "storyboard_sketch_generation_prompt": "Architectural black-and-white & amber storyboard concept panel, 2.39:1 widescreen frame, bold dynamic symmetry grid lines, central stone pillar dividing frame, left side shows man with umbrella in doorway, right side shows elderly woman seated on floor by oil lamp, directional 3D camera push-in arrow on floor plane, rack focus depth rings marked at 1.5m and 4.2m, Ridley Scott & Bong Joon-ho storyboard pencil and ink wash style --ar 21:9"
  }
}
```
