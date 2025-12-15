#!/usr/bin/env python3
"""
Generate deterministic monogram SVGs for company tables in the active deck.

Why:
- The presentation auto-renders logos for tables that include a `Company` column.
- This script creates clean, trademark-safe placeholder "logos" (monograms) so the deck
  looks polished out of the box.

How it works:
- Reads `final-presentation/deck.md` to find active slide markdown files.
- Extracts company names from markdown pipe tables that have a `Company` header.
- Writes `final-presentation/assets/logos/<slug>.svg` for each company if the file
  does not already exist (so real logos can override later).
"""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


RE_CODE_MD = re.compile(r"`([^`]+\.md)`", re.IGNORECASE)
RE_PLAIN_MD = re.compile(r"([\w./-]+\.md)\b", re.IGNORECASE)
RE_SEPARATOR = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
RE_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
RE_MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
RE_PARENS = re.compile(r"\([^)]*\)")


def slugify(value: str) -> str:
    v = (value or "").strip().lower()
    v = v.replace("&", " and ")
    v = re.sub(r"[^a-z0-9]+", "-", v)
    v = re.sub(r"-+", "-", v)
    return v.strip("-")


def strip_markdown(text: str) -> str:
    t = (text or "").strip()
    t = RE_MD_LINK.sub(r"\1", t)
    t = t.replace("`", "")
    t = re.sub(r"[*_]+", "", t)
    t = re.sub(r"<[^>]+>", "", t)
    return t.strip()


def split_table_row(line: str) -> list[str]:
    return [c.strip() for c in (line or "").strip().strip("|").split("|")]


def extract_deck_paths(deck_md: str) -> list[str]:
    paths: list[str] = []
    for line in (deck_md or "").splitlines():
        code = RE_CODE_MD.search(line)
        if code:
            paths.append(code.group(1))
            continue
        plain = RE_PLAIN_MD.search(line)
        if plain:
            paths.append(plain.group(1))
    return [normalize_deck_path(p) for p in paths if normalize_deck_path(p)]


def normalize_deck_path(p: str) -> str | None:
    v = (p or "").strip()
    if not v:
        return None
    v = re.sub(r"^(\./)+", "", v)
    v = re.sub(r"^/+", "", v)
    v = re.sub(r"^agent-builder-tools/final-presentation/", "", v)
    v = re.sub(r"^final-presentation/", "", v)
    return v or None


@dataclass(frozen=True)
class Company:
    name: str
    slug: str
    source: str


def extract_companies_from_markdown(md: str, source: str) -> list[Company]:
    lines = (md or "").splitlines()
    out: list[Company] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if not RE_TABLE_ROW.match(line):
            i += 1
            continue

        header = split_table_row(line)
        if i + 1 >= len(lines) or not RE_SEPARATOR.match(lines[i + 1] or ""):
            i += 1
            continue

        # Consume table rows.
        rows: list[list[str]] = []
        j = i + 2
        while j < len(lines) and RE_TABLE_ROW.match(lines[j] or ""):
            rows.append(split_table_row(lines[j]))
            j += 1

        i = j

        normalized = [strip_markdown(h).lower() for h in header]
        try:
            company_idx = normalized.index("company")
        except ValueError:
            continue

        for row in rows:
            if company_idx >= len(row):
                continue
            raw = strip_markdown(row[company_idx])
            name = raw.strip()
            if not name:
                continue
            s = slugify(name)
            if not s:
                continue
            out.append(Company(name=name, slug=s, source=source))

    return out


def initials_from_token(token: str) -> str:
    if not token:
        return ""
    caps = re.findall(r"[A-Z]", token)
    if len(caps) >= 2:
        return "".join(caps[:2]).upper()
    return token[:2].upper()


def initials(name: str) -> str:
    cleaned = strip_markdown(name)
    cleaned = RE_PARENS.sub(" ", cleaned)
    cleaned = cleaned.replace("&", " and ")
    tokens = [t for t in re.split(r"[^A-Za-z0-9]+", cleaned) if t]

    stop = {
        "inc",
        "llc",
        "ltd",
        "co",
        "corp",
        "corporation",
        "company",
        "technologies",
        "technology",
        "systems",
        "labs",
        "group",
        "holdings",
    }
    filtered = [t for t in tokens if t.lower() not in stop]
    tokens = filtered or tokens

    if not tokens:
        return "?"

    if len(tokens) >= 2:
        first = tokens[0]
        second = tokens[1]
        if first.isupper() and len(first) <= 3:
            return first
        return (first[0] + second[0]).upper()

    only = tokens[0]
    if only.isupper() and len(only) <= 3:
        return only
    return initials_from_token(only) or only[:1].upper()


def hsl(h: float, s: float, l: float) -> str:
    return f"hsl({h:.0f} {s:.0f}% {l:.0f}%)"


def color_pair(slug: str) -> tuple[str, str]:
    digest = hashlib.sha256(slug.encode("utf-8")).digest()
    h0 = (digest[0] / 255.0) * 360.0
    delta = 12.0 + (digest[1] / 255.0) * 18.0
    h1 = (h0 + delta) % 360.0
    sat = 68.0 + (digest[2] % 18)
    l_top = 56.0 + (digest[3] % 8)
    l_bot = 42.0 + (digest[4] % 8)
    return hsl(h0, sat, l_top), hsl(h1, sat, l_bot)


def monogram_svg(company_name: str, slug: str) -> str:
    label = initials(company_name)
    top, bot = color_pair(slug)

    if len(label) >= 3:
        font_size = 42
        letter_spacing = "0.02em"
    elif len(label) == 2:
        font_size = 54
        letter_spacing = "0.04em"
    else:
        font_size = 60
        letter_spacing = "0.02em"

    # SVG text vertical centering is inconsistent across fonts; y=74 is a good
    # visual center for 128×128 at these sizes.
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128" role="img" aria-label="{company_name} logo">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{top}" />
      <stop offset="100%" stop-color="{bot}" />
    </linearGradient>
  </defs>
  <rect x="6" y="6" width="116" height="116" rx="28" fill="url(#g)" />
  <rect x="6" y="6" width="116" height="116" rx="28" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="2" />
  <text x="64" y="74" text-anchor="middle"
        font-family="Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="{font_size}" font-weight="800"
        letter-spacing="{letter_spacing}"
        fill="rgba(255,255,255,0.94)">{label}</text>
</svg>
"""


def iter_active_slides(final_presentation_dir: Path) -> Iterable[Path]:
    deck_path = final_presentation_dir / "deck.md"
    deck_text = deck_path.read_text(encoding="utf-8")
    for rel in extract_deck_paths(deck_text):
        p = final_presentation_dir / rel
        if p.exists() and p.is_file():
            yield p


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate monogram SVG logos for companies in the active deck.")
    parser.add_argument(
        "--final-presentation-dir",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to final-presentation/ (default: inferred from script location).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing generated SVGs (will NOT overwrite non-SVG files).",
    )
    args = parser.parse_args()

    final_dir = Path(args.final_presentation_dir).resolve()
    logos_dir = final_dir / "assets" / "logos"
    logos_dir.mkdir(parents=True, exist_ok=True)

    companies: list[Company] = []
    for slide in iter_active_slides(final_dir):
        md = slide.read_text(encoding="utf-8")
        companies.extend(extract_companies_from_markdown(md, source=str(slide.relative_to(final_dir))))

    # De-dupe by slug, but keep the first name seen for initials/label.
    by_slug: dict[str, Company] = {}
    collisions: dict[str, set[str]] = {}
    for c in companies:
        if c.slug in by_slug and by_slug[c.slug].name != c.name:
            collisions.setdefault(c.slug, set()).update({by_slug[c.slug].name, c.name})
            continue
        by_slug.setdefault(c.slug, c)

    created = 0
    skipped = 0
    overwritten = 0

    for slug, c in sorted(by_slug.items(), key=lambda kv: kv[0]):
        existing = []
        for ext in ("svg", "png", "jpg", "jpeg"):
            p = logos_dir / f"{slug}.{ext}"
            if p.exists():
                existing.append(p)

        # Never overwrite non-SVG logos; they are assumed to be intentional overrides.
        if any(p.suffix.lower() != ".svg" for p in existing):
            skipped += 1
            continue

        out_path = logos_dir / f"{slug}.svg"
        if out_path.exists() and not args.force:
            skipped += 1
            continue

        if out_path.exists() and args.force:
            overwritten += 1
        else:
            created += 1

        out_path.write_text(monogram_svg(c.name, slug), encoding="utf-8")

    # Write a simple mapping file for transparency/debugging.
    mapping_path = logos_dir / "_generated_monograms.txt"
    lines: list[str] = []
    for slug, c in sorted(by_slug.items(), key=lambda kv: kv[0]):
        lines.append(f"{slug}\t{c.name}\t{c.source}")
    mapping_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if collisions:
        print("\nSlug collisions (review / standardize names if desired):")
        for slug, names in sorted(collisions.items(), key=lambda kv: kv[0]):
            print(f"- {slug}: {', '.join(sorted(names))}")

    print(f"Companies found: {len(companies)}")
    print(f"Unique slugs: {len(by_slug)}")
    print(f"Created SVGs: {created}")
    if args.force:
        print(f"Overwritten SVGs: {overwritten}")
    print(f"Skipped existing logos: {skipped}")
    print(f"Logos dir: {logos_dir}")
    print(f"Generated mapping: {mapping_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
