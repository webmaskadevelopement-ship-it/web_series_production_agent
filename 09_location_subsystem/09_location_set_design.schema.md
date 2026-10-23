# SCHEMA 09: LOCATION, ARCHITECTURAL SET & ENVIRONMENT SYSTEM (`09_location_set_design.schema.md`)

*(Decompiled from architectural drafting standards, gaffer lighting plot blueprints, and environmental acoustics)*

Every Location in `09_Location_System_Design.md` MUST be engineered as a complete physical/virtual set blueprint:

```json
{
  "location_environment_blueprint": {
    "location_uuid": "LOC_01",
    "location_name_bilingual": "शर्मा पुश्तैनी हवेली — आँगन और दालन (Sharma Ancestral Haveli — Courtyard & Pillared Veranda)",
    "geographical_and_cultural_anchor": "Ahilyabai Ghat inner lanes, Old Varanasi, Uttar Pradesh (Constructed c. 1895, late Banarasi-Mughal merchant courtyard typology)",
    "scenes_hosted": ["SCN_01", "SCN_03", "SCN_04", "SCN_08", "SCN_10"],
    "architectural_geometry_and_floorplan": {
      "overall_footprint_xyz": "Width (X): 12.8m x Length (Z): 14.2m x Height (Y): 7.6m (Two-story interior façade)",
      "central_aangan_well": "8.0m x 8.0m open-to-sky square sunken by 15cm stone curb (`Katghara`), drained by a carved stone gargoyle drain (`Parnaala`) in the Northeast corner.",
      "veranda_dalaan_zones": "2.4m deep perimeter colonnade on all 4 sides, supported by 12 fluted Chunar sandstone pillars (32cm diameter, 2.8m inter-columnar spacing, cusped Mughal arches).",
      "aperture_and_threshold_dimensions": "North Main Entrance (`Deorhi`): 1.35m wide x 2.20m high heavy double-leaf teakwood door set inside an L-shaped privacy baffle corridor."
    },
    "camera_sightlines_and_blocking_traps": {
      "long_axis_sightline": "14.2m diagonal throw from NW Threshold through central pillar gap into SE Kitchen alcove (allows up to 135mm telephoto compression inside interior set).",
      "dirty_frame_occlusion_elements": "12 fluted pillars, carved stone Jali lattice screens on upper mezzanine (`Jharokha`), and hanging brass bell chains provide natural foreground occlusion at any 360° pan angle."
    },
    "surface_materiality_and_albedo_physics": {
      "floor_surface": "Hand-dressed pink-ochre Chunar sandstone slabs (60cm x 60cm); Dry Albedo: 0.28 | Wet Specular Reflectance: 0.68 with green moss growth along mortar joints.",
      "wall_surfaces": "60cm thick load-bearing Lakhori brick walls coated in aged lime-surkhi plaster (`Chuna`); peeling pale indigo/ochre distemper wash revealing efflorescence salt crystals up to 1.2m height from rising damp.",
      "woodwork": "Dark oil-seasoned Burma teak doors and window shutters with oxidized iron rings (`Kundi`)."
    },
    "lighting_plot_and_solar_mechanics": {
      "natural_daylight_behavior": "Open zenith courtyard acts as a 8m x 8m overhead softbox during overcast monsoon days; direct sun shafts only strike the West wall between 09:00–11:30 IST.",
      "practical_lighting_fixtures": [
        {
          "fixture_id": "PRAC_LOC01_01",
          "type": "Traditional Brass Oil Diya (Mustard oil + twisted cotton wick)",
          "position_xyz": "East Pillar Base (`X:+1.6m, Y:+0.15m, Z:4.2m`)",
          "photometrics": "1900K–2200K color temp | 12 Lumens natural (augmented on-set by hidden Astera NYX / DMG Dash at 2150K with organic flame flicker curve)"
        },
        {
          "fixture_id": "PRAC_LOC01_02",
          "type": "Vintage 40W Clear Filament Incandescent Bulb in Rusted Wire Cage",
          "position_xyz": "South Corridor Wall (`X:-0.5m, Y:+2.4m, Z:11.8m`)",
          "photometrics": "2400K warm tungsten | Plugged into inline dimmer at 65% voltage with occasional 50Hz brownout dip"
        }
      ]
    },
    "micro_climate_and_atmospheric_physics": {
      "temperature_and_humidity": "29°C, 88% relative humidity (causes visible condensation on metal props and damp skin sheen).",
      "volumetric_particulates": "Fine monsoon drizzle mist falling vertically through central 8m x 8m sky opening (droplet velocity: 4.2 m/s) + subtle wood-smoke haze drifting from SE kitchen hearth (Reel EFX DF-50 oil hazer at 15% density)."
    },
    "set_dressing_and_lived_in_entropy": {
      "north_threshold_zone": "Cast-iron shoe scraper, damp coir doormat, rusted iron bicycle leaning against peeling indigo wall, string of dried mango leaves (`Toran`) from a festival two years ago.",
      "east_veranda_living_zone": "Low wooden *Chauki* stool, woven *Moorah* reed chair with fraying twine, wall niche holding brass *Paan-daan* (PROP_01), ancestral black-and-white framed photograph of Raghav's father with faded marigold garland."
    }
  }
}
```
