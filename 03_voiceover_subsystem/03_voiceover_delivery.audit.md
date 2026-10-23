# VOICEOVER DELIVERY AUDIT CHECKLIST (`03_voiceover_delivery.audit.md`)

## 1. QUALITY ASSURANCE GATES
Before exporting `03_Voiceover_System.md`:

- [ ] **1. Shot UID Linkage:** Is every voiceover cue strictly mapped to a valid `shot_uid` in `02_Shot_Breakdown.md`?
- [ ] **2. Timecode Synchronization:** Does the cue timecode span fit within the start and end timecode of the linked shot?
- [ ] **3. Three Linguistic Layers:** Are Devanagari, IPA transliteration, and English subtext translation provided for every line?
- [ ] **4. Paralinguistic Breath Tags:** Are pre-speech inhales, glottal holds, and exhalation markers explicitly timed?
- [ ] **5. Studio Chain Completeness:** Are microphone polar pattern, distance, preamp gain, and 7-stage plugin DSP chain fully detailed?
- [ ] **6. JSON Schema Validity:** Does the embedded JSON comply with `03_voiceover_prosody.schema.md`?
- [ ] **7. Anti-Truncation Compliance:** Contains zero placeholder abbreviations or `"continues"` phrases.
