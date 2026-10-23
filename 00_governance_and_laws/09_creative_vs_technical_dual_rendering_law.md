# LAW 09: CREATIVE VS. TECHNICAL DUAL-RENDERING LAW (`09_creative_vs_technical_dual_rendering_law.md`)

## 1. PURPOSE & CORE PRINCIPLE
Production deliverables serve two distinct audiences in a film studio ecosystem:
1. **Executive, Client & Creative Stakeholders (Producers, Investors, Actors, Casting, Client Brands):**
   Need clean, readable, immersive, unencumbered cinematic deliverables that can be shared, evaluated, and performed without drowning in engineering code blocks, DSP matrices, or sensor math.
2. **Technical Heads of Department (DP, 1st AD, Colorist, Sound Designer, VFX Supervisor, Gaffer):**
   Require exhaustive, uncompressed, deterministic engineering blueprints (Cooke /i metadata, IRE exposure values, ACES 12-node trees, FACS Action Units, Dolby Atmos XYZ panning, PBR physics).

To eliminate friction while preserving complete technical rigor, the Autonomous Studio System enforces **Dual-Mode Rendering**:
- **Option A: Creative Master Suite (Executive / Client Shareable Edition)** — Abstract final deliverables without technical blocks.
- **Option B: Technical File Master Suite (Deep Engineering Decompilation)** — Full drop-down of all generation mode options.
- **Option C: Unified Studio Master (Both Suites Simultaneously)**.

---

## 2. DUAL-MODE SPECIFICATIONS BY DEPARTMENT

### Department 01: Master Screenplay (`01_script_subsystem`)
- **Creative Master (`01_Script_Creative_Master.md` / `.pdf`):**
  - Standard Industry Screenplay formatting (Scene Sluglines, Scene Action, Character Names, Parentheticals, Dialogue).
  - Strictly budgeted to the requested page length (e.g., 6–7 pages for a 6–7 minute episode).
  - **Omissions:** Excludes camera optical cues, lens choices, sensor ratings, and deep metadata dumps from action paragraphs. Only pure visual action, character behavior, and dramatic dialogue.
- **Technical File Master (`01_Script_Technical_Master.md`):**
  - Includes scene timing math, sub-location zoning, lighting clock tags, character speech register tags, and embedded continuity markers.

---

### Department 02: Master Shot Breakdown (`02_shot_breakdown_subsystem`)
- **Creative Master (`02_Shot_Breakdown_Creative_Master.md` / `.pdf`):**
  - **10-Column Master Production Tables ONLY** (grouped by Act, then by Scene).
  - Columns: Shot ID | Shot Type | Camera Angle | Camera Movement | Lens Focal Length | Subject/Action | Sound/Dialogue Cue | Lighting Setup | Pacing/Sec | Dramatic Function.
  - **Omissions:** Completely omits the Deep Technical Decompilation JSON blocks (no optical aberration specs, circle of confusion, hyperfocal math, FACS Action Units, or PBR coordinates).
  - Provides a clean, print-ready document for production meetings, director review, and client approval.
- **Technical File Master (`02_Shot_Breakdown_Technical_Master.md` / `.pdf`):**
  - Delivers **BOTH** the 10-Column Master Production Tables AND the complete Deep Technical Decompilation JSON block for every single individual shot without truncation.

---

### Department 03: Voiceover & Prosody System (`03_voiceover_subsystem`)
- **Creative Master (`03_Voiceover_Creative_Master.md` / `.pdf`):**
  - **Plain Prose Voiceover Script:** Clean, elegant, performable literary prose organized by Act and Scene.
  - Includes dramatic mood tags, scene context notes, and clear delivery pacing guidance.
  - Designed specifically for voice talent, directors, and client review to read aloud effortlessly.
  - **Omissions:** Excludes vocal DSP signal chains (preamps, EQ Hz cuts/boosts, LA-2A compressor specs), microphone polar physics, acoustic RT60 values, and IPA phonetic transcriptions.
- **Technical File Master (`03_Voiceover_Technical_Master.md`):**
  - Full acoustic engineering dossier: Devanagari phonetics with Mahaprana/Anunasika markings, pitch contour semitone tables, WPM curves, Neumann U87 / Sennheiser 416 specs, and studio DSP routing.

---

### Department 04: Storyboard Pre-Vis System (`04_storyboard_subsystem`)
- **Creative Master:** Clean 2-liner visual narrative descriptions, focal character blocking, and emotional tone notes per frame.
- **Technical Master:** Full dynamic symmetry ratios, horizon line coordinates, motion vectors, and generative AI prompt engineering trees.

---

### Department 05–09: Post-Production & Asset Systems
- **Creative Master:** Executive summaries, color mood palettes, narrative soundscape descriptions, character profile summaries, key prop lists, and location lookbooks.
- **Technical Master:** Exhaustive 12-node ACES trees, printer lights, 7.1.4 Atmos stem routing, FACS/Laban matrices, PBR roughness/metallic tables, and architectural floorplans.

---

## 3. STRICT ISOLATION & NO-DEGRADATION GUARANTEE
1. **The Creative Master does NOT diminish the Technical Brain:**
   Generating a Creative Master does not mean the system skipped technical calculations; the Two-Brain analysis always runs internally to ensure continuity and spatial realism. The Creative Master renderer simply filters out raw technical blocks for executive consumption.
2. **Zero Truncation Remains Inviolable:**
   In both modes, every scene and every shot is accounted for. Creative Master tables list every shot (e.g., all 168 shots in a 6-minute film); they simply do so in compact table rows rather than multi-page JSON blocks.
