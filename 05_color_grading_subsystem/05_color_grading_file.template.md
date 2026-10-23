# COLOR GRADING FILE TEMPLATE (`05_color_grading_file.template.md`)

This template dictates how `workspace/exports/05_Color_Grading_File.md` must be constructed:

```markdown
<!-- SCENE COLOR START: {{SCENE_ID}} -->
# {{SCENE_ID}}: COLOR SCIENCE & DI SPECIFICATION
> **Look ID:** `{{LOOK_ID}}` | Linked Shots: {{LINKED_SHOTS_SPAN}}  
> **Master Title:** {{LOOK_TITLE}}  
> **Dominant Rasa:** {{DOMINANT_RASA}} (Chromatic Split: {{CHROMATIC_SPLIT_DESC}})  
> **Film Emulation:** Negative: {{NEGATIVE_STOCK}} | Print LUT: {{PRINT_LUT}}  

---

## 1. COLOR MANAGEMENT PIPELINE
- **IDT (Input Device Transform):** `{{IDT_TRANSFORM}}`
- **Working Timeline Space:** `{{WORKING_COLOR_SPACE}}` (32-bit Float)
- **ODT (Output Device Transform):** `{{ODT_TRANSFORM}}`

---

## 2. GLOBAL PARAMETERS & PRIMARY BALANCE
- **White Balance:** Temp: {{WB_TEMP_OFFSET}} | Tint: {{WB_TINT_OFFSET}}
- **Printer Lights:** Red: {{PRINTER_RED}} | Green: {{PRINTER_GREEN}} | Blue: {{PRINTER_BLUE}}
- **Master Exposure:** {{MASTER_EXPOSURE_EV}} EV
- **Contrast & Pivot:** Contrast: {{CONTRAST_VALUE}} | Pivot: {{CONTRAST_PIVOT}}
- **Subtractive Density:** {{SUBTRACTIVE_DENSITY_VALUE}}

---

## 3. COLOR WHEELS (LIFT / GAMMA / GAIN)
- **Lift (Shadows):** R: {{LIFT_R}} | G: {{LIFT_G}} | B: {{LIFT_B}} | Luma: {{LIFT_LUMA}}
- **Gamma (Midtones):** R: {{GAMMA_R}} | G: {{GAMMA_G}} | B: {{GAMMA_B}} | Luma: {{GAMMA_LUMA}}
- **Gain (Highlights):** R: {{GAIN_R}} | G: {{GAIN_G}} | B: {{GAIN_B}} | Luma: {{GAIN_LUMA}}

---

## 4. SIX-VECTOR HSL QUALIFIER & SKIN-TONE PROTECTION
- **Vectorscope I-Line Lock:** {{SKIN_LINE_LOCKED_BOOL}}
- **Orange / Skin Vector:** Hue: {{SKIN_HUE}} | Sat: {{SKIN_SAT}} | Luma: {{SKIN_LUMA}}
- **Yellows (Flame):** Hue: {{YELLOW_HUE}} | Sat: {{YELLOW_SAT}} | Luma: {{YELLOW_LUMA}}
- **Blues / Cyans (Twilight):** Hue: {{BLUE_HUE}} | Sat: {{BLUE_SAT}} | Luma: {{BLUE_LUMA}}

---

## 5. ANALOG FINISHING: HALATION, GRAIN & OPTICS
- **Halation:** Scatter: {{HALATION_INTENSITY}} | Threshold: {{HALATION_THRESHOLD}} | Color: `{{HALATION_COLOR}}`
- **Glow & Bloom:** Intensity: {{BLOOM_INTENSITY}} | Threshold: {{BLOOM_THRESHOLD}}
- **Film Grain:** Stock: {{GRAIN_STOCK_TYPE}} | Intensity: {{GRAIN_INTENSITY}}
- **Vignette:** Falloff: {{VIGNETTE_EV}} EV | Feather: {{VIGNETTE_FEATHER}}%

---

## 6. FIXED 12-NODE RESOLVE SPECIFICATION & MACHINE JSON
```json
{{COMPILED_COLOR_GRADING_EMULATION_JSON}}
```
<!-- SCENE COLOR END: {{SCENE_ID}} -->
```
