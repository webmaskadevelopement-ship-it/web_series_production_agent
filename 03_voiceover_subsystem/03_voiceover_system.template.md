# VOICEOVER SYSTEM TEMPLATE (`03_voiceover_system.template.md`)

This template dictates how `workspace/exports/03_Voiceover_System.md` must be constructed:

```markdown
# MASTER VOICEOVER SYSTEM & ACOUSTIC PROSODY BIBLE

## 1. NARRATOR PSYCHOLOGICAL PERSONA & VOCAL ARCHITECTURE
- **Narrator UUID:** {{NARRATOR_ID}} (Linked: {{LINKED_CHARACTER_UUID}})
- **Vantage Point:** {{NARRATIVE_VANTAGE_POINT}}
- **Vocal Age & Physiology:** {{VOCAL_AGE_AND_PHYSIOLOGY}}
- **Timbre & Resonance:** {{TIMBRE_AND_RESONANCE}}
- **Dialect & Phonetic Register:** {{DIALECT_AND_PHONETIC_PROFILE}}

---

## 2. STUDIO RECORDING & DSP SIGNAL CHAIN SPECIFICATION
- **Acoustic Environment:** {{ACOUSTIC_ROOM_SPEC}}
- **Microphone Rig:** {{MICROPHONE_MODEL}} (Distance: {{MIC_DISTANCE}}, Angle: {{MIC_ANGLE}})
- **Preamp & Conversion:** {{PREAMP_MODEL}} (Gain: {{PREAMP_GAIN}}) -> 24-bit / 96 kHz PCM
- **Insert Plugin Order:**
  1. {{INSERT_01}}
  2. {{INSERT_02}}
  3. {{INSERT_03}}
  4. {{INSERT_04}}
  5. {{INSERT_05}}
  6. {{INSERT_06}}
  7. {{INSERT_07}}
- **Loudness Target:** Integrated {{INTEGRATED_LKFS}} | True Peak {{TRUE_PEAK_DBTP}}

---

## 3. SHOT-SYNCED PROSODY & PHONETIC CUE LEDGER

<!-- CUE START: {{VO_CUE_ID}} -->
### {{VO_CUE_ID}} | Linked Shot: `{{LINKED_SHOT_UID}}`
> **Timecode:** `{{TIMECODE_IN}}` to `{{TIMECODE_OUT}}` (Duration: {{DURATION_SECONDS}}s)  
> **Metrics:** Pacing: {{PACING_WPM}} WPM | Syllable Rate: {{SYLLABLE_RATE}} | Pitch F0: {{PITCH_CURVE_HZ}}  

#### 1. Annotated Devanagari Layer
> **{{DEVANAGARI_ANNOTATED_TEXT}}**

#### 2. IPA & Roman Phonetic Guide
```text
{{IPA_AND_ROMAN_PHONETIC}}
```

#### 3. English Subtext & Dramatic Translation
> *Literal:* "{{ENGLISH_LITERAL}}"  
> *Subtext:* "{{ENGLISH_SUBTEXT}}"  

#### 4. Respiratory & Acoustic Delivery Directives
- **Word Stresses:** {{WORD_STRESS_WEIGHTS}}
- **Breath Cues:** {{RESPIRATORY_AND_MOUTH_CUES}}
<!-- CUE END: {{VO_CUE_ID}} -->

---

## 4. COMPLETE MACHINE-READABLE VOICEOVER SYSTEM JSON
```json
{{COMPILED_VOICEOVER_SYSTEM_JSON}}
```
```
