# CAMERA RIG MOVEMENT & KINEMATICS MATH (`technical_brain/03_camera_rig_movement_and_kinematics_math.md`)

## 1. RIG SUPPORT TAXONOMY

1. **Precision Tubular Dolly:** Chapman PeeWee IV / Fisher 10 on precision leveled Mitchell steel track over neoprene vibration pads. Linear tracking along X or Z axis ($0.0\text{ cm/s}$ to $40.0\text{ cm/s}$). Imperfection float: `0.0`.
2. **Fluid Head on Heavy Sticks:** OConnor 2575D / Ronford Baker heavy tripod. Locked spirit level ($0.0^\circ$ Dutch). Pan/Tilt drag settings: 4/10 to 7/10.
3. **Steadicam / Trinity Rig:** ARRI Trinity 2 motorized 5-axis hybrid stabilizer. Dynamic walking pursuit with 32-axis inertial compensation. Imperfection float: `0.15` to `0.25`.
4. **Physiological Handheld:** EasyRig Vario 5 with Serene arm. Organic breathing motion and footsteps. Imperfection float: `0.35` to `0.65`.

---

## 2. KINEMATIC MOTION PARAMETERS
For every moving shot in `02_Shot_Breakdown.md`:
- **Vector Axis:** X-axis lateral track, Y-axis vertical jib/pedestal, Z-axis push/pull.
- **Linear Velocity:** Measured in $\text{cm/second}$ (e.g., $8.0\text{ cm/s}$ slow creep).
- **Feathering & Curve:** Ease-in / Ease-out duration in seconds (e.g., $0.8\text{s}$ sinusoidal ramp).
- **Imperfection Float:** A value between `0.0` (machine perfection) and `1.0` (uncontrolled documentary chaos).
