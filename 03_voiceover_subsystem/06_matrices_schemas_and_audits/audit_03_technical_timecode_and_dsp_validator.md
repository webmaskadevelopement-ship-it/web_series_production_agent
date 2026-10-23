# AUDIT 03: TECHNICAL TIMECODE & DSP VALIDATOR (`audit_03_technical_timecode_and_dsp_validator.md`)

## 1. THE 1:1 SHOT UUID CONTRACT
- **Verification Rule:** Every `vo_cue_id` in `03_Voiceover_System.md` MUST link to an exact `linked_shot_uid` existing in `02_Shot_Breakdown.pdf`.
- **Orphan Cues Forbidden:** Any voiceover cue without a valid visual shot anchor will fail compilation.

## 2. DSP & LOUDNESS INTEGRITY
- **Target Integrated Loudness:** `-24.0 LKFS / LUFS` (±0.5 LUFS).
- **True Peak Ceiling:** `-2.0 dBTP`.
- **High-Pass Engagement:** 75 Hz 24dB/oct verified on all voice tracks.
- **Sidechain Ducking:** -3.5 dB music duck verified during active speech.
