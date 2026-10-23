# PRODUCTION TEMPLATE REGISTRY (`template_registry.md`)

This registry maintains the master catalog of all production templates supported by the Autonomous Studio System. Every template defines standard duration, target shot density, average shot duration (ASL), page count targets, and deliverable specifications.

---

## 1. TEMPLATE CATALOG OVERVIEW

| Template ID | Template Title | Target Duration | Target Cuts / Min | Avg Shot Length (ASL) | Total Shots Range | Script Page Budget | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`T01_SHORT_EPISODE_6_7MIN`** | **Short Episode Film** | **6.0 – 7.0 Min** | **25 – 27 shots/min** | **~2.2s – 3.5s** | **150 – 189 shots** | **6 – 7 Pages** | **Anthologies, Web Series Episodes, High-Density Festival Shorts** |
| `T02_SOCIAL_MICRO_SHORT_60S` | Social Micro-Short | 60 – 75 Seconds | 30 – 40 shots/min | ~1.5s – 2.0s | 30 – 45 shots | 1 – 1.5 Pages | Reels, TikTok narrative arcs, Teaser spots |
| `T03_EPISODIC_TV_30MIN` | Episodic Drama Episode | 26.0 – 30.0 Min | 14 – 18 shots/min | ~3.5s – 4.5s | 380 – 540 shots | 26 – 30 Pages | Streaming series, TV broadcast episodes |
| `T00_DYNAMIC_FEATURE` | Dynamic Custom / Feature | Unrestricted | Story-derived | Variable | Beat-driven | 1 min = 1 page | Standard full-length screenplays & arthouse cinema |

---

## 2. TEMPLATE SELECTION RESOLUTION
When a template is selected:
1. **Total Shot Calculation:**
   $$\text{Target Shots} = \text{Target Duration (Minutes)} \times \text{Cuts Per Minute}$$
   *For Template 1:* $6.5 \times 26 = 169\text{ shots}$.
2. **Page Budgeting:**
   - 1 Page of screenplay corresponds strictly to 1 minute of screen time (standard industry pacing math in `01_script_subsystem/technical_brain/04_scene_transition_and_page_timing_math.md`).
   - For Template 1, the script must compile to exactly **6 to 7 formatted Courier/Devanagari pages**.
3. **Sub-Asks & Deliverable Modes:**
   Each template natively provides two distinct presentation profiles:
   - **Creative Master (Executive / Client Edition):** Formatted for review, performance, and pitch. Clean typography, 10-column tables without technical JSON, readable prose VO.
   - **Technical File Master:** Full engineering drop-down with complete optical, acoustic, and lighting schemas.
