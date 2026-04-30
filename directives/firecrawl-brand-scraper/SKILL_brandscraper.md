---
name: firecrawl-brand-scraper
description: Use this skill whenever the user asks to extract brand data, colors, typography, fonts, images, logos, or UI styles from a website URL. This will use the Firecrawl API to scrape the site and generate a brand profile.
---

# Firecrawl Brand Scraper Skill

You are using the Firecrawl Brand Scraper. This skill uses the Firecrawl API to scrape a target URL and extract structured brand identity information (colors, fonts, UI components) along with markdown, images, and a full-page screenshot.

## Instructions

1. **Check Prerequisites**: Ensure that `.env` contains a `FIRECRAWL_API_KEY`. If it doesn't, inform the user and stop.
2. **Execute the Scraper Script**: 
   Run the following command to scrape the target URL:
   ```bash
   python execution/scrape_brand_data.py <URL> --output tmp/brand_data.json
   ```
   *Note: Always use `tmp/brand_data.json` for intermediate outputs to adhere to the repository rules.*

3. **Parse and Process**:
   After the script completes successfully, read the contents of `tmp/brand_data.json`.
   The JSON will contain fields like `branding`, `markdown`, `images`, and `screenshot`. Look specifically inside `branding` for `colors`, `typography`, `fonts`, `logo`, and `components`.

4. **Present the Brand Guide**:
   Synthesize the extracted data into a beautiful and well-structured Markdown Brand Guide. 
   Include:
   - **Visuals**: Logo and Screenshot (using markdown image syntax).
   - **Color Palette**: Show the extracted colors (primary, secondary, background, text, etc.) with their respective hex codes.
   - **Typography**: List the fonts, headings, and font weights.
   - **Components**: Detail the buttons or other UI elements found.
   - **Content Summary**: A very brief summary of the site based on the `markdown` format.

## Troubleshooting
- If you encounter rate limits or missing elements, self-anneal by noting the error and trying once more if applicable. 
- If it consistently fails, check the `markdown` fallback to piece together colors/fonts if possible, or gracefully explain the error to the user and suggest an alternative url.
