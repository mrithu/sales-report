Built as part of Google's Build with AI initiative powered by Hack2Skill

# Feastables Sales Report & Brand Toolkit

Welcome to the Feastables Sales Report project. This repository serves two main purposes:
1. An interactive, highly-branded frontend dashboard for tracking Feastables sales metrics.
2. A suite of custom agentic skills (using a strict 3-Layer Directive architecture) built to automatically scrape, parse, and enforce brand guidelines using the Firecrawl API.

---

## 🚀 Features

### 1. The Feastables Dashboard
Located at [`dashboard.html`](./dashboard.html), this is a single-page, vanilla HTML/JS/CSS web application that embodies the playful, high-energy aesthetic of the Feastables brand. 
- **Real Data Integration:** Features actual products (Mario Galaxy Cocoa Crunch, Milk Chocolate, etc.) and imagery pulled directly from Feastables.com.
- **Interactive Charting:** Dynamic, tab-based switching between line charts, bar charts, and doughnut graphs powered by Chart.js.
- **Brutalist/Playful UI:** Implements sharp 0px borders, offset drop shadows, background patterns, and high-contrast neon colors extracted directly from the brand guidelines.

### 2. Firecrawl Brand Scraper Skill
A custom AI skill designed to extract brand visual identity from any URL.
- **Directive:** Located in `directives/firecrawl-brand-scraper/SKILL.md`. Guides the AI on when and how to extract data.
- **Execution Script:** Located in `execution/scrape_brand_data.py`. Uses `firecrawl-py` to fetch logos, hex colors, typography, and UI component shapes.
- **Output:** Saves rich JSON data (like the provided `brand-data/feastables.json`) for downstream consumption.

### 3. Brand Guidelines Enforcer
Located in `brand-guidelines/SKILL_brandguidelines.md`. It acts as the final step in the pipeline, translating the raw JSON from the scraper into actionable AI formatting rules (e.g., use Kanit font, #72E2FF Primary Blue) for generating strictly on-brand frontend designs.

---

## 🛠️ Setup & Usage

### Viewing the Dashboard
Simply double-click the `dashboard.html` file in your file explorer to open it in your default web browser. No local development server or build step is required!

### Using the Brand Scraper
To scrape a new brand's guidelines:
1. Ensure your dependencies are installed:
   ```bash
   pip install firecrawl-py python-dotenv
   ```
2. Add your Firecrawl API key to the `.env` file in the root directory:
   ```env
   FIRECRAWL_API_KEY="fc-your-api-key-here"
   ```
3. Run the extraction script:
   ```bash
   python execution/scrape_brand_data.py https://example.com --output brand-data/example.json
   ```

---

## 🏗️ Architecture Note
This project was built adhering to the repository's strict **3-Layer Agent Architecture**:
- **Layer 1 (Directive):** High-level markdown SOPs detailing intent (stored in `directives/`).
- **Layer 2 (Orchestration):** The AI Agent routing tasks and making decisions.
- **Layer 3 (Execution):** Deterministic, reliable Python scripts handling business logic (stored in `execution/`).
