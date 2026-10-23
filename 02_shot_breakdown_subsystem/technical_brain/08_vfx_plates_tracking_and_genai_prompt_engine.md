# VFX PLATES, TRACKING & DETERMINISTIC GENAI PROMPT ENGINE (`technical_brain/08_vfx_plates_tracking_and_genai_prompt_engine.md`)

## 1. COMPOSITING & TRACKING SPECIFICATIONS
For every shot requiring post-production augmentation:
1. **Compositing Cues:** E.g., *Add subtle 2.5D volumetric monsoon mist drifting down through open courtyard sky zenith (Nuke deep-compositing pass, 12% opacity).*
2. **Motion Tracking Data:** E.g., *Export Cooke `/i` lens metadata (focal length, T-stop, focus distance per frame) + 3D camera track solve from sandstone floor joints.*
3. **Clean Plate Requirements:** Clean background plate of unpeeled garlic plate, undisturbed sandstone step.

---

## 2. DETERMINISTIC GENERATIVE AI PROMPT COMPILER
Every shot must generate two deterministic prompts directly synthesized from its camera, lighting, and wardrobe parameters:

### A. Midjourney v6.1 Keyframe Prompt
Formula:
```text
[Shot Type], [Focal Length & Lens Series] at [T-stop], [Setting & Location description], [Time of Day & Solar State], [Composition & Dynamic Symmetry framing], [Subject Description, Age, Wardrobe & Blocking], [Lighting Mood, Kelvin contrast, IRE ratios], [Camera body, Sensor & Color Science], [Film Stock Emulation] --ar 21:9 --style raw --v 6.1
```

### B. Video Motion Prompt (Sora / Runway Gen-3 / Kling)
Formula:
```text
[Exact Camera Rig Movement, Vector Axis & Velocity], [Focus Pull / Rack transition with start/end targets], [Character physical micro-action], [Environmental movement: rain, smoke, flame flicker], cinematic photorealistic lighting continuity.
```
