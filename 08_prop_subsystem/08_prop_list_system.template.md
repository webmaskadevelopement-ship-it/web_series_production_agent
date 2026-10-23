# PROP LIST SYSTEM TEMPLATE (`08_prop_list_system.template.md`)

This template governs the appending of props into `workspace/exports/08_Prop_List_System.md`:

```markdown
<!-- PROP ENTRY START: {{PROP_UUID}} -->
# {{PROP_UUID}}: {{PROP_NAME_BILINGUAL}}
> **Classification:** {{CLASSIFICATION}} (Category {{CATEGORY_TIER}})  
> **Linked Characters:** {{LINKED_CHARACTERS}}  
> **Scenes Present:** {{SCENES_PRESENT_LIST}}  

---

## 1. PHYSICAL & PBR MATERIAL SPECIFICATIONS
- **Dimensions & Geometry:** {{GEOMETRY_AND_DIMENSIONS}}
- **Mass:** {{MASS_GRAMS}} grams
- **Primary Material:** {{PRIMARY_MATERIAL}}
- **PBR Values:** Base: `{{BASE_COLOR_HEX}}` | Metallic: {{METALLIC}} | Roughness: {{SPECULAR_ROUGHNESS}} | IOR: {{INDEX_OF_REFRACTION}}
- **Patina & Aging Chemistry:** {{PATINA_AND_AGING_CHEMISTRY}}

---

## 2. ACOUSTIC FOLEY & CONTACT PROFILE
- **Latch / Action Transient:** {{LATCH_TRANSIENT_SPEC}}
- **Surface Contact Scraping:** {{SURFACE_CONTACT_SOUND}}

---

## 3. NARRATIVE DRAMATURGY & SYMBOLISM
{{NARRATIVE_DRAMATURGY_PROSE}}

---

## 4. SHOT-BY-SHOT CONTINUITY LEDGER
| Scene ID | Shots Visible | Spatial Coordinates | Physical State & Continuity Notes |
| :--- | :--- | :--- | :--- |
| `{{SCENE_ID_01}}` | `{{SHOTS_LIST_01}}` | `{{COORDINATES_01}}` | {{PHYSICAL_STATE_01}} |
| `{{SCENE_ID_02}}` | `{{SHOTS_LIST_02}}` | `{{COORDINATES_02}}` | {{PHYSICAL_STATE_02}} |

---

## 5. MACHINE-READABLE PROP JSON
```json
{{COMPILED_PROP_MASTER_ENTRY_JSON}}
```
<!-- PROP ENTRY END: {{PROP_UUID}} -->
```
