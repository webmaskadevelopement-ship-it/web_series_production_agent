# ENTITY EXTRACTION & UUID ASSIGNER (`technical_brain/02_entity_extraction_and_uuid_assigner.md`)

## 1. PURPOSE & EXTRACTION ENGINE
During the ingestion of the raw Hindi story, the entity extraction algorithm scans the entire text and builds three immutable registers:
1. **Character Registry (`CHAR_XX`):** Every person named, addressed, or remembered who affects dramatic action.
2. **Prop Registry (`PROP_XX`):** Every physical object handled, worn, referenced, or acting as a narrative symbol.
3. **Location Registry (`LOC_XX`):** Every distinct physical environment, room, corridor, exterior alley, or architectural space.

---

## 2. PARSING & TAGGING RULES

### Character Extraction
- Must extract: Full Name (Hindi & English), Kinship Terms, Narrative Tier (Protagonist / Antagonist / Supporting / Atmospheric), and Generational Trajectory.
- Must identify the Character Ghost / Core Wound and physical age.
- UUID format: `CHAR_01`, `CHAR_02`... in order of dramatic appearance.

### Prop Extraction
- Must classify each prop into:
  - **Category A (Hero Action Prop):** Objects directly manipulated by actors that reveal character or advance plot (requires 3 duplicates: Macro, Stunt, Clean).
  - **Category B (Set Dressing / Living Texture):** Static objects populating shelves, niches, or tables that establish lived-in entropy.
  - **Category C (Consumables):** Food items, tea, bidi, matches, paper deeds that get destroyed or depleted during the take.
- UUID format: `PROP_01`, `PROP_02`... in order of narrative mention.

### Location Extraction
- Must decompose environments into:
  - Master Location: E.g., `LOC_01` (Sharma Ancestral Haveli).
  - Sub-Location Zones: E.g., Central Courtyard (Aangan), North Veranda (Dalaan), Upper Mezzanine (Jharokha), Kitchen Alcove.
  - Interior vs. Exterior (INT./EXT.).
- UUID format: `LOC_01`, `LOC_02`...

---

## 3. REGISTRY INTEGRITY CONTRACT
Once assigned in `workspace/state/00_canonical_story_bible.md`, these UUIDs are locked for the lifetime of the project. No downstream department may alter the UUID or assign a new entity without registering it in this canonical ledger.
