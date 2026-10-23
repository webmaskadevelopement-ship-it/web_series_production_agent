# WORKSPACE PROJECTS DIRECTORY (DYNAMIC GOOGLE DRIVE SYNC)

This directory houses dedicated, project-titled production folders automatically instantiated whenever a script or story PDF is ingested by Sub-System 00.

## Hierarchical Directory Layout per Project
```
workspace/projects/{PROJECT_SCRIPT_TITLE}/
├── 00_Project_Bible_and_Canonical_State/
│   ├── 00_canonical_story_bible.md               # Complete story breakdown, Navarasa, pre-calculated shots, UUIDs
│   └── 00_project_metadata.json                  # Pacing math, duration budget, template selection, timestamps
├── 01_Creative_Master_Suite/                     # [EXECUTIVE / CLIENT SHAREABLE EDITION]
│   ├── 01_Script_Creative_Master.md (.pdf)       # Clean prose screenplay budgeted to page count (no tech metadata)
│   ├── 02_Shot_Breakdown_Creative_Master.md (.pdf)# 10-Column Master Production Tables ONLY (zero technical JSON)
│   ├── 03_Voiceover_Creative_Master.md (.pdf)    # Plain prose voiceover script (no DSP/frequency blocks)
│   └── 04_Storyboarding_Creative_Master.md       # 2-Liner narrative shot descriptions
├── 02_Technical_Master_Suite/                    # [DEEP ENGINEERING DECOMPILATION]
│   ├── 01_Script_Technical_Master.md             # Sub-location geometry, lighting clock, speech register tags
│   ├── 02_Shot_Breakdown_Technical_Master.md (.pdf)# 10-Col Tables + Deep Optical Cooke/ARRI, FACS, IRE, Atmos JSON
│   ├── 03_Voiceover_Technical_Master.md          # Devanagari phonetics, WPM curves, Neumann U87, 5-stage DSP chain
│   ├── 04_Storyboarding_Technical_Master.md      # Dynamic symmetry, horizon floats, GenAI prompt syntax
│   ├── 05_Color_Grading_Technical_Master.md      # ACEScc 12-node DaVinci Resolve trees, CDL, Kodak 2383
│   ├── 06_Sound_Design_Technical_Master.md       # 7.1.4 Dolby Atmos XYZ panning, stem routing, RT60, Foley
│   ├── 07_Character_Technical_Master.md          # Anatomical, psychological, textile GSM weave & wear
│   ├── 08_Prop_Technical_Master.md               # PBR material physics, patina distress chemistry
│   └── 09_Location_Technical_Master.md           # Floorplans, architectural sightlines, practical fixtures
└── 03_Production_Logs_and_Audits/
    ├── 00_ingestion_completeness.audit.md        # Story bible validation log
    ├── *.audit.md                                # Departmental quality audits
    └── production_manifest.json                  # Immutable deliverable hash & verification seal
```

*(Note: Legacy paths `workspace/state/` and `workspace/exports/` are maintained in parallel to guarantee 100% backward compatibility).*
