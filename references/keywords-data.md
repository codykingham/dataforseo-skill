# Keywords Data API Reference

The Keywords Data module provides tools for keyword research and trend analysis. It covers Google Ads search volume data, Google Trends exploration, and DataForSEO Trends (an independent trends data source with demographic and geographic breakdowns).

## Table of Contents

- [kw_data_google_ads_locations](#kw_data_google_ads_locations)
- [kw_data_google_ads_search_volume](#kw_data_google_ads_search_volume)
- [kw_data_dfs_trends_explore](#kw_data_dfs_trends_explore)
- [kw_data_dfs_trends_demography](#kw_data_dfs_trends_demography)
- [kw_data_dfs_trends_subregion_interests](#kw_data_dfs_trends_subregion_interests)
- [kw_data_google_trends_categories](#kw_data_google_trends_categories)
- [kw_data_google_trends_explore](#kw_data_google_trends_explore)

---

### kw_data_google_ads_locations

**Description**: Utility tool for kw_data_google_ads_search_volume to get list of available locations.
**Endpoint**: `POST /v3/keywords_data/google_ads/locations`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| country_iso_code | string | Yes | - | ISO 3166-1 alpha-2 country code, for example: US, GB, MT |
| location_type | string | No | - | Type of location. Possible variants: 'TV Region', 'Postal Code', 'Neighborhood', 'Governorate', 'National Park', 'Quarter', 'Canton', 'Airport', 'Okrug', 'Prefecture', 'City', 'Country', 'Province', 'Barrio', 'Sub-District', 'Congressional District', 'Municipality District', 'district', 'DMA Region', 'Union Territory', 'Territory', 'Colloquial Area', 'Autonomous Community', 'Borough', 'County', 'State', 'District', 'City Region', 'Commune', 'Region', 'Department', 'Division', 'Sub-Ward', 'Municipality', 'University' |
| location_name | string | No | - | Name of location or its part. |

#### Example

```bash
echo '{"country_iso_code": "US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/keywords_data/google_ads/locations
```

---

### kw_data_google_ads_search_volume

**Description**: Get search volume data for keywords from Google Ads
**Endpoint**: `POST /v3/keywords_data/google_ads/search_volume/live`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| location_name | string | No | `United States` | Full name of the location. Location format - hierarchical, comma-separated (from most specific to least). Can be one of: 1. Country only: "United States" 2. Region,Country: "California,United States" 3. City,Region,Country: "San Francisco,California,United States" |
| language_code | string (nullable) | No | `null` | Language two-letter ISO code (e.g., 'en'). Optional field. |
| keywords | array of strings | Yes | - | Array of keywords to get search volume for |

#### Example

```bash
echo '{"keywords": ["seo tools", "keyword research"], "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/keywords_data/google_ads/search_volume/live
```

---

### kw_data_dfs_trends_explore

**Description**: This endpoint will provide you with the keyword popularity data from DataForSEO Trends. You can check keyword trends for Google Search, Google News, and Google Shopping.
**Endpoint**: `POST /v3/keywords_data/dataforseo_trends/explore/live`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| location_name | string (nullable) | No | `null` | Full name of the location. Optional field. Format: "Country" (e.g., "United Kingdom"). |
| keywords | array of strings | Yes | - | Keywords to analyze. The maximum number of keywords you can specify: 5. |
| type | enum | No | `web` | DataForSEO trends type. One of: `web`, `news`, `ecommerce`. |
| date_from | string | No | - | Starting date of the time range. If not specified, the current day and month of the preceding year will be used by default. Minimal value for web type: 2004-01-01. Minimal value for other types: 2008-01-01. Date format: "yyyy-mm-dd". |
| date_to | string | No | - | Ending date of the time range. If not specified, today's date will be used by default. Date format: "yyyy-mm-dd". |
| time_range | enum | No | `past_7_days` | Preset time ranges. One of: `past_4_hours`, `past_day`, `past_7_days`, `past_30_days`, `past_90_days`, `past_12_months`, `past_5_years`. If date_from or date_to are specified, this field will be ignored. |

#### Example

```bash
echo '{"keywords": ["artificial intelligence", "machine learning"], "type": "web", "time_range": "past_12_months"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/keywords_data/dataforseo_trends/explore/live
```

---

### kw_data_dfs_trends_demography

**Description**: This endpoint will provide you with the demographic breakdown (by age and gender) of keyword popularity per each specified term based on DataForSEO Trends data.
**Endpoint**: `POST /v3/keywords_data/dataforseo_trends/demography/live`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| location_name | string (nullable) | No | `null` | Full name of the location. Optional field. Format: "Country" (e.g., "United Kingdom"). |
| keywords | array of strings | Yes | - | Keywords to analyze. The maximum number of keywords you can specify: 5. |
| type | enum | No | `web` | DataForSEO trends type. One of: `web`, `news`, `ecommerce`. |
| date_from | string | No | - | Starting date of the time range. If not specified, the current day and month of the preceding year will be used by default. Minimal value for web type: 2004-01-01. Minimal value for other types: 2008-01-01. Date format: "yyyy-mm-dd". |
| date_to | string | No | - | Ending date of the time range. If not specified, today's date will be used by default. Date format: "yyyy-mm-dd". |
| time_range | enum | No | `past_7_days` | Preset time ranges. One of: `past_4_hours`, `past_day`, `past_7_days`, `past_30_days`, `past_90_days`, `past_12_months`, `past_5_years`. If date_from or date_to are specified, this field will be ignored. |

#### Example

```bash
echo '{"keywords": ["fitness", "yoga"], "location_name": "United States", "type": "web", "time_range": "past_30_days"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/keywords_data/dataforseo_trends/demography/live
```

---

### kw_data_dfs_trends_subregion_interests

**Description**: This endpoint will provide you with location-specific keyword popularity data from DataForSEO Trends.
**Endpoint**: `POST /v3/keywords_data/dataforseo_trends/subregion_interests/live`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| location_name | string (nullable) | No | `null` | Full name of the location. Optional field. Format: "Country" (e.g., "United Kingdom"). |
| keywords | array of strings | Yes | - | Keywords to analyze. The maximum number of keywords you can specify: 5. |
| type | enum | No | `web` | DataForSEO trends type. One of: `web`, `news`, `ecommerce`. |
| date_from | string | No | - | Starting date of the time range. If not specified, the current day and month of the preceding year will be used by default. Minimal value for web type: 2004-01-01. Minimal value for other types: 2008-01-01. Date format: "yyyy-mm-dd". |
| date_to | string | No | - | Ending date of the time range. If not specified, today's date will be used by default. Date format: "yyyy-mm-dd". |
| time_range | enum | No | `past_7_days` | Preset time ranges. One of: `past_4_hours`, `past_day`, `past_7_days`, `past_30_days`, `past_90_days`, `past_12_months`, `past_5_years`. If date_from or date_to are specified, this field will be ignored. |

#### Example

```bash
echo '{"keywords": ["remote work"], "location_name": "United States", "type": "web", "time_range": "past_12_months"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/keywords_data/dataforseo_trends/subregion_interests/live
```

---

### kw_data_google_trends_categories

**Description**: This endpoint will provide you list of Google Trends Categories.
**Endpoint**: `GET /v3/keywords_data/google_trends/categories/live`
**AI-condensed**: Yes

#### Parameters

This tool takes no parameters.

#### Example

```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/keywords_data/google_trends/categories/live --method GET
```

---

### kw_data_google_trends_explore

**Description**: This endpoint will provide you with the keyword popularity data from the 'Explore' feature of Google Trends. You can check keyword trends for Google Search, Google News, Google Images, Google Shopping, and YouTube.
**Endpoint**: `POST /v3/keywords_data/google_trends/explore/live`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| location_name | string (nullable) | No | `null` | Full name of the location. Optional field. Format: "Country" (e.g., "United Kingdom"). |
| language_code | string (nullable) | No | `null` | Language two-letter ISO code (e.g., 'en'). Optional field. |
| keywords | array of strings | Yes | - | Keywords to analyze. Max 5 keywords. Max 100 characters per keyword. Min length > 1 character. Commas in keywords will be ignored. Note: keywords cannot consist of a combination of: < > \| \\ " - + = ~ ! : * ( ) [ ] { }. Note: to obtain google_trends_topics_list and google_trends_queries_list items, specify no more than 1 keyword. |
| type | enum | No | `web` | Google trends type. One of: `web`, `news`, `youtube`, `images`, `froogle`. |
| date_from | string | No | - | Starting date of the time range. If not specified, the current day and month of the preceding year will be used by default. Minimal value for web type: 2004-01-01. Minimal value for other types: 2008-01-01. Date format: "yyyy-mm-dd". |
| date_to | string | No | - | Ending date of the time range. If not specified, today's date will be used by default. Date format: "yyyy-mm-dd". |
| time_range | enum | No | `past_7_days` | Preset time ranges. One of: `past_hour`, `past_4_hours`, `past_day`, `past_7_days`, `past_30_days`, `past_90_days`, `past_12_months`, `past_5_years`. If date_from or date_to are specified, this field will be ignored. |
| item_types | array of enums | No | `["google_trends_graph"]` | Types of items returned. Possible values: `google_trends_graph`, `google_trends_map`, `google_trends_topics_list`, `google_trends_queries_list`. To speed up execution, specify one item at a time. |
| category_code | number (nullable) | No | `null` | Google trends search category. You can receive the list of available categories with their category_code by making a separate request to the kw_data_google_trends_categories tool. |

#### Example

```bash
echo '{"keywords": ["chatgpt"], "type": "web", "time_range": "past_12_months", "item_types": ["google_trends_graph"]}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/keywords_data/google_trends/explore/live
```
