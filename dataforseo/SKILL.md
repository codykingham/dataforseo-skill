---
name: dataforseo
description: Query the DataForSEO API for SEO data including SERP results, keyword research, backlink analysis, domain analytics, content analysis, AI optimization, and more. Use when the user asks about SEO metrics, keyword data, backlinks, domain rankings, SERP analysis, Google Trends, or any search-engine optimization research task.
allowed-tools: Bash
compatibility: Requires Python 3.10+, network access to api.dataforseo.com, and DATAFORSEO_USERNAME / DATAFORSEO_PASSWORD environment variables.
license: MIT
metadata:
  version: "1.0.0"
  author: codykingham
  source: https://github.com/codykingham/dataforseo-skill
---

# DataForSEO Skill

Query the DataForSEO API for comprehensive SEO data across 9 modules and 80 endpoints.

## Prerequisites

**Required environment variables:**
- `DATAFORSEO_USERNAME` -- your DataForSEO API login
- `DATAFORSEO_PASSWORD` -- your DataForSEO API password

**Optional environment variables:**
- `DATAFORSEO_FULL_RESPONSE` -- set to `true` to return full API responses instead of AI-condensed ones (default: `false`)
- `DATAFORSEO_SIMPLE_FILTER` -- set to `true` to use simplified filter syntax (default: `false`)
- `FIELD_CONFIG_PATH` -- path to a custom field configuration file for response field filtering
- `DEBUG` -- set to `true` to enable debug logging (default: `false`)

**Runtime:** Python 3.10+

## Quick Start

```bash
echo '{"keyword":"seo","location_name":"United States","language_code":"en"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/google/organic/live/advanced
```

## How to Use

Follow this 3-step workflow for every request:

### Step 1: Find the Right Endpoint

Check the reference docs in `$SKILL_DIR/references/` for the module that matches the user's request. Each reference file lists every available endpoint, its purpose, required parameters, and example payloads.

### Step 2: Build the JSON Payload

Construct a JSON object with the parameters specified in the reference doc. At minimum, most endpoints require a target (domain/URL) or keyword plus a location and language code.

### Step 3: Run the Script

Pipe the JSON payload into the script with the `--endpoint` flag:

```bash
echo '<json_payload>' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint <endpoint_path>
```

The script wraps the payload in an array automatically (the API expects `[{...}]`). Use `--no-wrap-array` if your payload is already an array.

## Available Modules

| Module | Reference | Tools | Description |
|--------|-----------|-------|-------------|
| SERP | `$SKILL_DIR/references/serp.md` | 7 | Google/Bing/Yahoo organic SERP results and YouTube search |
| Keywords Data | `$SKILL_DIR/references/keywords-data.md` | 7 | Google Ads search volume, Google Trends, DataForSEO Trends |
| Backlinks | `$SKILL_DIR/references/backlinks.md` | 20 | Backlink profiles, anchors, referring domains, competitors, bulk analysis |
| DataForSEO Labs | `$SKILL_DIR/references/dataforseo-labs.md` | 21 | Keyword research, competitor research, domain rankings, traffic estimation |
| OnPage | `$SKILL_DIR/references/onpage.md` | 3 | Content parsing, instant page audits, Lighthouse scores |
| AI Optimization | `$SKILL_DIR/references/ai-optimization.md` | 13 | LLM mentions tracking, AI search keyword data, ChatGPT scraping |
| Business Data | `$SKILL_DIR/references/business-data.md` | 2 | Business listings search and filters |
| Domain Analytics | `$SKILL_DIR/references/domain-analytics.md` | 4 | WHOIS data, technology stack detection |
| Content Analysis | `$SKILL_DIR/references/content-analysis.md` | 3 | Citation search, content summaries, phrase trends |

For script options, response modes, filters, and suggested workflows, see `$SKILL_DIR/references/usage.md`.
