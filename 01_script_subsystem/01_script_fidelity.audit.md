# SCREENPLAY FIDELITY AUDIT CHECKLIST (`01_script_fidelity.audit.md`)

## 1. QUALITY ASSURANCE GATES
Before finalizing any scene block in `01_Script.md`, verify:

- [ ] **1. Slugline Format:** Does the slugline include INT./EXT., master location, sub-zone, solar state, and lighting context?
- [ ] **2. 100% Filmable Prose:** Are all thoughts, backstories, and internal feelings translated into visible physical action?
- [ ] **3. Three Dialogue Layers:** Does every dialogue line include Unicode Devanagari, Romanized phonetics, and English literal + subtext?
- [ ] **4. Thehraav Silences:** Are dramatic pauses explicitly timed and coded with environmental Foley?
- [ ] **5. Entity Tagging:** Are all characters (`CHAR_XX`), props (`PROP_XX`), and locations (`LOC_XX`) tagged with persistent UUIDs?
- [ ] **6. JSON Data Contract:** Does the embedded scene unit JSON pass validation against `01_script_structure.schema.md`?
- [ ] **7. Anti-Truncation Compliance:** Contains zero instances of `"etc."`, `"..."`, or skipped dialogue exchanges.
