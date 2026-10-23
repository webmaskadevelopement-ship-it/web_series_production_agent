# LAW 07: PDF EXPORT FORMATTING & PRINT ENGINE (`07_pdf_export_formatting_and_print_engine.md`)

## 1. DUAL EXPORT PRINT MANDATE
While Deliverables 3 through 9 are generated and preserved in deep, machine-readable Markdown format (`.md`), Deliverables 1 and 2 represent the industry's primary physical documents:
1. **Export 1:** `01_Script.pdf` (Master Screenplay)
2. **Export 2:** `02_Shot_Breakdown.pdf` (Master 10-Column Production Table)

Standard web PDF tools fail on Indian film production documents because:
- Multi-column shot tables clip horizontally on standard portrait pages.
- Devanagari ligatures (matras, halanta, conjuncts) fracture and render as disjointed glyphs in generic PDF libraries.
- Page pagination splits scenes and table rows unpredictably across page breaks.

This document establishes the precise rendering and styling rules for compiling print-ready PDFs.

---

## 2. EXPORT 1: SCREENPLAY PDF SPECIFICATION (`01_Script.pdf`)

### Layout & Geometry
- **Page Size:** Standard US Letter (8.5 x 11 inches) or International A4.
- **Margins:**
  - Left Margin: `1.5 inches` (to accommodate physical 3-hole brass brad binding).
  - Right Margin: `1.0 inch`.
  - Top Margin: `1.0 inch`.
  - Bottom Margin: `1.0 inch`.

### Typography & Font Pairing
- **English & Technical Action Blocks:** Standard `Courier Prime` 12pt (monospaced, exact 10 characters per inch).
- **Hindi Devanagari Blocks:** `Noto Sans Devanagari` or `Rozha One` paired seamlessly at matching x-height.
- **Line Spacing:** Single-spaced within paragraphs; double-spaced between sluglines, action blocks, and character dialogue cues.

### Block Indentations
- **Slugline (Scene Heading):** Left-aligned, ALL CAPS, bold.
- **Action Blocks:** Left-aligned, full width (6.0-inch line limit).
- **Character Cue:** Indented `3.7 inches` from left edge, ALL CAPS.
- **Parenthetical Direction:** Indented `3.1 inches` from left edge.
- **Dialogue Text:** Indented `2.5 inches` from left edge (3.0 to 3.5 inches maximum width).
- **Transitions (CUT TO:, FADE OUT:):** Right-aligned.

---

## 3. EXPORT 2: MASTER SHOT BREAKDOWN PDF SPECIFICATION (`02_Shot_Breakdown.pdf`)

### Layout & Geometry
- **Orientation:** Strict **A3 or A4 Landscape** orientation (`11.7 x 16.5 inches` or `8.27 x 11.69 inches`).
- **Margins:** Top/Bottom `12mm`, Left/Right `15mm`.

### The 10-Column Master Production Table Grid
The table spans the full landscape width with fixed percentage column widths:
1. **Shot ID & Cadence (8%):** UID, Shot #, Duration (sec/frames), Frame Rate, Shutter.
2. **Framing & Angle (10%):** Shot Size (EWS/WS/MS/CU/ECU), Pitch, Yaw, Roll, Height.
3. **Lens & Sensor (12%):** Focal length, Anamorphic squeeze, T-stop, Sensor mode, ISO, DR.
4. **Camera Movement & Rig (10%):** Rig type, track axis, travel speed (cm/s), imperfection float.
5. **Focus & Depth of Field (9%):** Near/Far limits, rack focus timing curve, Circle of Confusion.
6. **Lighting & Photometrics (11%):** Contrast ratio, Key/Fill Kelvin, skin IRE zones, practicals.
7. **Visual Action & Blocking (14%):** Character stage coordinates (X/Y/Z), micro-expressions.
8. **Audio & Sound Design (12%):** Spoken dialogue/VO, Foley tags, ambient beds, musical raga.
9. **Editorial Transition (7%):** In/Out cut points, pacing tempo, Murch cut justification.
10. **VFX & GenAI Prompts (7%):** Tracking tags, 2.5D cards, Midjourney v6 / Sora prompt strings.

### Page-Break Logic
- Table headers repeat automatically on every new page (`thead { display: table-header-group; }`).
- Rows never split across a page boundary (`tr { page-break-inside: avoid; }`).
- Each new Scene begins with the high-contrast **Scene Metadata Header Banner**.
