# Usage Reference

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
