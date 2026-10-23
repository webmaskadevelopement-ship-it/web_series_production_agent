# INGESTION COMPLETENESS AUDIT CHECKLIST (`00_ingestion_completeness.audit.md`)

## 1. QUALITY ASSURANCE CRITERIA
Before presenting the Canonical Ingestion Summary Box to the user, Sub-System 00 must self-audit against these non-negotiable verification gates:

- [ ] **1. Narrative Completeness:** Has 100% of the input text or PDF been parsed without summarizing or skipping ending paragraphs?
- [ ] **2. Act Boundary Verification:** Are all 3 Acts clearly identified with dramatic polarity shifts and runtime allocations?
- [ ] **3. Scene Integrity:** Does every scene have a complete slugline, solar lighting state, weather condition, and dominant *Rasa*?
- [ ] **4. Shot Calculation Verification:** Has every scene been assigned a pre-calculated shot count derived from the granularity estimator equation?
- [ ] **5. Entity Registry Completeness:** Are all speaking characters, prominent physical props, and architectural spaces tagged with immutable UUIDs (`CHAR_XX`, `PROP_XX`, `LOC_XX`)?
- [ ] **6. JSON Schema Validation:** Does the embedded JSON block in `workspace/state/00_canonical_story_bible.md` pass 100% schema validation against `00_canonical_story_bible.schema.md`?
- [ ] **7. Zero Blacklist Tokens:** Does the output contain zero occurrences of `"etc."`, `"TBD"`, `"..."`, or grouped IDs?

If any check fails, regenerate the deficient section before presenting the interactive menu to the user.
