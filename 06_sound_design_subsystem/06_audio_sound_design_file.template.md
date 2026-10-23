# AUDIO & SOUND DESIGN TEMPLATE (`06_audio_sound_design_file.template.md`)

This template governs the appending of scene audio specifications into `workspace/exports/06_Audio_Sound_Design_File.md`:

```markdown
<!-- SCENE AUDIO START: {{SCENE_ID}} -->
## {{SCENE_ID}}: AUDIO & SOUND DESIGN SPECIFICATION

### 1. PRO TOOLS HDX STEMS & LOUDNESS TARGETS
- **Delivery Standard:** {{DELIVERY_FORMAT}} (96 kHz / 24-bit)
- **Program Loudness:** {{PROGRAM_LOUDNESS_LKFS}} | Dialogue Anchor: {{DIALOGUE_ANCHOR_LKFS}}
- **True Peak Max:** {{TRUE_PEAK_MAX}} | LFE Filter: {{LFE_FILTER_SPEC}}

### 2. ROOM ACOUSTICS & REVERB PROFILE
- **Location UUID:** `{{LOCATION_UUID}}` ({{LOCATION_NAME}})
- **Cubic Volume & Surfaces:** {{ROOM_CUBIC_VOLUME}} | {{SURFACE_ABSORPTION_SPECS}}
- **Convolution Preset:** {{CONVOLUTION_PRESET_NAME}} (Pre-Delay: {{PRE_DELAY_MS}}ms)
- **RT60 Decays:** 500Hz: {{RT60_500HZ}} | 1kHz: {{RT60_1KHZ}} | 4kHz: {{RT60_4KHZ}}

### 3. SEVEN-BAND FREQUENCY ALLOCATION
- **Sub-Bass (20-60Hz):** {{SUB_BASS_ROUTING}}
- **Bass (60-250Hz):** {{BASS_ROUTING}}
- **Low-Mids (250-500Hz):** {{LOW_MIDS_ROUTING}}
- **Midrange (500-2kHz):** {{MIDRANGE_ROUTING}}
- **Upper-Mids (2k-4kHz):** {{UPPER_MIDS_ROUTING}}
- **Presence (4k-8kHz):** {{PRESENCE_ROUTING}}
- **Air (8k-20kHz):** {{AIR_ROUTING}}

### 4. SHOT-WISE MULTI-STEM CUE SHEET

<!-- SHOT AUDIO: {{SHOT_UID}} -->
#### {{SHOT_UID}} | Timecode: `{{TIMECODE_SPAN}}`
- **Dialogue / VO:** {{DIALOGUE_TRACK_CUE}} (Level: {{DX_LEVEL_LUFS}}, Panning: `{{DX_PANNING_XYZ}}`)
- **Foley Elements:**
  - `{{FOLEY_ID_01}}`: {{FOLEY_DESC_01}} (Sync: {{SYNC_FRAMES_01}}, Level: {{FOLEY_LEVEL_01}}, Pan: `{{FOLEY_PAN_01}}`)
- **Spot SFX (fFxA):** `{{SFX_ID_01}}`: {{SFX_DESC_01}} (Sync: {{SFX_SYNC_01}}, Pan: `{{SFX_PAN_01}}`)
- **Ambiences (fBG):** `{{BG_ID_01}}`: {{BG_DESC_01}} (Level: {{BG_LEVEL_01}}, Pan: `{{BG_PAN_01}}`)
- **Score (fMx):** `{{MUSIC_ID_01}}`: {{SCORE_CUE_TITLE}} (Raga: {{RAGA_NAME}}, Level: {{MX_LEVEL_01}})

### 5. MACHINE-READABLE AUDIO JSON
```json
{{COMPILED_SCENE_AUDIO_JSON}}
```
<!-- SCENE AUDIO END: {{SCENE_ID}} -->
```
