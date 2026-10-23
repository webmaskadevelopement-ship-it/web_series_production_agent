# FIXED 12-NODE DAVINCI RESOLVE TREE ARCHITECTURE (`technical_brain/02_fixed_12_node_davinci_resolve_tree_architecture.md`)

## 1. THE 12-NODE FIXED SIGNAL FLOW
To ensure non-destructive, reproducible color science, every shot grading specification must adhere strictly to this 12-node order of operations:

1. **Node 01 [CST In / IDT]:** ARRI LogC4 / AWG4 $\rightarrow$ DaVinci Wide Gamut / Intermediate.
2. **Node 02 [Raw Exposure & Denoise]:** Temporal Noise Reduction (2 frames, Better) + Master Exposure Offset (EV).
3. **Node 03 [Primary Balance & Printer Lights]:** Quarter-light RGB printer point trims ($+1.25\text{ R}, 0.00\text{ G}, +0.75\text{ B}$) + Tint offset.
4. **Node 04 [Contrast & Pivot]:** Photochemical S-curve contrast ($+14.0$) at $0.385$ pivot with HDR shadow recovery.
5. **Node 05 [Subtractive Density (HSV)]:** Node color space set to HSV; H & S disabled; Gamma pull on Luma ($-0.06$) for rich subtractive color density.
6. **Node 06 [Color Wheels Split-Toning]:** Slate-teal into Lift, warm ochre into Gamma, $2200\text{K}$ golden-amber into Gain.
7. **Node 07 [HSL 6-Vectors]:** Hue, Saturation, and Luminance shifts across Red, Yellow, Green, Cyan, Blue, Magenta.
8. **Node 08 [Skin-Tone Qualifier]:** 3D qualifier isolating actor skin along the Vectorscope I-line; protects Indian melanin from shadow cyan bleed.
9. **Node 09 [Power Windows & Relighting]:** Soft tracked radial window boosting warm gain on brass diya (`PROP_02`); top-down cool linear gradient on left doorway.
10. **Node 10 [Halation & Highlight Bloom]:** 35mm red-layer scatter ($18\%$) and organic highlight bloom ($22\%$).
11. **Node 11 [FPE Print Film LUT / ODT]:** Kodak 2383 D60 Print Emulation transform to Rec.709 Gamma 2.4.
12. **Node 12 [Film Grain & Vignette]:** Live-scanned 35mm 500T 4-perf grain overlay + elliptical anamorphic vignette ($-0.22\text{ EV}$).
