# DIALOGUE, PARENTHETICAL & BEAT CODING (`technical_brain/03_dialogue_parenthetical_and_beat_coding.md`)

## 1. CHARACTER CUE SYNTAX
Character headings above dialogue must adhere to industry conventions:
- `SAVITRI (MAA)`
- `RAGHAV (V.O.)` — Voiceover (retrospective narrator).
- `RAGHAV (O.S.)` — Off-screen (speaking from inside corridor while camera frames courtyard).
- `SAVITRI (CONT'D)` — Continuing dialogue after an intervening action block.

---

## 2. PARENTHETICAL MICRO-DIRECTIONS
Parentheticals `( )` must be concise (1 to 2 lines maximum) and specify:
1. Physical action accompanying speech: `(thumb splitting a garlic pod)`
2. Acoustic vocal register: `(whispered at -6 dB; voice flat and uninflected)`
3. Eye gaze or proxemic direction: `(without looking up; eyes fixed on brass thali)`

---

## 3. BEAT CODING
Every beat is uniquely tagged (`SCN01_BT01`, `SCN01_BT02`...) and mapped to one or more shot IDs in the Master Shot Breakdown:
```json
{
  "beat_id": "SCN01_BT01",
  "linked_shot_ids": ["ACT1_SCN01_SHT01A", "ACT1_SCN01_SHT01B"],
  "element_type": "ACTION_KINAESTHETIC | DIALOGUE_BLOCK | THEHRAAV_PAUSE | TRANSITION"
}
```
