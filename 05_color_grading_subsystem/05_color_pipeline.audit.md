# COLOR PIPELINE AUDIT CHECKLIST (`05_color_pipeline.audit.md`)

## 1. QUALITY ASSURANCE GATES
Before finalizing `05_Color_Grading_File.md`:

- [ ] **1. Scene-Referred Pipeline:** Are IDT, Working Space (DWG/ACES), and ODT explicitly defined?
- [ ] **2. 12-Node Completeness:** Are all 12 nodes in the signal tree populated with valid operations?
- [ ] **3. Printer Lights Accuracy:** Are RGB printer points defined in quarter-point increments?
- [ ] **4. Mathematical Validity of Floats:** Do Lift, Gamma, and Gain values remain within $-1.000$ to $+1.000$?
- [ ] **5. Skin Tone Protection:** Is the Vectorscope I-line lock confirmed for Indian melanin preservation?
- [ ] **6. Subtractive Density Integration:** Is the HSV Luma-pull specified to avoid digital neon saturation?
- [ ] **7. Schema Compliance:** Does the embedded JSON validate against `05_color_grading_di.schema.md`?
- [ ] **8. Zero Blacklist Tokens:** Free from `"etc."`, `"same as before"`, and `"TBD"`.
