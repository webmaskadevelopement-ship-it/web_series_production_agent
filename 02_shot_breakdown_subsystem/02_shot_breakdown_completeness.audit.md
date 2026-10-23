# SHOT BREAKDOWN COMPLETENESS AUDIT CHECKLIST (`02_shot_breakdown_completeness.audit.md`)

## 1. QUALITY ASSURANCE GATES
Before finalizing any scene breakdown in `02_Shot_Breakdown.md`:

- [ ] **1. Zero Shot Grouping:** Are all cuts enumerated as distinct shot records (`01A`, `01B`, `01C`) with zero grouped ranges (`01A-01D`)?
- [ ] **2. 10-Column Parity:** Does every shot have a corresponding entry in both the Landscape Master Table and the Deep JSON block?
- [ ] **3. Optical Specification Completeness:** Are focal length, T-stop, sensor model, ISO, dynamic range, and lens character fully declared?
- [ ] **4. Kinematics & Rig Math:** Are movement axis, linear velocity (cm/s), feathering ramp, and imperfection float explicitly defined?
- [ ] **5. Photometrics & IRE Waveform:** Are key/fill Kelvin, contrast ratios, and skin IRE values specified?
- [ ] **6. Walter Murch Justification:** Does every cut point cite Emotion (51%), Story, Rhythm, and Eye-Trace screen coordinates?
- [ ] **7. Deterministic Prompts:** Does every shot include both a Midjourney v6.1 keyframe prompt string and a video motion prompt?
- [ ] **8. Zero Blacklist Tokens:** Free from `"etc."`, `"same as previous"`, `"continues"`, and `"TBD"`.
