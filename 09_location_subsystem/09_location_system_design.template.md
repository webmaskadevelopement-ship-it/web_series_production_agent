# LOCATION SYSTEM DESIGN TEMPLATE (`09_location_system_design.template.md`)

This template governs the appending of location blueprints into `workspace/exports/09_Location_System_Design.md`:

```markdown
<!-- LOCATION BLUEPRINT START: {{LOCATION_UUID}} -->
# {{LOCATION_UUID}}: {{LOCATION_NAME_BILINGUAL}}
> **Geographical Anchor:** {{GEOGRAPHICAL_AND_CULTURAL_ANCHOR}}  
> **Scenes Hosted:** {{SCENES_HOSTED_LIST}}  
> **Acoustic Volume:** {{TOTAL_CUBIC_VOLUME}} m³  

---

## 1. ARCHITECTURAL GEOMETRY & FLOORPLAN ELEVATIONS
- **Footprint Dimensions:** Width ($X$): {{WIDTH_X}}m $\times$ Length ($Z$): {{LENGTH_Z}}m $\times$ Height ($Y$): {{HEIGHT_Y}}m
- **Central Courtyard (Aangan):** {{CENTRAL_AANGAN_DIMENSIONS}}
- **Colonnade & Verandas:** {{VERANDA_DALAAN_ZONES}}
- **Thresholds & Apertures:** {{THRESHOLDS_AND_APERTURES}}

---

## 2. CAMERA SIGHTLINES & DIRTY-FRAME OCCLUSION TRAPS
- **Maximum Throw Distance:** {{LONG_AXIS_SIGHTLINE}} (enabling up to {{MAX_TELEPHOTO_MM}}mm telephoto compression)
- **Foreground Occlusion Elements:** {{FOREGROUND_OCCLUSION_ELEMENTS}}

---

## 3. SURFACE MATERIALITY & ALBEDO PHYSICS
- **Floor Surfaces:** {{FLOOR_SURFACES_PBR}}
- **Wall Surfaces:** {{WALL_SURFACES_PBR}}
- **Timber & Doors:** {{TIMBER_AND_WOODWORK_PBR}}

---

## 4. LIGHTING PLOT & SOLAR PATH
- **Natural Daylight Behavior:** {{NATURAL_DAYLIGHT_BEHAVIOR}}
- **Practical Fixtures Rigging Plot:**
  - `{{PRAC_FIXTURE_01_ID}}`: {{PRAC_FIXTURE_01_TYPE}} (Position: `{{PRAC_FIXTURE_01_POS}}`, Photometrics: {{PRAC_FIXTURE_01_PHOTO}})
  - `{{PRAC_FIXTURE_02_ID}}`: {{PRAC_FIXTURE_02_TYPE}} (Position: `{{PRAC_FIXTURE_02_POS}}`, Photometrics: {{PRAC_FIXTURE_02_PHOTO}})

---

## 5. MICRO-CLIMATE & ATMOSPHERIC PHYSICS
- **Temperature & Humidity:** {{TEMPERATURE_AND_HUMIDITY_METRICS}}
- **Volumetric Particulates & Mist:** {{VOLUMETRIC_PARTICULATES_SPEC}}
- **Acoustic RT60 Reverberation:** {{ACOUSTIC_RT60_SPEC}}

---

## 6. SET DRESSING & LIVED-IN ENTROPY
- **Entrance Threshold Zone:** {{ENTRANCE_ZONE_DRESSING}}
- **Living Veranda Zone:** {{LIVING_ZONE_DRESSING}}

---

## 7. MACHINE-READABLE LOCATION BLUEPRINT JSON
```json
{{COMPILED_LOCATION_BLUEPRINT_JSON}}
```
<!-- LOCATION BLUEPRINT END: {{LOCATION_UUID}} -->
```
