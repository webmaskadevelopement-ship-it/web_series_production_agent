#!/usr/bin/env python3
"""Deterministic pre-PDF gate for Hindi documentary voiceover drafts.

Usage:
  python validate_voiceover_draft.py draft.md --target-minutes 6.5 --target-wpm 87
  python validate_voiceover_draft.py draft.md --sibling sibling.md
"""
import argparse, json, re
from difflib import SequenceMatcher
from pathlib import Path

BANNED_DEVANAGARI = ["एसएसपी", "डीजीपी", "ई-सर्विलांस", "बोनट", "जीप", "प्रेस विज्ञप्तियाँ"]
APPROVED_TAGS = {"thoughtful", "serious", "annoyed", "excited", "measured", "quietly", "whispers", "clears throat", "inhales deeply", "exhales sharply", "chuckles", "sighs", "short pause", "long pause", "gunshot"}

def strip_tags(text):
    return re.sub(r"\[[^\]]+\]", "", text)

def spoken_body(text):
    """Remove Markdown/title metadata so runtime gates count only narrated prose."""
    body = re.sub(r"```.*?```", "", text, flags=re.S)
    keep=[]
    for line in body.splitlines():
        stripped=line.strip()
        if not stripped:
            keep.append("")
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("*") or stripped.startswith("कुल अवधि"):
            continue
        keep.append(line)
    return "\n".join(keep)

def spoken_words(text):
    body = strip_tags(spoken_body(text))
    return re.findall(r"\S+", body)

def normalize(text):
    body = strip_tags(text).lower()
    body = re.sub(r"^#+.*$", "", body, flags=re.M)
    body = re.sub(r"[*_`>#|]", " ", body)
    return re.sub(r"\s+", " ", body).strip()

def short_sentence_streak(text):
    streak = 0
    bad = []
    for sentence in re.split(r"[।!?]+", strip_tags(spoken_body(text))):
        clean = sentence.strip()
        if not clean:
            continue
        if len(clean.split()) <= 4:
            streak += 1
            if streak >= 3:
                bad.append(clean)
        else:
            streak = 0
    return bad

def cue_report(text):
    cues = re.findall(r"\[([^\]]+)\]", text)
    unknown = sorted(set(cues) - APPROVED_TAGS)
    paragraphs = [p.strip() for p in spoken_body(text).split("\n\n") if p.strip()]
    mid = 0
    for p in paragraphs:
        without_start = re.sub(r"^\[[^\]]+\]\s*", "", p)
        if re.search(r"\[[^\]]+\]", without_start):
            mid += 1
    return cues, unknown, mid, len(paragraphs)

def validate(text, target_minutes=6.5, target_wpm=87, siblings=None, preset="civic_noir"):
    errors=[]; warnings=[]
    words=spoken_words(text)
    target=target_minutes*target_wpm
    lo=target*0.96; hi=target*1.04
    if not (lo <= len(words) <= hi):
        errors.append(f"WORD_COUNT_FAIL: {len(words)} spoken words; expected {lo:.0f}–{hi:.0f} at {target_wpm} WPM for {target_minutes} minutes")
    ellipses=text.count("...")
    if preset == "civic_noir" and ellipses < 8:
        errors.append(f"CADENCE_FAIL: {ellipses} ellipsis groups; Civic Noir requires at least 8")
    streak=short_sentence_streak(text)
    if streak:
        errors.append(f"STACCATO_FAIL: {len(streak)} three-or-more short-sentence streak(s)")
    banned=[x for x in BANNED_DEVANAGARI if x in text]
    if banned:
        errors.append(f"SCRIPT_HYGIENE_FAIL: Romanize operational terms: {banned}")
    cues, unknown, mid, paragraphs=cue_report(text)
    if unknown:
        errors.append(f"TAG_FAIL: Unknown cues {unknown}")
    if cues and mid < max(3, paragraphs//2):
        errors.append(f"TAG_PLACEMENT_FAIL: only {mid}/{paragraphs} paragraphs contain mid-paragraph cues")
    if "[whispers]" in text and "[gunshot]" in text:
        if re.search(r"\[whispers\].{0,120}\[gunshot\]", text, re.S):
            errors.append("TAG_LOGIC_FAIL: [whispers] is too close to [gunshot]; change energy before kinetic action")
    for sibling in siblings or []:
        score=SequenceMatcher(None, normalize(text), normalize(sibling)).ratio()
        if score >= 0.82:
            errors.append(f"DRAFT_DUPLICATION_FAIL: sibling similarity {score:.3f} >= 0.82")
        elif score >= 0.65:
            warnings.append(f"DRAFT_SIMILARITY_WARNING: sibling similarity {score:.3f}")
    return {"passed": not errors, "spoken_word_count": len(words), "target_words": target, "projected_seconds_at_target_wpm": len(words)/target_wpm*60, "ellipsis_count": ellipses, "mid_paragraph_cue_paragraphs": mid, "paragraph_count": paragraphs, "errors": errors, "warnings": warnings}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("draft"); ap.add_argument("--sibling", action="append", default=[]); ap.add_argument("--target-minutes", type=float, default=6.5); ap.add_argument("--target-wpm", type=float, default=87); ap.add_argument("--preset", default="civic_noir"); ap.add_argument("--json", action="store_true"); args=ap.parse_args()
    text=Path(args.draft).read_text(encoding="utf-8")
    siblings=[Path(p).read_text(encoding="utf-8") for p in args.sibling]
    report=validate(text,args.target_minutes,args.target_wpm,siblings,args.preset)
    print(json.dumps(report,ensure_ascii=False,indent=2)) if args.json else print("PASS" if report["passed"] else "FAIL", report)
    raise SystemExit(0 if report["passed"] else 1)
if __name__ == "__main__": main()
