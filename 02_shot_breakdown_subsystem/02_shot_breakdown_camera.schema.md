# SCHEMA 02: MASTER SHOT BREAKDOWN & CAMERA OPTICAL BIBLE (`02_shot_breakdown_camera.schema.md`)

*(Expands your `50mm Prime` and `Master Shot Breakdown` JSON references with full Cooke/ARRI `/i` lens metadata, IRE exposure zones, FACS Action Units, Laban efforts, and A3/A4 Tabular PDF layout rules)*

`02_Shot_Breakdown.md` (and `02_Shot_Breakdown.pdf`) MUST render every Act -> Scene -> Shot in **Two Synchronized Formats per Scene**:
1. **The 10-Column Master Production Table** (grouped by Act, then by Scene).
2. **The Deep Technical Decompilation Block** for every individual Shot ID, strictly obeying this schema:

```json
{
  "act_container": {
    "act_id": "ACT_01",
    "act_title": "The Threshold of Return",
    "act_visual_grammar": "Locked-off classical geometry, wide-to-normal focal lengths (32mm–50mm), deep negative fill, high architectural separation.",
    "scenes": [
      {
        "scene_metadata": {
          "scene_number": "SCN_01",
          "location_uuid": "LOC_01",
          "setting_and_location": "INT. SHARMA ANCESTRAL HAVELI - CENTRAL COURTYARD (VARANASI)",
          "time_of_day": "INT./EXT. DUSK (18:15 IST — Blue Hour Zenith + Warm Practical Tungsten/Flame)",
          "dramatic_purpose": "Establish the moral gulf between Raghav (urban legal pragmatism) and Savitri (ancestral permanence).",
          "scene_duration_total": "142.0 seconds (3,408 frames @ 24.000 fps)",
          "total_shots_in_scene": 18,
          "axis_of_action_180_line": "North-South axis connecting Main Threshold (North) to Kitchen Veranda Pillar (South). Camera stays strictly on West side (180° compliant) until Beat 04 reversal."
        },
        "shots": [
          {
            "shot_identity": {
              "shot_uid": "ACT1_SCN01_SHT01A",
              "shot_number": "01A",
              "timecode_in": "00:00:00:00",
              "timecode_out": "00:00:06:12",
              "duration_seconds": 6.5,
              "duration_frames": 156,
              "frame_rate": "24.000 fps (True Cinema Cadence)",
              "shutter_angle_and_speed": "180.0° shutter (1/48 sec exposure time)"
            },
            "camera_and_framing": {
              "shot_type": "Extreme Wide Master (EWS)",
              "camera_angle_vertical": "High Angle (-12.5° pitch downward)",
              "camera_angle_horizontal": "Frontal 0° orthogonal to North Archway (Wes Anderson / Ozu architectural symmetry broken by central pillar)",
              "dutch_roll_angle": "0.0° (Spirit-level locked)",
              "camera_height_from_floor": "1.65 meters",
              "aspect_ratio_and_extraction": "2.39:1 Anamorphic Desqueeze (from 4:3 Open Gate sensor area)"
            },
            "profile": {
              "profile_name": "50mm Prime (Cooke Anamorphic /i Full Frame Plus Special Flare)",
              "lens_identity": {
                "focal_length": "50mm",
                "type": "1.8x / 2x Hybrid Anamorphic Prime Lens",
                "aperture_range": "T2.3–T22",
                "shooting_aperture_t_stop": "T2.8 (1/3 stop closed down from wide open for center crispness)",
                "minimum_focus_distance": "85cm (Front element to film plane)",
                "image_circle_coverage": "46.3mm Full-Frame diagonal",
                "character": "Natural horizontal field of view with vertical anamorphic compression, warm skin-tone rendering ('The Cooke Look'), oval bokeh, gentle astigmatism in outer 15% of frame"
              },
              "sensor_character": {
                "camera_body": "ARRI Alexa 35 (4.6K Super35 / Large Format configuration)",
                "type": "ALEV 4 CMOS cinema sensor with REVEAL Color Science",
                "resolution_and_codec": "4608 x 3164 (ARRIRAW 13-bit uncompressed)",
                "exposure_index_iso": "EI 800 (Enhanced Sensitivity Mode: Off)",
                "dynamic_range": "17.0 stops (9.2 stops above middle grey, 7.8 stops below middle grey)",
                "highlight_rolloff": "Smooth logarithmic shoulder; practical oil flame core holds detail up to 98 IRE",
                "shadow_compression": "Low; retains wet sandstone porosity between 6 IRE and 18 IRE",
                "noise": "Minimal at EI 800; organic unsharpened luminance grain structure (-52 dB SNR)",
                "color_science": "ARRI Wide Gamut 4 (AWG4) / LogC4 — neutral, high cyan-amber separation, natural melanin skin rendering"
              },
              "movement": {
                "type": "Precision Dolly Push-In on leveled Mitchell tubular track",
                "rig_and_support": "Chapman PeeWee IV Dolly + OConnor 2575D Fluid Head (Drag setting: 4/10)",
                "speed": "Ultra-slow creeping push (8.0 cm/second linear velocity, 0.8s ease-in/ease-out feathering)",
                "axis": "Z-axis forward push along central courtyard symmetry line (52cm total travel)",
                "height": "Constant 1.65m (zero boom/jib vertical delta)",
                "imperfection": 0.0,
                "stabilization": "Hard-mounted on steel track over neoprene vibration pads",
                "motion_blur": "None from camera pan/tilt; subtle radial Z-push parallax; subject micro-motion blur at 180° shutter",
                "note": "The zero-imperfection mechanical creep contrasts with the crumbling organic decay of the haveli."
              },
              "focus_behavior": {
                "type": "Programmed selective focus transition (Preston FI+Z 3-channel wireless control)",
                "rack_focus": "3.0-second sinusoidal rack focus from Foreground Brass Kalash (1.50m at 00:01:00) to Savitri's hands (4.20m at 00:04:00)",
                "focus_hunting": "none (mechanical hard stops locked on follow-focus ring)",
                "focus_plane": "Tilted 0° parallel to sensor plane"
              },
              "depth_of_field": {
                "character": "Shallow-to-moderate anamorphic separation",
                "near_focus_limit": "1.41m at start; 3.82m at end of rack",
                "far_focus_limit": "1.60m at start; 4.66m at end of rack",
                "circle_of_confusion": "0.025mm",
                "bokeh": "2x vertical oval squeeze, smooth cat-eye rounding near frame corners, zero onion-ring artifacts"
              },
              "optical_artifacts": {
                "barrel_distortion": 0.03,
                "edge_softness": 0.06,
                "veiling_glare": 0.05,
                "chromatic_aberration": 0.04,
                "focus_breathing_compensation": "Uncompensated natural Cooke breathing (4% FOV shift during rack)",
                "flaring": "Controlled horizontal amber streak triggered by 2200K brass diya at X:72%, Y:68%"
              },
              "composition_rules": {
                "subject_fidelity": true,
                "environment_fidelity": true,
                "casualness": 0.0,
                "dynamic_symmetry_grid": "Central architectural stone pillar splits frame from X:48% to X:54%, physically walling off CHAR_01 (Left quadrant) from CHAR_02 (Right quadrant)",
                "headroom_and_leadroom": "Excessive oppressive headroom above CHAR_01 (top 35% of frame is dark dripping stone arch)"
              }
            },
            "lighting_and_color": {
              "lighting_mood": "Low-Key Chiaroscuro Dusk — Cold Zenith Skylight vs. Warm Low-Floor Firelight",
              "color_temperature_map": {
                "ambient_zenith_fill": "6800K (Natural Twilight Open Courtyard Sky, CRI 99)",
                "key_practical_source": "2100K (Mustard-oil brass diya flame + concealed Astera NYX bulb dimmed to 12% at 2200K, TLCI 98)",
                "background_accent": "2700K (Flickering 40W tungsten bulb inside corridor cage at Z-depth 9.5m)"
              },
              "photometrics_and_exposure_ire": {
                "skin_key_ire": "Savitri's cheek (lit side): 42 IRE (-0.7 EV under middle grey)",
                "skin_shadow_ire": "Savitri's shadow cheek: 11 IRE (-3.2 EV)",
                "specular_highlight_ire": "Diya flame core: 94 IRE | Wet stone reflection: 58 IRE",
                "black_clip_floor_ire": "Deep corridor recess: 4 IRE (unclipped shadow texture)",
                "shadow_contrast_ratio": "8:1 (3-stop key-to-fill differential)"
              },
              "grip_and_diffusion_rigging": "12x12 Ultra-Bounce Black (Negative Fill) rigged on West veranda to kill bounce on shadow side; 1/4 Grid Cloth over diya key."
            },
            "action_and_performance": {
              "visual_action": "Raghav (CHAR_01) stands immobile on the raised stone threshold, rainwater dripping from the tip of his folded black umbrella (PROP_04) onto the dry red sandstone step. Across the central pillar, Savitri (CHAR_02) sits cross-legged on a low wooden chauki, methodically peeling dry garlic cloves into a tarnished brass thali (PROP_02).",
              "character_blocking_xyz": {
                "CHAR_01": "X: -1.8m (Left of center), Y: +0.15m (Raised step), Z: 6.10m from lens. Body angled 15° toward pillar, feet parallel.",
                "CHAR_02": "X: +1.4m (Right of center), Y: 0.0m (Floor level), Z: 4.20m from lens. Torso pitched forward 20° over brass thali."
              },
              "laban_movement_profile": {
                "CHAR_01": "Effort: Bound Flow + Heavy Weight + Sustained Time + Direct Space ('Press' state — paralyzed by guilt).",
                "CHAR_02": "Effort: Bound Flow + Light Weight + Sustained Time + Direct Space (Mechanical domestic precision masking rage)."
              },
              "psychology_and_subtext": "Neither character acknowledges the other's physical presence; Savitri refuses to grant Raghav the relief of a greeting, forcing him to speak first.",
              "facs_micro_expressions": "CHAR_02: AU4 (Brow Lowerer - Intensity B) + AU17 (Chin Raiser - Intensity C) + AU24 (Lip Pressor - Intensity D); zero blink for 6.5 seconds."
            },
            "audio_and_sound_design": {
              "dialogue_and_vo": "[NO ON-SCREEN DIALOGUE] — Linked to VO_001 ('कुछ घर ईंट और पत्थर से नहीं...') entering at 00:00:01:12.",
              "sfx_and_foley": "1) Rhythmic dry papery crack of garlic skin peeling (`FOL_Garlic_Peel_01` at 00:01:08, 00:03:19). 2) Heavy water drops falling from umbrella tip onto porous stone (`FOL_Umbrella_Drip` every 28 frames).",
              "ambient_room_tone": "Wet courtyard air bed + distant muffled Dashashwamedh Ghat evening bells (`-34 LKFS`, low-passed at 1.8 kHz).",
              "musical_cues": "Cue `M1_Threshold_Drone`: Solo acoustic Sarangi harmonic drone enters on F#2 at 00:04:00 (`-29 LKFS`)."
            },
            "editorial_and_transitions": {
              "in_point_transition": "2.0-second (48-frame) slow dissolve from Black; ambient rain & temple bell audio pre-laps picture by 36 frames (J-Cut).",
              "out_point_transition": "Hard cut on Frame 156 (exact transient frame where the 5th umbrella droplet shatters on the sandstone).",
              "pacing_and_rhythm": "Slow contemplative tension; establishes spatial geography before cutting to 100mm macro insert in Shot 01B.",
              "murch_cut_justification": "1) Emotion (100%): Holds the unbearable awkwardness of arrival. 2) Eye-Trace: Rack focus pulls viewer's eye to Bottom-Right quadrant (`X:68%, Y:72%`), matching exact screen coordinates of Savitri's hands in Shot 01B."
            },
            "vfx_and_post_production": {
              "compositing_cues": "Add subtle 2.5D volumetric monsoon mist drifting down through open courtyard sky zenith (Nuke deep-compositing pass, 12% opacity).",
              "motion_tracking": "Export Cooke `/i` lens metadata (focal distance & T-stop per frame) + 3D camera track solve from sandstone floor joints.",
              "generative_ai_prompts": {
                "midjourney_v6_keyframe": "Cinematic extreme wide master shot, 50mm Cooke Anamorphic lens at T2.8, interior of ancient weathered Varanasi stone haveli courtyard at blue hour dusk, central fluted sandstone pillar dividing the frame in half, on the left a 34-year-old lean Indian man in damp off-white linen shirt stands frozen in arched doorway holding a dripping black umbrella, on the right an elderly Indian woman in faded ochre cotton saree sits on floor peeling garlic into a brass plate illuminated by a single warm 2200K flickering oil diya, 8:1 chiaroscuro contrast, 6800K cold twilight overhead sky vs warm amber floor light, wet stone specular reflections, ARRI Alexa 35, Kodak 2383 film emulation --ar 21:9 --style raw --v 6.1",
                "video_motion_prompt": "Slow mechanical dolly push-in along central courtyard axis at 8cm/s, rack focus from foreground brass water vessel to elderly woman's hands peeling garlic in right midground, rainwater dripping steadily from umbrella tip on left, flickering warm oil lamp shadows."
              },
              "visual_references": "Satyajit Ray's 'Aparajito' Varanasi courtyard staging + Park Chan-wook's 'Decision to Leave' split-frame architectural blocking."
            }
          }
        ]
      }
    ]
  }
}
```
