# LAW 06: BILINGUAL DEVANAGARI PRESERVATION STANDARD (`06_bilingual_devanagari_preservation_standard.md`)

## 1. CULTURAL INTEGRITY & SCRIPT PRESERVATION
Hindi cinema and South Asian dramatic literature rely profoundly on vernacular idiolects, regional dialects (Khari Boli, Awadhi, Bhojpuri, Braj, Bundeli, Marwari), cultural idioms, and rhythmic cadence. Translating Hindi dialogue into generic English erases cultural subtext, emotional resonance (*Bhava*), and authentic colloquial nuance.

This standard mandates **Three Synchronized Linguistic Layers** for every spoken line, voiceover cue, and lyric in the system.

---

## 2. THE THREE MANDATORY LINGUISTIC LAYERS

Every dialogue block in `01_Script.md`, `03_Voiceover_System.md`, and all relevant cues in `02_Shot_Breakdown.md` and `06_Audio_Sound_Design_File.md` must be formatted with the following structure:

### Layer 1: Pristine Devanagari Script (`hindi_devanagari`)
- Rendered in grammatically correct Unicode Devanagari script.
- Must preserve exact matras, conjuncts (samyuktakshar), half-characters, and regional punctuation.
- Preserves accurate *Nukta* (़) placement for Urdu/Persian loan words (e.g., काग़ज़, ग़म, फ़ैसला, नज़दीक) and authentic regional inflections (e.g., Purvanchali "नाही", Banarasi "का हो").

### Layer 2: Roman Phonetic Transliteration (`roman_phonetic_transliteration` / `ipa_and_roman_phonetic`)
- Precise phonetic spelling representing actual spoken pronunciation for non-Hindi-reading directors, sound engineers, and international crew.
- Explicitly marks retroflex stops (`T`, `D`, `R`), dental stops (`t`, `d`), aspirated consonants (`kh`, `gh`, `chh`, `jh`, `th`, `dh`, `ph`, `bh`), and nasalization (`~` / `ng`).
- Includes exact micro-pause and breathing markers: `[PAUSE: 0.8s]`, `[SLOW_EXHALE]`, `[GLOTTAL_CATCH]`.

### Layer 3: English Dramatic Subtext & Literal Translation (`english_literal_and_subtext`)
- Dual-part translation:
  - **Literal:** Exact word-for-word semantic translation.
  - **Subtext:** The unspoken psychological objective, status transaction, or emotional accusation behind the words.

---

## 3. FORMATTED PRODUCTION EXAMPLE

```json
{
  "dialogue_layers": {
    "hindi_devanagari": "छत टपकती थी तो तुम्हारे बाबूजी ने तसला रख दिया था... [PAUSE: 1.2s] तुम तो पूरा आँगन ही बेचने का काग़ज़ ले आए।",
    "roman_phonetic_transliteration": "Chhat tapakti thi toh tumhare Babuji ne tasla rakh diya tha... [PAUSE: 1.2s - nasal inhale] tum toh poora aangan hi bechne ka kaagaz le aaye.",
    "english_literal_and_subtext": "Literal: 'When the roof leaked, your father placed a basin underneath... you have brought papers to sell the entire courtyard.' | Subtext: 'Your father endured poverty and structural decay to shelter us; you erase our ancestral foundation for modern convenience.'"
  }
}
```

---

## 4. DIALECT INTEGRITY PROTOCOL
- Never standardize a rural or regional character's speech into formal metropolitan Hindi unless dramaturgically motivated.
- Characters migrating from rural backgrounds to metropolitan centers (e.g., Raghav in Varanasi vs. Delhi) must reflect linguistic code-switching depending on stress levels, as codified in `07_character_subsystem`.
