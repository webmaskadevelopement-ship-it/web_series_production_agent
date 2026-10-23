# SUBTRACTIVE CMY DENSITY & SPLIT-TONING (`technical_brain/07_subtractive_cmy_density_and_split_toning.md`)

## 1. THE HELMHOLTZ-KOHLRAUSCH EFFECT & FILM DENSITY
Digital color saturation increases luminance: as a color becomes more saturated, it appears brighter and can clip into harsh digital neon. In contrast, **Photochemical Film Saturation is Subtractive**: as dye layers (Cyan, Magenta, Yellow) become more saturated, they absorb more light and become darker and richer.

In Node 05:
- The node color space is converted to **HSV**.
- The Hue and Saturation channels are disabled; only the Value (Luminance) channel is processed.
- The Gamma wheel is pulled down by $-0.06$.
- *Operational Result:* Saturated reds, terracotta stones, and amber lights become deeper, darker, and more velvety, emulating rich print film chemistry.
