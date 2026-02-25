# AI Optimization API Reference

Tools for tracking LLM mentions of brands/keywords, AI search keyword data, ChatGPT scraping, and LLM response retrieval.

---

## Keyword Data

### ai_opt_kw_data_loc_and_lang
**Description**: Utility tool for 'AI Optimization Keyword Data Locations and Languages' (ai_opt_kw_data_loc_and_lang) to get list of available locations and languages
**Endpoint**: `GET /v3/ai_optimization/ai_keyword_data/locations_and_languages`
**AI-condensed**: No (supportOnlyFullResponse -- use `--full-response`)

#### Parameters
_No parameters required._

#### Example
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/ai_keyword_data/locations_and_languages \
  --method GET --full-response
```

---

### ai_optimization_keyword_data_search_volume
**Description**: This endpoint provides search volume data for your target keywords, reflecting their estimated usage in AI LLMs
**Endpoint**: `POST /v3/ai_optimization/ai_keyword_data/keywords_search_volume/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keywords | string[] | Yes | -- | Keywords to check. Maximum 1000 keywords |
| location_name | string | No | `"United States"` | Full name of the location (e.g., "United Kingdom") |
| language_code | string | Yes | -- | Language code (e.g., "en") |

#### Example
```bash
echo '{"keywords":["best crm software","project management tools"],"location_name":"United States","language_code":"en"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/ai_optimization/ai_keyword_data/keywords_search_volume/live
```

---

## LLM Models & Responses

### ai_optimization_llm_models
**Description**: Utility tool for ai_optimization_llm_response to get list of available locations and languages
**Endpoint**: `GET /v3/ai_optimization/{llm_type}/llm_responses/models`
**AI-condensed**: Yes (uses `--full-response` internally)

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| llm_type | string | Yes | -- | Type of LLM. Must be one of: `claude`, `gemini`, `chat_gpt`, `perplexity` |

#### Example
```bash
echo '{"llm_type":"chat_gpt"}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/chat_gpt/llm_responses/models \
  --method GET --full-response
```

---

### ai_optimization_llm_response
**Description**: This endpoint allows you to retrieve structured responses from a specific AI model, based on the input parameters
**Endpoint**: `POST /v3/ai_optimization/{llm_type}/llm_responses/live`
**AI-condensed**: Yes (uses `--full-response` internally)

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| llm_type | string | Yes | -- | Type of LLM. Must be one of: `claude`, `gemini`, `chat_gpt`, `perplexity` |
| user_prompt | string | Yes | -- | The question or task to send to the AI model. Up to 500 characters |
| model_name | string | Yes | -- | Name of the AI model (actual model name + version). Use `ai_optimization_llm_models` first to get available models |
| temperature | number | No | -- | Randomness of the AI response. Higher = more diverse, lower = more focused |
| top_p | number | No | -- | Controls diversity by limiting token selection |
| web_search | boolean | No | -- | Enable web search for current information. Model can access and cite current web info |

#### Example
```bash
echo '{"llm_type":"chat_gpt","user_prompt":"What are the best SEO tools?","model_name":"gpt-4o"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/chat_gpt/llm_responses/live --full-response
```

---

## ChatGPT Scraper

### ai_optimization_chat_gpt_scraper_locations
**Description**: Utility tool for ai_optimization_chat_gpt_scraper to get list of available locations
**Endpoint**: `GET /v3/ai_optimization/chat_gpt/llm_scraper/locations` (GET if no params, POST with params)
**AI-condensed**: No (supportOnlyFullResponse -- use `--full-response`)

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| country_iso_code | string | No | -- | ISO 3166-1 alpha-2 country code (e.g., "US", "GB", "MT") |
| location_name | string | No | -- | Name of location or part of it |

#### Example
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/chat_gpt/llm_scraper/locations \
  --method GET --full-response
```

```bash
echo '{"country_iso_code":"US"}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/chat_gpt/llm_scraper/locations --full-response
```

---

### ai_optimization_chat_gpt_scraper
**Description**: This endpoint provides results from ChatGPT searches
**Endpoint**: `POST /v3/ai_optimization/chat_gpt/llm_scraper/live/advanced`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | -- | Search keyword. Up to 2000 characters. `%` codes are decoded; use `%25` for literal `%`, `%2B` for literal `+` |
| location_name | string | No | `"United States"` | Full name of the location |
| language_code | string | Yes | -- | Language code (e.g., "en") |
| force_web_search | boolean | No | -- | Force AI agent to use web search |

#### Example
```bash
echo '{"keyword":"best project management software","location_name":"United States","language_code":"en"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/ai_optimization/chat_gpt/llm_scraper/live/advanced
```

---

## LLM Mentions

### ai_optimization_llm_mentions_filters
**Description**: This endpoint provides all the necessary information about filters that can be used with AI Optimization LLM Mentions API endpoints
**Endpoint**: `GET /v3/ai_optimization/llm_mentions/available_filters`
**AI-condensed**: No (supportOnlyFullResponse -- use `--full-response`)

#### Parameters
_No parameters required._

#### Example
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/llm_mentions/available_filters \
  --method GET --full-response
```

---

### ai_opt_llm_ment_loc_and_lang
**Description**: Utility tool for 'AI Optimization LLM Mentions Locations and Languages' (ai_opt_llm_ment_loc_and_lang) to get list of available locations and languages
**Endpoint**: `GET /v3/ai_optimization/llm_mentions/locations_and_languages`
**AI-condensed**: No (supportOnlyFullResponse -- use `--full-response`)

#### Parameters
_No parameters required._

#### Example
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/ai_optimization/llm_mentions/locations_and_languages \
  --method GET --full-response
```

---

### ai_opt_llm_ment_search
**Description**: This endpoint provides aggregated LLM mentions metrics grouped by the most frequently mentioned pages for the specified target
**Endpoint**: `POST /v3/ai_optimization/llm_mentions/search/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | array | Yes | -- | Array of target objects. Each must contain either `domain` or `keyword`. Max 1000 targets. See target format below |
| location_name | string | No | -- | Full name of the location (e.g., "United States") |
| language_code | string | No | -- | Language code (e.g., "en") |
| platform | string | No | -- | Platform to search. One of: `chat_gpt`, `google` |
| filters | array | No | -- | Filter array (max 8 filters). See `ai_optimization_llm_mentions_filters` for available fields. See `$SKILL_DIR/references/filters-and-sorting.md` |
| order_by | string[] | No | -- | Sorting rules (max 3). Format: `["field,desc"]`. See `ai_optimization_llm_mentions_filters` for available fields |
| limit | number | No | 10 | Number of results to return. Max 1000 |

**Target object format (domain type):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| domain | string | Yes | Target domain to search for LLM mentions |
| search_filter | string | No | `include` or `exclude` |
| search_scope | string[] | No | Array of: `any`, `question`, `answer` |

**Target object format (keyword type):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| keyword | string | Yes | Target keyword to search for LLM mentions |
| match_type | string | No | `word_match` or `partial_match` |
| search_filter | string | No | `include` or `exclude` |
| search_scope | string[] | No | Array of: `any`, `question`, `answer` |

#### Example
```bash
echo '{"target":[{"keyword":"best crm software","match_type":"word_match","search_scope":["answer"]}],"location_name":"United States","language_code":"en","platform":"chat_gpt","limit":10}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/ai_optimization/llm_mentions/search/live
```

---

### ai_opt_llm_ment_agg_metrics
**Description**: This endpoint provides aggregated metrics for mentions of the keywords or domains specified in the target array of the request.
**Endpoint**: `POST /v3/ai_optimization/llm_mentions/aggregated_metrics/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | array | Yes | -- | Array of target objects (domain or keyword). Max 1000 targets. Same format as `ai_opt_llm_ment_search` |
| location_name | string | No | -- | Full name of the location |
| language_code | string | No | -- | Language code (e.g., "en") |
| platform | string | No | -- | Platform: `chat_gpt` or `google` |
| filters | array | No | -- | Filter array (max 8 filters). See `ai_optimization_llm_mentions_filters` for available fields |
| internal_list_limit | number | No | -- | Limit the number of items processed internally |

#### Example
```bash
echo '{"target":[{"domain":"hubspot.com","search_scope":["answer"]}],"location_name":"United States","language_code":"en","platform":"chat_gpt"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/ai_optimization/llm_mentions/aggregated_metrics/live
```

---

### ai_opt_llm_ment_cross_agg_metrics
**Description**: This endpoint provides aggregated metrics grouped by custom keys for mentions of the keywords or domains specified in the target array of the request
**Endpoint**: `POST /v3/ai_optimization/llm_mentions/cross_aggregated_metrics/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array | Yes | -- | Array of objects with `aggregation_key` and `target`. Min 2, max 10 target groups. See format below |
| location_name | string | No | -- | Full name of the location |
| language_code | string | No | -- | Language code (e.g., "en") |
| platform | string | No | -- | Platform: `chat_gpt` or `google` |
| filters | array | No | -- | Filter array (max 8 filters). See `ai_optimization_llm_mentions_filters` |
| internal_list_limit | number | No | -- | Limit the number of items processed internally |

**Targets array item format:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| aggregation_key | string | Yes | Custom key for grouping results |
| target | array | Yes | Array of domain/keyword target objects (up to 10 per group). Same format as `ai_opt_llm_ment_search` |

#### Example
```bash
echo '{"targets":[{"aggregation_key":"brand_a","target":[{"domain":"hubspot.com"}]},{"aggregation_key":"brand_b","target":[{"domain":"salesforce.com"}]}],"location_name":"United States","language_code":"en"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/ai_optimization/llm_mentions/cross_aggregated_metrics/live
```

---

### ai_opt_llm_ment_top_domains
**Description**: This endpoint provides aggregated LLM mentions metrics grouped by the most frequently mentioned domains for the specified target
**Endpoint**: `POST /v3/ai_optimization/llm_mentions/top_domains/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | array | Yes | -- | Array of target objects (domain or keyword). Max 1000 targets. Same format as `ai_opt_llm_ment_search` |
| location_name | string | No | -- | Full name of the location |
| language_code | string | No | -- | Language code (e.g., "en") |
| platform | string | No | -- | Platform: `chat_gpt` or `google` |
| links_scope | string | No | -- | Which links to use for domain extraction: `sources` or `search_results` |
| initial_dataset_filters | array | No | -- | Filter array (max 8 filters). See `ai_optimization_llm_mentions_filters` |
| items_list_limit | number | No | -- | Max results in items array. Min 1, max 10 |
| internal_list_limit | number | No | -- | Max elements within internal arrays. Min 1, max 10 |

#### Example
```bash
echo '{"target":[{"keyword":"best crm software","search_scope":["answer"]}],"location_name":"United States","language_code":"en","platform":"chat_gpt","items_list_limit":5}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/ai_optimization/llm_mentions/top_domains/live
```

---

### ai_opt_llm_ment_top_pages
**Description**: This endpoint provides aggregated LLM mentions metrics grouped by the most frequently mentioned pages for the specified target
**Endpoint**: `POST /v3/ai_optimization/llm_mentions/top_pages/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | array | Yes | -- | Array of target objects (domain or keyword). Max 1000 targets. Same format as `ai_opt_llm_ment_search` |
| location_name | string | No | -- | Full name of the location |
| language_code | string | No | -- | Language code (e.g., "en") |
| platform | string | No | -- | Platform: `chat_gpt` or `google` |
| links_scope | string | No | -- | Which links to use for page extraction: `sources` or `search_results` |
| initial_dataset_filters | array | No | -- | Filter array (max 8 filters). See `ai_optimization_llm_mentions_filters` |
| items_list_limit | number | No | -- | Max results in items array. Min 1, max 10 |
| internal_list_limit | number | No | -- | Max elements within internal arrays. Min 1, max 10 |

#### Example
```bash
echo '{"target":[{"domain":"hubspot.com","search_scope":["answer"]}],"location_name":"United States","language_code":"en","platform":"chat_gpt","items_list_limit":5}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/ai_optimization/llm_mentions/top_pages/live
```
