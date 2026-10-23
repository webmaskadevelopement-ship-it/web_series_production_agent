# BLOCKING, PROXEMICS & 180-DEGREE AXIS (`technical_brain/07_blocking_proxemics_and_180_degree_axis.md`)

## 1. 3D CARTESIAN STAGE COORDINATES
To eliminate vague stage blocking ("character stands near the wall"), every shot breakdown must define actor and camera positions in metric 3D space:
- **Origin $(0,0,0)$:** The primary dramatic focal center (e.g., Central courtyard symmetry axis at floor level).
- **X-axis (Lateral):** Left ($-$) to Right ($+$) relative to camera perspective.
- **Y-axis (Vertical):** Floor ($0.0\text{m}$) to Ceiling ($+\text{meters}$).
- **Z-axis (Depth):** Distance from the camera lens ($+\text{meters}$).

### Example Specification
- `CHAR_01 (Raghav)`: `X: -1.8m, Y: +0.15m (Raised threshold step), Z: 6.10m from lens. Body angled 15° toward pillar.`
- `CHAR_02 (Savitri)`: `X: +1.4m, Y: 0.0m (Floor chauki), Z: 4.20m from lens. Torso pitched forward 20°.`

---

## 2. THE 180-DEGREE AXIS OF ACTION
Every scene must declare its imaginary **180° Axis Line**:
- E.g., *North-South axis connecting Main Threshold (North) to Kitchen Veranda Pillar (South).*
- All coverage camera placements must remain strictly on the declared side (e.g., West side) to preserve consistent screen direction (Raghav looking frame-right; Savitri looking frame-left).
- An intentional crossing of the line ("Axis Reversal") must be motivated by a major dramatic power reversal.
