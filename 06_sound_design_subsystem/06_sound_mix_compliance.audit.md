# SOUND MIX COMPLIANCE AUDIT CHECKLIST (`06_sound_mix_compliance.audit.md`)

## 1. QUALITY ASSURANCE GATES
Before finalizing `06_Audio_Sound_Design_File.md`:

- [ ] **1. DM&E Bus Integrity:** Are all 7 stems (Dx, VO, Foley, Fx-A, Fx-B, BG, Mx) explicitly defined?
- [ ] **2. ITU-R BS.1770-4 Compliance:** Is integrated program loudness locked at $-24.0\text{ LKFS}$ ($\pm 0.5\text{ LU}$) and True Peak at $-2.0\text{ dBTP}$?
- [ ] **3. 3D Atmos Coordinates:** Do all spot effects and Foley cues specify Cartesian coordinates ($X, Y, Z$)?
- [ ] **4. Sabine RT60 Calculation:** Are pre-delay (ms) and multi-band RT60 decay values mathematically consistent with the location's dimensions?
- [ ] **5. Masking Conflict Resolution:** Are frequency ducking and carving protocols defined between dialogue and score?
- [ ] **6. Schema Compliance:** Does the embedded JSON validate against `06_audio_sound_design.schema.md`?
- [ ] **7. Anti-Truncation Compliance:** Contains zero placeholder sound tags like `"music continues"` or `"standard Foley"`.
