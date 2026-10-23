# TEMPLATE 01: TECHNICAL MASTER SPECIFICATION (`technical_master_spec.md`)

## 1. PURPOSE OF TECHNICAL MASTER DELIVERABLES
The Technical Master Suite is the comprehensive engineering dossier for Heads of Department (Director of Photography, 1st AD, Chief Lighting Technician, Production Sound Mixer, Supervising Sound Editor, Lead Colorist, and VFX Supervisor).

It delivers the **Full Drop-Down of All Generation Options** across all 150 to 189 shots without a single line of truncation.

---

## 2. DEPARTMENTAL TECHNICAL MASTER SPECIFICATIONS

### 1. Master Screenplay (`01_Script_Technical_Master.md`)
- Complete screenplay embedded with sub-location geometry, solar/lighting clock tags, speaker register markers (Tatsama vs Tadbhava vs Hinglish), and page timing validation math.

---

### 2. Master Shot Breakdown (`02_Shot_Breakdown_Technical_Master.md` / `.pdf`)
- Delivers **BOTH**:
  1. The 10-Column Master Production Table for high-level continuity.
  2. The **Deep Technical Decompilation JSON Block** for every individual shot ID (`ACT1_SCN01_SHT01A` through `ACT3_SCN0X_SHTYYZ`):
     - Sensor specification (Alexa 35, Venice 2, EI, Dynamic range).
     - Cooke /i or ARRI LDS-2 optical metadata (focal length, T-stop, focus distance, hyperfocal, depth of field, optical aberrations, halation).
     - Rig kinematics (dolly, Steadicam, handheld imperfection coefficient 0.0–1.0).
     - Photometric lighting profile (key/fill ratio, kelvin, IRE zones 1–10, foot-candles).
     - FACS facial action units & Laban effort elements.
     - VFX tracking markers and GenAI deterministic prompt tokens.

---

### 3. Voiceover & Acoustic Engineering Sheet (`03_Voiceover_Technical_Master.md`)
- Complete Devanagari script with Mahaprana/Anunasika markings.
- Prosody pitch contour curves (semitone drops), WPM mathematical speed curves.
- Respiratory and paralinguistic tags (`[INHALE-0.4s]`, `[GLOTTAL-STOP]`, `[VOCAL-FRY]`).
- Studio hardware specifications: Neumann U87 Ai / Sennheiser 416 polar pattern & proximity effect.
- 5-stage Vocal DSP signal chain (preamp impedance, parametric EQ Hz cuts/boosts, LA-2A gain reduction, Lexicon 480L reverb decay).

---

### 4. Post-Production Technical Suites (04 through 09)
- **04 Storyboarding:** Dynamic symmetry grids, horizon coordinate floats, motion vectors.
- **05 Color Grading:** ACEScc 12-node DaVinci Resolve trees, CDL lift/gamma/gain, Kodak 2383 D65 print LUTs.
- **06 Audio Design:** 7.1.4 Dolby Atmos XYZ coordinates, Pro Tools stem routing, RT60 decay, foley PBR.
- **07 Character:** Complete anatomical, psychological, and textile weight/weave GSM specifications.
- **08 Prop List:** PBR material chemistry, patina distress stages, continuity tracking.
- **09 Location:** Floorplans, practical lighting rigging, acoustic boundary absorption.

---

## 3. FILE DESTINATION
All Technical Master files are compiled and saved directly into:
`workspace/projects/{PROJECT_SCRIPT_TITLE}/02_Technical_Master_Suite/`
