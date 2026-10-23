# ITU-R BS.1770-4 LOUDNESS & CREST DYNAMICS (`technical_brain/03_itu_bs1770_loudness_lufs_and_crest_dynamics.md`)

## 1. CALIBRATED BROADCAST & THEATRICAL TARGETS
Every sound mix in Sub-System 06 must conform to international broadcast and theatrical mastering specs:

| Standard / Metric | Target Value | Tolerance | Mastering Processor |
| :--- | :--- | :--- | :--- |
| **Integrated Program Loudness** | **-24.0 LKFS / LUFS** | $\pm 0.5\text{ LU}$ | ITU-R BS.1770-4 / EBU R128 |
| **Dialogue Gated Anchor** | **-27.0 LKFS** | $\pm 1.0\text{ LU}$ | Dolby Dialogue Intelligence |
| **Maximum True Peak** | **-2.0 dBTP** | Ceiling limit | Avid Pro Limiter / FabFilter Pro-L 2 |
| **Maximum Short-Term Loudness (3s)**| **-18.0 LUFS** | Ceiling limit | TC Electronic LM6 Radar |
| **LFE Low-Pass Filter** | **120 Hz** | $24\text{ dB/oct}$ brickwall | Linear-phase sub-bass crossover |
