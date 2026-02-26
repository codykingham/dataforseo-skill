# SERP API Reference

The SERP module provides tools for retrieving search engine results pages (SERPs) from Google, Bing, Yahoo, and YouTube. It supports organic web search results as well as YouTube-specific searches including video info, comments, and subtitles.

## Table of Contents

- [serp_organic_live_advanced](#serp_organic_live_advanced)
- [serp_locations](#serp_locations)
- [serp_youtube_locations](#serp_youtube_locations)
- [serp_youtube_organic_live_advanced](#serp_youtube_organic_live_advanced)
- [serp_youtube_video_info_live_advanced](#serp_youtube_video_info_live_advanced)
- [serp_youtube_video_comments_live_advanced](#serp_youtube_video_comments_live_advanced)
- [serp_youtube_video_subtitles_live_advanced](#serp_youtube_video_subtitles_live_advanced)
- [Suggested Workflows](#suggested-workflows)

---

### serp_organic_live_advanced

**Description**: Get organic search results for a keyword in specified search engine
**Endpoint**: `POST /v3/serp/{search_engine}/organic/live/advanced`
**AI-condensed**: Yes

> Note: The `{search_engine}` segment in the endpoint path is dynamically replaced by the `search_engine` parameter value (e.g., `google`, `yahoo`, `bing`).

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| search_engine | string | No | `google` | Search engine name, one of: google, yahoo, bing. |
| location_name | string | No | `United States` | Full name of the location. Location format - hierarchical, comma-separated (from most specific to least). Can be one of: 1. Country only: "United States" 2. Region,Country: "California,United States" 3. City,Region,Country: "San Francisco,California,United States" |
| depth | number | No | `10` | Parsing depth. Number of results in SERP. Min: 10, Max: 700. |
| language_code | string | Yes | - | Search engine language code (e.g., 'en') |
| keyword | string | Yes | - | Search keyword |
| max_crawl_pages | number | No | `1` | Page crawl limit. Number of search results pages to crawl. Min: 1, Max: 7. Note: the max_crawl_pages and depth parameters complement each other. |
| device | string | No | `desktop` | Device type. Can take the values: desktop, mobile. |
| people_also_ask_click_depth | number | No | - | Clicks on the corresponding element. Specify the click depth on the people_also_ask element to get additional people_also_ask_element items. Min: 1, Max: 4. |

#### Example

```bash
echo '{"keyword": "best coffee shops", "language_code": "en", "location_name": "New York,New York,United States", "depth": 10}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/google/organic/live/advanced
```

---

### serp_locations

**Description**: Utility tool for serp_organic_live_advanced to get list of available locations.
**Endpoint**: `POST /v3/serp/{search_engine}/locations`
**AI-condensed**: Yes

> Note: The `{search_engine}` segment in the endpoint path is dynamically replaced by the `search_engine` parameter value (e.g., `google`, `yahoo`, `bing`).

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| search_engine | string | No | `google` | Search engine name, one of: google, yahoo, bing. |
| country_iso_code | string | Yes | - | ISO 3166-1 alpha-2 country code, for example: US, GB, MT |
| location_type | string | No | - | Type of location. Possible variants: 'TV Region', 'Postal Code', 'Neighborhood', 'Governorate', 'National Park', 'Quarter', 'Canton', 'Airport', 'Okrug', 'Prefecture', 'City', 'Country', 'Province', 'Barrio', 'Sub-District', 'Congressional District', 'Municipality District', 'district', 'DMA Region', 'Union Territory', 'Territory', 'Colloquial Area', 'Autonomous Community', 'Borough', 'County', 'State', 'District', 'City Region', 'Commune', 'Region', 'Department', 'Division', 'Sub-Ward', 'Municipality', 'University' |
| location_name | string | No | - | Name of location or its part. |

#### Example

```bash
echo '{"search_engine": "google", "country_iso_code": "US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/google/locations
```

---

### serp_youtube_locations

**Description**: Utility tool to get list of available locations for: serp_youtube_organic_live_advanced, serp_youtube_video_info_live_advanced, serp_youtube_video_comments_live_advanced, serp_youtube_video_subtitles_live_advanced.
**Endpoint**: `POST /v3/serp/youtube/locations`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| country_iso_code | string | Yes | - | ISO 3166-1 alpha-2 country code, for example: US, GB, MT |
| location_type | string | No | - | Type of location. Possible variants: 'TV Region', 'Postal Code', 'Neighborhood', 'Governorate', 'National Park', 'Quarter', 'Canton', 'Airport', 'Okrug', 'Prefecture', 'City', 'Country', 'Province', 'Barrio', 'Sub-District', 'Congressional District', 'Municipality District', 'district', 'DMA Region', 'Union Territory', 'Territory', 'Colloquial Area', 'Autonomous Community', 'Borough', 'County', 'State', 'District', 'City Region', 'Commune', 'Region', 'Department', 'Division', 'Sub-Ward', 'Municipality', 'University' |
| location_name | string | No | - | Name of location or its part. |

#### Example

```bash
echo '{"country_iso_code": "US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/youtube/locations
```

---

### serp_youtube_organic_live_advanced

**Description**: Provides top 20 blocks of YouTube search engine results for a keyword
**Endpoint**: `POST /v3/serp/youtube/organic/live/advanced`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | - | Search keyword |
| location_name | string | Yes | - | Full name of the location. Location format - hierarchical, comma-separated (from most specific to least). Can be one of: 1. Country only: "United States" 2. Region,Country: "California,United States" 3. City,Region,Country: "San Francisco,California,United States" |
| language_code | string | Yes | - | Search engine language code (e.g., 'en') |
| device | string | No | `desktop` | Device type. Can take the values: desktop, mobile. |
| os | string | No | `windows` | Device operating system. If desktop: windows, macos (default: windows). If mobile: android, ios (default: android). |
| block_depth | number | No | `20` | Parsing depth. Number of blocks of results in SERP. Max value: 700. |

#### Example

```bash
echo '{"keyword": "python tutorial", "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/youtube/organic/live/advanced
```

---

### serp_youtube_video_info_live_advanced

**Description**: Provides data on the video you specify
**Endpoint**: `POST /v3/serp/youtube/video_info/live/advanced`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| video_id | string | Yes | - | ID of the video |
| location_name | string | Yes | - | Full name of the location. Location format - hierarchical, comma-separated (from most specific to least). Can be one of: 1. Country only: "United States" 2. Region,Country: "California,United States" 3. City,Region,Country: "San Francisco,California,United States" |
| language_code | string | Yes | - | Search engine language code (e.g., 'en') |
| device | string | No | `desktop` | Device type. Can take the values: desktop, mobile. |
| os | string | No | `windows` | Device operating system. If desktop: windows, macos (default: windows). If mobile: android, ios (default: android). |

#### Example

```bash
echo '{"video_id": "dQw4w9WgXcQ", "location_name": "United States", "language_code": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/youtube/video_info/live/advanced
```

---

### serp_youtube_video_comments_live_advanced

**Description**: Provides data on the video comments you specify
**Endpoint**: `POST /v3/serp/youtube/video_comments/live/advanced`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| video_id | string | Yes | - | ID of the video |
| location_name | string | Yes | - | Full name of the location. Location format - hierarchical, comma-separated (from most specific to least). Can be one of: 1. Country only: "United States" 2. Region,Country: "California,United States" 3. City,Region,Country: "San Francisco,California,United States" |
| language_code | string | Yes | - | Search engine language code (e.g., 'en') |
| device | string | No | `desktop` | Device type. Can take the values: desktop, mobile. |
| os | string | No | `windows` | Device operating system. If desktop: windows, macos (default: windows). If mobile: android, ios (default: android). |
| depth | number | No | `20` | Parsing depth, number of results in SERP. Max value: 700. |

#### Example

```bash
echo '{"video_id": "dQw4w9WgXcQ", "location_name": "United States", "language_code": "en", "depth": 50}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/youtube/video_comments/live/advanced
```

---

### serp_youtube_video_subtitles_live_advanced

**Description**: Provides data on the video subtitles you specify
**Endpoint**: `POST /v3/serp/youtube/video_subtitles/live/advanced`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| video_id | string | Yes | - | ID of the video |
| location_name | string | Yes | - | Full name of the location. Location format - hierarchical, comma-separated (from most specific to least). Can be one of: 1. Country only: "United States" 2. Region,Country: "California,United States" 3. City,Region,Country: "San Francisco,California,United States" |
| language_code | string | Yes | - | Search engine language code (e.g., 'en') |
| subtitles_language | string | No | - | Language code of original text (e.g., 'en') |
| subtitles_translate_language | string | No | - | Language code of translated text (e.g., 'en') |
| device | string | No | `desktop` | Device type. Can take the values: desktop, mobile. |
| os | string | No | `windows` | Device operating system. If desktop: windows, macos (default: windows). If mobile: android, ios (default: android). |

#### Example

```bash
echo '{"video_id": "dQw4w9WgXcQ", "location_name": "United States", "language_code": "en", "subtitles_language": "en"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/youtube/video_subtitles/live/advanced
```

---

## Suggested Workflows

### 1. Analyze Local SEO Differences in the Top 10 Google Results for Two Target Markets

Compare how search results differ between two geographic locations for the same keyword.

1. **Fetch SERP results for location 1** using `serp_organic_live_advanced`:
   ```bash
   echo '{"keyword": "best restaurants", "language_code": "en", "location_name": "New York,New York,United States", "depth": 10}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/google/organic/live/advanced
   ```

2. **Fetch SERP results for location 2** using `serp_organic_live_advanced`:
   ```bash
   echo '{"keyword": "best restaurants", "language_code": "en", "location_name": "Los Angeles,California,United States", "depth": 10}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/google/organic/live/advanced
   ```

3. **Compare results**: Display a unified table of the top 10 results for both locations side-by-side, with columns: Rank, Domain, Title, Snippet (shortened), URL, and Element Type (e.g., Organic, Knowledge Graph, Featured Snippet, etc.).

### 2. Monitor Visibility for Key Branded Searches in Real-Time

Check if a domain currently ranks in top positions or SERP features for a branded keyword.

1. **Fetch real-time SERP** using `serp_organic_live_advanced`:
   ```bash
   echo '{"keyword": "your brand name", "language_code": "en", "location_name": "United States", "depth": 10}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/google/organic/live/advanced
   ```

2. **Analyze results**: Check if the target domain ranks in the top 3 organic results or SERP features like featured snippet or knowledge graph. Identify what competitors are showing in SERP features if the target domain is not featured.

### 3. Generate Domain Visibility Reports and Track Ranking Changes

Generate a domain visibility snapshot including estimated organic traffic, top 10 rankings percentage, and SERP position breakdown.

1. **Fetch current SERP data** using `serp_organic_live_advanced`:
   ```bash
   echo '{"keyword": "target keyword", "language_code": "en", "location_name": "United States", "depth": 100}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/serp/google/organic/live/advanced
   ```

2. **Analyze domain positions**: List estimated organic traffic, percentage of top 10 rankings, and SERP position breakdown for the target domain.
