# CUSTOM LUMA & PER-CHANNEL RGB CURVES (`technical_brain/05_custom_luma_and_per_channel_rgb_curves.md`)

## 1. KODAK 2383 S-CURVE ANCHOR POINTS
Node 04 applies a custom sensitometric S-curve replicating the characteristic density curve of Kodak 2383 print stock:

- **Black Point Anchor:** $[0.00, 0.03]$ (clean, non-clipped black toe).
- **Toe Inflection Point:** $[0.18, 0.14]$ (deepens lower-shadow contrast).
- **Middle Grey Pivot:** $[0.40, 0.40]$ (locked midtone exposure).
- **Shoulder Compression:** $[0.75, 0.82]$ (filmic knee preventing harsh digital clipping).
- **White Ceiling Rolloff:** $[1.00, 0.96]$ (creamy, non-clipped specular highlights).

---

## 2. PER-CHANNEL RGB SPLIT CURVES
- **Red Channel:** Subtle dip in bottom 10% (cooling deep blacks), lifted $+4\%$ across $0.35-0.85$ range for warm midtone skin dominance.
- **Green Channel:** Linear neutral anchor from $0.00$ to $0.70$, slight $+2\%$ lift in upper shoulder to prevent magenta highlight skew.
- **Blue Channel:** Lifted $+3\%$ in $0.05-0.20$ shadow toe (slate-blue shadows), pulled down $-12\%$ in $0.65-1.00$ highlights (golden D60 print roll-off).
