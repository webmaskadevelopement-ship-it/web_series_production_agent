# SCHEMA 05: COLOR GRADING & DI COLOR SCIENCE BIBLE (`05_color_grading_di.schema.md`)

*(Expands your `color_grading_emulation_system` JSON reference to include full ACEScct/DaVinci Wide Gamut color management, Printer Lights, 12-Node Fixed Signal Flow, Subtractive Density, Skin-Tone Protection, and Kodak 2383 Photochemical Print Emulation)*

Every Scene and Key Shot in `05_Color_Grading_File.md` MUST contain both the **Creative Colorist Look Analysis** and the **Complete DaVinci Resolve Emulation & 12-Node Technical Specification**:

```json
{
  "color_grading_emulation_system": {
    "metadata": {
      "look_id": "LOOK_ACT1_SCN01_MONSOON_DUSK_DIYA",
      "linked_scene_and_shots": "SCN_01 (Master Look applied to Shots 01A–01R, with per-shot trim offsets)",
      "title": "Varanasi Monsoon Twilight & Mustard-Oil Chiaroscuro",
      "reference_image": "Rain-soaked Pink-Ochre Sandstone Courtyard under 6800K Zenith Twilight with 2200K Practical Oil Flame",
      "mood": "Cinematic, Melancholic, Tactile, Oppressive, Nostalgic, High-Tension",
      "dominant_rasa_chromatic_mapping": "Karuna (Pathos) — Split-complementary tension between cold slate-cyan shadows (#1B262C) and bruised amber-gold highlights (#D9822B)",
      "negative_film_stock_emulation": "Kodak Vision3 500T 5219 (Tungsten balanced negative response)",
      "suggested_lut": "Kodak 2383 Print Film Emulation (D60 White Point Curve) inside DaVinci Wide Gamut",
      "time_of_day": "Dusk / Blue Hour transitioning to Night (18:15 IST)"
    },
    "color_management_pipeline": {
      "input_device_transform_idt": "ARRI LogC4 / ARRI Wide Gamut 4",
      "working_color_space": "DaVinci Wide Gamut (DWG) / DaVinci Intermediate (Scene-Referred 32-bit Float)",
      "output_device_transform_odt": "Rec.709 Gamma 2.4 (Broadcast/Web) & DCI-P3 D65 ST.2084 (Theatrical Mastering)"
    },
    "global_parameters": {
      "white_balance": {
        "temperature": "-150K offset on ambient bed (preserving 6800K cold twilight); +350K localized window on diya pool",
        "tint": "+6.5 (Subtle shift toward magenta/sepia to prevent digital green cast in wet stone shadows)"
      },
      "printer_lights_offset": {
        "red_printer_points": "+1.25 (Quarter-light increments)",
        "green_printer_points": "0.00",
        "blue_printer_points": "+0.75",
        "master_exposure_ev": "-0.35 EV (Underexposed to protect diya core and deepen architectural negative space)"
      },
      "contrast": "+14.0 (Firm photochemical toe, high midtone separation)",
      "contrast_pivot": "0.385 (Pivoted slightly below LogC4 middle grey to expand shadow micro-contrast)",
      "saturation": "-8.0 (Global saturation pull to avoid digital neon clipping)",
      "subtractive_color_density": "+22.0 (Deeper Helmholtz-Kohlrausch luminance darkening on saturated reds, ochres, and blues)",
      "hdr_whites": "+12.0 (Pushing specular intensity on wet floor droplets and flame tip)",
      "hdr_blacks": "-18.0 (Firming the 4–8 IRE shadow floor in deep veranda arches)",
      "hdr_shadows": "+10.0 (Opening texture in damp sandstone between 10–22 IRE)",
      "hdr_highlights": "-28.0 (Compressing 80–98 IRE shoulder for smooth filmic roll-off)"
    },
    "color_wheels": {
      "lift_shadows": {
        "red": "-0.035",
        "green": "-0.005",
        "blue": "+0.045",
        "luma": "-0.015",
        "description": "Injects a dense, cold slate-teal monsoon shadow floor into the unlit sandstone walls and arches."
      },
      "gamma_midtones": {
        "red": "+0.065",
        "green": "+0.020",
        "blue": "-0.055",
        "luma": "-0.010",
        "description": "Warms skin tones and midtone stone surfaces toward earthy ochre-amber without contaminating the deepest blacks."
      },
      "gain_highlights": {
        "red": "+0.140",
        "green": "+0.085",
        "blue": "-0.165",
        "luma": "+0.020",
        "description": "Creates the rich 2200K golden-amber glow in the oil lamp pool and specular water reflections."
      },
      "offset_global": {
        "red": "+25.5",
        "green": "+25.0",
        "blue": "+24.2",
        "description": "Scene-referred global balance trim prior to contrast pivot."
      }
    },
    "hsl_qualifier_and_six_vectors": {
      "red": {
        "hue": "+4.0 (Shift slightly toward rust/terracotta)",
        "saturation": "+12.0",
        "luminance": "-15.0 (Subtractive film density on red sandstone and sindoor)"
      },
      "yellow": {
        "hue": "-8.0 (Push yellow flame toward deep amber-orange)",
        "saturation": "+24.0",
        "luminance": "+10.0"
      },
      "green": {
        "hue": "-18.0 (Shift courtyard moss/foliage toward decayed olive-ochre)",
        "saturation": "-35.0",
        "luminance": "-12.0"
      },
      "cyan": {
        "hue": "+6.0 (Push twilight sky reflection toward deep petrol-blue)",
        "saturation": "-10.0",
        "luminance": "-8.0"
      },
      "blue": {
        "hue": "-4.0 (Shift toward slate-cyan to harmonize with amber highlights)",
        "saturation": "-25.0 (Controlled desaturation so evening shadows feel natural, not sci-fi)",
        "luminance": "-14.0"
      },
      "orange_skin_tone_protection": {
        "vectorscope_skin_line_lock": true,
        "hue": "+1.5",
        "saturation": "+8.0",
        "luminance": "-4.0 (Preserves rich Indian Type IV-V melanin density without blowing out highlights)"
      }
    },
    "curves": {
      "luma_curve": "Classic Kodak 2383 S-curve: Anchor black point at [0.00, 0.03], toe inflection at [0.18, 0.14], middle grey locked at [0.40, 0.40], shoulder compression starting at [0.75, 0.82], soft ceiling roll-off at [1.00, 0.96].",
      "red_channel": "Subtle dip in bottom 10% (cooling blacks), lifted +4% across 0.35–0.85 range for warm midtone/highlight dominance.",
      "green_channel": "Linear neutral anchor from 0.00 to 0.70, slight +2% lift in upper shoulder to prevent magenta highlight skew.",
      "blue_channel": "Lifted +3% in 0.05–0.20 shadow toe (slate-blue shadows), pulled down -12% in 0.65–1.00 highlights (golden D60 print roll-off).",
      "luma_vs_saturation_curve": "Roll off saturation to 0% at Luma 0.00–0.05 (clean neutral blacks) and Luma 0.92–1.00 (clean creamy white speculars)."
    },
    "effects_and_finishing": {
      "atmospheric_haze": {
        "enabled": true,
        "color": "#4A6070 (Cool Monsoon Mist in upper frame) & #D98A3C (Warm Diya Glow in lower right)",
        "opacity": "18%",
        "position": "Top 45% of courtyard opening, soft gradient falloff along Z-depth",
        "blur": "0.65 Gaussian radius (Optical diffusion emulation: 1/4 Black Pro-Mist)"
      },
      "glow_bloom": {
        "enabled": true,
        "intensity": "22%",
        "threshold": "0.78 Luma (Affects only the diya flame, tungsten bulb, and wet specular droplets)",
        "spread_radius": "0.42",
        "blend_mode": "Soft Light / Screen hybrid (Gamma-compensated)",
        "color": "#FFE4B5 (Warm Moccasin White)"
      },
      "halation": {
        "enabled": true,
        "emulation_model": "35mm Remjet-stripped red-layer scatter",
        "intensity": "18%",
        "threshold": "0.82 Luma",
        "radius": "0.14 (Tight organic edge bleed)",
        "color": "#E84A27 (Deep Red-Orange fringe around high-contrast lamp cage and doorway silhouettes)"
      },
      "film_grain": {
        "enabled": true,
        "type": "35mm 4-Perf Full Aperture (Kodak Vision3 500T 5219 live scan)",
        "intensity": "0.38 (Medium-fine organic texture)",
        "size": "0.45",
        "softness": "0.25",
        "shadow_mid_highlight_distribution": "Shadows: 60% | Midtones: 100% | Highlights: 35%"
      },
      "vignette": {
        "enabled": true,
        "amount": "-0.22 EV (Natural anamorphic optical illumination falloff)",
        "feather": "85%",
        "roundness": "0.65 (Anamorphic elliptical)",
        "offset_x_y": "X: +0.08, Y: -0.05 (Biased slightly toward Savitri's oil lamp pool)"
      }
    },
    "node_structure_emulation": {
      "node_01_cst_in": "Color Space Transform: ARRI LogC4 / AWG4 -> DaVinci Wide Gamut / DaVinci Intermediate.",
      "node_02_raw_exposure_denoise": "Temporal NR (2 frames, Better, Luma: 4.0, Chroma: 8.0) + Master Exposure Offset (-0.35 EV).",
      "node_03_primary_printer_lights": "Set Quarter-Light RGB Printer Points (+1.25 R, 0.00 G, +0.75 B) and White Balance Tint (+6.5).",
      "node_04_contrast_and_pivot": "Apply filmic S-curve contrast (+14.0) at 0.385 pivot with HDR shadow/highlight recovery.",
      "node_05_subtractive_hsv_density": "Convert node color space to HSV; disable H & S channels; pull Gamma -0.06 on Luma channel for rich subtractive saturation.",
      "node_06_color_wheels_split": "Inject slate-teal into Lift, earthy ochre into Gamma, and 2200K golden-amber into Gain.",
      "node_07_hsl_six_vectors": "Compress green/blue saturation, deepen terracotta reds, and shift yellows toward warm amber.",
      "node_08_skin_tone_qualifier": "3D HSL Qualifier isolating Savitri and Raghav's skin tones along the Vectorscope I-line; protect melanin density from cyan shadow bleed.",
      "node_09_power_windows_relighing": "Soft radial gradient window (+0.45 EV Gain warm boost) tracked to brass diya (PROP_02); linear top-down window (-0.30 EV cool tint) on left doorway.",
      "node_10_halation_and_bloom": "Apply physical red-channel edge halation (18%) and highlight bloom (22%) in scene-referred linear space.",
      "node_11_fpe_print_lut_odt": "Kodak 2383 D60 Print Film Emulation + Output Transform to Rec.709 Gamma 2.4 / P3-D65.",
      "node_12_grain_and_vignette": "Post-LUT 35mm 500T film grain overlay + anamorphic elliptical vignette + Luma-vs-Sat black/white clean-up."
    }
  }
}
```
