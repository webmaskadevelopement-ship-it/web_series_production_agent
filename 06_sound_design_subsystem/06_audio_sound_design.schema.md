# SCHEMA 06: TECHNICAL AUDIO & DOLBY ATMOS SOUND DESIGN (`06_audio_sound_design.schema.md`)

*(Scraped from professional Pro Tools HDX DM&E mix templates and Dolby Atmos theatrical specifications)*

Every Scene and Shot in `06_Audio_Sound_Design_File.md` MUST specify the **Pro Tools HDX Bus & Loudness Architecture**, **Room Acoustics & Frequency Allocation Matrix**, and **Shot-by-Shot Multi-Stem Cue Sheet**:

```json
{
  "audio_and_sound_design_system": {
    "scene_id": "SCN_01",
    "delivery_and_mix_spec": {
      "format": "Dolby Atmos 7.1.4 Theatrical Home Master (96 kHz / 24-bit) + 5.1 & Stereo Downmix",
      "protools_dme_stem_architecture": [
        "STEM_01_fDx (Dialogue Routing Folder: 8 Production Dx Tracks + 4 ADR Tracks + 2Dx Futz/Worldize Tracks)",
        "STEM_02_fVO (Voiceover Master Bus with Sidechain Send to Mx and BG)",
        "STEM_03_fFoley (Foley Routing Folder: Cloth_Mono, Footsteps_L/R, Specific_Props_Mono/Stereo)",
        "STEM_04_fFxA (Hard / Diegetic Spot Effects: Water, Doors, Metal, Weather Transients)",
        "STEM_05_fFxB (Designed / Subjective Psychological Sound Effects & Sub-Bass LFE Pulses)",
        "STEM_06_fBG (Backgrounds & Ambiences: Quad Surround Beds + Top Height Air Beds)",
        "STEM_07_fMx (Score & Acoustic Raga Instrumentation Bus)"
      ],
      "loudness_and_limiter_targets": {
        "integrated_program_loudness": "-24.0 LKFS (+/- 0.5 LU, ITU-R BS.1770-4)",
        "dialogue_gated_anchor": "-27.0 LKFS",
        "maximum_true_peak": "-2.0 dBTP (Avid Pro Limiter / FabFilter Pro-L2 on Print Master)",
        "Maximum_short_term_3s": "-18.0 LUFS",
        "lfe_low_pass_filter": "120 Hz brickwall 24 dB/oct roll-off"
      }
    },
    "architectural_acoustics_and_reverb_engine": {
      "location_uuid": "LOC_01 (Varanasi Sandstone Haveli Courtyard)",
      "cubic_volume_and_surfaces": "384 m³ open-zenith stone courtyard; 80% wet Chunar sandstone & lime plaster (absorption coefficient 0.04 at 1 kHz), 20% open sky (absorption 1.00)",
      "impulse_response_parameters": {
        "convolution_preset": "Altiverb 8 Custom IR: Stone Courtyard with Pillared Veranda",
        "pre_delay_ms": 28,
        "rt60_decay_time": "1.45s @ 500 Hz | 1.62s @ 1 kHz | 0.95s @ 4 kHz (dampened by high monsoon humidity)",
        "early_reflections_to_tail_ratio": "+4.5 dB early slap off stone pillars at 14ms and 22ms"
      }
    },
    "frequency_spectrum_allocation_7band": {
      "sub_bass_20_60hz": "LFE psychological tension drone & distant monsoon thunder roll (High-passed off all Dx and Foley tracks)",
      "bass_60_250hz": "RaghavVO chest fundamental (98–140 Hz) and heavy teakwood door resonance",
      "low_mids_250_500hz": "Warmth of Sarangi body and courtyard rain-air bed (carved -3.5 dB whenever Dx is active)",
      "midrange_500_2khz": "Primary vowel intelligibility zone for Savitri and Raghav's Hindi dialogue",
      "upper_mids_2khz_4khz": "Foley transient definition (garlic skin crack, umbrella water drop impact, brass thali contact) — sidechained via FabFilter Pro-MB (-4 dB ducking) during consonant speech",
      "presence_4khz_8khz": "Hindi dental/retroflex consonant clarity ('त/ट', 'द/ड', 'श/ष/स')",
      "brilliance_air_8khz_20khz": "Fine monsoon mist hiss in Height channels (Ltf/Rtf/Ltr/Rtr), distant Ganga temple bell overtones"
    },
    "shot_wise_audio_cue_matrix": [
      {
        "linked_shot_uid": "ACT1_SCN01_SHT01A",
        "timecode_span": "00:00:00:00 – 00:00:06:12",
        "dialogue_and_vo_cues": [
          {
            "track": "VO_1 (Center Channel Object)",
            "cue_ref": "VO_CUE_001",
            "level_lufs": "-24.0 LKFS",
            "panning_xyz": "X: 0.00 (Center), Y: -1.00 (Screen Front), Z: 0.00 (Ear Height), Size: 0%"
          }
        ],
        "foley_cues": [
          {
            "foley_id": "FOL_01A_01",
            "category": "Prop / Domestic Handling",
            "sound_description": "Dry fibrous crack and peel of papery garlic husk between weathered thumb and index finger, followed by clove dropping onto tarnished brass thali.",
            "recording_spec": "Sennheiser MKH 8040 hyper-cardioid at 12cm in dead Foley pit; transient boosted +3 dB @ 3.4 kHz.",
            "sync_frames": ["Frame 26", "Frame 88", "Frame 134"],
            "level_db": "-22.0 dBFS",
            "panning_xyz": "X: +0.42 (Right-Center matching Savitri's screen position), Y: -0.85, Z: -0.35 (Floor plane)"
          },
          {
            "foley_id": "FOL_01A_02",
            "category": "Cloth & Movement",
            "sound_description": "Heavy wet linen sleeve slight tension rub as Raghav tightens grip on wooden umbrella handle.",
            "sync_frames": ["Frame 52"],
            "level_db": "-31.0 dBFS",
            "panning_xyz": "X: -0.48 (Left-Center), Y: -0.90, Z: 0.00"
          }
        ],
        "spot_sfx_cues": [
          {
            "sfx_id": "SFX_01A_01",
            "stem": "fFxA (Hard Diegetic)",
            "sound_description": "Individual heavy rainwater droplets detaching from nylon umbrella tip and striking porous Chunar sandstone with a hollow liquid 'plink'.",
            "sync_frames": ["Frame 16", "Frame 51", "Frame 86", "Frame 121", "Frame 156 (Cut Point)"],
            "level_db": "-20.5 dBFS (Frame 156 final drop boosted +2.5 dB to drive hard cut to Shot 01B)",
            "panning_xyz": "X: -0.45, Y: -0.80, Z: -0.60 (Sent 18% to Courtyard Stone Convolution Reverb)"
          }
        ],
        "background_ambience_beds": [
          {
            "bg_id": "BG_01A_01",
            "layer_name": "AMB_Varanasi_Haveli_Courtyard_Dusk_Rain_Air",
            "level_db": "-34.0 dBFS",
            "panning_xyz": "7.1.2 Bed: Wide surround decorrelated field + Ltf/Rtf Top Height channels carrying soft overhead drizzle air"
          },
          {
            "bg_id": "BG_01A_02",
            "layer_name": "AMB_Distant_Ghat_Aarti_Bells_Worldized",
            "processing": "Low-pass filter @ 1.6 kHz + Altiverb 'Behind Thick Stone Wall' occlusion IR",
            "level_db": "-38.0 dBFS",
            "panning_xyz": "X: +0.85 (Right Surround Rear), Y: +0.60, Z: +0.20"
          }
        ],
        "musical_score_cues": [
          {
            "music_id": "MX_01A_01",
            "cue_title": "M1_Unspoken_Threshold",
            "entry_timecode": "00:00:04:00 (Frame 96)",
            "raga_and_scale": "Raga Marwa (Thaat Marwa: Sa, Komal Re, Ga, Tivra Ma, Dha, Ni — omits Pancham/5th entirely to deny harmonic resolution)",
            "instrumentation": "Solo bowed acoustic Sarangi (playing sustained Komal Re -> Ga microtonal meend) + sub-octave Tanpura drone on C#1 (34.6 Hz)",
            "level_db": "-28.5 dBFS"
          }
        ]
      }
    ]
  }
}
```
