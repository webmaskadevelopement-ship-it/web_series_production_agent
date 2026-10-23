# AUDIT 02: RHYTHM, SYLLABLE & THEHRAAV VERIFIER (`audit_02_rhythm_syllable_and_thehraav_verifier.md`)

## 1. MATHEMATICAL TIMECODE SYNC VERIFICATION
This audit verifies that the generated voiceover cue physically fits within the timecode boundaries of the assigned shot in `02_Shot_Breakdown.pdf`.

$$	ext{Calculated Duration} = rac{	ext{Devanagari Syllables}}{SyllableRate(WPM)} + \sum 	ext{Pause Durations} \le 	ext{Shot Duration (Seconds)}$$

- **Slack Buffer Rule:** Every voiceover cue MUST leave at least **0.5 seconds of clean head room** after shot In-point, and **0.5 seconds of tail room** before shot Out-point.
- **Thehraav Ratio:** In dramatic and grief scenes, silence duration must constitute **between 25% and 40%** of the total cue duration.
