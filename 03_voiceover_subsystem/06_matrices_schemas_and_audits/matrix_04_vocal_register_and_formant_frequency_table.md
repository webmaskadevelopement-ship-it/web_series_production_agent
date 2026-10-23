# MATRIX 04: VOCAL REGISTER & FORMANT FREQUENCY TABLE (`matrix_04_vocal_register_and_formant_frequency_table.md`)

## 1. THE ACOUSTIC FORMANT MATRIX FOR VOICE DIRECTORS & DSP ENGINEERS

| Vocal Register | Pitch Range ($F_0$) | Dominant Gender / Age | First Formant ($F_1$) | Second Formant ($F_2$) | Third Formant ($F_3$) | Studio Microphone Choice | Preamp & EQ Recipe |
|---|:---:|---|:---:|:---:|:---:|---|---|
| **Deep Bass (गंभीर मंद्र)** | 75 Hz – 98 Hz | Mature Male (50–70 yrs) | 280 Hz – 380 Hz | 850 Hz – 1100 Hz | 2100 Hz – 2400 Hz | Neumann U87 Ai (Cardioid, 12cm) | Neve 1073: +40dB, HPF @ 60Hz; Pro-Q3: -3dB @ 300Hz |
| **Gravel Baritone (खुरदुरा मध्य)** | 95 Hz – 125 Hz | Adult Male (35–55 yrs) | 350 Hz – 480 Hz | 1100 Hz – 1400 Hz | 2300 Hz – 2700 Hz | Sennheiser MKH 416 (Shotgun, 18cm) | API 512c: +44dB; Pro-Q3: -2.5dB @ 340Hz, +2dB @ 4kHz |
| **Clear Tenor (तार स्वर)** | 130 Hz – 175 Hz | Young Male (18–30 yrs) | 450 Hz – 600 Hz | 1400 Hz – 1800 Hz | 2600 Hz – 3100 Hz | Schoeps MK41 (Supercardioid, 22cm) | Grace Design m101: Linear; Pro-Q3: +1.5dB @ 2.8kHz |
| **Earthy Contralto (गहरा स्त्री स्वर)** | 140 Hz – 185 Hz | Mature Female (40–65 yrs) | 400 Hz – 550 Hz | 1300 Hz – 1700 Hz | 2500 Hz – 3000 Hz | Neumann U87 Ai (Cardioid, 15cm) | Neve 1073: HPF @ 80Hz; Pro-Q3: -2dB @ 400Hz |
| **Warm Mezzo-Soprano (मधुर स्त्री मध्य)** | 180 Hz – 240 Hz | Adult Female (25–45 yrs) | 500 Hz – 700 Hz | 1600 Hz – 2100 Hz | 2800 Hz – 3400 Hz | AKG C414 XLS (Cardioid, 16cm) | Avalon Vt-737sp: Optical leveling, +1dB air @ 12kHz |
| **Lyrical Soprano (उच्च तार स्त्री)** | 240 Hz – 350 Hz | Young Female / Child | 650 Hz – 900 Hz | 2000 Hz – 2600 Hz | 3200 Hz – 4000 Hz | Neumann TLM 103 (Cardioid, 20cm) | Millennia HV-3C: Ultra-clean; De-Esser @ 6.5kHz |

---

## 2. DSP DE-ESSING AND RESONANCE SUPPRESSION DIRECTIVE
- For **Deep Bass & Baritones**, retroflex clicks and plosives peak between 3.6 kHz and 4.4 kHz. FabFilter Pro-DS must be sidechained to this specific band with a 1.2ms lookahead.
- For **Mezzo & Soprano voices**, sibilants (`स, श, ज़`) peak between 6.2 kHz and 8.5 kHz. Engagement of dynamic notch filtering prevents piercing ear fatigue on AirPods and mobile speakers.
