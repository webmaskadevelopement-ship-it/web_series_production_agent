# BILINGUAL COURIER & DEVANAGARI PDF LAYOUT (`technical_brain/05_bilingual_courier_devanagari_pdf_layout.md`)

## 1. COMPILATION & CSS SPECIFICATION
This document specifies the exact CSS print stylesheet used to render `01_Script.md` into `01_Script.pdf`:

```css
@page {
  size: letter portrait;
  margin-top: 1.0in;
  margin-bottom: 1.0in;
  margin-left: 1.5in;
  margin-right: 1.0in;
  @top-right {
    content: counter(page) ".";
    font-family: "Courier Prime", monospace;
    font-size: 10pt;
  }
}

body {
  font-family: "Courier Prime", "Noto Sans Devanagari", monospace;
  font-size: 12pt;
  line-height: 100%;
  color: #000000;
}

.scene-header {
  font-weight: bold;
  text-transform: uppercase;
  margin-top: 18pt;
  margin-bottom: 12pt;
  page-break-after: avoid;
}

.action-block {
  margin-bottom: 12pt;
  line-height: 120%;
}

.character-cue {
  margin-left: 2.2in;
  margin-top: 12pt;
  margin-bottom: 0pt;
  text-transform: uppercase;
  page-break-after: avoid;
}

.parenthetical {
  margin-left: 1.6in;
  margin-right: 1.6in;
  margin-bottom: 0pt;
  font-style: italic;
  page-break-after: avoid;
}

.dialogue-text {
  margin-left: 1.0in;
  margin-right: 1.5in;
  margin-bottom: 12pt;
  line-height: 120%;
}

.devanagari-line {
  font-family: "Noto Sans Devanagari", sans-serif;
  font-size: 11pt;
  margin-bottom: 4pt;
}

.roman-line {
  font-style: italic;
  font-size: 10.5pt;
  color: #333333;
  margin-bottom: 4pt;
}

.english-subtext {
  font-size: 10pt;
  color: #555555;
  margin-bottom: 8pt;
}
```
