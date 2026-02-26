# Filters and Sorting Reference

Cross-module documentation for the filter and order_by syntax used by many DataForSEO API endpoints.

---

## Filter Syntax

Filters are passed as JSON arrays in the `filters` (or `initial_dataset_filters`) parameter of the request payload.

### Basic Filter (single condition)

Format: `["field", "operator", "value"]`

```json
["domain_rank", ">", 500]
```

```json
["dofollow", "=", true]
```

### Compound Filter (two conditions)

Two filters joined by a logical operator (`"and"` or `"or"`):

```json
[["dofollow", "=", true], "and", ["page_from_rank", ">", 50]]
```

### Nested Compound Filter

Compound conditions can be nested:

```json
[
  ["domain_rank", ">", 800],
  "and",
  [
    ["page_types", "has", "ecommerce"],
    "or",
    ["content_info.text_category", "has", 10994]
  ]
]
```

### Available Filter Operators

| Operator | Description |
|----------|-------------|
| `=` | Equal to |
| `<>` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `in` | Value is in a given list |
| `not_in` | Value is not in a given list |
| `contains` | String contains substring |
| `not_contains` | String does not contain substring |
| `like` | SQL-style pattern match (use `%` for wildcards) |
| `not_like` | Negated SQL-style pattern match |
| `ilike` | Case-insensitive `like` |
| `not_ilike` | Case-insensitive `not_like` |
| `regex` | Regular expression match |
| `not_regex` | Negated regular expression match |
| `match` | Match |
| `not_match` | Negated match |
| `has` | Contains element (for arrays) |
| `has_not` | Does not contain element (for arrays) |

**Note:** Not all operators are available for all endpoints. Use the corresponding `available_filters` tool for each module to check supported operators per field.

### Maximum Filters

Most endpoints support up to **8 filters** in a single request.

---

## OrderBy Syntax

Sorting rules are passed as a JSON array of strings in the `order_by` parameter.

### Format

Each sort rule is a string: `"field,direction"` where direction is `asc` or `desc`.

```json
["page_from_rank,desc"]
```

### Multiple Sort Fields

You can specify multiple sort rules (up to 3 in most endpoints):

```json
["rating.value,desc", "rating.votes_count,desc"]
```

```json
["ai_search_volume,desc"]
```

---

## How to Pass in JSON Payloads

Filters and order_by are included directly in the JSON payload piped to the script:

```bash
echo '{
  "target": "example.com",
  "filters": [["dofollow", "=", true], "and", ["page_from_rank", ">", 50]],
  "order_by": ["page_from_rank,desc"],
  "limit": 20
}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/backlinks/live
```

For endpoints that use `initial_dataset_filters` instead of `filters` (Content Analysis Summary, Content Analysis Phrase Trends, LLM Mentions Top Domains, LLM Mentions Top Pages):

```bash
echo '{
  "keyword": "seo tools",
  "initial_dataset_filters": [["domain", "<>", "logitech.com"], "and", ["content_info.connotation_types.negative", ">", 1000]],
  "date_from": "2024-01-01"
}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/content_analysis/phrase_trends/live
```

---

## Which Modules/Tools Support Filters

### Backlinks Module
Tools using `filters` + `order_by` (via `formatFilters`/`formatOrderBy`):
- `backlinks_backlinks` -- backlink list for a target
- `backlinks_anchors` -- anchor text distribution
- `backlinks_referring_domains` -- referring domains list
- `backlinks_referring_networks` -- referring networks
- `backlinks_competitors` -- backlink competitors
- `backlinks_domain_pages` -- pages of a domain with backlink data
- `backlinks_domain_pages_summary` -- summary of domain pages
- `backlinks_domain_intersection` -- shared referring domains between targets
- `backlinks_page_intersection` -- shared backlinks between pages

**Available filters tool**: `backlinks_available_filters`

### DataForSEO Labs Module
Tools using `filters` + `order_by`:
- `dataforseo_labs_google_ranked_keywords` -- ranked keywords for a domain
- `dataforseo_labs_google_serp_competitors` -- SERP competitors
- `dataforseo_labs_google_subdomains` -- subdomains of a domain
- `dataforseo_labs_google_relevant_pages` -- relevant pages
- `dataforseo_labs_google_domain_intersection` -- keyword intersection between domains
- `dataforseo_labs_google_page_intersection` -- keyword intersection between pages
- `dataforseo_labs_google_competitors_domain` -- domain competitors
- `dataforseo_labs_google_keyword_ideas` -- keyword ideas
- `dataforseo_labs_google_keyword_suggestions` -- keyword suggestions
- `dataforseo_labs_google_keywords_for_site` -- keywords for a site
- `dataforseo_labs_google_related_keywords` -- related keywords
- `dataforseo_labs_google_top_searches` -- top searches

**Available filters tool**: `dataforseo_labs_available_filters`

### Business Data Module
Tools using `filters` + `order_by`:
- `business_data_business_listings_search` -- business listings search

**Available filters tool**: `business_data_business_listings_filters`

### Domain Analytics Module
Tools using `filters` + `order_by`:
- `domain_analytics_whois_overview` -- WHOIS overview with SEO data

**Available filters tools**:
- `domain_analytics_whois_available_filters` -- for WHOIS endpoints
- `domain_analytics_technologies_available_filters` -- for Technologies endpoints

### Content Analysis Module
Tools using `filters` + `order_by`:
- `content_analysis_search` -- citation search (uses `filters` + `order_by`)

Tools using `initial_dataset_filters` (no `order_by`):
- `content_analysis_summary` -- citation summary (uses `initial_dataset_filters`)
- `content_analysis_phrase_trends` -- phrase trends (uses `initial_dataset_filters`)

### AI Optimization Module
Tools using `filters` (with `order_by` where noted):
- `ai_opt_llm_ment_search` -- LLM mentions search (uses `filters` + `order_by`)
- `ai_opt_llm_ment_agg_metrics` -- aggregated mention metrics (uses `filters` only)
- `ai_opt_llm_ment_cross_agg_metrics` -- cross-aggregated metrics (uses `filters` only)

Tools using `initial_dataset_filters`:
- `ai_opt_llm_ment_top_domains` -- top mentioned domains (uses `initial_dataset_filters`)
- `ai_opt_llm_ment_top_pages` -- top mentioned pages (uses `initial_dataset_filters`)

**Available filters tool**: `ai_optimization_llm_mentions_filters`

---

## Querying Available Filters with `--full-response`

All `available_filters` endpoints require the `--full-response` flag because they return metadata rather than standard API results (they have `supportOnlyFullResponse` set).

### Example: Get available filters for Backlinks
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/backlinks/available_filters \
  --method GET --full-response
```

### Example: Get available filters for Business Listings
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/business_data/business_listings/available_filters \
  --method GET --full-response
```

### Example: Get available filters for WHOIS
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/domain_analytics/whois/available_filters \
  --method GET --full-response
```

### Example: Get available filters for Technologies
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/domain_analytics/technologies/available_filters \
  --method GET --full-response
```

### Example: Get available filters for LLM Mentions
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/llm_mentions/available_filters \
  --method GET --full-response
```

---

## Filter Normalization Note

The script automatically normalizes singly-nested arrays that LLMs sometimes produce. Specifically:

- `[["field", "op", "val"]]` (array wrapped in an extra array) is automatically unwrapped to `["field", "op", "val"]`

This happens recursively, so deeply nested single-element arrays are flattened correctly. This normalization is implemented in the `formatFilters` method of the base tool class via the `removeNested` helper, which checks if any element in the filter array is itself a single-element array containing another array, and if so, unwraps it.

This means you do **not** need to worry about accidentally double-wrapping filter expressions -- the script handles it automatically.
