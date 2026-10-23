# PBR SURFACE PHYSICS: ALBEDO, ROUGHNESS & IOR (`technical_brain/02_pbr_surface_physics_albedo_roughness_ior.md`)

## 1. PHYSICALLY BASED RENDERING (PBR) SPECIFICATIONS
For every prop, Sub-System 08 defines physical rendering properties for VFX CGI integration and lighting response:

### Example: Brass Paan-Daan (`PROP_01`)
- **Dimensions:** Octagonal casket: $185\text{ mm}$ diameter $\times 92\text{ mm}$ height, wall thickness $1.8\text{ mm}$.
- **Mass:** $680\text{ grams}$.
- **Base Color Hex:** `#B58938` (Polished yellow brass high-points) / `#3B4D3E` (Recessed copper verdigris).
- **Metallic Float:** `0.88` (Conductor material response).
- **Specular Roughness:** `0.32` on thumb-latch (worn smooth by thumb contact); `0.78` inside engraved grooves.
- **Index of Refraction (IOR):** `2.45` (Tarnished brass oxide film).
