# SEVEN-BAND FREQUENCY ALLOCATION & CARVING (`technical_brain/04_seven_band_frequency_allocation_and_carving.md`)

## 1. 7-BAND SPECTRAL DIVISION MATRIX
To prevent frequency masking between dialogue, music, Foley, and environmental effects:

| Frequency Band | Range | Primary Assigned Stems | Carving & Dynamic Sidechain Action |
| :--- | :--- | :--- | :--- |
| **Sub-Bass** | $20\text{ Hz} – 60\text{ Hz}$ | LFE psychological tension drone, thunder roll | High-passed off all Dx and Foley tracks ($24\text{ dB/oct}$). |
| **Bass** | $60\text{ Hz} – 250\text{ Hz}$ | RaghavVO chest fundamental, heavy door resonance | Carved $-2.5\text{ dB}$ on Mx stem during speech. |
| **Low-Mids** | $250\text{ Hz} – 500\text{ Hz}$ | Sarangi body warmth, courtyard rain-air bed | Dynamic notch $-3.5\text{ dB}$ on BG whenever Dx is active. |
| **Midrange** | $500\text{ Hz} – 2.0\text{ kHz}$ | Primary Hindi dialogue vowel intelligibility | Protected exclusive corridor; score notched out. |
| **Upper-Mids** | $2.0\text{ kHz} – 4.0\text{ kHz}$ | Foley transients (garlic crack, water plink) | Sidechained via FabFilter Pro-MB during speech. |
| **Presence** | $4.0\text{ kHz} – 8.0\text{ kHz}$ | Hindi dental/retroflex consonant clarity | De-essed dynamically on sibilant bursts. |
| **Brilliance / Air** | $8.0\text{ kHz} – 20.0\text{ kHz}$| Open courtyard mist hiss, temple bell overtones | High-shelf air injected into Atmos top height channels. |
