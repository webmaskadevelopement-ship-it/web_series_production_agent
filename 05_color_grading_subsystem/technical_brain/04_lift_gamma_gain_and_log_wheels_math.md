# LIFT, GAMMA, GAIN & LOG WHEELS MATH (`technical_brain/04_lift_gamma_gain_and_log_wheels_math.md`)

## 1. 3-WAY COLOR WHEEL FLOAT CALIBRATION
Color offsets in Node 06 are expressed as normalized RGB floats ($-1.000$ to $+1.000$):

### Lift (Shadow Floor)
- Controls shadows below $20\text{ IRE}$.
- `Red: -0.035`, `Green: -0.005`, `Blue: +0.045`, `Luma: -0.015`.
- *Operational Result:* Injects a dense slate-teal monsoon tone into sandstone shadows while firming the black floor.

### Gamma (Midtones)
- Controls the $20\text{ IRE} – 70\text{ IRE}$ range centered around middle grey ($0.385$ pivot).
- `Red: +0.065`, `Green: +0.020`, `Blue: -0.055`, `Luma: -0.010`.
- *Operational Result:* Warms skin tones and stone surfaces toward earthy ochre-amber without dirtying deep blacks.

### Gain (Highlights)
- Controls the $70\text{ IRE} – 100\text{ IRE}$ range.
- `Red: +0.140`, `Green: +0.085`, `Blue: -0.165`, `Luma: +0.020`.
- *Operational Result:* Creates the rich $2200\text{K}$ golden-amber glow around oil lamp flames and wet floor reflections.
