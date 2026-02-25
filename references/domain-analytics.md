# Domain Analytics API Reference

Tools for WHOIS domain data enriched with SEO metrics, and technology stack detection for domains.

---

## WHOIS

### domain_analytics_whois_available_filters
**Description**: Here you will find all the necessary information about filters that can be used with DataForSEO WHOIS API endpoints. Please, keep in mind that filters are associated with a certain object in the result array, and should be specified accordingly.
**Endpoint**: `GET /v3/domain_analytics/whois/available_filters`
**AI-condensed**: No (supportOnlyFullResponse -- use `--full-response`)

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tool | string | No | -- | The name of the tool to get filters for. If omitted, returns filters for all tools. Valid value: `domain_analytics_whois_overview` |

#### Example
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/domain_analytics/whois/available_filters \
  --method GET --full-response
```

---

### domain_analytics_whois_overview
**Description**: This endpoint will provide you with Whois data enriched with backlink stats, and ranking and traffic info from organic and paid search results. Using this endpoint you will be able to get all these data for the domains matching the parameters you specify in the request
**Endpoint**: `POST /v3/domain_analytics/whois/overview/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| limit | number | No | 10 | Max number of returned domains. Min 1, max 1000 |
| offset | number | No | 0 | Offset in the results array. Use for pagination |
| filters | array | No | -- | Filter array (max 8 filters). Use `domain_analytics_whois_available_filters` to see available fields. See `$SKILL_DIR/references/filters-and-sorting.md` |
| order_by | string[] | No | -- | Sorting rules (max 3). Format: `["field,desc"]`. Example: `["rating.value,desc","rating.votes_count,desc"]` |
| is_claimed | boolean | No | true | Whether the business is verified by its owner on Google Maps |

#### Example
```bash
echo '{"filters":["domain","like","%example%"],"limit":10}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/domain_analytics/whois/overview/live
```

```bash
echo '{"filters":[["expiration_datetime","<","2025-12-31"],"and",["backlinks_info.referring_domains",">",100]],"order_by":["backlinks_info.referring_domains,desc"],"limit":20}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/domain_analytics/whois/overview/live
```

---

## Technologies

### domain_analytics_technologies_available_filters
**Description**: Here you will find all the necessary information about filters that can be used with DataForSEO Technologies API endpoints. Please, keep in mind that filters are associated with a certain object in the result array, and should be specified accordingly.
**Endpoint**: `GET /v3/domain_analytics/technologies/available_filters`
**AI-condensed**: No (supportOnlyFullResponse -- use `--full-response`)

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tool | string | No | -- | The name of the tool to get filters for. If omitted, returns filters for all tools. Valid values: `domain_analytics_technologies_domains_by_technology`, `domain_analytics_technologies_aggregation_technologies`, `domain_analytics_technologies_technologies_summary`, `domain_analytics_technologies_domains_by_html_terms` |

#### Example
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/domain_analytics/technologies/available_filters \
  --method GET --full-response
```

---

### domain_analytics_technologies_domain_technologies
**Description**: Using this endpoint you will get a list of technologies used in a particular domain
**Endpoint**: `POST /v3/domain_analytics/technologies/domain_technologies/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | -- | Domain name of the website to analyze. Results will be returned for the specified domain only |

#### Example
```bash
echo '{"target":"github.com"}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/domain_analytics/technologies/domain_technologies/live
```
