# LOCATION SPATIAL AUDIT CHECKLIST (`09_location_spatial.audit.md`)

## 1. QUALITY ASSURANCE GATES
Before exporting `09_Location_System_Design.md`:

- [ ] **1. Location UUID Match:** Does every location entry match a registered `LOC_XX` in `00_canonical_story_bible.md`?
- [ ] **2. Spatial Fit Verification:** Do actor blocking coordinates from `02_Shot_Breakdown.md` physically fit within the room dimensions ($X, Y, Z$)?
- [ ] **3. Sightline Clearance:** Does the long-axis throw accommodate the maximum telephoto focal lengths called for in the shot breakdown?
- [ ] **4. PBR Albedo Accuracy:** Are dry albedo and wet specular reflectance coefficients specified for floors and walls?
- [ ] **5. Practical Rigging Reality:** Are all practical lighting fixtures positioned with metric coordinates and realistic photometrics?
- [ ] **6. Micro-Climate Acoustics:** Are humidity, volumetric haze density, and Sabine RT60 values mathematically defined?
- [ ] **7. Schema Compliance:** Does the embedded JSON validate against `09_location_set_design.schema.md`?
- [ ] **8. Zero Blacklist Tokens:** Free from `"etc."`, `"typical courtyard"`, and `"TBD"`.
