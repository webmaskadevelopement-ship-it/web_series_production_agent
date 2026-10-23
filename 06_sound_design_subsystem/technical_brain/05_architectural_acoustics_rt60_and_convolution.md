# ARCHITECTURAL ACOUSTICS, RT60 & CONVOLUTION (`technical_brain/05_architectural_acoustics_rt60_and_convolution.md`)

## 1. SABINE REVERBERATION CALCULATION
Reverberation time ($RT_{60}$) in seconds is calculated via the Sabine formula:

$$RT_{60} = \frac{0.161 \times V}{\sum (S_i \times \alpha_i)}$$

Where:
- $V$: Cubic volume of room ($384\text{ m}^3$ for haveli courtyard).
- $S_i$: Surface area of boundary elements (stone slabs, plaster walls, open sky).
- $\alpha_i$: Absorption coefficient (Chunar sandstone: $\alpha = 0.04$ at $1\text{ kHz}$; open sky zenith: $\alpha = 1.00$).

---

## 2. REVERB ENGINE PARAMETERS (SCENE 01)
- **Convolution Engine:** Audio Ease Altiverb 8 Custom IR: *Varanasi Sandstone Pillared Courtyard*.
- **Pre-Delay:** $28\text{ ms}$ (representing sound travel to closest colonnade pillar).
- **Multi-Band RT60:**
  - $500\text{ Hz}$: $1.45\text{ seconds}$
  - $1.0\text{ kHz}$: $1.62\text{ seconds}$
  - $4.0\text{ kHz}$: $0.95\text{ seconds}$ (dampened by high monsoon air humidity).
- **Early Reflections to Tail Ratio:** $+4.5\text{ dB}$ early slap off sandstone pillars at $14\text{ ms}$ and $22\text{ ms}$.
