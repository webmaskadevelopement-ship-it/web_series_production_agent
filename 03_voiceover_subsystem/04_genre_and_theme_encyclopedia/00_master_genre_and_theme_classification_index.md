# MASTER GENRE & THEME CLASSIFICATION INDEX (`00_master_genre_and_theme_classification_index.md`)

## 1. THE 17 CANONICAL PRODUCTION PLAYBOOKS TAXONOMY

In the Hindi cinema voiceover architecture, genre is not merely a marketing tag; it is an **acoustic and literary contract** determining the narrator's moral distance, words-per-minute speed curve, consonant allocation, microphone distance, and philosophical worldview.

| Playbook ID | Primary Genre & Domain | Recommended Writer Blend | Target WPM | Acoustic Spec (F0 / Mic Proximity) | Primary Lexical Tier |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `GP_01` | **Documentary: Investigative & Socio-Political** | Manto (50%) + Parsai (30%) + Ray (20%) | 105–115 WPM | F0: 105–118 Hz \| 15 cm | Tier 2 (Khari Boli) 50% + Legal Terms 20% |
| `GP_02` | **Documentary: Nature, Wildlife & Ecological** | Gulzar (45%) + Renu (35%) + Bachchan (20%) | 80–92 WPM | F0: 95–110 Hz \| 12 cm | Tier 2 (Tadbhava) 45% + Tier 5 (Deshaj) 30% |
| `GP_03` | **Documentary: Historical & Civilizational** | Bachchan (45%) + Akhtar (35%) + Ray (20%) | 90–100 WPM | F0: 88–104 Hz \| 18 cm | Tier 1 (Tatsama) 40% + Tier 4 (Rekhta) 35% |
| `GP_04` | **Documentary: Biographical & Intimate** | Neelesh Misra (45%) + Agyeya (35%) + Gulzar (20%)| 88–98 WPM | F0: 100–114 Hz \| 10 cm | Tier 3 (Hindustani) 50% + Tier 4 (Rekhta) 30% |
| `GP_05` | **Crime: Hinterland Heartland & Blood Feuds** | Piyush Mishra (45%) + Dhulia (35%) + Shukla (20%)| 110–128 WPM | F0: 110–135 Hz \| 15 cm | Tier 5 (Deshaj Purvanchali) 50% + Slang 25% |
| `GP_06` | **Crime: Urban Underworld & Mumbai Metro Noir** | Manto (45%) + Kashyap (40%) + Grover (15%) | 95–108 WPM | F0: 92–108 Hz \| 8 cm | Tier 3 (Bambaiya/Hindustani) 45% + Urdu 35% |
| `GP_07` | **Crime: True Crime, Police Procedural & Forensic**| Manto (60%) + Ray (25%) + Grover (15%) | 98–110 WPM | F0: 102–115 Hz \| 14 cm | Tier 2 (Khari Boli) 55% + Forensic Nouns 25% |
| `GP_08` | **Crime: White Collar, Financial Scam & Hustle** | Akhtar (40%) + Parsai (35%) + Kashyap (25%) | 120–138 WPM | F0: 115–130 Hz \| 12 cm | Financial Jargon 30% + Mumbai Street 40% |
| `GP_09` | **Thriller: Psychological, Paranoia & Fractured**| Agyeya (50%) + Manto (30%) + Bharati (20%) | 78–115 WPM | F0: 90–125 Hz \| 6–8 cm | Tier 1 (Tatsama) 35% + Sensory Whispers 45% |
| `GP_10` | **Thriller: Espionage & Geopolitical Covert Ops** | Ray (40%) + Akhtar (35%) + Agyeya (25%) | 95–105 WPM | F0: 94–106 Hz \| 12 cm | Intelligence Jargon 25% + Cold Urdu 40% |
| `GP_11` | **Thriller: Mystery, Whodunit & Conspiracy Web** | Ray (50%) + Neelesh Misra (30%) + Manto (20%) | 92–104 WPM | F0: 98–112 Hz \| 12 cm | Tier 3 (Hindustani) 50% + Deductive Clues 30% |
| `GP_12` | **Action: Mass Mythic & Heroic Folklore** | Akhtar (55%) + Bachchan (30%) + Mishra (15%) | 85–100 WPM | F0: 85–102 Hz \| 20 cm | Tier 1 (Tatsama) 35% + Heroic Rekhta 45% |
| `GP_13` | **Action: Gritty Tactical Survival & Revenge** | Manto (50%) + Dhulia (35%) + Kashyap (15%) | 90–112 WPM | F0: 105–125 Hz \| 10 cm | Tier 5 (Deshaj) 40% + Tactical Nouns 40% |
| `GP_14` | **Horror: Indian Folklore, Occult & Atmospheric** | Renu (40%) + Gulzar (35%) + Manto (25%) | 75–88 WPM | F0: 82–96 Hz \| 8 cm | Tier 5 (Archaic Deshaj) 45% + Whispers 35% |
| `GP_15` | **Period Epic: Mythological & Royal Grandeur** | Bachchan (50%) + Bharati (30%) + Akhtar (20%) | 82–94 WPM | F0: 80–95 Hz \| 22 cm | Tier 1 (Classical Tatsama) 60% + Shuddh 30% |
| `GP_16` | **Drama: Family Generational & Domestic Ache** | Premchand (40%) + Gulzar (35%) + Grover (25%) | 82–95 WPM | F0: 95–110 Hz \| 10 cm | Tier 2 (Tadbhava) 50% + Ganga-Jamuni 35% |
| `GP_17` | **Romance & Satire: Melancholy Viraha / Absurdity**| Gulzar/Bharati (50%) + Parsai/Shukla (50%) | 80 / 118 WPM | F0: 92–115 Hz \| 10–14 cm| Dual Register: Poetic Urdu vs Satiric Khari |

---

## 2. CROSS-GENRE HYBRIDIZATION ROUTING RULES

In complex contemporary storytelling, projects frequently blend two genres. The runtime engine calculates the weighted vector:

### FORMULA:
$$	ext{Vector}_{	ext{Final}} = w_1 \cdot 	ext{Playbook}_A + w_2 \cdot 	ext{Playbook}_B$$
Where $w_1 + w_2 = 1.0$ (typically $0.70$ primary and $0.30$ secondary).

### CANONICAL HYBRIDS:
1. **Hinterland Crime + Dark Satire (e.g., Gangs of Wasseypur / Mirzapur):**
   - Blend: `70% GP_05 (Hinterland Crime) + 30% GP_17B (Parsai Satire)`
   - Effect: Brutal homicide narrated with tea-stall black humor.
2. **Family Generational Drama + Mystery/Noir (e.g., Kohrra / Pataal Lok):**
   - Blend: `65% GP_16 (Family Ache) + 35% GP_07 (Forensic True Crime)`
   - Effect: Broken homes and ancestral shame unraveled through autopsy timestamps.
3. **Period Historical + Mythic Mass Action (e.g., RRR / Tanhaji / Kantara):**
   - Blend: `60% GP_12 (Mass Action) + 40% GP_14 (Folk Occult Dread)`
   - Effect: Divine ancestral retribution channeled into bone-breaking kinetic warfare.
