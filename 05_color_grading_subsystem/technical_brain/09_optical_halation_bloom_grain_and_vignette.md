# OPTICAL HALATION, BLOOM, GRAIN & VIGNETTE (`technical_brain/09_optical_halation_bloom_grain_and_vignette.md`)

## 1. PHYSICAL ANALOG EMULATION PARAMETERS

### Halation (Red-Layer Scatter)
- **Mechanism:** Red light bouncing off the film base back into the red-sensitive emulsion layer in 35mm film.
- **Intensity:** `18%`.
- **Threshold:** `0.82 Luma`.
- **Radius:** `0.14` (tight edge bleed).
- **Color:** `#E84A27` (Deep Red-Orange fringe around high-contrast lamp filaments, candles, and doorway edges).

### Highlight Bloom
- **Intensity:** `22%`.
- **Threshold:** `0.78 Luma`.
- **Diffusion Blur:** `0.65` Gaussian radius (emulating a 1/4 Black Pro-Mist filter).
- **Color:** `#FFE4B5` (Warm Moccasin White).

### Film Grain
- **Source:** 35mm 4-perf Kodak Vision3 500T 5219 live film scan.
- **Intensity:** `0.38`.
- **Tonal Distribution:** Shadows: $60\%$ | Midtones: $100\%$ | Highlights: $35\%$.

### Vignette
- **Type:** Anamorphic elliptical falloff ($-0.22\text{ EV}$, $85\%$ feather).
