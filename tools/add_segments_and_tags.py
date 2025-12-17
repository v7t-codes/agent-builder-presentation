#!/usr/bin/env python3
"""
Script to add segment and tag information to company financial data based on the markdown file.
"""

import json
import re
from pathlib import Path

def extract_companies_with_segments():
    """Extract companies and their segments from the markdown file"""
    md_file = Path(__file__).parent.parent / "assets" / "logos" / "all_companies_with_links.md"
    
    companies_map = {}
    current_segment = None
    
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        # Detect segment headers
        if line.startswith("## Segment"):
            match = re.search(r"Segment \d+:\s*(.+)", line)
            if match:
                current_segment = match.group(1).strip()
        
        # Parse table rows
        if line.startswith("|") and "|" in line and i > 0:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3 and parts[0].lower() != "company":
                company_name = parts[0]
                slug = parts[1] if len(parts) > 1 else None
                
                # Skip header rows
                if (company_name and slug and 
                    company_name not in ["Company", "---------", "---"] and
                    slug not in ["Slug", "------", "---"] and
                    not company_name.startswith("-") and
                    not slug.startswith("-")):
                    
                    # Normalize segment name
                    segment_map = {
                        "Developer & SDK-first": "Developer & SDK-first",
                        "No-code & Visual": "No-code & Visual",
                        "Vertical-specific": "Vertical-specific",
                        "Agent Studios": "Agent Studios",
                        "AI Employees Overlay": "AI Employees Overlay"
                    }
                    
                    segment = segment_map.get(current_segment, current_segment)
                    
                    companies_map[slug] = {
                        "segment": segment,
                        "name": company_name
                    }
    
    return companies_map

def get_tags_for_company(company_name, segment):
    """Generate appropriate tags based on company name and segment"""
    tags = []
    name_lower = company_name.lower()
    
    # Segment-based tags
    if segment == "Developer & SDK-first":
        tags.append("developer-tools")
        tags.append("sdk")
    elif segment == "No-code & Visual":
        tags.append("no-code")
        tags.append("visual-builder")
    elif segment == "Vertical-specific":
        tags.append("vertical-specific")
    elif segment == "Agent Studios":
        tags.append("consulting")
        tags.append("services")
    elif segment == "AI Employees Overlay":
        tags.append("ai-employees")
        tags.append("autonomous-agents")
    
    # Industry/domain tags based on company name
    if any(x in name_lower for x in ["healthcare", "health", "medical", "notable", "qventus"]):
        tags.append("healthcare")
    if any(x in name_lower for x in ["legal", "law", "harvey", "contract", "evisort", "ironclad"]):
        tags.append("legal")
    if any(x in name_lower for x in ["customer", "support", "service", "ada", "zendesk", "freshworks"]):
        tags.append("customer-support")
    if any(x in name_lower for x in ["sales", "crm", "salesforce", "hubspot"]):
        tags.append("sales")
    if any(x in name_lower for x in ["hr", "human", "recruiting", "paradox"]):
        tags.append("hr")
    if any(x in name_lower for x in ["finance", "expense", "appzen", "auditoria", "glean"]):
        tags.append("finance")
    if any(x in name_lower for x in ["security", "cyber", "palo", "swimlane", "tines", "torq"]):
        tags.append("security")
    if any(x in name_lower for x in ["chatbot", "conversational", "cognigy", "boost", "kore"]):
        tags.append("conversational-ai")
    if any(x in name_lower for x in ["automation", "rpa", "uipath", "automation anywhere"]):
        tags.append("automation")
    if any(x in name_lower for x in ["data", "databricks", "snowflake"]):
        tags.append("data-platform")
    if any(x in name_lower for x in ["cloud", "aws", "azure", "gcp", "google cloud"]):
        tags.append("cloud")
    if any(x in name_lower for x in ["openai", "anthropic", "mistral", "cohere"]):
        tags.append("foundation-model")
    
    # Remove duplicates
    return list(set(tags))

def main():
    """Update financial data with segments and tags"""
    data_file = Path(__file__).parent.parent / "assets" / "company_financial_data.json"
    
    # Load existing data
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Get segment mapping
    companies_map = extract_companies_with_segments()
    
    updated = 0
    for slug, company_data in data.get("companies", {}).items():
        if slug in companies_map:
            segment_info = companies_map[slug]
            
            # Add segment if not present
            if "segment" not in company_data or company_data["segment"] != segment_info["segment"]:
                company_data["segment"] = segment_info["segment"]
                updated += 1
            
            # Add tags if not present
            if "tags" not in company_data or not company_data["tags"]:
                tags = get_tags_for_company(company_data.get("name", ""), segment_info["segment"])
                if tags:
                    company_data["tags"] = tags
                    updated += 1
    
    # Save updated data
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Updated {updated} companies with segments and tags")
    print(f"Total companies: {len(data.get('companies', {}))}")

if __name__ == "__main__":
    main()

