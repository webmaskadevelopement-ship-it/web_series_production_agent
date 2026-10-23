# SCHEMA 03: VOICEOVER & ACOUSTIC PROSODY SYSTEM (`03_voiceover_prosody.schema.md`)

Every Voiceover cue in `03_Voiceover_System.md` MUST be defined by the **Global Narrator & Studio Signal Chain Architecture** followed by **Shot-Synced Prosody & Phonetic Cue Cards**:

```json
{
  "voiceover_master_system": {
    "narrator_psychological_persona": {
      "narrator_id": "VO_NARRATOR_01",
      "linked_character_uuid": "CHAR_01 (Aged 20 years forward from story events)",
      "narrative_vantage_point": "Retrospective Confessional — speaking from an empty room long after the haveli was demolished",
      "vocal_age_and_physiology": "54 years old; slightly reduced lung vital capacity; subtle laryngeal tension on words connected to his mother",
      "timbre_and_resonance": "Warm, dry chest-dominant baritone (Fundamental frequency F0: 98 Hz – 115 Hz); slight gravel/vocal fry on phrase endings",
      "dialect_and_phonetic_profile": "Educated Khari Boli Hindi with softened Purvanchali vowel rounding and crisp dental/retroflex distinction"
    },
    "studio_recording_and_dsp_chain": {
      "acoustic_room_spec": "Dead ADR isolation booth (Noise floor: NC-15, RT60: 0.14 seconds at 500 Hz)",
      "microphone_rig": {
        "model": "Neumann U87 Ai Large-Diaphragm Condenser (coupled with Schoeps CMC641 backup boom at 45cm)",
        "polar_pattern": "Cardioid",
        "distance_and_angle": "14 cm from lip plane, 15° off-axis horizontally to prevent Devanagari 'प/फ/ब/भ' (labial aspirate) plosives without dulling high transients",
        "pop_filtration": "Dual-layer Stedman Proscreen XL metal mesh"
      },
      "preamp_and_conversion": "Neve 1073OPX Class-A Preamp (+42 dB gain, 1200 Ohm impedance for low-mid harmonic thickness) -> 24-bit / 96 kHz PCM",
      "insert_plugin_chain_order": [
        "01_Izotope_RX_Mouth_DeClick: Sensitivity 3.5 (removes wet saliva clicks while retaining intentional dry lip separation)",
        "02_FabFilter_Pro_Q3_Subtractive: 24 dB/oct High-Pass @ 72 Hz; Dynamic notch -3.2 dB @ 285 Hz (boxiness); -2.5 dB @ 3.8 kHz (harsh retroflex sibilance)",
        "03_UAD_1176LN_Fast_Peak_Catcher: Ratio 4:1, Attack 4, Release 7, catching only +6 dB transient spikes (-2 dB max GR)",
        "04_Teletronix_LA2A_Silver_Leveler: Smooth optical leveling (-3.5 dB average GR) to lock intimate whisper-to-speech dynamics",
        "05_FabFilter_Pro_DS: Split-band de-essing between 5.5 kHz and 9.2 kHz (-4 dB threshold)",
        "06_Pultec_EQP1A_Additive: +1.5 dB warm boost @ 100 Hz; +2.0 dB silky air boost @ 12 kHz",
        "07_Altiverb_8_Aux_Send: 6% wet mix of 'Small Wooden Study with Bookshelves' (Pre-delay: 22ms, RT60: 0.32s, High-cut @ 4.5 kHz)"
      ],
      "loudness_calibration": "Integrated -24.0 LKFS | True Peak -2.0 dBTP | Sidechain triggers -3.5 dB dynamic dip on Score stem at 800 Hz – 3.5 kHz"
    },
    "voiceover_cue_ledger": [
      {
        "vo_cue_id": "VO_CUE_001",
        "act_scene_shot_link": "ACT1_SCN01_SHT01A",
        "timecode_in": "00:00:01:12",
        "timecode_out": "00:00:06:04",
        "total_duration_seconds": 4.66,
        "text_layers": {
          "devanagari_annotated": "कुछ घर ईंट और पत्थर से नहीं... [INHALE_NOSE_0.4s] [HOLD_0.5s] अधूरे वादों की नमी से बने होते हैं। [EXHALE_TRAIL_0.6s]",
          "ipa_and_roman_phonetic": "kʊtʃʰ ɡʱər iːɳʈ ɔːr pət̪t̪ʰər seː nəɦiː... [0.9s PAUSE] əd̪ʱuːreː ʋɑːd̪oːŋ kiː nəmiː seː bəneː ɦoːt̪eː ɦɛ̃ː.",
          "english_dramatic_translation": "Some homes aren't built of brick and stone... they are built from the dampness of unkept promises."
        },
        "prosody_and_suprasegmentals": {
          "overall_tempo_wpm": 86,
          "syllable_rate": "3.1 syllables/second",
          "fundamental_pitch_curve_hz": "Starts at 112 Hz on 'कुछ घर' -> rises slightly to 118 Hz on 'पत्थर' -> drops across the 0.9s pause to 96 Hz on 'अधूरे' -> ends in an unvoiced 90 Hz vocal-fry trail on 'होते हैं'.",
          "word_stress_weights": {
            "ईंट (eent)": "Primary dental-retroflex crisp attack (+2 dB)",
            "अधूरे (adhoore)": "Elongated 'oo' vowel (380ms duration) with breathy aspirated 'dh'",
            "नमी (nami)": "Soft nasalized intimacy, 30% higher breath-to-tone ratio"
          },
          "respiratory_and_mouth_cues": "00:01:08 (4 frames before speech): Subtle dry lip part. 00:03:06: Slow closed-mouth nasal inhale (0.4s) followed by 0.5s glottal suspension before delivering the second clause."
        }
      }
    ]
  }
}
```
