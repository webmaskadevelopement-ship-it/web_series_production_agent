# FOCUS PULLING, DEPTH OF FIELD & BOKEH (`technical_brain/04_focus_pulling_depth_of_field_and_bokeh.md`)

## 1. OPTICAL DEPTH OF FIELD MATH
Depth of field (DoF) is determined by:
- Focal Length ($f$)
- Shooting Aperture ($N = \text{T-stop}$)
- Circle of Confusion ($c = 0.025\text{ mm}$ for Super 35 / Large Format)
- Subject Focus Distance ($s$)

### Near and Far Focus Limits
$$D_{\text{near}} = \frac{H \times s}{H + (s - f)}, \quad D_{\text{far}} = \frac{H \times s}{H - (s - f)}$$
Where hyperfocal distance $H = \frac{f^2}{N \times c} + f$.

---

## 2. RACK FOCUS BEHAVIOR SPECIFICATION
For shots involving rack focus:
1. **Control Rig:** Preston FI+Z 3-channel wireless follow-focus with digital lens mapping and mechanical hard stops (zero hunting).
2. **Transition Curve:** E.g., *3.0-second sinusoidal rack focus starting at 00:01:00 from Foreground Brass Kalash (1.50m) to Savitri's hands (4.20m) ending at 00:04:00*.
3. **Bokeh Signature:**
   - 2x Anamorphic: Tall vertical elliptical squeeze, cat-eye rounding at frame extremities, zero onion-ring artifacts.
   - Spherical: Circular Gaussian falloff.
