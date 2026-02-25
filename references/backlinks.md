# Backlinks API Reference

The Backlinks API provides comprehensive backlink analysis tools for domains, subdomains, and webpages. These tools let you examine backlink profiles, anchor text distribution, referring domains, competitors, domain/page intersections, and historical backlink trends.

## Table of Contents

1. [backlinks_summary](#backlinks_summary)
2. [backlinks_backlinks](#backlinks_backlinks)
3. [backlinks_anchors](#backlinks_anchors)
4. [backlinks_referring_domains](#backlinks_referring_domains)
5. [backlinks_referring_networks](#backlinks_referring_networks)
6. [backlinks_competitors](#backlinks_competitors)
7. [backlinks_domain_pages](#backlinks_domain_pages)
8. [backlinks_domain_pages_summary](#backlinks_domain_pages_summary)
9. [backlinks_domain_intersection](#backlinks_domain_intersection)
10. [backlinks_page_intersection](#backlinks_page_intersection)
11. [backlinks_bulk_backlinks](#backlinks_bulk_backlinks)
12. [backlinks_bulk_referring_domains](#backlinks_bulk_referring_domains)
13. [backlinks_bulk_ranks](#backlinks_bulk_ranks)
14. [backlinks_bulk_spam_score](#backlinks_bulk_spam_score)
15. [backlinks_bulk_new_lost_backlinks](#backlinks_bulk_new_lost_backlinks)
16. [backlinks_bulk_new_lost_referring_domains](#backlinks_bulk_new_lost_referring_domains)
17. [backlinks_bulk_pages_summary](#backlinks_bulk_pages_summary)
18. [backlinks_timeseries_summary](#backlinks_timeseries_summary)
19. [backlinks_timeseries_new_lost_summary](#backlinks_timeseries_new_lost_summary)
20. [backlinks_available_filters](#backlinks_available_filters)
21. [Suggested Workflows](#suggested-workflows)

---

### backlinks_summary

**Description**: This endpoint will provide you with an overview of backlinks data available for a given domain, subdomain, or webpage.

**Endpoint**: `POST /v3/backlinks/summary/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| include_subdomains | boolean | No | true | If set to true, the results will include data on indirect links pointing to a page that either redirects to the target, or points to a canonical page. If set to false, indirect links will be ignored. |
| exclude_internal_backlinks | boolean | No | true | If set to true, the results will not include data on internal backlinks from subdomains of the same domain as target. If set to false, internal links will be included in the results. |

#### Example

```bash
echo '{"target": "forbes.com", "include_subdomains": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/summary/live
```

---

### backlinks_backlinks

**Description**: This endpoint will provide you with a list of backlinks and relevant data for the specified domain, subdomain, or webpage.

**Endpoint**: `POST /v3/backlinks/backlinks/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| mode | string | No | "as_is" | Results grouping type. Possible values: `as_is` (returns all backlinks), `one_per_domain` (returns one backlink per domain), `one_per_anchor` (returns one backlink per anchor). |
| limit | number | No | 10 | The maximum number of returned backlinks. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned backlinks. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Operators: `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `regex`, `not_regex`, `match`, `not_match`. Use logical operators `and`, `or` between conditions. |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["domain_from_rank,desc","page_from_rank,asc"]` |

#### Example

```bash
echo '{"target": "forbes.com", "mode": "one_per_domain", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/backlinks/live
```

---

### backlinks_anchors

**Description**: This endpoint will provide you with a detailed overview of anchors used when linking to the specified website with relevant backlink data for each of them.

**Endpoint**: `POST /v3/backlinks/anchors/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| limit | number | No | 10 | The maximum number of returned anchors. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned anchors. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Operators: `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `regex`, `not_regex`, `match`, `not_match`. |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["domain_from_rank,desc","page_from_rank,asc"]` |

#### Example

```bash
echo '{"target": "forbes.com", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/anchors/live
```

---

### backlinks_referring_domains

**Description**: This endpoint will provide you with a detailed overview of referring domains pointing to the target you specify.

**Endpoint**: `POST /v3/backlinks/referring_domains/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| limit | number | No | 10 | The maximum number of returned pages. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned pages. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Operators: `regex`, `not_regex`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `match`, `not_match`. |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["page_summary.backlinks,desc","page_summary.rank,asc"]` |

#### Example

```bash
echo '{"target": "forbes.com", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/referring_domains/live
```

---

### backlinks_referring_networks

**Description**: This endpoint will provide you with a detailed overview of referring domains pointing to the target you specify.

**Endpoint**: `POST /v3/backlinks/referring_networks/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| network_address_type | string | No | "ip" | Indicates the type of network to get data for. Possible values: `ip`, `subnet`. |
| limit | number | No | 10 | The maximum number of returned networks. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned networks. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Operators: `regex`, `not_regex`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `match`, `not_match`. |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["backlinks,desc","rank,asc"]` |

#### Example

```bash
echo '{"target": "forbes.com", "network_address_type": "subnet", "limit": 10}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/referring_networks/live
```

---

### backlinks_competitors

**Description**: This endpoint will provide you with a list of competitors that share some part of the backlink profile with a target website, along with a number of backlink intersections and the rank of every competing website.

**Endpoint**: `POST /v3/backlinks/competitors/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| limit | number | No | 10 | The maximum number of returned domains. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned networks. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Operators: `regex`, `not_regex`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `match`, `not_match`. |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["intersections,desc","rank,asc"]` |
| main_domain | boolean | No | true | Indicates if only the main domain of the target will be included in the search. |
| exclude_large_domains | boolean | No | true | If set to true, results from large domains (google.com, amazon.com, etc.) will be omitted. |
| exclude_internal_backlinks | boolean | No | true | If set to true, the results will not include data on internal backlinks from subdomains of the same domain as target. |

#### Example

```bash
echo '{"target": "forbes.com", "limit": 20, "exclude_large_domains": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/competitors/live
```

---

### backlinks_domain_pages

**Description**: This endpoint will provide you with a detailed overview of domain pages with backlink data for each page.

**Endpoint**: `POST /v3/backlinks/domain_pages/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| limit | number | No | 10 | The maximum number of returned pages. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned pages. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Operators: `regex`, `not_regex`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `match`, `not_match`. |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["page_summary.backlinks,desc","page_summary.rank,asc"]` |

#### Example

```bash
echo '{"target": "forbes.com", "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/domain_pages/live
```

---

### backlinks_domain_pages_summary

**Description**: This endpoint will provide you with detailed summary data on all backlinks and related metrics for each page of the target domain or subdomain you specify. If you indicate a single page as a target, you will get comprehensive summary data on all backlinks for that page.

**Endpoint**: `POST /v3/backlinks/domain_pages_summary/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain, subdomain or webpage to get backlinks for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| limit | number | No | 10 | The maximum number of returned anchors. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the results array of returned anchors. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Operators: `regex`, `not_regex`, `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `match`, `not_match`. |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["backlinks,desc","rank,asc"]` |

#### Example

```bash
echo '{"target": "forbes.com", "limit": 10}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/domain_pages_summary/live
```

---

### backlinks_domain_intersection

**Description**: This endpoint will provide you with the list of domains pointing to the specified websites. This endpoint is especially useful for creating a Link Gap feature that shows what domains link to your competitors but do not link out to your website.

**Endpoint**: `POST /v3/backlinks/domain_intersection/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

> **Important -- Numbered Dictionary Format**: This tool uses `mapArrayToNumberedKeys` internally. The `targets` parameter accepts an array, but the API requires targets to be passed as a numbered dictionary. The skill handles this conversion automatically. When using the raw API endpoint directly, you must convert the array to numbered keys:
>
> Array input: `["forbes.com", "cnn.com"]`
> Converted format: `{"1": "forbes.com", "2": "cnn.com"}`
>
> Filters for intersection tools reference targets by their numbered index (e.g., `"1.backlinks"`, `"2.referring_pages"`).

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get links for. You can set up to 20 domains, subdomains or webpages. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| limit | number | No | 10 | The maximum number of returned results. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the array of returned results. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Filters reference targets by numbered index. Example: `["1.internal_links_count",">","1"]` |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["backlinks,desc","rank,asc"]` |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com", "bbc.com"], "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/domain_intersection/live
```

---

### backlinks_page_intersection

**Description**: This endpoint will provide you with the list of domains pointing to the specified websites. This endpoint is especially useful for creating a Link Gap feature that shows what domains link to your competitors but do not link out to your website.

**Endpoint**: `POST /v3/backlinks/page_intersection/live`

**AI-condensed**: Yes

> Supports filters and sorting. See `$SKILL_DIR/references/filters-and-sorting.md`

> **Important -- Numbered Dictionary Format**: This tool uses `mapArrayToNumberedKeys` internally. The `targets` parameter accepts an array, but the API requires targets to be passed as a numbered dictionary. The skill handles this conversion automatically. When using the raw API endpoint directly, you must convert the array to numbered keys:
>
> Array input: `["https://forbes.com/page1", "https://cnn.com/page2"]`
> Converted format: `{"1": "https://forbes.com/page1", "2": "https://cnn.com/page2"}`
>
> Filters for intersection tools reference targets by their numbered index (e.g., `"1.rank"`, `"2.page_from_rank"`).

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get links for. You can set up to 20 domains, subdomains or webpages. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). |
| limit | number | No | 10 | The maximum number of returned results. Min: 1, Max: 1000. |
| offset | number | No | 0 | Offset in the array of returned results. |
| filters | array | No | - | Array of results filtering parameters. Up to 8 filters maximum. Filters reference targets by numbered index. Example: `["1.rank",">","80"]` |
| order_by | array of strings | No | - | Results sorting rules. Use `asc` or `desc`. Max 3 sorting rules. Example: `["domain_from_rank,desc","page_from_rank,asc"]` |

#### Example

```bash
echo '{"targets": ["https://forbes.com/", "https://cnn.com/"], "limit": 20}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/page_intersection/live
```

---

### backlinks_bulk_backlinks

**Description**: This endpoint will provide you with the number of backlinks pointing to domains, subdomains, and pages specified in the targets array. The returned numbers correspond to all live backlinks, that is, total number of referring links with all attributes (e.g., nofollow, noreferrer, ugc, sponsored etc) that were found during the latest check. Note that if you indicate a domain as a target, you will get results for the root domain (domain with all of its subdomains).

**Endpoint**: `POST /v3/backlinks/bulk_backlinks/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get rank for. You can set up to 1000 targets. The domain or subdomain should be specified without `https://` and `www.`. The page should be specified with absolute URL (including `http://` or `https://`). |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com", "bbc.com"]}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/bulk_backlinks/live
```

---

### backlinks_bulk_referring_domains

**Description**: This endpoint will provide you with the number of referring domains pointing to domains, subdomains, and pages specified in the targets array. The returned numbers are based on all live referring domains. Note that if you indicate a domain as a target, you will get result for the root domain (domain with all of its subdomains).

**Endpoint**: `POST /v3/backlinks/bulk_referring_domains/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get rank for. You can set up to 1000 targets. The domain or subdomain should be specified without `https://` and `www.`. The page should be specified with absolute URL (including `http://` or `https://`). |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com", "bbc.com"]}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/bulk_referring_domains/live
```

---

### backlinks_bulk_ranks

**Description**: This endpoint will provide you with rank scores of the domains, subdomains, and pages specified in the targets array. The score is based on the number of referring domains pointing to the specified domains, subdomains, or pages. Rank values range from 0 (no backlinks detected) to 1,000 (highest rank). A similar scoring system is used in Google's Page Rank algorithm.

**Endpoint**: `POST /v3/backlinks/bulk_ranks/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get rank for. You can set up to 1000 targets. The domain or subdomain should be specified without `https://` and `www.`. The page should be specified with absolute URL (including `http://` or `https://`). |
| rank_scale | string | No | "one_thousand" | Defines the scale used for calculating and displaying rank values. Possible values: `one_hundred` (0-100 scale), `one_thousand` (0-1000 scale). |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com", "bbc.com"], "rank_scale": "one_hundred"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/bulk_ranks/live
```

---

### backlinks_bulk_spam_score

**Description**: This endpoint will provide you with spam scores of the domains, subdomains, and pages you specified in the targets array. Spam Score is DataForSEO's proprietary metric that indicates how "spammy" your target is on a scale from 0 to 100.

**Endpoint**: `POST /v3/backlinks/bulk_spam_score/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get spam score for. You can set up to 1000 targets. The domain or subdomain should be specified without `https://` and `www.`. The page should be specified with absolute URL (including `http://` or `https://`). |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com", "bbc.com"]}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/bulk_spam_score/live
```

---

### backlinks_bulk_new_lost_backlinks

**Description**: This endpoint will provide you with the number of referring domains pointing to domains, subdomains, and pages specified in the targets array. The returned numbers are based on all live referring links. Note that if you indicate a domain as a target, you will get result for the root domain (domain with all of its subdomains).

**Endpoint**: `POST /v3/backlinks/bulk_new_lost_backlinks/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get rank for. You can set up to 1000 targets. The domain or subdomain should be specified without `https://` and `www.`. The page should be specified with absolute URL (including `http://` or `https://`). |
| date_from | string | No | Today minus one month | Starting date of the time range. Backlinks that appeared after this date are considered new; those not found after this date but present before are considered lost. Minimum value: today minus one year. Format: `yyyy-mm-dd`. Example: `"2021-01-01"` |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com"], "date_from": "2025-01-01"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/bulk_new_lost_backlinks/live
```

---

### backlinks_bulk_new_lost_referring_domains

**Description**: This endpoint will provide you with the number of referring domains pointing to the domains, subdomains and pages specified in the targets array. Note that if you indicate a domain as a target, you will get result for the root domain (domain with all of its subdomains).

**Endpoint**: `POST /v3/backlinks/bulk_new_lost_referring_domains/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get rank for. You can set up to 1000 targets. The domain or subdomain should be specified without `https://` and `www.`. The page should be specified with absolute URL (including `http://` or `https://`). |
| date_from | string | No | Today minus one month | Starting date of the time range. Backlinks that appeared after this date are considered new; those not found after this date but present before are considered lost. Minimum value: today minus one year. Format: `yyyy-mm-dd`. Example: `"2021-01-01"` |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com"], "date_from": "2025-01-01"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/bulk_new_lost_referring_domains/live
```

---

### backlinks_bulk_pages_summary

**Description**: This endpoint will provide you with a comprehensive overview of backlinks and related data for a bulk of up to 1000 pages, domains, or subdomains. If you indicate a single page as a target, you will get comprehensive summary data on all backlinks for that page.

**Endpoint**: `POST /v3/backlinks/bulk_pages_summary/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| targets | array of strings | Yes | - | Domains, subdomains or webpages to get summary data for. A domain or subdomain should be specified without `https://` and `www.`. A page should be specified with absolute URL (including `http://` or `https://`). You can specify up to 1000 pages, domains, or subdomains. Note that the URLs in a single request cannot belong to more than 100 different domains. |
| include_subdomains | boolean | No | true | If set to true, the results will include data on indirect links pointing to a page that either redirects to the target, or points to a canonical page. If set to false, indirect links will be ignored. |

#### Example

```bash
echo '{"targets": ["forbes.com", "cnn.com", "bbc.com"], "include_subdomains": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/bulk_pages_summary/live
```

---

### backlinks_timeseries_summary

**Description**: This endpoint will provide you with an overview of backlink data for the target domain available during a period between the two indicated dates. Backlink metrics will be grouped by the time range that you define: day, week, month, or year. Data from this endpoint will be especially helpful for building time-series graphs of daily, weekly, monthly, and yearly link-building progress.

**Endpoint**: `POST /v3/backlinks/timeseries_summary/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain to get data for. A domain should be specified without `https://` and `www.`. Example: `"forbes.com"` |
| date_from | string | No | - | Starting date of the time range. Minimum value: `2019-01-30`. Maximum value: must not exceed `date_to`. Format: `yyyy-mm-dd`. |
| date_to | string | No | Today's date | Ending date of the time range. Minimum value: must not precede `date_from`. Maximum value: today's date. Format: `yyyy-mm-dd`. |
| group_range | string | No | "month" | Time range for grouping results. Possible values: `day`, `week`, `month`, `year`. For day, returns items for all dates between date_from and date_to. For week/month/year, returns items for full periods with the last day of each period. |

#### Example

```bash
echo '{"target": "forbes.com", "date_from": "2025-01-01", "date_to": "2025-06-01", "group_range": "month"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/timeseries_summary/live
```

---

### backlinks_timeseries_new_lost_summary

**Description**: This endpoint will provide you with the number of new and lost backlinks and referring domains for the domain specified in the target field. The results will be provided for a period between the two indicated dates, and metrics will be grouped by the time range that you define: day, week, month, or year. Data from this endpoint will be especially helpful for building time-series graphs of new and lost backlinks and referring domains.

**Endpoint**: `POST /v3/backlinks/timeseries_new_lost_summary/live`

**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| target | string | Yes | - | Domain to get data for. A domain should be specified without `https://` and `www.`. Example: `"forbes.com"` |
| date_from | string | No | - | Starting date of the time range. Minimum value: `2019-01-30`. Maximum value: must not exceed `date_to`. Format: `yyyy-mm-dd`. |
| date_to | string | No | Today's date | Ending date of the time range. Minimum value: must not precede `date_from`. Maximum value: today's date. Format: `yyyy-mm-dd`. |
| group_range | string | No | "month" | Time range for grouping results. Possible values: `day`, `week`, `month`, `year`. For day, returns items for all dates between date_from and date_to. For week/month/year, returns items for full periods with the last day of each period. |

#### Example

```bash
echo '{"target": "forbes.com", "date_from": "2025-01-01", "date_to": "2025-06-01", "group_range": "week"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/backlinks/timeseries_new_lost_summary/live
```

---

### backlinks_available_filters

**Description**: Here you will find all the necessary information about filters that can be used with DataForSEO Backlinks API endpoints. Filters are associated with a certain object in the result array, and should be specified accordingly.

**Endpoint**: `GET /v3/backlinks/available_filters`

**AI-condensed**: No (use `--full-response`)

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tool | string | No | - | The name of the tool to get filters for. If omitted, returns filters for all tools. |

#### Example

```bash
echo '{"tool": "backlinks_backlinks"}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/backlinks/available_filters \
  --method GET --full-response
```

---

## Suggested Workflows

### 1. Discover Your Strongest Backlinks for Authority Building

Find the top highest-authority backlinks to a domain, grouped by referring domain.

**Parameters**: `domain` (string) -- The domain to find backlinks for.

**Prompt**: Identify the top 10 highest-authority backlinks to the domain, grouped by referring domain. Include backlink type, anchor text, and target page.

**Tools used**: `backlinks_backlinks`, `backlinks_anchors`

---

### 2. See Which Blog Content Earns You the Most Backlinks

Discover which blog posts attract the most backlinks.

**Parameters**: `domain` (string) -- The domain to analyze.

**Prompt**: Show which blog posts on the domain attract the most backlinks. List the top 5 by backlink count, and include title, referring domains, and anchor types.

**Tools used**: `backlinks_domain_pages`, `backlinks_anchors`

---

### 3. Find New Link Opportunities from Competitor Backlinks

Discover domains that link to competitors but not to you.

**Parameters**:
- `my_domain` (string) -- Your domain to compare against competitors
- `competitor_1` (string) -- First competitor domain
- `competitor_2` (string) -- Second competitor domain

**Prompt**: Which websites link to my competitors but not to my domain? Return 15 domains to target for outreach.

**Tools used**: `backlinks_domain_intersection`, `backlinks_competitors`

---

### 4. Locate Broken or Redirected Pages That Waste Valuable Links

Find internal pages with many backlinks that are returning 404 or redirecting.

**Parameters**:
- `domain` (string) -- The domain to analyze
- `backlinks_count` (number, default: 30) -- Minimum number of backlinks to consider a page valuable

**Prompt**: Find internal pages on the domain that have over N backlinks but are 404 or redirected. Return URL, status code, backlink count, and top referring domains.

**Tools used**: `backlinks_domain_pages`, `backlinks_backlinks`

---

### 5. Benchmark Backlink Gaps Between You and a Competitor

Compare backlink profiles between two domains and find gaps.

**Parameters**:
- `my_domain` (string) -- Your domain to compare against a competitor
- `competitor` (string) -- Competitor domain to analyze

**Prompt**: Compare backlinks between your domain and the competitor. Show 10 domains linking only to the competitor domain. Include domain authority and link count.

**Tools used**: `backlinks_domain_intersection`, `backlinks_bulk_ranks`
