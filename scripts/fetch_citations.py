#!/usr/bin/env python3
"""
Fetch citation counts from Google Scholar and update citation data file.
"""

import json
from scholarly import scholarly
import time

# Your Google Scholar user ID
SCHOLAR_ID = "iL2j_yAAAAAJ"

# Paper mapping: title -> display name
PAPERS = {
    "Sonic: Shifting focus to global audio perception in portrait animation": "Sonic",
    "RealTalk: Real-time and Realistic Audio-driven Face Generation with 3D Facial Prior-guided Identity Alignment Network": "RealTalk",
    "Real-World Super-Resolution via Kernel Estimation and Noise Injection": "RealSR",
    "UniM-OV3D: Uni-Modality Open-Vocabulary 3D Scene Understanding with Fine-Grained Feature Representation": "UniM-OV3D",
    "ColorFormer: Image Colorization via Color Memory Assisted Hybrid-Attention Transformer": "ColorFormer",
    "Spectrum-to-Kernel Translation for Accurate Blind Image Super-Resolution": "Spectrum-to-Kernel",
    "Frequency Consistent Adaptation for Real World Super Resolution": "FCA"
}

def fetch_scholar_data():
    """Fetch author and publication data from Google Scholar."""
    print(f"Fetching data for scholar ID: {SCHOLAR_ID}")

    try:
        # Search for author by ID
        author = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(author)

        # Extract citation data
        citation_data = {
            "last_updated": time.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "total_citations": author.get('citedby', 0),
            "h_index": author.get('hindex', 0),
            "i10_index": author.get('i10index', 0),
            "papers": {}
        }

        # Process each publication
        for pub in author.get('publications', []):
            title = pub['bib'].get('title', '')

            # Match with our paper list
            for paper_title, paper_key in PAPERS.items():
                if paper_title.lower() in title.lower() or title.lower() in paper_title.lower():
                    citations = pub.get('num_citations', 0)
                    pub_year = pub['bib'].get('pub_year', 'N/A')

                    citation_data['papers'][paper_key] = {
                        "title": title,
                        "citations": citations,
                        "year": pub_year,
                        "url": pub.get('author_pub_id', '')
                    }
                    print(f"  {paper_key}: {citations} citations")
                    break

        return citation_data

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    """Main function to fetch and save citation data."""
    print("Starting Google Scholar citation fetch...")

    # Fetch data
    data = fetch_scholar_data()

    if data:
        # Save to JSON file
        output_file = "_data/citations.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\nSuccessfully saved citation data to {output_file}")
        print(f"Total citations: {data['total_citations']}")
        print(f"Papers tracked: {len(data['papers'])}")
    else:
        print("Failed to fetch citation data")
        exit(1)

if __name__ == "__main__":
    main()
