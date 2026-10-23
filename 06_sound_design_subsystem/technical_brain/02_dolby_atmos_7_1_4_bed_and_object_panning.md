# DOLBY ATMOS 7.1.4 BED & OBJECT PANNING (`technical_brain/02_dolby_atmos_7_1_4_bed_and_object_panning.md`)

## 1. 3D CARTESIAN ACOUSTIC COORDINATES
In Dolby Atmos 7.1.4 cinema mixing, sound cues are positioned as dynamic 3D objects or fixed surround beds:
- **X-axis (Lateral Width):** $-1.00$ (Left) to $+1.00$ (Right), with $0.00$ at Center.
- **Y-axis (Front-to-Back Depth):** $-1.00$ (Screen Front) to $+1.00$ (Rear Surround Wall).
- **Z-axis (Height):** $-1.00$ (Floor Plane) to $+1.00$ (Ceiling Top Height Speakers).
- **Size / Divergence:** $0\%$ (point source object) to $100\%$ (diffuse room-filling bed).

### Examples from Scene 01
- **Raghav Umbrella Drip (`SFX_01A_01`):** `X: -0.45, Y: -0.80, Z: -0.60` (Floor plane left-center, matching stone contact).
- **Savitri Garlic Peel (`FOL_01A_01`):** `X: +0.42, Y: -0.85, Z: -0.35` (Floor plane right-center, matching wooden chauki).
- **Monsoon Courtyard Rain Air (`BG_01A_01`):** Routed to Top Height channels (`Ltf/Rtf/Ltr/Rtr`) at `Z: +0.80` to simulate open zenith sky.
