import os
import json
import argparse
from dotenv import load_dotenv
from firecrawl import Firecrawl

def scrape_brand_data(url, output_path):
    load_dotenv()
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        raise ValueError("FIRECRAWL_API_KEY is not set in the environment or .env file.")

    print(f"Scraping {url} with Firecrawl...")
    app = Firecrawl(api_key=api_key)
    
    result = app.scrape(
        url=url,
        formats=["branding", "images", "markdown", "screenshot"]
    )
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully scraped brand data. Results saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape a website for brand data using Firecrawl.")
    parser.add_argument("url", help="The URL to scrape (e.g., https://firecrawl.dev)")
    parser.add_argument("--output", default="tmp/brand_data.json", help="Path to save the JSON output")
    args = parser.parse_args()
    
    try:
        scrape_brand_data(args.url, args.output)
    except Exception as e:
        print(f"Error scraping {args.url}: {str(e)}")
        exit(1)
