# FREQUENCY MASKING AVOIDANCE MATRIX (`matrices/frequency_masking_avoidance_matrix.md`)

## 1. COMPETING STEMS DUCKING PROTOCOL

| Primary Active Stem | Competing Background Stem | Masking Frequency Zone | Required Dynamic DSP Action |
| :--- | :--- | :--- | :--- |
| **Male Dialogue (Raghav)** | Acoustic Sarangi (Score) | $800\text{ Hz} – 2.5\text{ kHz}$ | Dynamic notch $-3.5\text{ dB}$ on Score bus via sidechain trigger. |
| **Female Dialogue (Savitri)** | Courtyard Rain Hiss (BG) | $2.5\text{ kHz} – 5.5\text{ kHz}$ | High-shelf duck $-4.0\text{ dB}$ on rain ambience during female speech. |
| **Hero Foley (Garlic Peel)** | Atmospheric Drone (Fx-B) | $2.8\text{ kHz} – 4.2\text{ kHz}$ | Transient booster $+3\text{ dB}$ on Foley; carve notch on Fx-B. |
| **Voiceover (Narrator)** | Full DME Stems | $120\text{ Hz} – 3.5\text{ kHz}$ | Global sidechain ducking of $-3.5\text{ dB}$ on Score and $-2.0\text{ dB}$ on Ambiences. |
