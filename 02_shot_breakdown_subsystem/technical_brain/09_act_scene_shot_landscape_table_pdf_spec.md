# A3/A4 LANDSCAPE TABLE PDF SPECIFICATION (`technical_brain/09_act_scene_shot_landscape_table_pdf_spec.md`)

## 1. PRINT CSS COMPILATION DIRECTIVES
This document specifies the exact CSS styling used to render the 10-Column Master Production Table in `02_Shot_Breakdown.pdf`:

```css
@page {
  size: A3 landscape;
  margin: 10mm 15mm 10mm 15mm;
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: "Courier Prime", monospace;
    font-size: 8pt;
  }
}

body {
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 8.5pt;
  line-height: 120%;
  color: #111111;
}

.production-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  margin-bottom: 20pt;
}

.production-table thead {
  display: table-header-group;
}

.production-table th {
  background-color: #1A1A1A;
  color: #FFFFFF;
  font-weight: bold;
  font-size: 8pt;
  text-transform: uppercase;
  padding: 6pt 4pt;
  border: 1px solid #333333;
  text-align: left;
}

.production-table td {
  border: 1px solid #CCCCCC;
  padding: 5pt 4pt;
  vertical-align: top;
  word-wrap: break-word;
}

.production-table tr {
  page-break-inside: avoid;
}

.production-table tr:nth-child(even) {
  background-color: #F9F9F9;
}

/* 10-Column Width Allocation */
.col-shot-id { width: 7%; }
.col-framing { width: 9%; }
.col-lens-sensor { width: 12%; }
.col-movement { width: 10%; }
.col-focus-dof { width: 9%; }
.col-lighting { width: 11%; }
.col-action-blocking { width: 15%; }
.col-audio { width: 13%; }
.col-edit-murch { width: 7%; }
.col-vfx-prompts { width: 7%; }
```
