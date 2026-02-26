---
name: dataforseo
description: Query the DataForSEO API for SEO data including SERP results, keyword research, backlink analysis, domain analytics, content analysis, AI optimization, and more. Use when the user asks about SEO metrics, keyword data, backlinks, domain rankings, SERP analysis, Google Trends, or any search-engine optimization research task.
---

# DataForSEO Skill

Query the DataForSEO API for comprehensive SEO data across 9 modules and 79 endpoints.

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
| Keywords Data | `$SKILL_DIR/references/keywords-data.md` | 6 | Google Ads search volume, Google Trends, DataForSEO Trends |
| Backlinks | `$SKILL_DIR/references/backlinks.md` | 20 | Backlink profiles, anchors, referring domains, competitors, bulk analysis |
| DataForSEO Labs | `$SKILL_DIR/references/dataforseo-labs.md` | 21 | Keyword research, competitor research, domain rankings, traffic estimation |
| OnPage | `$SKILL_DIR/references/onpage.md` | 3 | Content parsing, instant page audits, Lighthouse scores |
| AI Optimization | `$SKILL_DIR/references/ai-optimization.md` | 13 | LLM mentions tracking, AI search keyword data, ChatGPT scraping |
| Business Data | `$SKILL_DIR/references/business-data.md` | 2 | Business listings search and filters |
| Domain Analytics | `$SKILL_DIR/references/domain-analytics.md` | 4 | WHOIS data, technology stack detection |
| Content Analysis | `$SKILL_DIR/references/content-analysis.md` | 3 | Citation search, content summaries, phrase trends |

## Script Options

| Flag | Description |
|------|-------------|
| `--endpoint` | **(Required)** The DataForSEO API endpoint path (e.g., `/v3/serp/google/organic/live/advanced`) |
| `--method` | HTTP method, `POST` (default) or `GET` |
| `--full-response` | Return the full API response instead of the AI-condensed version |
| `--fields` | Comma-separated list of fields to include in the response (e.g., `keyword,search_volume,cpc`) |
| `--field-config` | Path to a JSON field configuration file for custom response filtering |
| `--debug` | Enable debug output to stderr |
| `--no-wrap-array` | Do not wrap the input JSON in an array before sending (use when your payload is already an array) |

## Response Modes

**AI-condensed (default):** The script appends `.ai` to the endpoint path, which returns a streamlined response optimized for LLM consumption. Use this for most requests -- it reduces token usage and focuses on the most relevant data.

**Full response:** Pass `--full-response` or set `DATAFORSEO_FULL_RESPONSE=true`. Returns the complete API response with all fields. Use this when you need raw data, debugging, or fields not included in the AI-condensed response.

## Filters and Sorting

Many endpoints support powerful filtering and sorting via `filters` and `order_by` parameters in the JSON payload. Filters use the format `["field","operator","value"]` and can be combined with `"and"`/`"or"` logical operators.

See `$SKILL_DIR/references/filters-and-sorting.md` for full syntax documentation and examples.

## Suggested Workflows

**Keyword Research Pipeline:**
1. Get keyword ideas with DataForSEO Labs (`keyword_ideas` or `keyword_suggestions`)
2. Check search volumes with Keywords Data (`google_ads/search_volume`)
3. Assess difficulty with DataForSEO Labs (`bulk_keyword_difficulty`)
4. Analyze search intent (`search_intent`)

**Competitor Analysis:**
1. Get domain rank overview with DataForSEO Labs (`domain_rank_overview`)
2. Find domain competitors (`domain_competitors`)
3. Compare keyword overlap with domain intersection (`domain_intersection`)
4. Check ranked keywords (`ranked_keywords`)

**Backlink Audit:**
1. Get backlink summary (`backlinks/summary`)
2. Analyze referring domains (`backlinks/referring_domains`)
3. Check anchor text distribution (`backlinks/anchors`)
4. Identify toxic links via spam scores (`backlinks/bulk_spam_score`)

**Content & SERP Analysis:**
1. Get SERP results for target keywords (`serp/google/organic/live/advanced`)
2. Analyze content citations (`content_analysis/search`)
3. Track phrase trends over time (`content_analysis/phrase_trends`)

**AI Search Optimization:**
1. Check LLM mentions for a brand (`llm_mentions/search`)
2. Review aggregated mention metrics (`llm_mentions/aggregated_metrics`)
3. Find top domains cited by LLMs (`llm_mentions/top_domains`)

Refer to the individual module reference files for detailed endpoint parameters and example payloads.
