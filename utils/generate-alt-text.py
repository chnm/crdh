#!/usr/bin/env python3
"""Find images with missing or weak alt text (Markdown content + Hugo HTML
templates) and generate replacements with Claude Sonnet 5.

Flags Markdown alt that is empty, a placeholder, duplicated across images,
shorter than MIN_ALT_LEN, or contains a known typo; and <img> tags with no alt.
Human-written alt is kept: typos are fixed in place, and short or duplicate
alt gets one generated sentence of extra detail appended. Only missing or
placeholder alt is generated from scratch.

Usage:
    python utils/generate-alt-text.py                # dry-run: list + suggest
    python utils/generate-alt-text.py --apply        # patch files in place
    python utils/generate-alt-text.py --model opus   # other Claude model

Requires: claude CLI (Claude Code) installed and authenticated.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
LAYOUTS_DIR = ROOT / "layouts"
STATIC_DIR = ROOT / "static"

MD_IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"^(\s*|alt|alt[- ]text|image|todo)$", re.I)
MIN_ALT_LEN = 40
# ponytail: hand-picked misspellings seen in this corpus; swap for a real
# spellchecker (aspell/pyspellchecker) if the list keeps growing
TYPOS = {
    "newtwork": "network", "culster": "cluster", "catagor": "categor",
    "indcat": "indicat", "certian": "certain", "moblity": "mobility",
    "voitng": "voting", "aa digital": "a digital",
}
# <img ...> tags (may span lines) with no alt= and no Alpine :alt= binding
HTML_IMG_RE = re.compile(r"<img\b(?:(?!alt=)[^>])*>", re.I | re.S)
SRC_RE = re.compile(r'\bsrc="([^"]+)"')

EXTEND_TEMPLATE = (
    "Read the image at {image_path}. A human already wrote this alt text for it: "
    '"{existing}". Write ONE additional sentence adding specific visual detail '
    "not already stated (labels, place names, values, colors, layout) so a "
    "screen reader user can tell this figure apart from similar ones. "
    'Do not repeat or rephrase the existing text. Do not start with "This image". '
    "Always finish the sentence. Output ONLY the new sentence, no quotes."
)

PROMPT_TEMPLATE = (
    "Read the image at {image_path} and describe it in one or two concise "
    "sentences for use as alt text on a digital history and humanities website. "
    'Focus on what is visually depicted. Do not start with "This image shows" '
    'or "The image depicts". Just state what you see. '
    "Always finish your sentence — never cut off mid-word or mid-phrase. "
    "Aim for under 200 characters but completeness matters more than brevity. "
    "Output ONLY the alt text, nothing else — no labels, no quotes."
)


def weak_reason(alt: str, dupes: set[str]) -> str | None:
    """Why this alt needs regenerating, or None if it looks fine."""
    if PLACEHOLDER_RE.match(alt):
        return "missing"
    if alt.strip().lower() in dupes:
        return "duplicate"
    if len(alt.strip()) < MIN_ALT_LEN:
        return "short"
    if fix_typos(alt) != alt:
        return "typo"
    return None


def fix_typos(alt: str) -> str:
    for bad, good in TYPOS.items():
        alt = re.sub(re.escape(bad), lambda m: good.capitalize() if m.group(0)[0].isupper() else good, alt, flags=re.I)
    return alt


def find_missing() -> list[dict]:
    """Return {file, match, img_ref, line, type, reason} for every image needing alt."""
    found = []
    md_files = {md: md.read_text(encoding="utf-8") for md in sorted(CONTENT_DIR.rglob("*.md"))}
    alts = [m.group(1).strip().lower() for t in md_files.values() for m in MD_IMG_RE.finditer(t)]
    dupes = {a for a in alts if a and alts.count(a) > 1}
    for md, text in md_files.items():
        for m in MD_IMG_RE.finditer(text):
            reason = weak_reason(m.group(1), dupes)
            if reason:
                ref = m.group(2).split('"')[0].split("'")[0].strip()
                found.append(_entry(md, m, ref, text, "markdown", reason, m.group(1).strip()))
    for html in sorted(LAYOUTS_DIR.rglob("*.html")):
        text = html.read_text(encoding="utf-8")
        for m in HTML_IMG_RE.finditer(text):
            src = SRC_RE.search(m.group(0))
            found.append(_entry(html, m, src.group(1) if src else "", text, "html", "missing"))
    return found


def _entry(file, m, ref, text, kind, reason, alt=""):
    return {
        "alt": alt,
        "file": file,
        "match": m.group(0),
        "img_ref": ref,
        "line": text[: m.start()].count("\n") + 1,
        "type": kind,
        "reason": reason,
    }


def resolve_image_path(src_file: Path, img_ref: str) -> Path | None:
    """Map a reference to a file on disk: page-bundle relative or /static."""
    if not img_ref or "{{" in img_ref or img_ref.startswith(("http://", "https://")):
        return None
    if img_ref.startswith("/"):
        candidate = STATIC_DIR / img_ref.lstrip("/")
    else:
        candidate = src_file.parent / img_ref
    return candidate if candidate.exists() else None


def generate_alt_text(image_path: Path, model: str, existing: str = "") -> str:
    """Call claude -p for fresh alt text, or one extra sentence if alt exists."""
    if existing:
        prompt = EXTEND_TEMPLATE.format(image_path=image_path, existing=existing)
    else:
        prompt = PROMPT_TEMPLATE.format(image_path=image_path)
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model, "--allowedTools", "Read"],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        sys.exit("ERROR: 'claude' CLI not found. Install Claude Code first.")
    except subprocess.TimeoutExpired:
        print(f"  ERROR: claude timed out for {image_path}", file=sys.stderr)
        return ""
    if result.returncode != 0:
        print(f"  ERROR: claude failed for {image_path}: {result.stderr.strip()}", file=sys.stderr)
        return ""
    return clean(result.stdout)


def clean(text: str) -> str:
    text = re.sub(r"^\*\*.*?\*\*:?\s*", "", text.strip())
    if len(text) > 1 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1]
    text = " ".join(text.split())
    if text and text.rstrip("\"'")[-1:] not in (".", "!", "?"):
        text += "."
    return text


def new_alt(entry: dict, generated: str) -> str:
    """Combine human alt and generated text according to the flag reason."""
    if entry["reason"] == "typo":
        return fix_typos(entry["alt"])
    if entry["reason"] in ("short", "duplicate"):
        return clean(entry["alt"]) + " " + generated
    return generated


def patch(entry: dict, full: str) -> None:
    """Rewrite the matched image with alt text (first occurrence only)."""
    old = entry["match"]
    if entry["type"] == "markdown":
        new = f"![{full}]({entry['img_ref']})"
    else:
        new = old[:-1].rstrip() + f' alt="{full.replace(chr(34), "&quot;")}">'
    text = entry["file"].read_text(encoding="utf-8")
    entry["file"].write_text(text.replace(old, new, 1), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate alt text for images missing it.")
    parser.add_argument("--apply", action="store_true", help="Patch files in place (default: dry run)")
    parser.add_argument("--model", default="claude-sonnet-5", help="Claude model (default: claude-sonnet-5)")
    args = parser.parse_args()

    entries = find_missing()
    if not entries:
        print("No images with missing alt text found.")
        return
    print(f"Found {len(entries)} image(s) with missing or weak alt text.\n")

    processed = skipped = 0
    for e in entries:
        rel = e["file"].relative_to(ROOT)
        img = resolve_image_path(e["file"], e["img_ref"])
        if img is None:
            print(f"  SKIP [{e['type']}]: {rel}:{e['line']} — cannot resolve {e['img_ref'] or '(dynamic src)'}; add alt by hand")
            skipped += 1
            continue
        print(f"  [{e['type']}, {e['reason']}] {rel}:{e['line']} — {e['img_ref']}")
        generated = "" if e["reason"] == "typo" else generate_alt_text(img, args.model, e["alt"] if e["reason"] != "missing" else "")
        if not generated and e["reason"] != "typo":
            skipped += 1
            continue
        alt = new_alt(e, generated)
        print(f"    → {alt}")
        if args.apply:
            patch(e, alt)
            print("    ✓ Patched")
        processed += 1

    print(f"\nDone. Processed: {processed}, Skipped: {skipped}")
    if not args.apply and processed:
        print("Run with --apply to write changes to files.")


if __name__ == "__main__":
    main()
