# VOCAL DSP SIGNAL CHAIN: EQ, COMPRESSION & REVERB SPACE (`05_vocal_dsp_signal_chain_eq_compression.md`)

## 1. THE 6-STAGE ENTERPRISE ADR MASTERING CHAIN
The recorded voiceover must sit flawlessly in the 5.1 / Dolby Atmos theatrical mix, floating above the musical score (*fMx*) and atmospheric Foley (*fFx*) without masking them.

The Voiceover Subsystem defines a **Rigorous 6-Stage Hardware & Plugin DSP Chain**:

```text
[Microphone: U87/MKH416] 
  ──> 01_Neve 1073 Preamp (+42dB Gain, HPF 80Hz)
  ──> 02_iZotope RX Mouth De-Click (Sensitivity 3.2)
  ──> 03_FabFilter Pro-Q3 (Surgical Clean-up & Presence Notch)
  ──> 04_UAD 1176LN Peak Limiter (4:1 Ratio, Fast Attack/Release)
  ──> 05_Teletronix LA-2A Optical Leveler (Smooth 3-4dB RMS compression)
  ──> 06_Altiverb 8 Convolution Space Send (Acoustic Room Matching)
  ──> MASTER VO BUS (-24 LKFS / -2.0 dBTP)
```

---

## 2. SURGICAL EQ FREQUENCY TARGETS (FABFILTER PRO-Q3)
1. **High-Pass Filter:** 24 dB/octave cut at **75 Hz** (cleans out HVAC rumble and sub-harmonic plosives).
2. **Mud & Chest Boxiness Cut:** Dynamic notch cut of **-2.5 dB to -3.5 dB between 280 Hz and 340 Hz** (Q: 2.2). Essential for Indian male baritones.
3. **Nasal Resonance Cut:** Narrow dynamic notch of **-2.0 dB at 920 Hz** to tame thin nasal acoustic overtones.
4. **Retroflex Harshness Tamer:** Dynamic notch of **-2.8 dB at 3.8 kHz to 4.2 kHz** (clamps down on harsh retroflex dental clicks).
5. **Presence & Air Lift:** Gentle high shelf of **+1.8 dB at 11 kHz** for modern cinematic openness.

---

## 3. COMPRESSION & GAIN-STAGING DYNAMICS
- **Peak Limiting (UAD 1176LN):**
  - Ratio: `4:1` | Attack: 20 microseconds (Position 6) | Release: 80 milliseconds (Position 7).
  - Target Gain Reduction: Maximum **-2 dB to -3 dB** on occasional consonants (`क, ट, प`).
- **Optical RMS Leveling (Teletronix LA-2A):**
  - Peak Reduction knob tuned for **-3 dB to -5 dB** smooth compression on active words.
  - Locks whisper-to-speech intimacy into a uniform RMS pocket without audible pumping.

---

## 4. BROADCAST & STREAMING DELIVERY COMPLIANCE
- **Integrated Loudness:** **`-24.0 LKFS / LUFS`** (±0.5 LUFS) adhering to EBU R128 and ITU-R BS.1770-4.
- **Maximum True Peak:** **`-2.0 dBTP`** (prevents inter-sample clipping across lossy AAC/MP3 decoders).
- **Sidechain Ducking Directive:** Voiceover bus sends a sidechain control signal to the Music Score Bus, automatically dipping score volume by **-3.5 dB** across the 600 Hz–3.5 kHz midrange during active voice syllables.
