#!/usr/bin/env python3
"""Check extracted PDF text for common Devanagari mapping corruption.
Usage: python validate_pdf_unicode.py output.pdf --required 'कानून' --required 'में'
"""
import argparse, json, re, subprocess
from pathlib import Path
BAD_GLYPHS = set("ɟɡɞɝɧÕ")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('--required', action='append', default=[]); ap.add_argument('--json', action='store_true'); args=ap.parse_args()
    raw=subprocess.check_output(['pdftotext','-enc','UTF-8',args.pdf,'-'], text=True, errors='replace')
    errors=[]
    bad=sorted({c for c in raw if c in BAD_GLYPHS})
    if bad: errors.append(f"PDF_GLYPH_FAIL: suspicious extracted glyphs {bad}")
    normalized=re.sub(r"\s+", " ", raw)
    missing=[x for x in args.required if x not in normalized]
    if missing: errors.append(f"PDF_TOKEN_FAIL: representative Unicode tokens missing from extraction: {missing}")
    result={'passed':not errors,'bad_glyphs':bad,'missing_required_tokens':missing,'errors':errors,'extracted_characters':len(raw)}
    print(json.dumps(result,ensure_ascii=False,indent=2)) if args.json else print('PASS' if result['passed'] else 'FAIL',result)
    raise SystemExit(0 if result['passed'] else 1)
if __name__=='__main__': main()
