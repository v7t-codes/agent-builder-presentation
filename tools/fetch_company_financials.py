#!/usr/bin/env python3
"""
Script to fetch and populate financial data (revenue, fundraise, market cap) for companies.
This script helps research and populate the company_financial_data.json database.
"""

import json
import re
import sys
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse
import requests
from dataclasses import dataclass, asdict

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

@dataclass
class FinancialData:
    """Financial data for a company"""
    revenue: Optional[str] = None  # e.g., "$100M", "$1.2B", "Private"
    revenue_year: Optional[str] = None  # e.g., "2024"
    fundraise: Optional[str] = None  # e.g., "$50M Series B", "$200M total"
    fundraise_date: Optional[str] = None  # e.g., "2024", "Q1 2024"
    market_cap: Optional[str] = None  # e.g., "$5B", "Public"
    market_cap_date: Optional[str] = None  # e.g., "2024"
    source: Optional[str] = None  # URL or note about where data came from
    notes: Optional[str] = None  # Additional notes

def extract_companies_from_markdown() -> list[dict]:
    """Extract all companies from the markdown file"""
    md_file = Path(__file__).parent.parent / "assets" / "logos" / "all_companies_with_links.md"
    
    if not md_file.exists():
        print(f"Error: {md_file} not found")
        return []
    
    companies = []
    current_segment = None
    
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        # Detect segment headers
        if line.startswith("## Segment"):
            match = re.search(r"Segment \d+:\s*(.+)", line)
            if match:
                current_segment = match.group(1).strip()
        
        # Parse table rows (format: | Company | Slug | Primary Link |)
        if line.startswith("|") and "|" in line and i > 0:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3 and parts[0].lower() != "company":
                company_name = parts[0]
                slug = parts[1] if len(parts) > 1 else None
                primary_link = parts[2] if len(parts) > 2 else None
                
                # Skip header rows and invalid entries
                if (company_name and slug and 
                    company_name not in ["Company", "---------", "---"] and
                    slug not in ["Slug", "------", "---"] and
                    not company_name.startswith("-") and
                    not slug.startswith("-")):
                    companies.append({
                        "name": company_name,
                        "slug": slug,
                        "primary_link": primary_link,
                        "segment": current_segment
                    })
    
    return companies

def extract_domain_from_url(url: str) -> Optional[str]:
    """Extract main domain from URL"""
    if not url:
        return None
    try:
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path.split('/')[0]
        # Remove www., docs., github.com, etc.
        domain = re.sub(r'^(www\.|docs\.|github\.com|support\.)', '', domain)
        # Extract just the domain name
        domain = domain.split('/')[0].split(':')[0]
        return domain.lower() if domain else None
    except:
        return None

def normalize_company_name(name: str) -> str:
    """Normalize company name for searching"""
    # Remove common suffixes in parentheses
    name = re.sub(r'\s*\([^)]+\)', '', name)
    # Remove common prefixes
    name = re.sub(r'^(AWS|Google|Microsoft|IBM|Oracle|SAP|Salesforce|ServiceNow|UiPath|Zendesk|Zoho|HubSpot|Freshworks|Atlassian|Palo Alto Networks)\s+', '', name, flags=re.IGNORECASE)
    return name.strip()

def search_crunchbase(company_name: str, domain: Optional[str] = None) -> Optional[dict]:
    """
    Search Crunchbase for company financial data.
    Note: This is a placeholder - actual implementation would require Crunchbase API or web scraping.
    """
    # Placeholder - in real implementation, you'd use Crunchbase API or scrape
    print(f"  [Crunchbase] Searching for {company_name}...")
    return None

def search_web_for_financials(company_name: str, domain: Optional[str] = None) -> Optional[dict]:
    """
    Search web for company financial data.
    This is a placeholder - you can enhance with actual web scraping or API calls.
    """
    print(f"  [Web Search] Searching for financials for {company_name}...")
    
    # Common patterns to search for:
    # - "{company} funding" or "{company} raised"
    # - "{company} revenue"
    # - "{company} valuation" or "{company} market cap"
    # - "{company} IPO"
    
    return None

def get_known_financials() -> dict:
    """
    Return a dictionary of known financial data for major companies.
    This can be populated with publicly available information.
    """
    known_data = {
        # Major public companies
        "OpenAI": FinancialData(
            fundraise="$13B+",
            fundraise_date="2024",
            notes="Microsoft investment, valuation ~$80B+"
        ),
        "Anthropic": FinancialData(
            fundraise="$7.3B+",
            fundraise_date="2024",
            notes="Amazon & Google investments, valuation ~$18B"
        ),
        "Microsoft": FinancialData(
            market_cap="$3.2T+",
            market_cap_date="2024",
            revenue="$211B",
            revenue_year="2023"
        ),
        "Google": FinancialData(
            market_cap="$1.8T+",
            market_cap_date="2024",
            revenue="$307B",
            revenue_year="2023"
        ),
        "Amazon": FinancialData(
            market_cap="$1.8T+",
            market_cap_date="2024",
            revenue="$574B",
            revenue_year="2023"
        ),
        "Salesforce": FinancialData(
            market_cap="$250B+",
            market_cap_date="2024",
            revenue="$34.9B",
            revenue_year="2024"
        ),
        "ServiceNow": FinancialData(
            market_cap="$150B+",
            market_cap_date="2024",
            revenue="$9.0B",
            revenue_year="2023"
        ),
        "UiPath": FinancialData(
            market_cap="$10B+",
            market_cap_date="2024",
            revenue="$1.3B",
            revenue_year="2024"
        ),
        "Databricks": FinancialData(
            fundraise="$4.1B",
            fundraise_date="2024",
            notes="Valuation $43B"
        ),
        "Cohere": FinancialData(
            fundraise="$445M",
            fundraise_date="2024",
            notes="Valuation $2.2B"
        ),
        "Mistral AI": FinancialData(
            fundraise="$600M+",
            fundraise_date="2024",
            notes="Valuation $6B"
        ),
        "LangChain": FinancialData(
            fundraise="$45M",
            fundraise_date="2023",
            notes="Series A"
        ),
        "LlamaIndex": FinancialData(
            fundraise="$8.5M",
            fundraise_date="2023",
            notes="Seed"
        ),
        "Moveworks": FinancialData(
            fundraise="$310M",
            fundraise_date="2024",
            notes="Series C, Valuation $2.1B"
        ),
        "Cresta": FinancialData(
            fundraise="$80M",
            fundraise_date="2022",
            notes="Series C"
        ),
        "Harvey": FinancialData(
            fundraise="$100M+",
            fundraise_date="2024",
            notes="Series B, Valuation $715M"
        ),
        "LivePerson": FinancialData(
            market_cap="$200M+",
            market_cap_date="2024",
            revenue="$400M+",
            revenue_year="2023"
        ),
        "Zapier": FinancialData(
            fundraise="Private",
            notes="Bootstrapped, profitable"
        ),
        "n8n": FinancialData(
            fundraise="$12M",
            fundraise_date="2023",
            notes="Series A"
        ),
        "Voiceflow": FinancialData(
            fundraise="$15M",
            fundraise_date="2023",
            notes="Series A"
        ),
        "Dify": FinancialData(
            fundraise="$7M",
            fundraise_date="2024",
            notes="Seed"
        ),
        "Relevance AI": FinancialData(
            fundraise="$10M",
            fundraise_date="2023",
            notes="Seed"
        ),
        "Stack AI": FinancialData(
            fundraise="$3.5M",
            fundraise_date="2023",
            notes="Seed"
        ),
        "Lindy.ai": FinancialData(
            fundraise="$6M",
            fundraise_date="2023",
            notes="Seed"
        ),
        "Bardeen": FinancialData(
            fundraise="$15M",
            fundraise_date="2023",
            notes="Series A"
        ),
        "Cognition": FinancialData(
            fundraise="$175M",
            fundraise_date="2024",
            notes="Series B, Valuation $2B"
        ),
        "Sierra": FinancialData(
            fundraise="$110M",
            fundraise_date="2024",
            notes="Series A"
        ),
        "Yellow.ai": FinancialData(
            fundraise="$78M",
            fundraise_date="2022",
            notes="Series C"
        ),
        "Kore.ai": FinancialData(
            fundraise="$150M+",
            fundraise_date="2024",
            notes="Series D"
        ),
        "Uniphore": FinancialData(
            fundraise="$400M",
            fundraise_date="2022",
            notes="Series E, Valuation $2.5B"
        ),
        "Ironclad": FinancialData(
            fundraise="$150M",
            fundraise_date="2024",
            notes="Series E, Valuation $1.5B"
        ),
        "Evisort": FinancialData(
            fundraise="$100M",
            fundraise_date="2022",
            notes="Series C"
        ),
        "Forethought": FinancialData(
            fundraise="$65M",
            fundraise_date="2023",
            notes="Series C"
        ),
        "Observe.AI": FinancialData(
            fundraise="$125M",
            fundraise_date="2021",
            notes="Series C"
        ),
        "Replicant": FinancialData(
            fundraise="$78M",
            fundraise_date="2022",
            notes="Series B"
        ),
        "PolyAI": FinancialData(
            fundraise="$50M",
            fundraise_date="2023",
            notes="Series C"
        ),
        "Paradox": FinancialData(
            fundraise="$200M",
            fundraise_date="2022",
            notes="Series C, Valuation $1.5B"
        ),
        "Tines": FinancialData(
            fundraise="$50M",
            fundraise_date="2023",
            notes="Series B"
        ),
        "Torq": FinancialData(
            fundraise="$50M",
            fundraise_date="2023",
            notes="Series B"
        ),
        "Swimlane": FinancialData(
            fundraise="$70M",
            fundraise_date="2023",
            notes="Series C"
        ),
        "Palo Alto Networks": FinancialData(
            market_cap="$100B+",
            market_cap_date="2024",
            revenue="$7.5B",
            revenue_year="2024"
        ),
        "IBM": FinancialData(
            market_cap="$180B+",
            market_cap_date="2024",
            revenue="$60B+",
            revenue_year="2023"
        ),
        "Oracle": FinancialData(
            market_cap="$400B+",
            market_cap_date="2024",
            revenue="$50B+",
            revenue_year="2024"
        ),
        "SAP": FinancialData(
            market_cap="$200B+",
            market_cap_date="2024",
            revenue="$34B+",
            revenue_year="2023"
        ),
        "Snowflake": FinancialData(
            market_cap="$50B+",
            market_cap_date="2024",
            revenue="$2.8B",
            revenue_year="2024"
        ),
        "Atlassian": FinancialData(
            market_cap="$50B+",
            market_cap_date="2024",
            revenue="$3.8B",
            revenue_year="2024"
        ),
        "HubSpot": FinancialData(
            market_cap="$30B+",
            market_cap_date="2024",
            revenue="$2.2B",
            revenue_year="2023"
        ),
        "Zendesk": FinancialData(
            market_cap="$10B+",
            market_cap_date="2024",
            revenue="$1.7B",
            revenue_year="2023"
        ),
        "Freshworks": FinancialData(
            market_cap="$3B+",
            market_cap_date="2024",
            revenue="$600M+",
            revenue_year="2023"
        ),
        "Zoho": FinancialData(
            revenue="$1B+",
            revenue_year="2023",
            notes="Private, profitable"
        ),
        "Automation Anywhere": FinancialData(
            fundraise="$840M",
            fundraise_date="2021",
            notes="Valuation $6.8B"
        ),
        "Botpress": FinancialData(
            fundraise="$15M",
            fundraise_date="2023",
            notes="Series A"
        ),
        "Make": FinancialData(
            fundraise="$70M",
            fundraise_date="2022",
            notes="Series A"
        ),
        "Workato": FinancialData(
            fundraise="$200M",
            fundraise_date="2021",
            notes="Series E, Valuation $5.7B"
        ),
        "Tray.io": FinancialData(
            fundraise="$50M",
            fundraise_date="2021",
            notes="Series C"
        ),
    }
    
    # Convert to dict format
    return {k: asdict(v) for k, v in known_data.items()}

def load_existing_data() -> dict:
    """Load existing financial data from JSON file"""
    data_file = Path(__file__).parent.parent / "assets" / "company_financial_data.json"
    
    if data_file.exists():
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {"companies": {}}

def save_data(data: dict):
    """Save financial data to JSON file"""
    data_file = Path(__file__).parent.parent / "assets" / "company_financial_data.json"
    
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def match_company_name(company_name: str, known_data: dict) -> Optional[dict]:
    """Try to match company name with known financial data"""
    normalized = normalize_company_name(company_name)
    
    # Direct match
    if company_name in known_data:
        return known_data[company_name]
    
    # Try normalized match
    for known_name, data in known_data.items():
        if normalized.lower() == normalize_company_name(known_name).lower():
            return data
    
    # Try partial match (for cases like "Microsoft AutoGen" -> "Microsoft")
    for known_name in known_data.keys():
        if known_name.lower() in company_name.lower() or company_name.lower() in known_name.lower():
            return known_data[known_name]
    
    return None

def main():
    """Main function to populate financial data"""
    print("Fetching company financial data...")
    print("=" * 60)
    
    companies = extract_companies_from_markdown()
    print(f"Found {len(companies)} companies")
    
    existing_data = load_existing_data()
    known_financials = get_known_financials()
    
    updated = 0
    for company in companies:
        name = company["name"]
        slug = company["slug"]
        
        # Skip if already has data
        if slug in existing_data.get("companies", {}):
            continue
        
        print(f"\nProcessing: {name} ({slug})")
        
        # Try to match with known data
        financial_data = match_company_name(name, known_financials)
        
        if financial_data:
            existing_data.setdefault("companies", {})[slug] = {
                "name": name,
                **financial_data
            }
            updated += 1
            print(f"  ✓ Found financial data")
        else:
            # Add empty entry
            existing_data.setdefault("companies", {})[slug] = {
                "name": name,
                "revenue": None,
                "revenue_year": None,
                "fundraise": None,
                "fundraise_date": None,
                "market_cap": None,
                "market_cap_date": None,
                "source": None,
                "notes": None
            }
            print(f"  - No data found (placeholder added)")
    
    save_data(existing_data)
    print(f"\n{'=' * 60}")
    print(f"Updated {updated} companies with financial data")
    print(f"Total companies in database: {len(existing_data.get('companies', {}))}")
    print(f"\nData saved to: assets/company_financial_data.json")
    print("\nNote: You can manually edit the JSON file to add more data.")

if __name__ == "__main__":
    main()

