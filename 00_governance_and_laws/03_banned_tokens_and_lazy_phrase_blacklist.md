# LAW 03: BANNED TOKENS & LAZY PHRASE BLACKLIST (`03_banned_tokens_and_lazy_phrase_blacklist.md`)

## 1. PRINCIPLE OF EXPLICIT COMPLETENESS
In a professional studio environment, ambiguous shorthand, placeholder text, and lazy tokens create fatal production defects. If an AI agent emits a single placeholder token, it breaks downstream automation, automated PDF renderers, 3D tracking pipelines, and sound editing sessions.

This blacklist defines all globally prohibited terms, patterns, and abbreviations.

---

## 2. BLACKLIST TABLE & REMEDIATION MATRIX

| Prohibited Token / Phrase | Why It Is Fatal | Mandatory Replacement Protocol |
| :--- | :--- | :--- |
| `"etc."` or `"and so on"` | Fails to enumerate complete production requirements. | Write out every individual item, prop, action, or cue in full. |
| `"..."` (used as truncation) | Skips critical script lines, shots, or beats. | Render every beat, micro-action, and line of dialogue completely. |
| `"same as above"` / `"same as shot X"` | Breaks independent per-shot readability on set. | Copy and re-specify the full parameters, adjusting any subtle micro-changes. |
| `"TBD"` / `"To be decided"` | Defers engineering decisions to crew during shoot. | Calculate and lock the exact technical specification immediately. |
| `"standard lighting"` | "Standard" does not exist in cinema; fails to set exposure. | Specify Key, Fill, Backlight, Kelvin, Foot-candles, and IRE targets. |
| `"close-up"` (without mm/T-stop) | Ambiguous framing; does not dictate optical perspective. | State framing size (CU/MCU/ECU), lens focal length (e.g., 85mm), and T-stop (T2.0). |
| `"room tone continues"` | Ignores dynamic Foley and shifting background elements. | Break down individual acoustic beds, decibel levels, and spot FX. |
| `"Shots 01A–01D"` (grouped) | Violates the zero-grouping rule; hides editorial cuts. | Generate each cut as an autonomous record with distinct metadata. |
| `"appropriate music plays"` | Provides no direction to the music composer or sound mixer. | Specify instrument, Raga, scale, octave drone frequency, tempo, and entry timecode. |
| `"internal monologue"` | Internal thoughts cannot be photographed by a camera. | Convert internal emotion into visible micro-expressions (FACS AUs) or action prose. |

---

## 3. AUTOMATED LINTER RULES
Every departmental sub-system audit script must run a regex scan over generated output files.
If any match is detected for the following pattern:
```regex
\b(etc\.|and so on|same as above|same as previous|TBD|standard lighting|typical setup|continues as before|\.\.\.)\b
```
The generator must abort the commit, flag the exact line number, and trigger an automated expansion loop.
