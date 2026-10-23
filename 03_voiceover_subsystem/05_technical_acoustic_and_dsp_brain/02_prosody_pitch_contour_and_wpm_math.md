# PROSODY, PITCH CONTOUR & WPM MATHEMATICS (`02_prosody_pitch_contour_and_wpm_math.md`)

## 1. THE TIME-TO-SPEECH RATIO FORMULA
In visual editing, a shot has a rigid, immutable duration defined in timecode (`HH:MM:SS:FF`) or frames at 24.0 fps. A voiceover cue that overflows its shot boundary collides with the next cut or drowns out on-screen dialogue.

The Voiceover Subsystem enforces the **Syllable-Duration Mathematical Model**:
$$	ext{Duration (Seconds)} = \sum_{i=1}^{N} 	ext{Syllable}_i + \sum_{j=1}^{M} 	ext{Pause}_j$$

Where:
- **Short Vowels (`अ, इ, उ`):** 110ms to 140ms duration.
- **Long / Dipthong Vowels (`आ, ई, ऊ, ए, ऐ, ओ, औ`):** 220ms to 340ms duration.
- **Geminate / Conjunct Consonants (`त्त, ड्ड, क्क`):** Add +90ms occlusion pause.
- **WPM Conversion Rule:** 1 Word in literary Hindi averages 2.4 syllables. At 90 WPM, the delivery speed is 3.6 syllables per second (277ms per syllable).

---

## 2. PITCH CONTOUR & SEMITONE MODULATION

### 1. THE DECLARATIVE DROP (कथन का अधोगामी झुकाव)
- **Envelope:** Starts at the speaker's baseline fundamental frequency $F_0$ (e.g., 108 Hz for male baritone), climbs slightly (+2 semitones / 121 Hz) on the primary thematic focus word, and **drops by 4 to 5 semitones (down to 82–88 Hz)** on the final verb or auxiliary (*"रहते हैं"*, *"हो गया"*).
- **Acoustic Function:** Communicates fatalism, finality, and unchallengeable truth.

### 2. THE SUSPENDED CONDITIONAL (*AGAR* HOOK)
- **Envelope:** Enters flat, maintains pitch through the conditional clause, and **rises by 3 semitones (to 128 Hz)** at the end of the clause, suspending in dead silence before the main clause begins.
- **Example:** *"अगर वह दरवाज़ा न खोलता... [PITCH SUSPENDED @ 128 Hz] [PAUSE: 1.2s] तो शायद आज घर का यह हाल न होता।"*

---

## 3. MASTER PROSODY SPEED ENVELOPE TABLE

| Cinematic Genre | Target WPM Range | Syllable Rate (Syl/sec) | Average Sentence Syllables | Primary Pause Duration |
|---|:---:|:---:|:---:|:---:|
| Historical / Civilizational Epic | 80–92 WPM | 3.2 – 3.7 | 24–32 | 1.4s to 2.0s |
| Intimate Family Grief / Drama | 78–88 WPM | 3.1 – 3.5 | 14–20 | 1.2s to 1.8s |
| Metro Noir / Espionage | 92–104 WPM | 3.7 – 4.2 | 12–18 | 0.8s to 1.2s |
| Hinterland Crime / Feud | 110–128 WPM | 4.4 – 5.1 | 8–14 | 0.4s to 0.8s |
| White-Collar Financial Hustle | 120–138 WPM | 4.8 – 5.5 | 10–16 | 0.3s to 0.6s |
