# Content Analysis API Reference

Tools for analyzing content citations, summaries, and phrase trends across the web for target keywords.

---

### content_analysis_search
**Description**: This endpoint will provide you with detailed citation data available for the target keyword
**Endpoint**: `POST /v3/content_analysis/search/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | -- | Target keyword. To match an exact phrase, use double quotes and backslashes (e.g., `\"logitech mouse\"`) |
| keyword_fields | object | No | -- | Filter dataset by keywords in specific fields. Fields: `title`, `main_title`, `previous_title`, `snippet`. Example: `{"snippet":"\"logitech mouse\"","main_title":"sale"}` |
| page_type | string[] | No | -- | Target page types. Values: `ecommerce`, `news`, `blogs`, `message-boards`, `organization` |
| search_mode | string | No | -- | Results grouping type. Values: `as_is`, `one_per_domain` |
| limit | number | No | 10 | Max number of results. Min 1, max 1000 |
| offset | number | No | 0 | Offset in results array for pagination |
| filters | array | No | -- | Filter array (max 8 filters). Supported operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `match`, `not_match`. See `$SKILL_DIR/references/filters-and-sorting.md` |
| order_by | string[] | No | -- | Sorting rules (max 3). Format: `["field,desc"]`. Example: `["content_info.sentiment_connotations.anger,desc"]` |

#### Example
```bash
echo '{"keyword":"artificial intelligence","page_type":["news"],"limit":10}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/content_analysis/search/live
```

```bash
echo '{"keyword":"seo tools","filters":[["domain_rank",">",800],"and",["content_info.connotation_types.negative",">",0.9]],"order_by":["content_info.sentiment_connotations.anger,desc"],"limit":20}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/content_analysis/search/live
```

---

### content_analysis_summary
**Description**: This endpoint will provide you with an overview of citation data available for the target keyword
**Endpoint**: `POST /v3/content_analysis/summary/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | -- | Target keyword. To match an exact phrase, use double quotes and backslashes |
| keyword_fields | object | No | -- | Filter dataset by keywords in specific fields. Fields: `title`, `main_title`, `previous_title`, `snippet` |
| page_type | string[] | No | -- | Target page types. Values: `ecommerce`, `news`, `blogs`, `message-boards`, `organization` |
| initial_dataset_filters | array | No | -- | Initial dataset filtering parameters applied to Search endpoint fields. Max 8 filters. Supported operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `has`, `has_not`, `match`, `not_match`. See `$SKILL_DIR/references/filters-and-sorting.md` |
| positive_connotation_threshold | number | No | 0.4 | Probability index threshold for positive sentiment (0-1). Only citations with positive sentiment probability >= this value are included in `connotation_types` |
| sentiments_connotation_threshold | number | No | 0.4 | Probability index threshold for sentiment connotations (0-1). Only citations where probability per sentiment >= this value are included in `sentiment_connotations` |
| internal_list_limit | number | No | 1 | Max number of elements within internal arrays. Min 1, max 20 |

#### Example
```bash
echo '{"keyword":"machine learning","page_type":["blogs","news"]}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/content_analysis/summary/live
```

```bash
echo '{"keyword":"seo tools","initial_dataset_filters":["domain","<>","logitech.com"],"positive_connotation_threshold":0.6}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/content_analysis/summary/live
```

---

### content_analysis_phrase_trends
**Description**: This endpoint will provide you with data on all citations of the target keyword for the indicated date range
**Endpoint**: `POST /v3/content_analysis/phrase_trends/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | -- | Target keyword. To match an exact phrase, use double quotes and backslashes |
| keyword_fields | object | No | -- | Filter dataset by keywords in specific fields. Fields: `title`, `main_title`, `previous_title`, `snippet` |
| page_type | string[] | No | -- | Target page types. Values: `ecommerce`, `news`, `blogs`, `message-boards`, `organization` |
| initial_dataset_filters | array | No | -- | Initial dataset filtering parameters applied to Search endpoint fields. Max 8 filters. Supported operators: `regex`, `not_regex`, `<`, `<=`, `>`, `>=`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `has`, `has_not`, `match`, `not_match`. See `$SKILL_DIR/references/filters-and-sorting.md` |
| date_from | string | Yes | -- | Starting date of the time range. Format: `yyyy-mm-dd` |
| date_to | string | No | -- | Ending date of the time range. Format: `yyyy-mm-dd` |
| date_group | string | No | `"month"` | Date grouping type. Values: `day`, `week`, `month` |
| internal_list_limit | number | No | 1 | Max number of elements within internal arrays. Min 1, max 20 |

#### Example
```bash
echo '{"keyword":"artificial intelligence","date_from":"2024-01-01","date_to":"2024-12-31","date_group":"month"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/content_analysis/phrase_trends/live
```

```bash
echo '{"keyword":"seo","initial_dataset_filters":[["domain","<>","logitech.com"],"and",["content_info.connotation_types.negative",">",1000]],"date_from":"2024-06-01","date_group":"week"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/content_analysis/phrase_trends/live
```
