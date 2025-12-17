#!/usr/bin/env python3
"""
Fetch real company logos and replace monograms.

This script:
1. Extracts company names from markdown tables
2. Attempts to fetch logos from multiple sources
3. Downloads and saves logos as SVG
4. Verifies logo URLs are correct
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse
import requests
from io import BytesIO
from PIL import Image
import xml.etree.ElementTree as ET

# Reuse logic from generate_monogram_logos.py
RE_CODE_MD = re.compile(r"`([^`]+\.md)`", re.IGNORECASE)
RE_PLAIN_MD = re.compile(r"([\w./-]+\.md)\b", re.IGNORECASE)
RE_SEPARATOR = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
RE_TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
RE_MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
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
    v = re.sub(r"^final-presentation/", "", v)
    return v or None


@dataclass(frozen=True)
class Company:
    name: str
    slug: str
    source: str
    primary_link: str | None = None


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

        # Try to find primary link column
        link_idx = None
        for idx, h in enumerate(normalized):
            if "link" in h or "url" in h or "primary" in h:
                link_idx = idx
                break

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

            # Extract primary link if available
            primary_link = None
            if link_idx is not None and link_idx < len(row):
                link_match = RE_MD_LINK.search(row[link_idx])
                if link_match:
                    primary_link = link_match.group(2)
                else:
                    # Try plain URL
                    url_text = strip_markdown(row[link_idx])
                    if url_text.startswith("http"):
                        primary_link = url_text

            out.append(Company(name=name, slug=s, source=source, primary_link=primary_link))

    return out


def extract_domain_from_url(url: str) -> str | None:
    """Extract domain from URL."""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path.split("/")[0]
        # Remove www. prefix
        domain = domain.replace("www.", "")
        return domain.lower() if domain else None
    except Exception:
        return None


def extract_domain_from_company_name(name: str) -> str:
    """Try to extract a domain-like string from company name."""
    # Remove common suffixes and clean up
    name = name.lower()
    name = re.sub(r"\s*\([^)]*\)", "", name)  # Remove parentheses content
    name = re.sub(r"\s*\[[^\]]*\]", "", name)  # Remove brackets
    name = name.replace("&", "and")
    name = re.sub(r"[^a-z0-9\s]", "", name)
    words = name.split()
    
    # Remove common words
    stop_words = {"ai", "inc", "llc", "ltd", "co", "corp", "corporation", "company", 
                  "technologies", "technology", "systems", "labs", "group", "holdings",
                  "the", "a", "an", "amazon", "aws", "google", "cloud", "microsoft",
                  "agent", "agents", "sdk", "framework", "platform", "api"}
    words = [w for w in words if w not in stop_words]
    
    if not words:
        return ""
    
    # Take first 1-2 words
    domain = "".join(words[:2]) if len(words) >= 2 else words[0]
    return domain


def fetch_logo_clearbit(domain: str) -> bytes | None:
    """Fetch logo from Clearbit Logo API."""
    try:
        url = f"https://logo.clearbit.com/{domain}"
        response = requests.get(url, timeout=5, allow_redirects=True)
        if response.status_code == 200 and response.headers.get("content-type", "").startswith("image"):
            return response.content
    except Exception:
        pass
    return None


def fetch_logo_google_favicon(domain: str) -> bytes | None:
    """Fetch favicon from Google's favicon service."""
    try:
        url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.content
    except Exception:
        pass
    return None


def fetch_logo_direct(domain: str) -> bytes | None:
    """Try common logo paths on the domain."""
    common_paths = [
        f"https://{domain}/logo.svg",
        f"https://{domain}/assets/logo.svg",
        f"https://{domain}/images/logo.svg",
        f"https://www.{domain}/logo.svg",
        f"https://www.{domain}/assets/logo.svg",
        f"https://www.{domain}/images/logo.svg",
    ]
    
    for path in common_paths:
        try:
            response = requests.get(path, timeout=5, allow_redirects=True)
            if response.status_code == 200:
                content_type = response.headers.get("content-type", "")
                if "image" in content_type or path.endswith(".svg"):
                    return response.content
        except Exception:
            continue
    return None


def convert_to_svg(image_data: bytes, company_name: str) -> str | None:
    """Convert image to SVG format."""
    try:
        img = Image.open(BytesIO(image_data))
        
        # Convert RGBA to RGB if needed
        if img.mode == "RGBA":
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        elif img.mode != "RGB":
            img = img.convert("RGB")
        
        # Resize to 128x128 while maintaining aspect ratio
        img.thumbnail((128, 128), Image.Resampling.LANCZOS)
        
        # Create a square canvas
        size = max(img.size)
        canvas = Image.new("RGB", (size, size), (255, 255, 255))
        offset = ((size - img.size[0]) // 2, (size - img.size[1]) // 2)
        canvas.paste(img, offset)
        
        # Convert to base64
        import base64
        buffer = BytesIO()
        canvas.save(buffer, format="PNG")
        img_data = base64.b64encode(buffer.getvalue()).decode()
        
        # Create SVG wrapper
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="128" height="128" viewBox="0 0 {size} {size}" role="img" aria-label="{company_name} logo">
  <image width="{size}" height="{size}" xlink:href="data:image/png;base64,{img_data}"/>
</svg>'''
        return svg
    except Exception as e:
        print(f"  Error converting to SVG: {e}", file=sys.stderr)
        return None


def is_svg(data: bytes) -> bool:
    """Check if data is SVG."""
    try:
        text = data.decode("utf-8", errors="ignore")
        return text.strip().startswith("<svg") or text.strip().startswith("<?xml")
    except Exception:
        return False


def fetch_company_logo(company: Company) -> tuple[str | None, str]:
    """Fetch logo for a company. Returns (logo_data, source_method)."""
    domain = None
    
    # Try to get domain from primary link
    if company.primary_link:
        domain = extract_domain_from_url(company.primary_link)
        # Handle special cases
        if domain:
            # GitHub repos -> try to get org/company domain
            if "github.com" in domain:
                parts = domain.split("/")
                if len(parts) >= 2:
                    org = parts[1]
                    # Try common patterns for org domains
                    for tld in ["com", "io", "ai", "dev", "co", "app", "org"]:
                        test_domain = f"{org}.{tld}"
                        # Test if this domain exists by trying Clearbit
                        test_logo = fetch_logo_clearbit(test_domain)
                        if test_logo:
                            domain = test_domain
                            break
                    else:
                        # Fallback: use github.com for GitHub orgs
                        domain = "github.com"
            # docs.* subdomains -> try main domain
            elif domain.startswith("docs."):
                domain = domain.replace("docs.", "")
            # *.cloud.google.com -> google.com
            elif "cloud.google.com" in domain:
                domain = "google.com"
            # *.amazonaws.com -> amazon.com
            elif "amazonaws.com" in domain or "aws.amazon.com" in domain:
                domain = "amazon.com"
            # *.microsoft.com -> microsoft.com
            elif "microsoft.com" in domain:
                domain = "microsoft.com"
    
    # Fallback to extracting from company name
    if not domain:
        domain_guess = extract_domain_from_company_name(company.name)
        if domain_guess:
            # Try common TLDs
            for tld in ["com", "io", "ai", "dev", "co", "app", "org"]:
                test_domain = f"{domain_guess}.{tld}"
                # Quick test with Clearbit
                test_logo = fetch_logo_clearbit(test_domain)
                if test_logo:
                    domain = test_domain
                    break
    
    # Special mappings for known companies
    special_mappings = {
        "openai": "openai.com",
        "anthropic": "anthropic.com",
        "google cloud vertex ai": "google.com",
        "aws amazon bedrock agentcore": "amazon.com",
        "microsoft semantic kernel": "microsoft.com",
        "microsoft autogen": "microsoft.com",
        "databricks agent bricks": "databricks.com",
        "snowflake cortex agents": "snowflake.com",
        "ibm watsonx orchestrate": "ibm.com",
        "cohere": "cohere.com",
        "mistral agents api": "mistral.ai",
        "mozilla.ai agent platform": "mozilla.ai",
        "langchain": "langchain.com",
        "langgraph": "langchain.com",  # Same company
        "crewai": "crewai.com",
        "llamaindex": "llamaindex.ai",
        "haystack": "deepset.ai",
        "hugging face smolagents": "huggingface.co",
        "dspy": "stanford.edu",  # Stanford project
        "letta": "letta.com",
        "browserbase stagehand": "browserbase.com",
        "cyberdesk": "cyberdesk.io",
        "tinyfish / agentql": "agentql.com",
        "skyvern": "skyvern.com",
        "steel.dev": "steel.dev",
        "anchor browser": "anchorbrowser.io",
        "induced ai": "induced.ai",
        "scrapybara": "scrapybara.com",
        "browser use": "browser-use.com",
        "magnitude": "magnitude.run",
        "multion": "multion.ai",
        "simular ai": "simular.ai",
    }
    
    name_lower = company.name.lower()
    for key, mapped_domain in special_mappings.items():
        if key in name_lower:
            domain = mapped_domain
            break
    
    if not domain:
        return None, "no_domain"
    
    # Try Clearbit first (most reliable)
    logo_data = fetch_logo_clearbit(domain)
    if logo_data:
        if is_svg(logo_data):
            return logo_data.decode("utf-8"), "clearbit_svg"
        else:
            svg = convert_to_svg(logo_data, company.name)
            if svg:
                return svg, "clearbit_converted"
    
    # Try Google favicon
    logo_data = fetch_logo_google_favicon(domain)
    if logo_data:
        svg = convert_to_svg(logo_data, company.name)
        if svg:
            return svg, "google_favicon"
    
    # Try direct paths
    logo_data = fetch_logo_direct(domain)
    if logo_data:
        if is_svg(logo_data):
            return logo_data.decode("utf-8"), "direct_svg"
        else:
            svg = convert_to_svg(logo_data, company.name)
            if svg:
                return svg, "direct_converted"
    
    return None, "not_found"


def iter_active_slides(final_presentation_dir: Path) -> Iterable[Path]:
    deck_path = final_presentation_dir / "deck.md"
    deck_text = deck_path.read_text(encoding="utf-8")
    for rel in extract_deck_paths(deck_text):
        p = final_presentation_dir / rel
        if p.exists() and p.is_file():
            yield p


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch real company logos and replace monograms.")
    parser.add_argument(
        "--final-presentation-dir",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to final-presentation/ (default: inferred from script location).",
    )
    parser.add_argument(
        "--segment",
        help="Process only a specific segment file (e.g., 'part-1-market-segments/06_developer_and_sdk_first.md')",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing logos (including non-SVG files).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be fetched without downloading.",
    )
    args = parser.parse_args()

    final_dir = Path(args.final_presentation_dir).resolve()
    logos_dir = final_dir / "assets" / "logos"
    logos_dir.mkdir(parents=True, exist_ok=True)

    companies: list[Company] = []
    
    if args.segment:
        # Process only the specified segment
        slide_path = final_dir / args.segment
        if not slide_path.exists():
            print(f"Error: Segment file not found: {slide_path}", file=sys.stderr)
            return 1
        md = slide_path.read_text(encoding="utf-8")
        companies.extend(extract_companies_from_markdown(md, source=args.segment))
    else:
        # Process all active slides
        for slide in iter_active_slides(final_dir):
            md = slide.read_text(encoding="utf-8")
            companies.extend(extract_companies_from_markdown(md, source=str(slide.relative_to(final_dir))))

    # De-dupe by slug
    by_slug: dict[str, Company] = {}
    for c in companies:
        if c.slug not in by_slug:
            by_slug[c.slug] = c
        # Prefer company with primary_link if available
        elif c.primary_link and not by_slug[c.slug].primary_link:
            by_slug[c.slug] = c

    print(f"Found {len(companies)} company entries ({len(by_slug)} unique)")
    print(f"Processing logos...\n")

    fetched = 0
    skipped = 0
    failed = 0
    results = []

    for slug, company in sorted(by_slug.items(), key=lambda kv: kv[0]):
        logo_path = logos_dir / f"{slug}.svg"
        
        # Check if logo already exists
        if logo_path.exists() and not args.force:
            skipped += 1
            results.append((company.name, slug, "skipped_existing", None))
            continue
        
        if args.dry_run:
            print(f"Would fetch: {company.name} ({slug})")
            if company.primary_link:
                print(f"  Link: {company.primary_link}")
            continue
        
        print(f"Fetching logo for: {company.name}")
        if company.primary_link:
            print(f"  Using link: {company.primary_link}")
        
        logo_svg, method = fetch_company_logo(company)
        
        if logo_svg:
            logo_path.write_text(logo_svg, encoding="utf-8")
            fetched += 1
            results.append((company.name, slug, method, company.primary_link))
            print(f"  ✓ Fetched via {method}")
        else:
            failed += 1
            results.append((company.name, slug, method, company.primary_link))
            print(f"  ✗ Failed ({method})")
        print()

    if not args.dry_run:
        # Write results summary
        summary_path = logos_dir / "_logo_fetch_results.txt"
        lines = ["Company\tSlug\tMethod\tPrimary Link"]
        for name, slug, method, link in results:
            lines.append(f"{name}\t{slug}\t{method}\t{link or ''}")
        summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        
        print(f"\nSummary:")
        print(f"  Fetched: {fetched}")
        print(f"  Skipped: {skipped}")
        print(f"  Failed: {failed}")
        print(f"  Results saved to: {summary_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
