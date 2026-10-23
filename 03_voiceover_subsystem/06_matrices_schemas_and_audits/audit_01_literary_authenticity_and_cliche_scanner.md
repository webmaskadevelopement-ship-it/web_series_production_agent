# AUDIT 01: LITERARY AUTHENTICITY & CLICHÉ SCANNER (`audit_01_literary_authenticity_and_cliche_scanner.md`)

## 1. AUTOMATED PRE-FLIGHT QUALITY GATE
Before any voiceover output can be exported to `workspace/exports/03_Voiceover_System.md`, it MUST undergo an automated regex and linguistic audit against the rules of Directory 02.

### GATE CRITERIA 1: ZERO BANNED CLICHÉS
- The scanner runs an automated substring search against all 155 entries in `02_lexicon_and_word_selection_engine/10_ai_hindi_cliche_blacklist_and_banned_phrases.md`.
- **Tolerance:** `0 matches`. If even a single banned phrase (e.g., *"सन्नाटे को चीरती हुई आवाज़"*, *"अंधेरे की चादर"*) is detected, generation is HALTED and flagged for regeneration.

### GATE CRITERIA 2: NO DIRECT EMOTIONAL ADJECTIVES
- Scans for banned emotional state words: `[दुखी, खुश, डरा हुआ, गुस्सा, परेशान, अकेला, बेचैन, असहाय, भावुक, निराश]`.
- **Tolerance:** `0 matches`. All emotional states must be grounded in physical Objective Correlatives.

### GATE CRITERIA 3: CONTRAPUNTAL COMPLIANCE
- The script must not duplicate verbs or visual descriptions present in `02_Shot_Breakdown.pdf` for the matching shot UUID.
