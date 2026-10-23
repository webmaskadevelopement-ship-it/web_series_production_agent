# VOCAL DSP SIGNAL CHAIN, EQ & COMPRESSION (`technical_brain/05_vocal_dsp_signal_chain_eq_compression.md`)

## 1. HARDWARE PREAMP & CONVERSION
- **Analog Preamp:** Neve 1073OPX Class-A discrete transformer preamp ($+42\text{ dB}$ gain, $1200\ \Omega$ input impedance for harmonic richness in the $100\text{ Hz}-300\text{ Hz}$ chest zone).
- **A/D Conversion:** Lavry Blue / Burl Mothership running at $24\text{-bit} / 96\text{ kHz}$ uncompressed PCM.

---

## 2. 7-STAGE INSERT PLUGIN ORDER OF OPERATIONS
1. **iZotope RX Mouth De-Click:** Sensitivity `3.5`. Eliminates wet saliva clicks while retaining intentional lip separation transients.
2. **FabFilter Pro-Q 3 (Subtractive):**
   - $24\text{ dB/oct}$ High-Pass filter at $72\text{ Hz}$.
   - Dynamic notch $-3.2\text{ dB}$ at $285\text{ Hz}$ ($Q = 4.2$, removes haveli study boxiness).
   - Dynamic notch $-2.5\text{ dB}$ at $3.8\text{ kHz}$ (smooths harsh retroflex sibilance).
3. **UAD 1176LN (Fast Peak Catcher):** Ratio `4:1`, Attack `4` ($400\ \mu\text{s}$), Release `7` ($50\text{ ms}$), catching only transient spikes ($-2\text{ dB}$ max gain reduction).
4. **Teletronix LA-2A Silver (Optical Leveler):** Smooth leveling ($-3.5\text{ dB}$ average GR) locking intimate dynamics.
5. **FabFilter Pro-DS (De-Esser):** Split-band de-essing active between $5.5\text{ kHz}$ and $9.2\text{ kHz}$ ($-4\text{ dB}$ threshold).
6. **Pultec EQP-1A (Additive Air & Weight):** $+1.5\text{ dB}$ warm boost at $100\text{ Hz}$; $+2.0\text{ dB}$ silky air shelf at $12\text{ kHz}$.
7. **Altiverb 8 (Convolution Reverb Aux Send):** $6\%$ wet mix of *Small Wooden Study with Bookshelves* (Pre-delay: $22\text{ ms}$, RT60: $0.32\text{s}$, High-cut: $4.5\text{ kHz}$).
8. **Master Delivery Target:** Integrated $-24.0\text{ LKFS}$ ($\pm 0.5\text{ LU}$), True Peak $-2.0\text{ dBTP}$.
