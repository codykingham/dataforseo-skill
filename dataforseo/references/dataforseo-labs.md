# DataForSEO Labs API Reference

The DataForSEO Labs API provides keyword research, competitor analysis, and market analysis tools powered by Google data. These tools cover ranked keywords, domain competitors, keyword ideas, SERP analysis, traffic estimation, and more.

## Table of Contents

### Competitor Research
1. [dataforseo_labs_google_ranked_keywords](#dataforseo_labs_google_ranked_keywords)
2. [dataforseo_labs_google_competitors_domain](#dataforseo_labs_google_competitors_domain)
3. [dataforseo_labs_google_domain_rank_overview](#dataforseo_labs_google_domain_rank_overview)
4. [dataforseo_labs_google_historical_rank_overview](#dataforseo_labs_google_historical_rank_overview)
5. [dataforseo_labs_google_historical_serp](#dataforseo_labs_google_historical_serp)
6. [dataforseo_labs_google_serp_competitors](#dataforseo_labs_google_serp_competitors)
7. [dataforseo_labs_google_domain_intersection](#dataforseo_labs_google_domain_intersection)
8. [dataforseo_labs_google_page_intersection](#dataforseo_labs_google_page_intersection)
9. [dataforseo_labs_google_subdomains](#dataforseo_labs_google_subdomains)
10. [dataforseo_labs_google_relevant_pages](#dataforseo_labs_google_relevant_pages)
11. [dataforseo_labs_bulk_traffic_estimation](#dataforseo_labs_bulk_traffic_estimation)

### Keyword Research
12. [dataforseo_labs_google_keyword_ideas](#dataforseo_labs_google_keyword_ideas)
13. [dataforseo_labs_google_keyword_suggestions](#dataforseo_labs_google_keyword_suggestions)
14. [dataforseo_labs_google_related_keywords](#dataforseo_labs_google_related_keywords)
15. [dataforseo_labs_google_keyword_overview](#dataforseo_labs_google_keyword_overview)
16. [dataforseo_labs_google_historical_keyword_data](#dataforseo_labs_google_historical_keyword_data)
17. [dataforseo_labs_google_keywords_for_site](#dataforseo_labs_google_keywords_for_site)
18. [dataforseo_labs_bulk_keyword_difficulty](#dataforseo_labs_bulk_keyword_difficulty)
19. [dataforseo_labs_search_intent](#dataforseo_labs_search_intent)

### Market Analysis
20. [dataforseo_labs_google_top_searches](#dataforseo_labs_google_top_searches)

### Utility
21. [dataforseo_labs_available_filters](#dataforseo_labs_available_filters)

22. [Suggested Workflows](#suggested-workflows)

---

## Competitor Research

### dataforseo_labs_google_ranked_keywords

**Description**: This endpoint will provide you with the list of keywords that any domain or webpage is ranking for. You will also get SERP elements related to the keyword position, as well as impressions, monthly searches and other data relevant to the returned keywords.

**Endpoint**: `POST /v3/dataforseo_labs/google/ranked_keywords/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain name or page URL. The domain name must be specified without `https://` or `www.`. The webpage URL must be specified with `https://` or `www.`. Note: if you specify the webpage URL without `https://` or `www.`, the result will be returned for the entire domain rather than the specific page. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format (not city or region). Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `=`, `<>`, `<`, `<=`, `>`, `>=`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `regex`, `not_regex`, `match`, `not_match`. Example: `[["ranked_serp_element.serp_item.rank_group","<=",10]]` |
| order_by | array of strings | No | `["ranked_serp_element.serp_item.rank_group,asc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["keyword_data.keyword_info.search_volume,desc","keyword_data.keyword_info.cpc,desc"]` |
| include_subdomains | boolean | No | - | Include keywords from subdomains. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`, `ai_overview_reference`. |

#### Example

```bash
echo '{"target": "forbes.com", "location_name": "United States", "language_code": "en", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/ranked_keywords/live
```

---

### dataforseo_labs_google_competitors_domain

**Description**: This endpoint will provide you with a full overview of ranking and traffic data of the competitor domains from organic and paid search. In addition to that, you will get the metrics specific to the keywords both competitor domains and your domain rank for within the same SERP.

**Endpoint**: `POST /v3/dataforseo_labs/google/competitors_domain/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Target domain. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["metrics.organic.count",">",50]` |
| order_by | array of strings | No | `["relevance,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["relevance,desc","keyword_info.search_volume,desc"]` |
| exclude_top_domains | boolean | No | true | If true, exclude world's largest websites to get highly-relevant competitors. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`. |

#### Example

```bash
echo '{"target": "forbes.com", "location_name": "United States", "language_code": "en", "limit": 20, "exclude_top_domains": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/competitors_domain/live
```

---

### dataforseo_labs_google_domain_rank_overview

**Description**: This endpoint will provide you with ranking and traffic data from organic and paid search for the specified domain. You will be able to review the domain ranking distribution in SERPs as well as estimated monthly traffic volume for both organic and paid results.

**Endpoint**: `POST /v3/dataforseo_labs/google/domain_rank_overview/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Target domain. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |

#### Example

```bash
echo '{"target": "forbes.com", "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/domain_rank_overview/live
```

---

### dataforseo_labs_google_historical_rank_overview

**Description**: This endpoint will provide you with historical data on rankings and traffic of the specified domain, such as domain ranking distribution in SERPs and estimated monthly traffic volume for both organic and paid results.

**Endpoint**: `POST /v3/dataforseo_labs/google/historical_rank_overview/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Target domain. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"target": "forbes.com", "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/historical_rank_overview/live
```

---

### dataforseo_labs_google_historical_serp

**Description**: This endpoint will provide you with Google SERPs collected within the specified time frame. You will also receive a complete overview of featured snippets and other extra elements that were present within the specified dates. The data will allow you to analyze the dynamics of keyword rankings over time for the specified keyword and location.

**Endpoint**: `POST /v3/dataforseo_labs/google/historical_serps/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | - | Target keyword. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |

#### Example

```bash
echo '{"keyword": "seo tools", "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/historical_serps/live
```

---

### dataforseo_labs_google_serp_competitors

**Description**: This endpoint will provide you with a list of domains ranking for the keywords you specify. You will also get SERP rankings, rating, estimated traffic volume, and visibility values the provided domains gain from the specified keywords.

**Endpoint**: `POST /v3/dataforseo_labs/google/serp_competitors/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keywords | array of strings | Yes | - | Keywords array. UTF-8 encoding. Keywords will be converted to lowercase. Maximum of 200 keywords. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["median_position","in",[1,10]]` |
| order_by | array of strings | No | `["rating,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["avg_position,asc","etv,desc"]` |
| include_subdomains | boolean | No | - | Include keywords from subdomains. |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`. |

#### Example

```bash
echo '{"keywords": ["seo tools", "keyword research", "backlink checker"], "location_name": "United States", "language_code": "en", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/serp_competitors/live
```

---

### dataforseo_labs_google_domain_intersection

**Description**: This endpoint will provide you with the keywords for which both specified domains rank within the same SERP. You will get search volume, competition, cost-per-click and impressions data on each intersecting keyword. Along with that, you will get data on the first and second domain's SERP element discovered for this keyword, as well as the estimated traffic volume and cost of ad traffic.

**Endpoint**: `POST /v3/dataforseo_labs/google/domain_intersection/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target1 | string | Yes | - | Target domain 1. |
| target2 | string | Yes | - | Target domain 2. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["keyword_data.keyword_info.search_volume","in",[100,1000]]` |
| order_by | array of strings | No | `["keyword_data.keyword_info.search_volume,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["keyword_data.keyword_info.search_volume,desc","keyword_data.keyword_info.cpc,desc"]` |
| intersections | boolean | No | true | If true, returns keywords for which both target domains have results in the same SERP. If false, returns keywords for which target1 has results but target2 does not. Note: will not provide results if intersecting keywords exceed 10 million. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`. |

#### Example

```bash
echo '{"target1": "forbes.com", "target2": "cnn.com", "location_name": "United States", "language_code": "en", "limit": 20, "intersections": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/domain_intersection/live
```

---

### dataforseo_labs_google_page_intersection

**Description**: This endpoint will provide you with the keywords for which specified pages rank within the same SERP. You will get search volume, competition, cost-per-click and impressions data on each intersecting keyword. Along with that, you will get data on SERP elements that specified pages rank for in search results, as well as the estimated traffic volume and cost of ad traffic. Page Intersection supports organic, paid, local pack and featured snippet results.

**Find keywords several webpages rank for**: Specify webpages only in the `pages` object to receive intersected ranked keywords for the specified URLs.

**Find keywords your competitors rank for but you do not**: Use the `exclude_pages` array alongside `pages`. You will receive keywords the `pages` URLs rank for, but the `exclude_pages` URLs do not.

**Endpoint**: `POST /v3/dataforseo_labs/google/page_intersection/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

> **Important -- Numbered Dictionary Format**: This tool uses `mapArrayToNumberedKeys` internally for the `pages` parameter. The skill handles this conversion automatically. When using the raw API endpoint directly, you must convert the array to numbered keys:
>
> Array input: `["https://forbes.com/page1", "https://cnn.com/page2"]`
> Converted format: `{"1": "https://forbes.com/page1", "2": "https://cnn.com/page2"}`
>
> Filters for page intersection reference pages by their numbered index (e.g., `"intersection_result.1.etv"`, `"intersection_result.2.description"`).

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| pages | array of strings | Yes | - | Pages array. You can set up to 20 pages. Pages should be specified with absolute URLs (including `http://` or `https://`). You can use a wildcard (`*`) character to specify search patterns. Example: `"example.com/eng/*"`. Note: wildcard must be placed after the slash (`/`). |
| exclude_pages | array of strings | No | - | URLs of pages to exclude. Up to 10 pages. If used, results will contain keywords that URLs from `pages` rank for, but URLs from `exclude_pages` do not. Use wildcard (`*`) for patterns. |
| intersection_mode | enum | No | - | Indicates whether to intersect keywords. Possible values: `union` (results based on all keywords any URL from pages rank for), `intersect` (results based on keywords all URLs from pages rank for in the same SERP). Default is `intersect` when only `pages` is specified; `union` when `exclude_pages` is also specified. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["keyword_data.keyword_info.search_volume",">",100]` |
| order_by | array of strings | No | `["keyword_data.keyword_info.search_volume,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["intersection_result.1.rank_group,asc","intersection_result.2.rank_absolute,asc"]` |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`. |

#### Example

```bash
echo '{"pages": ["https://forbes.com/", "https://cnn.com/"], "location_name": "United States", "language_code": "en", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/page_intersection/live
```

---

### dataforseo_labs_google_subdomains

**Description**: This endpoint will provide you with a list of subdomains of the specified domain, along with the ranking distribution across organic and paid search. In addition to that, you will also get the estimated traffic volume of subdomains based on search volume.

**Endpoint**: `POST /v3/dataforseo_labs/google/subdomains/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Target domain. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["metrics.organic.count",">",50]` |
| order_by | array of strings | No | `["metrics.organic.count,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["metrics.organic.etv,desc","metrics.paid.count,asc"]` |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"target": "apple.com", "location_name": "United States", "language_code": "en", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/subdomains/live
```

---

### dataforseo_labs_google_relevant_pages

**Description**: This endpoint will provide you with rankings and traffic data for the web pages of the specified domain. You will be able to review each page's ranking distribution and estimated monthly traffic volume from both organic and paid searches.

**Endpoint**: `POST /v3/dataforseo_labs/google/relevant_pages/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Target domain. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["metrics.organic.count",">",50]` |
| order_by | array of strings | No | `["metrics.organic.count,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["metrics.organic.etv,desc","metrics.paid.count,asc"]` |
| exclude_top_domains | boolean | No | true | If true, exclude world's largest websites to get highly-relevant results. |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"target": "forbes.com", "location_name": "United States", "language_code": "en", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/relevant_pages/live
```

---

### dataforseo_labs_bulk_traffic_estimation

**Description**: This endpoint will provide you with estimated monthly traffic volumes for up to 1,000 domains, subdomains, or webpages. Along with organic search traffic estimations, you will also get separate values for paid search, featured snippet, and local pack results.

**Endpoint**: `POST /v3/dataforseo_labs/google/bulk_traffic_estimation/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Target domains, subdomains, and webpages. Domains and subdomains should be specified without `https://` and `www.`. Pages should be specified with absolute URL including `https://` and `www.`. Up to 1000 targets. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| ignore_synonyms | boolean | No | true | Ignore highly similar keywords. If set to true, results will be more accurate. |
| item_types | array of enum | No | `["organic"]` | Display results by item type. Possible values: `organic`, `paid`, `featured_snippet`, `local_pack`. |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com", "bbc.com"], "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/bulk_traffic_estimation/live
```

---

## Keyword Research

### dataforseo_labs_google_keyword_ideas

**Description**: The Keyword Ideas provides search terms that are relevant to the product or service categories of the specified keywords. The algorithm selects keywords which fall into the same categories as the seed keywords. As a result, you will get a list of relevant keyword ideas for up to 200 seed keywords. Along with each keyword idea, you will get its search volume rate for the last month, search volume trend for the previous 12 months, as well as current cost-per-click and competition values. Moreover, this endpoint supplies minimum, maximum and average values of daily impressions, clicks and CPC for each result.

**Endpoint**: `POST /v3/dataforseo_labs/google/keyword_ideas/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keywords | array of strings | Yes | - | Target keywords. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["keyword_info.search_volume",">",0]` |
| order_by | array of strings | No | `["relevance,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. `relevance` is the default sorting rule for the closest keyword ideas (internal identifier, cannot be used as a filter). Example: `["relevance,desc","keyword_info.search_volume,desc"]` |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"keywords": ["seo tools", "keyword research"], "location_name": "United States", "language_code": "en", "limit": 50}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/keyword_ideas/live
```

---

### dataforseo_labs_google_keyword_suggestions

**Description**: The Keyword Suggestions provides search queries that include the specified seed keyword. The algorithm is based on full-text search for the specified keyword and returns only those search terms that contain the keyword you set, with additional words before, after, or within the specified key phrase. As a result, you will get a list of long-tail keywords matching the specified search term. Along with each suggested keyword, you will get its search volume rate for the last month, search volume trend for the previous 12 months, as well as current cost-per-click and competition values.

**Endpoint**: `POST /v3/dataforseo_labs/google/keyword_suggestions/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | - | Target keyword. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["keyword_info.search_volume",">",0]` |
| order_by | array of strings | No | `["keyword_info.search_volume,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["keyword_info.search_volume,desc","keyword_info.cpc,desc"]` |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"keyword": "seo tools", "location_name": "United States", "language_code": "en", "limit": 50}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/keyword_suggestions/live
```

---

### dataforseo_labs_google_related_keywords

**Description**: The Related Keywords endpoint provides keywords appearing in the "searches related to" SERP element. You can get up to 4680 keyword ideas by specifying the search depth. Each related keyword comes with the list of relevant product categories, search volume rate for the last month, search volume trend for the previous 12 months, as well as current cost-per-click and competition values. Datasource: DataForSEO SERPs Database. Search algorithm: depth-first search for queries appearing in the "search related to" element of SERP.

**Endpoint**: `POST /v3/dataforseo_labs/google/related_keywords/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | - | Target keyword. |
| depth | number | No | 1 | Keyword search depth. Min: 0, Max: 4. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["keyword_data.keyword_info.search_volume",">",0]` |
| order_by | array of strings | No | `["keyword_data.keyword_info.search_volume,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["keyword_data.keyword_info.search_volume,desc","keyword_data.keyword_info.cpc,desc"]` |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"keyword": "seo tools", "depth": 2, "location_name": "United States", "language_code": "en", "limit": 50}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/related_keywords/live
```

---

### dataforseo_labs_google_keyword_overview

**Description**: This endpoint provides Google keyword data for specified keywords. For each keyword, you will receive current cost-per-click, competition values for paid search, search volume, search intent, monthly searches.

**Endpoint**: `POST /v3/dataforseo_labs/google/keyword_overview/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keywords | array of strings | Yes | - | Keywords. Maximum 700 keywords. Maximum 80 characters per keyword. Maximum 10 words per keyword phrase. Keywords will be converted to lowercase. Note: keywords not in the database will be omitted from results (no charge for omitted keywords). |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"keywords": ["seo tools", "keyword research", "backlink checker"], "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/keyword_overview/live
```

---

### dataforseo_labs_google_historical_keyword_data

**Description**: This endpoint provides Google historical keyword data for specified keywords, including search volume, cost-per-click, competition values for paid search, monthly searches, and search volume trends. You can get historical keyword data since August 2021, depending on keywords along with location and language combination.

**Endpoint**: `POST /v3/dataforseo_labs/google/historical_keyword_data/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keywords | array of strings | Yes | - | Keywords. Maximum 700 keywords. Maximum 80 characters per keyword. Maximum 10 words per keyword phrase. Keywords will be converted to lowercase. Note: keywords not in the database will be omitted from results (no charge for omitted keywords). |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |

#### Example

```bash
echo '{"keywords": ["seo tools", "keyword research"], "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/historical_keyword_data/live
```

---

### dataforseo_labs_google_keywords_for_site

**Description**: The Keywords For Site endpoint will provide you with a list of keywords relevant to the target domain. Each keyword is supplied with relevant search volume data for the last month, cost-per-click, and competition.

**Endpoint**: `POST /v3/dataforseo_labs/google/keywords_for_site/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Target domain. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["keyword_info.search_volume",">",0]` |
| order_by | array of strings | No | `["relevance,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["relevance,desc","keyword_info.search_volume,desc"]` |
| include_subdomains | boolean | No | - | Include keywords from subdomains. |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"target": "forbes.com", "location_name": "United States", "language_code": "en", "limit": 50}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/keywords_for_site/live
```

---

### dataforseo_labs_bulk_keyword_difficulty

**Description**: This endpoint will provide you with the Keyword Difficulty metric for a maximum of 1,000 keywords in one API request. Keyword Difficulty stands for the relative difficulty of ranking in the first top-10 organic results for the related keyword. Keyword Difficulty in DataForSEO API responses indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100.

**Endpoint**: `POST /v3/dataforseo_labs/google/bulk_keyword_difficulty/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keywords | array of strings | Yes | - | Target keywords. UTF-8 encoding. Maximum 1000 keywords. |
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |

#### Example

```bash
echo '{"keywords": ["seo tools", "keyword research", "backlink checker"], "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/bulk_keyword_difficulty/live
```

---

### dataforseo_labs_search_intent

**Description**: This endpoint will provide you with search intent data for up to 1,000 keywords. For each keyword, the API will return the keyword's search intent and intent probability. Besides the highest probable search intent, the results will also provide you with other likely search intent(s) and their probability. The system detects four types of search intent: informational, navigational, commercial, transactional.

**Endpoint**: `POST /v3/dataforseo_labs/google/search_intent/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keywords | array of strings | Yes | - | Target keywords. UTF-8 encoding. Maximum 1000 keywords. |
| language_code | string | Yes | "en" | Language code. Supported languages: ar, zh-TW, cs, da, nl, en, fi, fr, de, he, hi, it, ja, ko, ms, nb, pl, pt, ro, ru, es, sv, th, uk, vi, bg, hr, sr, sl, bs. |

#### Example

```bash
echo '{"keywords": ["buy running shoes", "how to tie a tie", "nike store"], "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/search_intent/live
```

---

## Market Analysis

### dataforseo_labs_google_top_searches

**Description**: The Top Searches endpoint of DataForSEO Labs API can provide you with over 7 billion keywords from the DataForSEO Keyword Database. Each keyword in the API response is provided with a set of relevant keyword data with Google Ads metrics.

**Endpoint**: `POST /v3/dataforseo_labs/google/top_searches/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| location_name | string | Yes | "United States" | Full name of the location. Only country format. Example: `"United Kingdom"`, `"United States"`, `"Canada"`. |
| language_code | string | Yes | "en" | Language code. Example: `"en"`. |
| limit | number | No | 10 | Maximum number of keywords to return. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned keywords. |
| filters | array | No | - | Array of filter conditions. Max 8 filters. Operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `match`, `not_match`, `ilike`, `not_ilike`, `like`, `not_like`. Example: `["keyword_info.search_volume",">",0]` |
| order_by | array of strings | No | `["keyword_info.search_volume,desc"]` | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["keyword_info.search_volume,desc","keyword_info.cpc,desc"]` |
| include_clickstream_data | boolean | No | false | Include or exclude data from clickstream-based metrics in the result. |

#### Example

```bash
echo '{"location_name": "United States", "language_code": "en", "limit": 50}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/dataforseo_labs/google/top_searches/live
```

---

## Utility

### dataforseo_labs_available_filters

**Description**: Here you will find all the necessary information about filters that can be used with DataForSEO Labs API endpoints. Filters are associated with a certain object in the result array, and should be specified accordingly.

**Endpoint**: `GET /v3/dataforseo_labs/available_filters`

**AI-condensed**: No (use `--full-response`)

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tool | string | No | - | The name of the tool to get filters for. If omitted, returns filters for all tools. |

#### Example

```bash
echo '{"tool": "dataforseo_labs_google_ranked_keywords"}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/dataforseo_labs/available_filters \
  --method GET --full-response
```

---

## Suggested Workflows

### 1. Create Content Targeting Decision-Stage Users

Find alternative/comparison search queries for a product.

**Parameters**: `product` (string) -- The product to search related keywords for.

**Prompt**: What are alternative or comparison ("vs", "alternative", "best", "compare") search queries people use for the product? Return 20 ideas with high search volume.

**Tools used**: `dataforseo_labs_google_keyword_ideas`, `dataforseo_labs_google_keyword_suggestions`

---

### 2. Generate SEO-Friendly Article Ideas

Generate article ideas that directly answer user questions.

**Parameters**: `topic` (string) -- The topic to research.

**Prompt**: Show 20 question-based keywords (what, why, how) for the topic with search volume >= 300. Include search intent and suggest article headlines that match the query tone.

**Tools used**: `dataforseo_labs_google_keyword_suggestions`, `dataforseo_labs_search_intent`

---

### 3. Focus on High-Converting Terms for Paid Campaigns

Find high-converting terms based on buyer readiness.

**Parameters**: `product` (string) -- The product/service to compare.

**Prompt**: Find 20 commercial and transactional keywords related to the product. Filter by CPC >= $2 and search volume >= 1,000. Suggest landing page angles based on intent.

**Tools used**: `dataforseo_labs_google_keyword_ideas`, `dataforseo_labs_search_intent`

---

### 4. Structure Site Content Based on Keyword Clusters

Organize content and internal linking based on keyword clusters.

**Parameters**: `keyword` (string) -- The keyword to cluster related keywords for.

**Prompt**: Provide a 20-term keyword cluster around the keyword. Group them by intent (informational, commercial, transactional) and list keyword difficulty and SERP features.

**Tools used**: `dataforseo_labs_google_related_keywords`, `dataforseo_labs_search_intent`, `dataforseo_labs_bulk_keyword_difficulty`

---

### 5. Competitor Comparison

Compare two sites by keyword overlap and backlink profile.

**Parameters**:
- `site_1` (string) -- The first site to compare
- `site_2` (string) -- The second site to compare

**Prompt**: Create a competitor comparison matrix between the two sites based on keyword overlap and backlink profile.

**Tools used**: `dataforseo_labs_google_domain_intersection`, `dataforseo_labs_google_domain_rank_overview`

---

### 6. Build Content That Aligns with User Research Behavior

Find informational keywords with low competition for content creation.

**Parameters**: `topic` (string) -- The keyword/topic to research.

**Prompt**: Give 20 informational keywords around the topic with low competition and moderate search volume (>=500). Group them by intent and suggest blog topics for each.

**Tools used**: `dataforseo_labs_google_keyword_ideas`, `dataforseo_labs_search_intent`, `dataforseo_labs_bulk_keyword_difficulty`

---

### 7. Track Long-Term SEO Performance

Track visibility shifts, ranking distribution, and seasonal trends over time.

**Parameters**:
- `domain` (string) -- The domain to analyze
- `location` (string) -- The location to analyze
- `language` (string) -- The language to analyze

**Prompt**: Show how the visibility and SERP position distribution of the domain changed over the past 12 months. Focus on top 3, top 10, and top 100 rankings, and highlight any traffic peaks.

**Tools used**: `dataforseo_labs_google_historical_rank_overview`

---

### 8. Compare Monthly Organic Traffic Trends Against a Competitor

Compare organic traffic trends and ranking distribution between two domains.

**Parameters**:
- `domain` (string) -- Your domain to analyze
- `competitor_domain` (string) -- Competitor domain to compare against
- `location` (string) -- The location to analyze
- `language` (string) -- The language to analyze

**Prompt**: Compare monthly organic traffic trends and ranking distribution of your domain vs competitor domain. Highlight who has better top 10 visibility and estimated traffic this month.

**Tools used**: `dataforseo_labs_google_domain_rank_overview`, `dataforseo_labs_google_historical_rank_overview`
